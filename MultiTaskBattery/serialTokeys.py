        
import serial
from pynput.keyboard import Controller
import threading

class Convertor:

    def __init__(self):
    

        self.keyboard = Controller()

         # Mapping of serial input integers (ASCII values) to keyboard characters
        self.key_mapping = {
            1: 'a',  # ASCII 49 (button 1) -> 'a'
            2: 's',  # ASCII 50 (button 2) -> 's'
            4: 'k',  # ASCII 51 (button 3) -> 'd'
            8: 'l',  # ASCII 52 (button 4) -> 'f'
            32: 't',  # trigger
            # Add mappings for other buttons if needed
                }

        self.running = False
        self.current_key = None
        self.thread = None

    def serial_reader(self):

        try:
            ser = serial.Serial(
            port='COM8',\
            baudrate=19200,\
            parity=serial.PARITY_NONE,\
            stopbits=serial.STOPBITS_ONE,\
            bytesize=serial.EIGHTBITS,\
            timeout=1)

            print("serial port COM(8)")
    
            while self.running:
            
                data = ser.read()  # Read one byte of data

                if data:
                    received = ord(data)  # Convert byte data to integer
                    #print(f"Received: {received}")

                    if received == 0:  # No button pressed
                        self.release_current_key()

                    elif received in self.key_mapping:  # A valid button press
                        self.hold_key(received)
            
            ser.close()
            print("Serial port closed.")

        except serial.SerialException as e:
            print(f"Serial Exception: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")
        finally:
            self.release_current_key()
    
    def hold_key(self, key_code):
        """
        Holds the key corresponding to the key_code if it's not already being held.
        """
        mapped_key = self.key_mapping[key_code]
        if self.current_key != mapped_key:  # Only press if it's a new key
            self.release_current_key()  # Release the previously held key
            print(f"Holding down key: {mapped_key}")
            self.keyboard.press(mapped_key)  # Simulate holding down the key
            self.current_key = mapped_key   # Update the current held key

    def release_current_key(self):
        """
        Releases the currently held key, if any.
        """
        if self.current_key:
            print(f"Releasing key: {self.current_key}")
            self.keyboard.release(self.current_key)
            self.current_key = None  # Reset the current key track
            
    def start_serial_reader(self):
        """
        Starts the serial reader in a background thread.
        """
        if not self.running:
            self.running = True
            self.thread = threading.Thread(target=self.serial_reader, daemon=True)
            self.thread.start()
            print("Serial reader started.")

    def stop_serial_reader(self):
        """
        Stops the serial reader.
        """

        if self.running:
            self.running = False
            if self.thread is not None:
                self.thread.join()  # Wait for the thread to finish
        print("Serial reader stopped.")
            
            
        