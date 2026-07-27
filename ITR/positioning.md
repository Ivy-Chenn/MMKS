# Positioning

> Source: Troubleshooting_数据表.csv · Records: 29

## 1. 定位问题 — 定位状态差，环境问题

**Primary Symptom:** 定位问题

**Secondary Symptom:** 定位状态差，环境问题

**Solution:**

1. 检查RTK基站是否正常开机上电，如RTK基站异常尝试补发
1. 判断用户所在区域，如在欧洲/英国考虑升级固件和手动升级RTK

**Remarks:** 1300定位状态差
1303/1304

**Applicable Models:** luba1, luba2, luba mini, luba mini LiDAR

**Query Page:** —

## 2. 定位问题 — 定位校准失败

**Primary Symptom:** 定位问题

**Secondary Symptom:** 定位校准失败

**Solution:**

1. 检查报错是否只出现在边界附件
1. 控车离开边界，到开阔作业区域位置
1. 检查app中是否伴随其他报错

**Remarks:** 1300定位状态差
1314定位精度差

**Applicable Models:** luba1, luba mini, luba mini LiDAR

**Query Page:** —

## 3. 定位问题 — app车位置偏移

**Primary Symptom:** 定位问题

**Secondary Symptom:** app车位置偏移

**Solution:**

1. 检查app和固件是否为最新版本

**Remarks:** —

**Applicable Models:** —

**Query Page:** —

## 4. 定位问题 — 定位报错/充电桩定位偏移/POS非Good状态

**Primary Symptom:** 定位问题

**Secondary Symptom:** 定位报错/充电桩定位偏移/POS非Good状态

**Solution:**

1. 确认是否绑定了RTK基站
1. 确认固件是否为最新版本，以及RTK是否正常上电
1. 检查割草机和RTK的link mode一致
1. 确保app中RTK lora number和RTK机身上的标签带有的一致
1. 若以上没问题但仍无法解决，更换RTK

**Remarks:** —

**Applicable Models:** luba2

**Query Page:** —

## 5. 充电桩问题 — 无法出桩自动作业

**Primary Symptom:** 充电桩问题

**Secondary Symptom:** 无法出桩自动作业

**Solution:**

1. 检查充电桩是否位于开阔位置
1. 检查RTK基站是否正常上电，如不正常则更换基站后重新测试

**Remarks:** —

**Applicable Models:** luba1, luba2

**Query Page:** —

## 6. 充电桩问题 — app提示设备不在工作区域内但实际在充电

**Primary Symptom:** 充电桩问题

**Secondary Symptom:** app提示设备不在工作区域内但实际在充电

**Solution:**

1. 检查充电桩所谓位置的周围环境是否有树/墙/建筑等遮挡物，应该将其安装在空旷的位置
1. 核实适用的定位模式，如果是RTK则需要检查RTK基站安装的位置是否有遮挡物

**Remarks:** —

**Applicable Models:** luba mini, luba mini LiDAR

**Query Page:** —

## 7. 充电桩问题 — 下桩后停在桩前不动

**Primary Symptom:** 充电桩问题

**Secondary Symptom:** 下桩后停在桩前不动

**Solution:**

1. 检查充电桩所谓位置的周围环境是否有树/墙/建筑等遮挡物，应该将其安装在空旷的位置
1. 核实适用的定位模式，如果是RTK则需要检查RTK基站安装的位置是否有遮挡物

**Remarks:** 1105下桩后停在桩前不动

**Applicable Models:** luba mini, luba mini LiDAR

**Query Page:** —

## 8. RTK — RTK基站断开连接

**Primary Symptom:** RTK

**Secondary Symptom:** RTK基站断开连接

**Solution:**

1. 核实机器人和RTK基站定位模式是否一致
1. 核实机器人和RTK的lora号是否一致，不同则改为一致
1. 核实机器人和RTK是否都有搜星数，若机器人搜星数为0则尝试多次重启设备，若RTK基站搜星数为0则检查RTK基站指示灯状态
1. 若RTK基站指示灯异常，检查充电桩后面的电源线接口，若正常则更换RTK适配器，若故障则进行不良品回收

**Remarks:** 1551 RTK断连报警

**Applicable Models:** —

**Query Page:** —

## 9. RTK — RTK指示灯不正常

**Primary Symptom:** RTK

**Secondary Symptom:** RTK指示灯不正常

**Solution:**

