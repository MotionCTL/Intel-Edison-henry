class MPUConst :
    MPU9150Address = 0x68
    RA = {
        "PWR_MGMT_1"   : 0x6B,
        "GYRO_CONFIG"  : 0x1B,
        "ACCEL_CONFIG" : 0x1C,
        "ACCEL_XOUT_H" : 0x3B,
        "ACCEL_XOUT_L" : 0x3C,
        "ACCEL_YOUT_H" : 0x3D,
        "ACCEL_YOUT_L" : 0x3E,
        "ACCEL_ZOUT_H" : 0x3F,
        "ACCEL_ZOUT_L" : 0x40,
        "GYRO_XOUT_H"  : 0x43,
        "GYRO_XOUT_L"  : 0x44,
        "GYRO_YOUT_H"  : 0x45,
        "GYRO_YOUT_L"  : 0x46,
        "GYRO_ZOUT_H"  : 0x47,
        "GYRO_ZOUT_L"  : 0x48,
    }

    Config = {
        "PWR_MGMT_1"    : 0x01,
        "GYRO_CONFIG"   : 0x08,
        "ACCEL_CONFIG"  : 0x08
    }
