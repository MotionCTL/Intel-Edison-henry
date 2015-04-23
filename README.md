# Intel-Edison-henry

* ライブラリのインストール方法<br>

  1.ホストPCからHenryPackageをEdisonに以下のように転送する<br>
  scp –r HenryPackage root@(EdisonのIP):~/<br>
  2.Edison上で、以下のコマンドを実行<br>
  sh ~/HenryPackage/setup.sh<br>
  3.Edison上でサンプルを動かして動作確認<br>
  python /eaglet/sample.py<br>
  4.加速度、角加速度の値がコンソール上に表示されれば成功！<br>

* アプリ上からライブラリを使うには、アプリ上からライブラリを下記の様にimportする必要があります。

  import sys<br>
  sys.path.append(‘/eaglet/lib’)<br>
  sys.path.append(‘/eaglet/module’)<br>
* 9軸センサー（MPU9250）モジュールを以下のようにimportします<br>
  from MPU9250 import MPU9250<br>
  初期化<br>
  mpu9250 = MPU9250()<br>
  加速度センサーの値取得<br>
  accel = mpu9250.getAcceleromter()<br>
  角加速度センサーの値取得<br>
  gyro = mpu9250.getGyro()<br>
  加速度、角加速度センサーの値は辞書形式で以下のように参照できます<br>
  accelX = accel[‘x’]<br>
  gyroZ  = gyro[‘z’]<br>
* I2CWrapperの使い方<br>
  i2cWrapperをインポートします<br>
  import i2cWrapper<br>
  APIとして以下のものを提供しています<br>
  //通常busは6を指定してください<br>
  I2CContext *i2cOpen(uint8_t bus, uint8_t slaveReg)<br>
  //1バイト指定したレジストリに書き込み<br>
  bool i2cWriteByte(I2CContext *context, uint8_t reg, uint8_t value) <br>
  //指定したバイト長指定したレジストリに書き込み<br>
  bool i2cWriteBytes(I2CContext *context, uint8_t reg, uint8_t length, uint8_t data)<br>
  //1バイト指定したレジストリから読み込み<br>
  uint8_t i2cReadByte(I2CContext *context, uint8_t reg)<br>
  //指定したバイト長指定したレジストリから読み込み<br>
  bool  i2cReadBytes(I2CContext *context, uint8_t reg, uint8_t length, uint8_t *data)<br>