1. 检查是否只是夜间不亮灯，升级后为正常现象
1. 如非夜间也不亮灯，则尝试其他供电方案（充电桩/RTK适配器）
1. RTK适配器供电正常，则检查充电桩连接基站接口是否损坏
1. 充电桩供电正常，则补发RTK适配器
1. 若都不正常，补发RTK

**Remarks:** —

**Applicable Models:** luba1, luba2, luba3, luba2x

**Query Page:** —

## 10. RTK — RTK一直亮红灯/闪红灯

**Primary Symptom:** RTK

**Secondary Symptom:** RTK一直亮红灯/闪红灯

**Solution:**

1. 检查RTK重新上电后是否正常
1. 若仍然异常则补发新基站

**Remarks:** —

**Applicable Models:** luba1, luba2

**Query Page:** —

## 11. RTK — RTK灯灭无卫星信号，需重启才能再次工作

**Primary Symptom:** RTK

**Secondary Symptom:** RTK灯灭无卫星信号，需重启才能再次工作

**Solution:**

1. 检查割草机和RTK固件是否为最新

**Remarks:** —

**Applicable Models:** luba2

**Query Page:** —

## 12. RTK — RTK-LoRa模式切换后连接不上

**Primary Symptom:** RTK

**Secondary Symptom:** RTK-LoRa模式切换后连接不上

**Solution:**

1. 检查RTK是否可以手动添加，如未绑定则重新添加
1. 检查割草机和RTK的link mode是否一致，需设置为相同

**Remarks:** —

**Applicable Models:** luba2

**Query Page:** —

## 13. RTK — App连不上RTK/RTK连不上WiFi

**Primary Symptom:** RTK

**Secondary Symptom:** App连不上RTK/RTK连不上WiFi

**Solution:**

1. 检查WiFi是否为2.4GHz或者2.4/5GHz网络及热点，如果不是则需切换至
1. 检查WiFi路由器是否设置了加密等级限制或者IP接入点不够分配

**Remarks:** —

**Applicable Models:** luba2, luba3, luba2x

**Query Page:** —

## 14. RTK — App连不上RTK/蓝牙连接失败

**Primary Symptom:** RTK

**Secondary Symptom:** App连不上RTK/蓝牙连接失败

**Solution:**

1. 检查RTK指示灯，并且排查WiFi/蓝牙/4G问题
1. 可以尝试用其他手机通过蓝牙连接RTK，安卓手机用自带功能搜索蓝牙，苹果手机可以通过BLE scanner或者其他蓝牙扫描app进行扫描

**Remarks:** —

**Applicable Models:** luba3, luba2x

**Query Page:** —

## 15. RTK适配器 — RTK电源适配器指示灯异常

**Primary Symptom:** RTK适配器

**Secondary Symptom:** RTK电源适配器指示灯异常

**Solution:**

1.确认插座供电正常 2.交叉验证：RTK基站支持RTK适配器和充电桩供电口供电 3.确认灯语

**Remarks:** —

**Applicable Models:** luba3, luba2x

**Query Page:** —

## 16. RTK适配器 — RTK电源适配器电压异常

**Primary Symptom:** RTK适配器

**Secondary Symptom:** RTK电源适配器电压异常

**Solution:**

1. 判断/测试RTK电源适配器电压是否为正常12V左右

**Remarks:** —

**Applicable Models:** luba3, luba2x

**Query Page:** —

## 17. iNavi — 定位无响应

**Primary Symptom:** iNavi

**Secondary Symptom:** 定位无响应

**Solution:**

1. 检查是否为最新固件版本，若不是则需要更新

**Remarks:** 1000020 定位无响应

**Applicable Models:** luba3, luba2x

**Query Page:** —

## 18. iNavi — 定位失败

**Primary Symptom:** iNavi

**Secondary Symptom:** 定位失败

**Solution:**

1. 确认是否在区域外建图时报错，需要开到区域内或充电桩上才能开始建图
1. 需要升级最近固件版本

**Remarks:** 1000019 定位失败

**Applicable Models:** luba3, luba2x

**Query Page:** —

## 19. iNavi — 车在狭窄通道或狭窄区丢失定位

**Primary Symptom:** iNavi

**Secondary Symptom:** 车在狭窄通道或狭窄区丢失定位

**Solution:**

1. 检查是否为最新固件版本，若不是则需要更新

**Remarks:** 1314定位精度差
1300工作环境中遮挡

**Applicable Models:** luba3, luba2x

