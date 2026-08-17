#Positioning Troubleshooting

##Positioning Issue - Poor Positioning, Environmental Issue

**Error Code:**

- 1300 Poor positioning status
- 1303/1304

**Solution:**

1. Check whether the RTK base station is properly powered on; if the RTK base station is abnormal, try to send a replacement.
2. Determine the user's region. For users in Europe / the UK, consider upgrading the firmware and manually upgrading the RTK.

**Query Page:**

1. Check Basic Info to confirm the current positioning mode of the robot.
2. Check the Device Profile and Self-check modules to confirm whether the robot's hardware connections are normal.
3. Based on the corresponding error code, preliminarily determine the type and possible cause of the robot's fault.

**If not sloved:**
 `Needs FAE Upgrade`

---

##Positioning Issue - Positioning Calibration Failed

**Error Code:**

- 1300 Poor positioning status
- 1314 Poor positioning accuracy

**Solution:**

1. Check whether the error only occurs near the boundary.
2. Manually drive the mower away from the boundary to an open working area.
3. Check whether there are any other errors in the app.

**Query Page:**

1. Check Basic Info to confirm the current positioning mode of the robot.
2. Check the Device Profile and Self-check modules to confirm whether the robot's hardware connections are normal.
3. Based on the corresponding error code, preliminarily determine the type and possible cause of the robot's fault.

**If not sloved:**
 `Needs FAE Upgrade`

---

##Positioning Issue - App Vehicle Position Offset

**Solution:**

1. Check whether the app and the firmware are the latest versions.

**Query Page:**

1. Check Basic Info to confirm the current positioning mode of the robot.
2. Check the Device Profile and Self-check modules to confirm whether the robot's hardware connections are normal.
3. Based on the corresponding error code, preliminarily determine the type and possible cause of the robot's fault.

**If not sloved:**
 `Needs FAE Upgrade`

---

##Positioning Issue - Positioning Error / Station Position Offset / POS Not Good

**Solution:**

1. Confirm whether the RTK base station is bound.
2. Confirm whether the firmware is the latest version, and whether the RTK is properly powered on.
3. Check that the link mode of the mower and the RTK are consistent.
4. Ensure that the RTK LoRa number in the app matches the one on the RTK body label.
5. If the above checks pass but the issue persists, replace the RTK.

**Query Page:**

1. Check Basic Info to confirm the current positioning mode of the robot.
2. Check the Device Profile and Self-check modules to confirm whether the robot's hardware connections are normal.
3. Based on the corresponding error code, preliminarily determine the type and possible cause of the robot's fault.

**If not sloved:**
 `Needs FAE Upgrade`

---

##Docking Issue - Cannot Exit Station to Auto-Work

**Solution:**

1. Check whether the charging station is located in an open area.
2. Check whether the RTK base station is properly powered on; if not, replace the base station and re-test.

**Query Page:**

1. Check Basic Info to confirm the current positioning mode of the robot.
2. Check the Device Profile and Self-check modules to confirm whether the robot's hardware connections are normal.
3. Based on the corresponding error code, preliminarily determine the type and possible cause of the robot's fault.

**If not sloved:**
 `Needs Repair`

---

##Docking Issue - App Shows Device Not in Work Zone but Actually Charging

**Solution:**

1. Check the surroundings of the charging station's location for any obstructions such as trees / walls / buildings; it should be installed in an open area.
2. Verify the applicable positioning mode. If it is RTK, check whether the RTK base station installation position has any obstructions.

**If not sloved:**
 `Needs FAE Upgrade`

---

##Docking Issue - Stops in Front of Station After Exiting

**Error Code:**

- 1105 Mower stops in front of the dock after leaving it

**Solution:**

1. Check the surroundings of the charging station's location for any obstructions such as trees / walls / buildings; it should be installed in an open area.
2. Verify the applicable positioning mode. If it is RTK, check whether the RTK base station installation position has any obstructions.

