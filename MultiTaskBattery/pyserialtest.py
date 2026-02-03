import serial

ser1 = serial.Serial(port='COM8',\
    baudrate=9600,\
        timeout=1)

while True:
    if ser1.isOpen():
        print(ser1)
        data = ser1.readline().decode().strip()

        if data:
            print("---",data)