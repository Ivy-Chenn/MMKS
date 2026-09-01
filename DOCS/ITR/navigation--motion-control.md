#Navigation & Motion Control Troubleshooting

## **Cross-Zone Recharge Issue** - Path Blocked / Work Stuck

**Error Code:**

- 1214 Path blocked

**Solution:**

1. Check whether the path at the stuck location is too close to obstacles.
2. Consider moving the obstacles away or redrawing the path to avoid the obstacles.

**Query Page:**

1. Check Basic Info to confirm the current positioning mode of the robot.
2. Check the Device Profile and Self-check modules to confirm whether the robot's hardware connections are normal.
3. Based on the corresponding error code, preliminarily determine the type and possible cause of the robot's fault.

**If not solved:**
 `Needs FAE Upgrade`

---

## **Cross-Zone Recharge Issue** - Cross-Zone Recharge Failed

**Error Code:**

- 1203 Return-to-dock failed

**Solution:**

1. Check whether the error code includes a path-blocked error.
2. Move the path obstacles away or redraw the path to avoid the obstacles.

**Query Page:**

1. Check Basic Info to confirm the current positioning mode of the robot.
2. Check the Device Profile and Self-check modules to confirm whether the robot's hardware connections are normal.
3. Based on the corresponding error code, preliminarily determine the type and possible cause of the robot's fault.

**If not solved:**
 `Needs FAE Upgrade`

---

## **Auto-Recharge Issue** - Recharge Failed

**Error Code:**

- 1200 Return-to-dock failed

**Solution:**

1. Check whether the charging station is placed on a level surface.
2. Place the mower about 1m in front of the dock and manually trigger return-to-dock to check whether it works abnormally.
3. Clear obstacles in the charging station area, ensuring no obstacles within a 2x2m range.
4. Use an Android phone to check the charging station's IR signal. If there is no signal, send a replacement charging station.

**Query Page:**

1. Check Basic Info to confirm the current positioning mode of the robot.
2. Check the Device Profile and Self-check modules to confirm whether the robot's hardware connections are normal.
3. Based on the corresponding error code, preliminarily determine the type and possible cause of the robot's fault.

**If not solved:**
 `Needs Repair`

---

## **Auto-Recharge Issue** - Recharge Failed

**Solution:**

1. Check whether there are any wheel hub motor / cutter motor errors in the app.

**Query Page:**

1. Check Basic Info to confirm the current positioning mode of the robot.
2. Check the Device Profile and Self-check modules to confirm whether the robot's hardware connections are normal.
3. Based on the corresponding error code, preliminarily determine the type and possible cause of the robot's fault.

**If not solved:**
 `Needs FAE Upgrade`

---

## **Entered No-Go Zone** - Entered No-Go Zone During Mowing, No Positioning Signal Issue

**Solution:**

/

**If not solved:**
 `Needs FAE Upgrade`

---

## **Crossed Virtual Wall** - Device Crossed Virtual Wall Set on Map

**Solution:**

/

**If not solved:**
 `Needs FAE Upgrade`

---

## **Task Interrupted** - Lawn Damaged During Mowing

**Solution:**

1. Check whether there are any motor-related errors in the app.
2. Restart the mower and check whether operation is normal.
3. Check whether the lawn is too wet. If so, consider not mowing the slippery area for the time being.

**Query Page:**

1. Check Basic Info to confirm the current positioning mode of the robot.
2. Check the Device Profile and Self-check modules to confirm whether the robot's hardware connections are normal.
3. Based on the corresponding error code, preliminarily determine the type and possible cause of the robot's fault.

**If not solved:**
 `Needs FAE Upgrade`

---

## **Task Interrupted** - Spinning / Grinding Lawn

**Solution:**

1. Check whether there are any motor-related errors in the app.

**Query Page:**

1. Check Basic Info to confirm the current positioning mode of the robot.
2. Check the Device Profile and Self-check modules to confirm whether the robot's hardware connections are normal.
3. Based on the corresponding error code, preliminarily determine the type and possible cause of the robot's fault.

**If not solved:**
 `Needs FAE Upgrade`

---

## **Task Interrupted** - Slipped During Work / Out of Boundary / Entered No-Go Zone and Stopped

**Solution:**

1. Check whether there is terrain on the boundary or in the no-go zone that is slippery or has a steep slope.
2. Adjust the map or the no-go zone boundary accordingly.

**Query Page:**

1. Check Basic Info to confirm the current positioning mode of the robot.
2. Check the Device Profile and Self-check modules to confirm whether the robot's hardware connections are normal.
3. Based on the corresponding error code, preliminarily determine the type and possible cause of the robot's fault.

**If not solved:**
 `Needs FAE Upgrade`

---

## **Robot Stuck** - Robot Got Stuck During Work

**Error Code:**

- 1201 Stuck

**Solution:**

1. Check whether there is terrain on the boundary or in the no-go zone that is slippery or has a steep slope.
2. Check whether the issue is improved after enabling the obstacle-avoidance mode.

**Query Page:**

1. Check Basic Info to confirm the current positioning mode of the robot.
2. Check the Device Profile and Self-check modules to confirm whether the robot's hardware connections are normal.
3. Based on the corresponding error code, preliminarily determine the type and possible cause of the robot's fault.

**If not solved:**
 `Needs FAE Upgrade`

---

## **Missed Mowing** - Grass Not Mowed / Missed Mowing / Grass Left in Middle

**Solution:**

1. Change the settings to cover missed grass strips. Set checkerboard mowing and set the cross pattern to a diamond. Adjust the path spacing to 20-15cm.

**If not solved:**
 `Needs Repair`

---

## **Missed Mowing** - No-Go Zone Edge Missed

**Solution:**

1. Confirm whether the no-go zone boundary-patrol function is enabled.

**If not solved:**
 `Needs FAE Upgrade`

---

## **Missed Mowing** - Mowing Zone Edge Missed

**Solution:**

1. Check whether there are stuck-detection or other errors. Prioritize troubleshooting as a stuck issue.
2. Confirm whether the mowing zone boundary-patrol function is enabled.

**If not solved:**
 `Needs FAE Upgrade`

---

## **Mowing Path Not Straight** - Mowing Path Not Straight on Flat Lawn

**Solution:**

/

**If not solved:**
 `Needs FAE Upgrade`

---

## **Device Dropped** - Device Fell into Pond / Water Area

**Solution:**

1. Verify the environment and location of the falling-into-water incident.

**If not solved:**
 `Needs FAE Upgrade`

---

## **Device Dropped** - Device Fell Off Cliff

**Solution:**

1. Check whether the current firmware is the latest version. An upgrade is required if not.
2. Set a virtual wall at the cliff location, and move the boundary inward. Test whether the issue is resolved.

**If not solved:**
 `Needs FAE Upgrade`

---