**Query Page:**

1. Check Basic Info to confirm the current positioning mode of the robot.
2. Check the Device Profile and Self-check modules to confirm whether the robot's hardware connections are normal.
3. Based on the corresponding error code, preliminarily determine the type and possible cause of the robot's fault.

**If not sloved:**
 `Needs FAE Upgrade`

---

##RTK - RTK Base Station Disconnected

**Error Code:**

- 1551 RTK disconnection alarm

**Solution:**

1. Verify that the positioning modes of the robot and the RTK base station are consistent.
2. Verify that the LoRa numbers of the robot and the RTK are consistent; if they differ, change them to be consistent.
3. Verify that both the robot and the RTK have a satellite count. If the robot's satellite count is 0, try restarting the device multiple times. If the RTK base station's satellite count is 0, check the RTK base station indicator status.
4. If the RTK base station indicator is abnormal, check the power cable interface on the back of the charging station. If the interface is normal, replace the RTK adapter; if the interface is faulty, perform a defective product return.

**If not sloved:**
 `Needs Repair`

---

##RTK - RTK Indicator Light Abnormal

**Solution:**

1. Check whether the indicator is off only at night. After the upgrade, this is normal.
2. If the indicator is also off during the daytime, try other power supply options (charging station / RTK adapter).
3. If the RTK adapter power supply works normally, check whether the interface on the charging station that connects to the base station is damaged.
4. If the charging station power supply works normally, send a replacement RTK adapter.
5. If neither option works normally, send a replacement RTK.

**If not sloved:**
 `Needs Repair`

---

##RTK - RTK Solid Red / Flashing Red Light

**Solution:**

1. Check whether the RTK works normally after being powered on again.
2. If the issue persists, send a replacement base station.

**If not sloved:**
 `Needs Repair`

---

##RTK - RTK Light Off, No Satellite Signal, Needs Restart

**Solution:**

1. Check whether both the mower and the RTK firmware are the latest versions.

**If not sloved:**
 `Needs Repair`

---

##RTK - Cannot Connect After RTK-LoRa Mode Switch

**Solution:**

1. Check whether the RTK can be added manually; if it is not bound, add it again.
2. Check that the link mode of the mower and the RTK are consistent; they need to be set to the same mode.

**If not sloved:**
 `Needs Repair`

---

##RTK - App Cannot Connect to RTK / RTK Cannot Connect to WiFi

**Solution:**

1. Check whether the Wi-Fi is a 2.4GHz or 2.4/5GHz network/hotspot. If not, switch to one of these bands.
2. Check whether the Wi-Fi router has encryption-level restrictions or insufficient IP address pool.

**If not sloved:**
 `Needs Repair`

---

##RTK - App Cannot Connect to RTK / Bluetooth Connection Failed

**Solution:**

1. Check the RTK indicator and troubleshoot any Wi-Fi / Bluetooth / 4G issues.
2. You can try connecting to the RTK via Bluetooth from another phone. Android phones can use the built-in Bluetooth search function; iPhones can use a BLE scanner or another Bluetooth-scanning app to scan.

**If not sloved:**
 `Needs Repair`

---

##RTK Adapter - RTK Power Adapter Indicator Light Abnormal

**Solution:**

1. Confirm that the power socket is supplying power normally.
2. Cross-verify: the RTK base station supports power supply from the RTK adapter and from the charging station's power port.
3. Confirm the indicator status.

**If not sloved:**
 `Needs Repair`

---

##RTK Adapter - RTK Power Adapter Voltage Abnormal

**Solution:**

1. Check / test that the voltage of the RTK power adapter is approximately the normal 12V.

**If not sloved:**
 `Needs Repair`

---

##iNavi - Positioning No Response

**Error Code:**

- 1000020 No response from positioning

**Solution:**

1. Check whether the firmware is the latest version; if not, it needs to be updated.

**Query Page:**

