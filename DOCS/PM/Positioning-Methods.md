# Positioning Methods

## Positioning Method Categories

We have four different positioning methods: RTK, nRTK/iNavi, LiDAR, V\-Slam

|Product Name|No\.|RTK|nRTK/iNavi|LiDAR|V\-Slam|
|---|---|---|---|---|---|
|Luba series||||||
|Luba 2 |Luba\-VS|✅|❌|❌|❌|
|Luba 2x \(Luba Pro\)|Luba\-VP|✅|✅|❌|❌|
|Luba 3|Luba\-VA|✅|✅|✅|❌|
|Luba 3 1500|Luba\-VA|❌|❌|✅|❌|
|Luba mini series||||||
|Luba mini|Luba\-MN|✅|✅|❌|❌|
|Luba mini LiDAR|Luba\-LD|❌|✅|✅|❌|
|Luba mini 2 LiDAR 1500|Luba\-MK|❌|✅|✅|❌|
|Luba mini 2 Vision 1000|Luba\-MB|❌|✅|❌|✅|
|Yuka series||||||
|Yuka 2025 \(Yuka Pro\)|Yuka\-YP|✅|✅|❌|❌|
|Yuka 2024|Yuka\-YV|✅|✅|❌|❌|
|Yuka mini series||||||
|Yuka mini|Yuka\-MN|✅|✅|❌|❌|
|Yuka mini Vision 700|Yuka\-MV|❌|✅|❌|✅|
|Yuka mini 2 Vision 800R|Yuka\-MV|❌|✅|❌|✅|
|Yuka mini 2 Vision 500G|Yuka\-MV|❌|❌|❌|✅|
|Yuka mini 2 LiDAR|Yuka\-ML|❌|❌|✅|❌|

## Working Range of LiDAR

||Maximum Range|FOV|Temperature|
|---|---|---|---|
|Luba 3 1500|70m/230ft \(80% reflectivity\)<br>40m/130ft \(10% reflectivity\)|360°\*59°|\-22°C\-\+55°C|
|Luba 3 3000|70m/230ft \(80% reflectivity\)<br>40m/130ft \(10% reflectivity\)|360°\*59°|\-22°C\-\+55°C|
|Luba 3 5000 |70m/230ft \(80% reflectivity\)<br>40m/130ft \(10% reflectivity\)|360°\*59°|\-22°C\-\+55°C|
|Luba 3 10000|70m/230ft \(80% reflectivity\)<br>40m/130ft \(10% reflectivity\)|360°\*59°|\-22°C\-\+55°C|
|Luba mini 2 LiDAR 1500|0\.1\-60m \(0\.3\-196ft\)|360°\*45°|\-10°C\-\+60°C|
|Yuka mini 2 LiDAR||360°\*45°|\-10°C\-\+60°C|

## Positioning Knowledge 

### RTK

**RTK（Real\-Time Kinematic / Antenna Over Datalink）**： This is a traditional physical local area connection mode\. The lawn mower and the RTK base station \(user\-installed\) primarily perform direct transmission and handshaking of positioning error correction data \(RTCM\) through dedicated local physical radio communication \(e\.g\., LoRa\)\. This mode does not require any internet traffic at all, but it is limited by the physical radio frequency distance between the base station and the lawn mower, and the signal can be easily blocked by physical obstacles such as thick walls\.

**LoRa（Antenna Over Datalink）**is a **local physical radio communication technology**\. In the robotic mower system, its core concept and features are as follows:

- **Core Function : **Enables point\-to\-point direct connection between the RTK base station and the mower unit, specifically responsible for transmitting positioning error correction data packets \(RTCM\) and heartbeat signals\.

- **Network\-Free : **Pure physical radio frequency transmission, completely independent of home WiFi and consuming no 4G mobile data\.

- **Physical Limitations : **Constrained by the physical distance between the base station and the mower; RF signals are easily attenuated or blocked by large physical obstacles such as thick walls and buildings\. The effective maximum range of LoRa is between 150 and 200 meters, and occasional base station disconnections may occur due to excessive distance from the base station\.

### NRTK/iNavi Service

**NRTK（Network RTK / Antenna Over Internet\):** This is an internet\-based network connection mode\. In this mode, the **RTK base station \(public base station\)** uploads error correction data to the cloud server via home WiFi, and the mower then downloads these positioning data from the cloud through its own 4G or WiFi\. It completely breaks the distance and occlusion limitations of physical radio waves, but heavily relies on the bidirectional internet connection stability between the base station and the mower end \(network fluctuations easily cause frequent disconnections\)\.

### LiDAR

**LiDAR（Light Detection and Ranging Positioning）**：An active 3D spatial perception technology\. The module on the top of the body rotates 360° to emit laser beams, and calculates the Time of Flight \(ToF\) of laser reflection to accurately measure the distance to the surrounding environment and obstacles, thereby constructing a high\-precision 3D "point cloud map" in real time in the machine's brain\. It does not rely on satellite signals from the sky at all\. In the Tri\-Fusion navigation system, when the machine drives into "signal black holes" such as extremely dense woods and high\-wall corridors where RTK satellite signals are lost, LiDAR can instantly take over navigation and continue to travel accurately relying on physical contours\.

### Vision

**Vision Positioning（Stereo Camera）：**The core lies in SLAM \(Simultaneous Localization and Mapping\) and VIO \(Visual Inertial Odometry\)\. It does not care about what specific objects are in the picture, but specifically tracks **"feature points \(such as ground texture, brick edges\)"** in consecutive image frames\. By calculating the pixel displacement of these feature points and combining with the chassis IMU \(Inertial Measurement Unit\) data, it accurately back\-calculates the machine's movement distance, rotation angle and absolute coordinates\. When the machine drives into "black hole areas" such as dense woods and deep eaves where RTK satellite signals are completely lost, visual positioning will instantly take over\. As long as the ground has rich texture, the machine can continue to "blind walk" smoothly relying on feature point tracking, perfectly eliminating positioning dead zones\.

### Comparison of four positioing methods

|**Positioning Method**|**Advantages**|**Disadvantages**|
|---|---|---|
|**RTK**|**Network\-independent :** Local physical radio direct connection, no data consumption, extremely stable connection as long as there is no occlusion\.|Occlusion\-sensitive : Base station needs to be installed by the user, and work efficiency may be affected in occluded areas<br>|
|**nRTK/iNavi**|**Distance and occlusion resistant : **Data transmitted via cloud, breaking through limitations of physical structures and transmission distance\. No need to install a private base station\.|Unstable WiFi/4G signals can also impact operational efficiency<br>|
|**LiDAR**|**Signal blackhole solution : **Active light emission for ranging and point cloud generation, satellite\-independent, seamlessly takes over navigation under trees and in corridors\.|It is prone to recognition errors in large, featureless environments|
|**Vision**|**Secondary backup line : **Captures environmental feature points to calculate displacement, enabling precise "blind navigation" without satellite signals\.|Its functionality may be restricted under pure white walls, textureless glass, or low\-light nighttime conditions<br>|



