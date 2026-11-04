# Agent安装入口

用户要求安装本仓库时，只安装技能。安装不授权开始审稿、登录飞书、创建周更任务或写评论。

## 目标

- 技能：`doubao-phone-content-review`
- 完整目录：`doubao-phone-content-review/`
- 目录链接：https://github.com/haowang836903800-cmyk/phone-content-review-skill/tree/main/doubao-phone-content-review
- 一起安装 `SKILL.md`、`references/`、`assets/`、`scripts/`、`agents/`；不能只下载主文件。

## 安装方式

1. 首选当前Agent已有的技能安装器，输入上面的目录链接。Codex可用自带skill-installer的GitHub URL安装方式。
2. 没有内置安装器、但有Node.js时，可用README里的 `npx skills add` 命令，选择当前Agent；仅安装这一项，不对所有Agent批量写入。
3. 手动安装时下载公开仓库，将完整技能文件夹放入当前Agent支持的技能目录。Codex自带安装器默认放入 `~/.codex/skills/`；其他Agent先查自身说明，不猜路径。
4. 若已有同名技能，比较来源和本地修改，先备份；不能用公开版覆盖使用者的私有案例、来源配置或学习记录。

## 验收

确认frontmatter的name、全部引用文件和实际安装位置，报告安装路径与调用方式。Codex自带安装器安装后可在下一轮对话使用。只读到网页、下载失败或仅生成草稿，不算安装成功。

第一次使用按需读取用户提供的待审稿件、当周BF和红线。没有飞书工具也能审核用户直接给的材料；不要在安装阶段索要飞书账号或复制他人的认证信息。
