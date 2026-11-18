# 城市更新资料契约

全部楼宇、机构、居民群体、设备、交易及事件均为本地合成，不对应新闻所涉真实主体，不声称新闻中发生这些业务问题。seed.json及各同名Parquet保留完全相同的原始值；actions.json是尚未应用的后续资料。inventory.json仅记录物理大小、摘要及行数，不是业务结论。原始量纲、空值和时区按下文解释。

tasks.quantity_total为合同工程量；progress给报告时点物理量/验收量/已知返工，known_at限制资料可用性。links为FS/SS/FF与工作小时lag，calendar指定工作窗口；资源只在施工而非养护等待占用。history有started/ended/censored_at及expedited，未完工为右删失。weather为共同日天气，anchors为不可移动窗口。options给措施增量资源/费用和时间或返工范围，每活动同组至多一种；equipment全项目共享。milestones给截止/逾期日费用，budget为措施上限；actions是复验失败返工指令，非完工预测。
