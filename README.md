# 手机内容审核skill

面向**豆包×努比亚手机 / 豆包手机助手**项目的内部初审技能。基于项目Brief、玩法实测、83位已发布达人稿件、甲方批注和改稿案例，用白话说清脚本和视频哪里要改。**调用本技能审核指定飞书稿件，默认用使用者本人的飞书身份在原稿留定位评论并回读；不只在Agent聊天里交一段建议。** 不自动改正文或新增版本。

这是包含项目经验、案例与来源的公开知识包。没有把它宣称为甲方自动终审，也没有未经验证的“审核准确率”。

## 能做什么

- **审脚本**：结合机构BF、达人BF、红线和当周要求，定位原句留评论，给具体改法及需要补的材料；不自动代写整稿、改正文或新增V3等版本。
- **审视频**：核当前版本实际画面、讲话、节奏与结果；在视频所属文档/附件块评论，写清文件名和时间点。
- **飞书内回写**：创建局部批注、在原评论串补复审意见；按明确目标更新当前身份自己的审核评论；逐条回读。
- **复审**：对照上轮意见核实际新版本，不凭“已改”或“已解决”判断完成。
- **说白话、看真实使用**：审核意见和达人说明直接讲具体问题和改法；看本人为什么这样用、怎么选、哪里想改，不能把连续念指令当成活人感，也不代编情绪和经历。
- **周更学习**：新增已发布案例、机构/达人BF、红线、周度推广方向和测试结果进入增量学习；形成知识变更后同步本机技能与此仓库。

“视频时间点意见”默认是飞书文档评论中的时间码；不冒称播放器原生时间轴批注。技能不去抖音公开评论区发审核意见，不重剪文件，不自动修改客户表状态或给甲方终审放行。

## 直接把链接发给你的 Agent

```text
请按我的Agent环境安装这个仓库里的 doubao-phone-content-review skill，读取INSTALL.md并确认完整资源已加载：
https://github.com/haowang836903800-cmyk/phone-content-review-skill
以后我给飞书稿件要求审核，默认用我自己的飞书身份在原稿留评论并回读；不改正文、不出新版。
如果当前环境不能安装技能或没有飞书评论工具，请说明实际缺哪一步，不要把聊天里的建议当成已经评论。
```

仓库公开，下载安装无需GitHub邀请或私有访问权限。Agent按 [INSTALL.md](INSTALL.md) 安装完整技能目录；[技能目录直达](https://github.com/haowang836903800-cmyk/phone-content-review-skill/tree/main/doubao-phone-content-review)。需要压缩包时用 [完整技能ZIP](https://github.com/haowang836903800-cmyk/phone-content-review-skill/raw/refs/heads/main/dist/doubao-phone-content-review.zip)，不要只上传SKILL.md。

也可用支持Agent Skills的安装工具，按提示选择你的Agent：

```bash
npx skills add https://github.com/haowang836903800-cmyk/phone-content-review-skill --skill doubao-phone-content-review
```

安装工具参数以 [skills官方说明](https://github.com/vercel-labs/skills/blob/main/docs/commands.md) 为准。用该工具安装后，可运行 `npx skills update doubao-phone-content-review` 获取更新。

## 安装与依赖

共用标准 `SKILL.md` 和完整资源目录，不绑定某个模型或Codex专有接口。已写明Codex、Claude Code、Cursor、Copilot、Gemini CLI、Kimi Code CLI、TRAE、Windsurf、OpenCode、OpenClaw等安装器路线，以及豆包/豆包工作的执行分支；详见 [跨Agent适配说明](doubao-phone-content-review/references/agent-adapters.md)。支持哪些安装器，不等于所有环境的飞书评论都已线上实测。

安装本身无需飞书登录。第一次真实审稿时检查本人的飞书身份、读评论/写评论及回读能力，优先可用连接器/MCP，也可用用户身份的 `lark-cli` 或本人已登录的浏览器。不同环境无需有相同的工具名；不能默认用应用机器人发言。缺工具或权限时说明实际阻碍及下一步，不将纯文字报告当成回写完成。

**豆包与豆包工作：** 审核规则及工具选择已适配；在有技能和飞书工具的工作环境中执行。普通聊天只有读附件能力时，不能替你进飞书评论。当前版本是否可自定义导入，须以实际入口确认；本仓库未上架豆包商店，不保证任意豆包客户端收到GitHub链接就能安装。豆包官方将技能与连接器分开，商店发行另有接入审核：[官方Skill指南](https://open.doubao.com/document/doubao-developer-guide/skill-integration-guide)。

## 怎么用

> 用手机内容审核skill审核这个脚本V2：〈稿件链接〉。

> 这是视频V3，审核文档在这里。按实际画面和讲话审，带时间点评论，并检查上轮意见有没有改好。

> 只分析，先别写入飞书。

上面的普通审核请求已经包含原稿评论，不需要再强调“请写入”。该默认交付适用于所有安装者；不继承的是维护者的账号、资料权限和自动化，而非评论这一步。明确“只分析/先别写/不要评论”才不回写；仅安装、学习或升级不试发历史稿评论。无新问题或同样意见已存在时可新增0条并解释原因。改正文、另写版本、删除已有版本、替换视频、发群或改变审核状态，须有用户另外明确要求。未知事实不替达人编造。

已安装过旧版的人需要更新本机副本并让Agent重新加载；GitHub更新不会自动替换每个人本地的skill。用上述安装器安装的可执行 `npx skills update doubao-phone-content-review`；手动/ZIP安装的先保留自己的配置，再用同一入口导入新版。升级不会自动替使用者登录飞书。

## 周更

项目用户已要求每周一10:00（北京时间）增量学习并自动更新GitHub。计划由Codex Automations管理；复制本仓库到另一台电脑不会自动创建定时任务，也不会后台监听所有飞书消息。

台账是 `doubao-phone-content-review/references/learning-state.json`。它区分已学习、部分核验和待补，不因日期推进把没看的视频标完成。每周记录放在 `updates/`。

机构BF中“怎么拍”、红线具体检查项和文件间口径差异，见 [BF与红线对照](doubao-phone-content-review/references/brief-and-redline-map.md)。本次已重新全文核对这三份飞书规范，包含红线中的开头要求图片；每周即使没有新发布案例，也检查规范变化。

## 研究与能力边界

初始资料快照为2026-11-04：83份稿件文档、244条评论卡及回复、407个选取历史快照；92份附件以抽帧与机器转写辅助核验，公开页打开21条，其中20条取得可见评论样本。**没有逐个完整人工听看所有历史视频版本。**

未来审视频仍要查看当次实际送审文件；声音、连续过程或结果不够时输出具体待核项，不能假通过。结构校验和离线演练不等于真实线上写入测试，实际每次评论必须回读验证。

主入口：[SKILL.md](doubao-phone-content-review/SKILL.md)。内部手册、达人说明、83位案例、玩法边界和写回流程均在技能的 `references/`；结构化模板在 `assets/`。
