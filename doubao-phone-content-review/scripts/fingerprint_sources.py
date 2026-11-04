#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Fingerprint complete local Feishu fetch/list-comments responses; no network or writes."""
import argparse
import hashlib
import json
from pathlib import Path


def digest(value):
    encoded = json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(encoded.encode("utf-8")).hexdigest()


def load_ok(path):
    result = json.loads(Path(path).read_text(encoding="utf-8"))
    if result.get("ok") is not True:
        raise ValueError("source response is not ok: " + str(path))
    return result["data"]


def comments_fingerprint(data):
    # Merge all pages and any truncated reply lists BEFORE calling this function.
    if data.get("has_more") is not False or "items" not in data:
        raise ValueError("comments must be an explicitly complete merged response")
    comments, ids = [], set()
    for item in data["items"]:
        cid = item["comment_id"]
        if cid in ids:
            raise ValueError("duplicate comment id: " + cid)
        ids.add(cid)
        reply_list = item.get("reply_list", {})
        if reply_list.get("has_more"):
            raise ValueError("incomplete replies for " + cid)
        replies, reply_ids = [], set()
        for reply in reply_list.get("replies", []):
            rid = reply["reply_id"]
            if rid in reply_ids:
                raise ValueError("duplicate reply id: " + rid)
            reply_ids.add(rid)
            replies.append({"reply_id": rid, "user_id": reply.get("user_id"),
                            "content": reply.get("content")})
        relation = item.get("relation") or {}
        raw = relation.get("relation") or "{}"
        positions = json.loads(raw) if isinstance(raw, str) else raw
        anchors = [entry.get("positionInfo", {}) for entry in positions.values()]
        anchors.sort(key=lambda value: json.dumps(value, sort_keys=True))
        comments.append({
            "comment_id": cid, "user_id": item.get("user_id"),
            "is_solved": item.get("is_solved"), "is_whole": item.get("is_whole"),
            "quote": item.get("quote"), "content_deleted": relation.get("content_deleted"),
            "anchors": anchors, "replies": sorted(replies, key=lambda value: value["reply_id"]),
        })
    return digest(sorted(comments, key=lambda value: value["comment_id"]))


def fingerprint(document_data, comments_data):
    document = document_data["document"]
    if comments_data.get("file_token") != document["document_id"]:
        raise ValueError("document and comment targets do not match")
    content = document.get("content")
    if not isinstance(content, str):
        raise ValueError("document content is missing, not an empty verified document")
    return {
        "fingerprint_version": "feishu-content-comments-v1",
        "document_id": document["document_id"],
        "revision_id": document.get("revision_id"),
        "content_sha256": hashlib.sha256(content.encode("utf-8")).hexdigest(),
        "comments_sha256": comments_fingerprint(comments_data),
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--doc", required=True, help="docs +fetch --detail full JSON")
    parser.add_argument("--comments", required=True, help="complete merged list-comments JSON")
    args = parser.parse_args()
    try:
        result = fingerprint(load_ok(args.doc), load_ok(args.comments))
    except (ValueError, KeyError, TypeError, OSError) as error:
        parser.exit(2, str(error) + "\n")
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