1. Check Basic Info to confirm the current positioning mode of the robot.
2. Check the Device Profile and Self-check modules to confirm whether the robot's hardware connections are normal.
3. Based on the corresponding error code, preliminarily determine the type and possible cause of the robot's fault.

**If not sloved:**
 `Needs FAE Upgrade`

---

##iNavi - Positioning Failed

**Error Code:**

- 1000019 Positioning failed

**Solution:**

1. Confirm whether the error is reported when mapping outside the zone; mapping can only be started inside the zone or on the charging station.
2. The firmware needs to be upgraded to the latest version.

**Query Page:**

1. Check Basic Info to confirm the current positioning mode of the robot.
2. Check the Device Profile and Self-check modules to confirm whether the robot's hardware connections are normal.
3. Based on the corresponding error code, preliminarily determine the type and possible cause of the robot's fault.

**If not sloved:**
 `Needs FAE Upgrade`

---

##iNavi - Vehicle Lost Positioning in Narrow Path/Zone

**Error Code:**

- 1314 Poor positioning accuracy
- 1300 Obstruction in working environment

**Solution:**

1. Check whether the firmware is the latest version; if not, it needs to be updated.

**Query Page:**

1. Check Basic Info to confirm the current positioning mode of the robot.
2. Check the Device Profile and Self-check modules to confirm whether the robot's hardware connections are normal.
3. Based on the corresponding error code, preliminarily determine the type and possible cause of the robot's fault.

**If not sloved:**
 `Needs FAE Upgrade`

---

##iNavi - iNavi Positioning Signal Weak

**Error Code:**

- 1314 Poor positioning accuracy
- 1554 Unstable Wi-Fi network
- 1556 Unstable 4G network

**Solution:**

1. Confirm whether the iNavi connection mode is Wi-Fi or 4G (both can be used at the same time, but iNavi takes priority).
2. Cross-verify by switching between the two.

**Query Page:**

1. Check Basic Info to confirm the current positioning mode of the robot.
2. Check the Device Profile and Self-check modules to confirm whether the robot's hardware connections are normal.
3. Based on the corresponding error code, preliminarily determine the type and possible cause of the robot's fault.

**If not sloved:**
 `Needs FAE Upgrade`

---

##iNavi - Positioning Timeout / Map Distorted / No Response

**Error Code:**

- 1418 Positioning timeout

**Solution:**

1. Check whether the firmware is the latest version; if not, it needs to be updated.

**Query Page:**

1. Check Basic Info to confirm the current positioning mode of the robot.
2. Check the Device Profile and Self-check modules to confirm whether the robot's hardware connections are normal.
3. Based on the corresponding error code, preliminarily determine the type and possible cause of the robot's fault.

**If not sloved:**
 `Needs FAE Upgrade`

---

##iNavi - Satellite Map Offset

**Solution:**

1. Check whether the firmware is the latest version; if not, it needs to be updated.

**Query Page:**

1. Check Basic Info to confirm the current positioning mode of the robot.
2. Check the Device Profile and Self-check modules to confirm whether the robot's hardware connections are normal.
3. Based on the corresponding error code, preliminarily determine the type and possible cause of the robot's fault.

**If not sloved:**
 `Needs FAE Upgrade`

---

##iNavi - iNavi Network Unstable / 4G or WiFi Connection Abnormal

**Error Code:**

- 1554 Network error
- 1556 iNavi network connection abnormal

**Solution:**

1. Check the Wi-Fi and 4G network. If the signal is poor, try connecting to another network or use the phone's hotspot.

**Query Page:**

1. Check Basic Info to confirm the current positioning mode of the robot.
2. Check the Device Profile and Self-check modules to confirm whether the robot's hardware connections are normal.
3. Based on the corresponding error code, preliminarily determine the type and possible cause of the robot's fault.

**If not sloved:**
 `Needs FAE Upgrade`

---

##iNavi - POS Status Single

**Solution:**

