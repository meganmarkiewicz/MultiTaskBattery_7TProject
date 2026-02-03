
import serial
from pynput.keyboard import Controller

ser = serial.Serial(
    port='COM8',\
    baudrate=19200,\
    parity=serial.PARITY_NONE,\
    stopbits=serial.STOPBITS_ONE,\
    bytesize=serial.EIGHTBITS,\
        timeout=1)

print("connected to: " + ser.portstr)
count=0

while True:
     # Read a line of data from the serial port
    data = ser.read()  # Reads one byte at a time

    if data:
     # Convert byte data to integer (ASCII value)
        received = ord(data)
        print(f"Received: {received}")

         # Check if the response matches the target_response
        if received == 54:
            print("Target response received. Closing the serial port.")
            break

        # Close the serial port
ser.close()
print("Serial port closed.")


