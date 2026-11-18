# underwrite · 公共电台实况、鸣谢约定与排段周单

使用 Python 3.11 标准库，不需要联网、第三方包或数据库。输入示例使用本地合成记录。

```sh
python3 -m underwrite ledger data/sample.json
python3 -m unittest discover -s tests -v
```

输出为 UTF-8 JSON。输入文件不可读、业务引用无效或记录不符合口径时退出码为 2，同时报告原因。

## 记录口径

`breaks` 给出节目单内鸣谢的 `id`、`donor`、`start/end`（自周日起的分钟，左闭右开）和 `replay_of`。`logs` 是站点的 `region` 和实况区间，`broadcast` 表示确定播出，`muted` 表示确定无播出，`unknown` 表示档案未齐。站点流可以并行。
`contracts` 给出允许地区、允许窗口、周目标与是否可计重播。`slots` 是候选节目段，包含可选捐助方、地区和鸣谢容量；`booking` 中 `notified` 的安排已对外承诺。当前报表的 scheduled 只是计划量，不代表履约。
