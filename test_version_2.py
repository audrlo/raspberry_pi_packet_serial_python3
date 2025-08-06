from roboclaw import Roboclaw
import time

roboclaw = Roboclaw("/dev/ttyACM0", 115200)
roboclaw.Open()

address = 0x80

result, version = roboclaw.ReadVersion(address)
print("Success:", result)
print("Version:", version)

roboclaw.ForwardM1(address, 64)  # Half speed
print("Move???")
time.sleep(2)
roboclaw.ForwardM1(address, 0)   # Stop
print("stopped")

# Check voltage
status, volts = roboclaw.ReadMainBatteryVoltage(address)
print("Battery voltage:", volts / 10.0, "V")

# Try using signed duty mode
print("Trying DutyM1...")
roboclaw.DutyM1(address, 32767)
roboclaw.DutyM2(address, -32767)
for i in range(40):
    print(roboclaw.ReadSpeedM1(address)[1] + roboclaw.ReadSpeedM2(address)[1])
    time.sleep(0.05)
roboclaw.DutyM1(address, 0)
roboclaw.DutyM2(address, 0)
print("Done.")

time.sleep(5)

print("Trying Speed")
roboclaw.SpeedM1(address, 10000)  # 10k encoder ticks/sec
roboclaw.SpeedM2(address, -10000)
for i in range(100):
    print(roboclaw.ReadSpeedM1(address)[1] + roboclaw.ReadSpeedM2(address)[1])
    time.sleep(0.05)
roboclaw.SpeedM1(address, 0)
roboclaw.SpeedM2(address, 0)
print("Done")
