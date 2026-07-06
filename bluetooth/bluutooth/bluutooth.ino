#include "BluetoothSerial.h"

// ตรวจสอบว่าเปิดใช้งาน Bluetooth หรือไม่
#if !defined(CONFIG_BT_ENABLED) || !defined(CONFIG_BLUEDROID_ENABLED)
#error Bluetooth is not enabled! Please run `make menuconfig` to and enable it
#endif

BluetoothSerial SerialBT;

void setup() {
  Serial.begin(115200);
  // ตั้งชื่อ Bluetooth ของ ESP32
  SerialBT.begin("ESP32_Bluetooth"); 
  Serial.println("The device started, now you can pair it with bluetooth!");
}

void loop() {
  // ถ้ามีข้อมูลส่งมาจาก Notebook (Bluetooth)
  if (SerialBT.available()) {
    String dataIn = SerialBT.readStringUntil('\n'); // อ่านข้อมูลจนเจอตัวขึ้นบรรทัดใหม่
    Serial.print("Received: ");
    Serial.println(dataIn);

    // ส่งข้อมูลกลับไปยัง Notebook
    SerialBT.println("Echo from ESP32: " + dataIn);
  }
  delay(20);
}