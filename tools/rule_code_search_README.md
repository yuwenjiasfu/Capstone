# rule_code_search.py

一个只做"规则相关位置检索"的静态工具，用来在反编译的 Android App 工程里，根据
本地论文规则库 `rule_catalog.tsv` 的每一条规则定位可能相关的代码或资源行。

**这个工具只定位位置，不判断漏洞是否成立。**

- 不写最终安全报告。
- 不输出 confirmed / supported_hypothesis / not_supported / not_testable。
- 不给风险等级、置信度、复杂原因、动态测试建议。
- 只输出：规则、论文、文件路径、行号、命中文本。

---

## 为什么不用简单 grep

健康 BLE 类 Android App 中像 `http://`、`Log.e`、`BluetoothGatt`、
`SharedPreferences`、`ContentProvider` 这些关键词动辄命中几百上千行，
人工无法阅读。

本工具因此采用"组合命中"的方式：除了命中行本身要匹配，还要求附近窗口内
或整个文件中同时出现语义相关词（例如 `http://` 必须附近出现 `upload`、
`login`、`token`、`health` 等），否则不输出。

设计原则：**可以接受漏报，不能接受海量无法阅读的宽泛命中。**

---

## 固定路径

以下路径写死在脚本里，请不要依赖命令行参数修改：

- 论文目录：`C:\wujiangliang\app\xiangshan\database_beginner`
  - `paper_catalog.tsv`
  - `rule_catalog.tsv`
- 输出根目录：`C:\wujiangliang\app\search\`
- 本次运行的输出子目录：`C:\wujiangliang\app\search\<--app-root 目录名>\`
  - 例如 `--app-root "C:\wujiangliang\app\bupa"`
    → `C:\wujiangliang\app\search\bupa\`

## 运行方式

在 `C:\wujiangliang\app\search` 下：

```powershell
python tools\rule_code_search.py --app-root "C:\path\to\decompiled_app"
```

- `--app-root` 指向某个反编译 App 工程根目录（例如 apktool/jadx 的输出目录）。
- 没有 `--database-root`、`--out` 这类参数。
- Python 3.10+，只依赖标准库。

## 输出

运行完成会在 `C:\wujiangliang\app\search\<app 目录名>\` 下生成：

```text
C:\wujiangliang\app\search\<app 目录名>\rule_hits.tsv
C:\wujiangliang\app\search\<app 目录名>\rule_hits.md
C:\wujiangliang\app\search\<app 目录名>\no_hit_rules.txt
```

例如 `--app-root "C:\wujiangliang\app\bupa"` 就是 `C:\wujiangliang\app\search\bupa\`。

### `rule_hits.tsv`

以 TAB 分隔，字段：

```tsv
rule_id    paper_id    paper_title    file_path    line_number    matched_text
```

- `file_path` 为相对 `--app-root` 的路径，使用正斜杠。
- `matched_text` 去掉前后空白并在超过 300 字符时截断。

### `rule_hits.md`

人类可读的命中汇总，按 `rule_id` 分节：

```md
## BR006

paper_id: B016
paper_title: A privacy and security analysis of early-deployed COVID-19 contact tracing Android apps

- `resources/AndroidManifest.xml:154`
  `android:usesCleartextTraffic="true"`
```

### `no_hit_rules.txt`

本次扫描中没有任何命中的规则 ID，一行一个。

---

## 控制台输出

运行结束后只会打印：

- 扫描到的文件数
- 命中总数
- 命中规则数
- 无命中规则数
- 输出目录绝对路径

其余进度、调试、错误文件都直接跳过，不会打印。

---

## 如何人工阅读结果

推荐的人工阅读顺序：

1. 打开 `rule_hits.md`，按规则分组浏览。
2. 对于某个规则，先看 `matched_text` 是否真的相关，再点进 `file_path:line_number` 查看上下文。
3. 不要把命中当成漏洞结论。只是"值得进一步看"的位置。
4. 对于没有命中的规则，参考 `no_hit_rules.txt`，自己判断是否确实无相关实现，或只是规则覆盖不到。

健康 BLE App 特别关注：

- **BLE**：`writeCharacteristic` / `onCharacteristicChanged` / `UUID.fromString` / 配对流程、协议解析、payload 构造。
- **健康数据**：heart / blood / spo / sleep / step / ecg / temperature 字段的持久化与上传。
- **本地存储**：SharedPreferences / MMKV / DataStore / SQLite / external storage 中的敏感键。
- **日志**：`Log.*` / `System.out.println` 输出的敏感内容。
- **网络传输**：`http://`、`ws://` 明文、TLS 配置、证书校验、HostnameVerifier。
- **导出组件**：`android:exported="true"` 的 activity / service / receiver / provider。
- **第三方 SDK**：广告、统计、推送、IM、崩溃上报 SDK，配合 `AD_ID` / AdvertisingId。
- **隐私政策**：策略 URL、第三方 SDK 披露、采集数据类型披露。

---

## 重要提醒

- **No hit 不代表 App 一定没有问题。** 规则可能写得偏保守、关键词不匹配、
  代码被混淆等都可能导致漏报。
- **Hit 也不代表漏洞成立。** 可能只是同名 API、无害日志、
  第三方库 noise 等。命中只是"看这里"的指针。
- 动态验证、人工审计、组合证据才能得出结论。本工具只负责把你"带到现场"。

---

## 实现要点

- 每条规则都会参与搜索。有手写 spec 的走 spec；没有的则从
  `rule_catalog.tsv` 对应字段（`risk_name`、`where_to_check`、
  `primary_static_or_code_signal`、`app_data_resource_policy_signal`、
  `dynamic_validation_signal`、`cloud_network_signal`、`minimum_evidence`）
  自动提取 fallback 关键词：
  - 按非字母数字下划线分词。
  - 保留长度 ≥ 5 的词。
  - 去掉常见 stop words。
  - 最多保留 12 个词。
  - 如果 fallback 关键词超过 3 个，则要求同一文件中至少出现 2 个不同关键词才输出。
- 组合命中 search spec 支持：`file_globs`、`path_any`、`line_any`、
  `line_all`、`near_any`、`near_all`、`file_any`、`file_all`、
  `near_window`。
- 跳过以下扩展名的明显二进制文件：`.so .png .jpg .jpeg .gif .webp .ttf .otf
  .dex .arsc .mp3 .mp4 .wav .amr .zip .jar` 等。
- 跳过大于 10 MB 的文件。
- 编码依次尝试 utf-8, utf-8-sig, gbk, latin-1；读取失败直接跳过。
- 所有匹配不区分大小写。
- 每条规则最多保留 80 条命中；高频规则（BLE、日志、http、SharedPreferences 等）
  最多 40 条。
- `(rule_id, file_path, line_number)` 三元组去重。