**Query Page:** —

## 20. iNavi — iNavi定位信号差

**Primary Symptom:** iNavi

**Secondary Symptom:** iNavi定位信号差

**Solution:**

1. 确认iNavi所用的模式时WiFi还是4G（可同时使用但iNavi优先）
1. 两者切换交叉验证

**Remarks:** 1314定位精度差
1554 WiFi网络不稳定
1556 4G网络不稳定

**Applicable Models:** luba3, luba2x

**Query Page:** —

## 21. iNavi — 定位超时/地图变形/定位无响应

**Primary Symptom:** iNavi

**Secondary Symptom:** 定位超时/地图变形/定位无响应

**Solution:**

1. 检查是否为最新固件版本，若不是则需要更新

**Remarks:** 1418定位超时

**Applicable Models:** luba3, luba2x

**Query Page:** —

## 22. iNavi — 卫星地图偏差

**Primary Symptom:** iNavi

**Secondary Symptom:** 卫星地图偏差

**Solution:**

1. 检查是否为最新固件版本，若不是则需要更新

**Remarks:** —

**Applicable Models:** luba3, luba2x

**Query Page:** —

## 23. iNavi — iNavi网络不稳定/4G或WiFi连接异常

**Primary Symptom:** iNavi

**Secondary Symptom:** iNavi网络不稳定/4G或WiFi连接异常

**Solution:**

1.检查WiFi和4G网络，若信号差可尝试连接其他网络或者手机热点

**Remarks:** 1554 网络报错
1556 iNavi联网异常

**Applicable Models:** luba3, luba2x

**Query Page:** —

## 24. iNavi — POS状态为Single

**Primary Symptom:** iNavi

**Secondary Symptom:** POS状态为Single

**Solution:**

1. 检查app和固件是否为最新版本
1. 检查网络信号，考虑切换到4G或其他WiFi网络，再尝试重启设备，重新尝试连接iNavi
1. 如果不是网络问题，则将link mode切换到其他，然后切回iNavi，再重启设备

**Remarks:** —

**Applicable Models:** luba3, luba2x

**Query Page:** —

## 25. 定位问题 — 地图变形/偏移/通道消失/充电桩位置偏移

**Primary Symptom:** 定位问题

**Secondary Symptom:** 地图变形/偏移/通道消失/充电桩位置偏移

**Solution:**

1. 提供充电桩位置照片和周围环境照片

**Remarks:** 1300/1000019

**Applicable Models:** —

**Query Page:** —

## 26. 定位问题 — 定位无响应

**Primary Symptom:** 定位问题

**Secondary Symptom:** 定位无响应

**Solution:**

1. 提供现场及周围环境
1. 提供app报错截图
1. 更新固件和app至最新版本
1. 尝试重启设备，如果重启未解决，则删除地图重新画或者回复出厂设置（同时提醒用户该操作需要重新绑定和配置设备）

**Remarks:** 1000020定位无响应

**Applicable Models:** —

**Query Page:** —

## 27. 定位问题 — 定位丢失/地图绘制失败

**Primary Symptom:** 定位问题

**Secondary Symptom:** 定位丢失/地图绘制失败

**Solution:**

1. 收集摄像头状态+现场环境+app报错+固件版本信息检查+重启
1. 检查是否忘记撕掉镜头膜

**Remarks:** 1315 因定位丢失导致地图绘制/建图失败

**Applicable Models:** —

**Query Page:** —

## 28. 定位问题 — 检测到充电桩位置变动

**Primary Symptom:** 定位问题

**Secondary Symptom:** 检测到充电桩位置变动

**Solution:**

1. 检查现场环境，app报错，确认充电桩附近的障碍物/物体是否移动过
1. 如有物体移动，则重新定位充电桩的位置

**Remarks:** 1132 检测到充电桩位置变动

**Applicable Models:** —

**Query Page:** —

## 29. 定位问题 — 定位超时/地图变形/定位无响应

**Primary Symptom:** 定位问题

**Secondary Symptom:** 定位超时/地图变形/定位无响应

**Solution:**

1. 提供现场及周围环境
1. 提供app报错截图
1. 更新固件和app至最新版本
1. 尝试重启设备，如果重启未解决，则删除地图重新画或者回复出厂设置（同时提醒用户该操作需要重新绑定和配置设备）

**Remarks:** 1418 定位超时

**Applicable Models:** —

**Query Page:** —

