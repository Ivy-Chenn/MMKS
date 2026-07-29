# Mapping

> Source: Troubleshooting_数据表.csv · Records: 13

## 1. 卫星地图 — 地图丢失

**Primary Symptom:** 卫星地图

**Secondary Symptom:** 地图丢失

**Solution:**

1. 基站位置变动大时会导致地图丢失，需要重新建立
1. 可能是手动误删了地图

**Remarks:** —

**Applicable Models:** luba1, luba2, luba2x, yuka 2024

**Query Page:** —



abcd
## 2. 卫星地图 — 卫星地图偏差

**Primary Symptom:** 卫星地图

**Secondary Symptom:** 卫星地图偏差

**Solution:**

1. 存在偏差是正常现象
1. 用于可以进入卫星地图手动纠偏

**Remarks:** —

**Applicable Models:** luba1, luba2, luba2x, yuka 2024

**Query Page:** —

## 3. 卫星地图 — 卫星地图背景变成黑色

**Primary Symptom:** 卫星地图

**Secondary Symptom:** 卫星地图背景变成黑色

**Solution:**

1. 确认固件和app是否为最新版
1. 确认网络连接是否正常，排查Wi-Fi和4G信号带来的问题

**Remarks:** —

**Applicable Models:** luba2x

**Query Page:** —

## 4. 充电桩问题 — 无法重置充电桩位置

**Primary Symptom:** 充电桩问题

**Secondary Symptom:** 无法重置充电桩位置

**Solution:**

1. 检查车在桩定位是否good，非good需要将充电桩移到开阔位置
1. 检查充电桩是否正常

**Remarks:** —

**Applicable Models:** luba1, luba2, yuka 2024

**Query Page:** —

## 5. 充电桩问题 — 无充电桩，但app显示RTK位置变化

**Primary Symptom:** 充电桩问题

**Secondary Symptom:** 无充电桩，但app显示RTK位置变化

**Solution:**

1. 核实是否重新安装了RTK
1. 引导用户重新定位RTK、并重新绘制草坪
1. 检查RTK安装是否牢固

**Remarks:** —

**Applicable Models:** luba2, yuka 2024

**Query Page:** —

## 6. 充电桩问题 — 无充电桩但app提示需重新定位

**Primary Symptom:** 充电桩问题

**Secondary Symptom:** 无充电桩但app提示需重新定位

**Solution:**

1. 将割草机返回充电桩，使用app里的“重新定位充电站”功能
1. 引导用户将充电桩放在至少90°开阔视野看到草坪的位置

**Remarks:** 1301充电桩位置已更改

**Applicable Models:** luba2, yuka 2024

**Query Page:** —

## 7. 连通路径问题 — app内提示无通道，客户按照指引画通道报错

**Primary Symptom:** 连通路径问题

**Secondary Symptom:** app内提示无通道，客户按照指引画通道报错

**Solution:**

1. 确认固件和app是否为最新版
2. 尝试重新定位充电桩+重画通道

**Remarks:** 1114连通路径已存在

**Applicable Models:** luba2x, luba mini, luba mini LiDAR, yuka 2025

**Query Page:** —

## 8. 建图问题 — 无法出桩建图或者出桩建图时提示定位异常

**Primary Symptom:** 建图问题

**Secondary Symptom:** 无法出桩建图或者出桩建图时提示定位异常

**Solution:**

1. 确认是否为最近固件
2. 移除桩前可能存在的障碍物

**Remarks:** —

**Applicable Models:** yuka mini2, yuka mini Vision, yuka mini LiDAR

**Query Page:** —

## 9. 建图问题 — 充电桩到工作区域的路径提示超出限制

**Primary Symptom:** 建图问题

**Secondary Symptom:** 充电桩到工作区域的路径提示超出限制

**Solution:**

1. 尽量沿直线控车，避免频繁掉头和后退
1. 可以在中间创建缓冲区

**Remarks:** —

**Applicable Models:** yuka mini2, yuka mini Vision, yuka mini LiDAR

**Query Page:** —

## 10. 建图问题 — 自动建图失败

**Primary Symptom:** 建图问题

**Secondary Symptom:** 自动建图失败

**Solution:**

1. 检查充电桩是否安装在前/左/右三个方向1.5m内无遮挡的环境中
1. 检查环境现场是否复杂
1. 建议尝试手动建图

**Remarks:** 1223边界不清晰
1188录制数据处理异常
1315定位丢失

**Applicable Models:** yuka mini2, yuka mini Vision, yuka mini LiDAR

**Query Page:** —

## 11. 建图问题 — 手动建图失败

**Primary Symptom:** 建图问题

**Secondary Symptom:** 手动建图失败

**Solution:**

1. 控车时尽量避免车速过快/频繁转弯/掉头/后退

**Remarks:** 1223边界不清晰，1188录制数据处理异常，1315定位丢失

**Applicable Models:** yuka mini2, yuka mini Vision, yuka mini LiDAR

**Query Page:** —

## 12. 连通路径问题 — 添加区域之间通道失败

**Primary Symptom:** 连通路径问题

**Secondary Symptom:** 添加区域之间通道失败

**Solution:**

1. 应从已有区域创建起点，控车到达要新建的区域后再设置终点
1. 控车中全程不要提举车面对空旷环境

**Remarks:** 1188数据处理异常

**Applicable Models:** yuka mini2, yuka mini Vision, yuka mini LiDAR

**Query Page:** —

## 13. 建图问题 — 创建孤岛区域失败

**Primary Symptom:** 建图问题

**Secondary Symptom:** 创建孤岛区域失败

**Solution:**

1. 确认固件是否更新到最新版本
1. 引导用户抱车的时候保持水平/车头朝前/不要遮挡视觉模组/速度不要过快/通道距离不要超过200m
1. 如果无法满足不超200m的条件，考虑根据对应场景使用dropmow模式

**Remarks:** 1188数据处理异常

**Applicable Models:** yuka mini2, yuka mini Vision, yuka mini LiDAR

**Query Page:** —

