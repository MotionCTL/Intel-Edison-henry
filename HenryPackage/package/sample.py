import sys
sys.path.append('/eaglet/lib')
sys.path.append('/eaglet/module')
from MPU9250 import MPU9250
from pprint import pprint
import time

mpu9250  = MPU9250()

while True :
    accel = mpu9250.getAcceleromter()
    gyro  = mpu9250.getGyro()
    print("Acceleromter : %5d, %5d, %5d" % (accel['x'], accel['y'], accel['z']))
    print("Gyro         : %5d, %5d, %5d" % (gyro['x'], gyro['y'], gyro['z']))
    time.sleep(0.05)