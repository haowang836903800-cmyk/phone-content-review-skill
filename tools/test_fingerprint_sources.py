"""Local integrity tests, not an evaluation of review accuracy."""
import copy
import importlib.util
from pathlib import Path
import unittest

path = Path(__file__).resolve().parents[1] / 'doubao-phone-content-review/scripts/fingerprint_sources.py'
spec = importlib.util.spec_from_file_location('fingerprint_sources', path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class FingerprintTests(unittest.TestCase):
    def setUp(self):
        self.doc = {'document': {'document_id': 'sample', 'content': 'current script', 'revision_id': 1}}
        self.comments = {'file_token': 'sample', 'has_more': False, 'items': [
            {'comment_id': 'c1', 'user_id': 'reviewer', 'is_solved': False,
             'reply_list': {'replies': [{'reply_id':'r1','user_id':'reviewer','content':{'text':'check result'}}]}}]}

    def test_valid_and_metadata_stable(self):
        expected = module.fingerprint(self.doc, self.comments)
        changed = copy.deepcopy(self.comments)
        changed['items'][0]['update_time'] = 123
        self.assertEqual(expected, module.fingerprint(self.doc, changed))

    def test_reply_pagination_in_both_locations(self):
        for location in ['comment', 'reply_list']:
            with self.subTest(location=location):
                changed = copy.deepcopy(self.comments)
                target = changed['items'][0]
                if location == 'reply_list': target = target['reply_list']
                target['has_more'] = True
                with self.assertRaisesRegex(ValueError, 'incomplete replies'):
                    module.fingerprint(self.doc, changed)

    def test_top_pagination_and_target_mismatch(self):
        for field, value in [('has_more', True), ('file_token', 'other')]:
            changed = copy.deepcopy(self.comments); changed[field] = value
            with self.assertRaises(ValueError): module.fingerprint(self.doc, changed)

    def test_reply_and_resolution_are_substantive(self):
        expected = module.fingerprint(self.doc, self.comments)['comments_sha256']
        changed = copy.deepcopy(self.comments)
        changed['items'][0]['reply_list']['replies'][0]['content'] = {'text':'recheck payment'}
        self.assertNotEqual(expected, module.fingerprint(self.doc, changed)['comments_sha256'])
        changed = copy.deepcopy(self.comments); changed['items'][0]['is_solved'] = True
        self.assertNotEqual(expected, module.fingerprint(self.doc, changed)['comments_sha256'])


if __name__ == '__main__': unittest.main()