1. Check whether the app and the firmware are the latest versions.
2. Check the network signal. Consider switching to 4G or another Wi-Fi network, then try restarting the device and re-connecting to iNavi.
3. If the issue is not network-related, switch the link mode to another option, then switch back to iNavi, and restart the device.

**Query Page:**

1. Check Basic Info to confirm the current positioning mode of the robot.
2. Check the Device Profile and Self-check modules to confirm whether the robot's hardware connections are normal.
3. Based on the corresponding error code, preliminarily determine the type and possible cause of the robot's fault.

**If not sloved:**
 `Needs FAE Upgrade`

---

##Positioning Issue - Map Distorted / Offset / Path Missing / Station Position Offset

**Error Code:**

- 1300/1000019

**Solution:**

1. Provide photos of the charging station's location and the surrounding environment.

**Query Page:**

1. Check Basic Info to confirm the current positioning mode of the robot.
2. Check the Device Profile and Self-check modules to confirm whether the robot's hardware connections are normal.
3. Based on the corresponding error code, preliminarily determine the type and possible cause of the robot's fault.

**If not sloved:**
 `Needs FAE Upgrade`

---

##Positioning Issue - Positioning No Response

**Error Code:**

- 1000020 No response from positioning

**Solution:**

1. Provide photos of the on-site and surrounding environment.
2. Provide a screenshot of the error in the app.
3. Update the firmware and the app to the latest versions.
4. Try restarting the device. If restarting does not resolve the issue, delete the map and re-draw it, or restore factory settings (and remind the user that this requires re-binding and reconfiguring the device).

**Query Page:**

1. Check Basic Info to confirm the current positioning mode of the robot.
2. Check the Device Profile and Self-check modules to confirm whether the robot's hardware connections are normal.
3. Based on the corresponding error code, preliminarily determine the type and possible cause of the robot's fault.

**If not sloved:**
 `Needs FAE Upgrade`

---

##Positioning Issue - Positioning Lost / Map Drawing Failed

**Error Code:**

- 1315 Mapping failed due to positioning loss

**Solution:**

1. Collect the camera status, on-site environment, app error, firmware version, and restart information for troubleshooting.
2. Check whether the protective film on the lens was forgotten to be removed.

**Query Page:**

1. Check Basic Info to confirm the current positioning mode of the robot.
2. Check the Device Profile and Self-check modules to confirm whether the robot's hardware connections are normal.
3. Based on the corresponding error code, preliminarily determine the type and possible cause of the robot's fault.

**If not sloved:**
 `Needs FAE Upgrade`

---

##Positioning Issue - Charging Station Position Change Detected

**Error Code:**

- 1132 Charging station position change detected

**Solution:**

1. Check the on-site environment and the app error, and confirm whether any obstacles or objects near the charging station have been moved.
2. If any object has been moved, re-position the charging station.

**Query Page:**

1. Check Basic Info to confirm the current positioning mode of the robot.
2. Check the Device Profile and Self-check modules to confirm whether the robot's hardware connections are normal.
3. Based on the corresponding error code, preliminarily determine the type and possible cause of the robot's fault.

**If not sloved:**
 `Needs FAE Upgrade`

---

##Positioning Issue - Positioning Timeout / Map Distorted / No Response

**Error Code:**

- 1418 Positioning timeout

**Solution:**

1. Provide photos of the on-site and surrounding environment.
2. Provide a screenshot of the error in the app.
3. Update the firmware and the app to the latest versions.
4. Try restarting the device. If restarting does not resolve the issue, delete the map and re-draw it, or restore factory settings (and remind the user that this requires re-binding and reconfiguring the device).

**Query Page:**

1. Check Basic Info to confirm the current positioning mode of the robot.
2. Check the Device Profile and Self-check modules to confirm whether the robot's hardware connections are normal.
3. Based on the corresponding error code, preliminarily determine the type and possible cause of the robot's fault.

**If not sloved:**
 `Needs FAE Upgrade`

---

