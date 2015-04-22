import subprocess
import i2cWrapper
from MPUConst import MPUConst
mpuConst  = MPUConst()

class MPU9250 :
    __i2c = i2cWrapper.i2cOpen(6, mpuConst.MPU9150Address)
    def __init__(self) :
	subprocess.call(['sh', '/eaglet/modeSettings.sh'])
        self.writeByteTo(mpuConst.RA['PWR_MGMT_1'], mpuConst.Config['PWR_MGMT_1'])
        self.writeByteTo(mpuConst.RA['GYRO_CONFIG'], mpuConst.Config['GYRO_CONFIG'])
        self.writeByteTo(mpuConst.RA['ACCEL_CONFIG'], mpuConst.Config['ACCEL_CONFIG'])

    def configure(self, powerManagementConfig1, gyroConfig, accelerometerConfig) :
        self.writeByteTo(mpuConst.RA['PWR_MGMT_1'], powerManagementConfig1)
        self.writeByteTo(mpuConst.RA['GYRO_CONFIG'], gyroConfig)
        self.writeByteTo(mpuConst.RA['ACCEL_CONFIG'], accelerometerConfig)


    def readByteFrom(self, registerAddress) :
        return i2cWrapper.i2cReadByte(self.__i2c, registerAddress)

    def writeByteTo(self, registerAddress, value) :
        return i2cWrapper.i2cWriteByte(self.__i2c, registerAddress, value)

    def getAcceleromter(self) :
        x = self.readByteFrom(mpuConst.RA['ACCEL_XOUT_H']) << 8
        x |= self.readByteFrom(mpuConst.RA['ACCEL_XOUT_L'])
        y = self.readByteFrom(mpuConst.RA['ACCEL_YOUT_H']) << 8
        y |= self.readByteFrom(mpuConst.RA['ACCEL_YOUT_L'])
        z = self.readByteFrom(mpuConst.RA['ACCEL_ZOUT_H']) << 8
        z |= self.readByteFrom(mpuConst.RA['ACCEL_ZOUT_L'])
        if x >> 15 == 1 :
            x ^= 0b1111111111111111
            x += 1
            x *= -1
        if y >> 15 == 1 :
            y ^= 0b1111111111111111
            y += 1
            y *= -1
        if z >> 15 == 1 :
            z ^= 0b1111111111111111
            z += 1
            z *= -1
        return {"x":x, "y":y, "z":z}

    def getGyro(self) :
        x = self.readByteFrom(mpuConst.RA['GYRO_XOUT_H']) << 8
        x |= self.readByteFrom(mpuConst.RA['GYRO_XOUT_L'])
        y = self.readByteFrom(mpuConst.RA['GYRO_YOUT_H']) << 8
        y |= self.readByteFrom(mpuConst.RA['GYRO_YOUT_L'])
        z = self.readByteFrom(mpuConst.RA['GYRO_ZOUT_H']) << 8
        z |= self.readByteFrom(mpuConst.RA['GYRO_ZOUT_L'])
        if x >> 15 == 1 :
            x ^= 0b1111111111111111
            x += 1
            x *= -1
        if y >> 15 == 1 :
            y ^= 0b1111111111111111
            y += 1
            y *= -1
        if z >> 15 == 1 :
            z ^= 0b1111111111111111
            z += 1
            z *= -1
        return {"x":x, "y":y, "z":z}
