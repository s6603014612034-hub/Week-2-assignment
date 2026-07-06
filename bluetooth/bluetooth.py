import serial
import time

# เปลี่ยน 'COM10' เป็นหมายเลข Port ของ Bluetooth ESP32 ที่เช็คจาก Windows
COM_PORT = 'COM10' 
BAUD_RATE = 115200

try:
    # เริ่มการเชื่อมต่อ Serial
    ser = serial.Serial(COM_PORT, BAUD_RATE, timeout=1)
    print(f"Connected to ESP32 on {COM_PORT}")
    time.sleep(2) # รอให้การเชื่อมต่อเสถียร

    print("Type your message and press Enter (Type 'exit' to quit):")

    while True:
        # รับค่าจากคีย์บอร์ดบน Notebook
        message = input("Send to ESP32: ")

        if message.lower() == 'exit':
            break

        # ส่งข้อมูลไปยัง ESP32 (ต้องเข้ารหัสเป็น bytes และใส่ \n)
        ser.write((message + '\n').encode('utf-8'))

        # รออ่านข้อมูลที่ ESP32 ส่งกลับมา (ถ้ามี)
        time.sleep(0.1)
        if ser.in_waiting > 0:
            response = ser.readline().decode('utf-8').strip()
            print(f"[ESP32 Response]: {response}")

    ser.close()
    print("Connection closed.")

except Exception as e:
    print(f"Error: {e}")