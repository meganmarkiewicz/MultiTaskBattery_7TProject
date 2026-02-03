from serialTokeys import Convertor
import time

l
def test_converter():
    """
    Tests the Convertor class for proper lifecycle management and functionality.
    """
    print("Creating instance of Convertor...")
    converter = Convertor()  # Instantiate the Convertor class
    
    print("Starting Convertor...")
    converter.start_serial_reader()  # Start the serial reader in the background

    print("\nSimulating main program behavior...")
    try:
        # Simulate other code running in the main thread for 10 seconds
        for i in range(200):
            print(f"Main thread running ({i+1}/200)...")
            time.sleep(1)  # Simulate work by sleeping for 1 
    except KeyboardInterrupt:
        print("\nKeyboard interrupt received. Stopping Convertor...")

    finally:
        converter.stop_serial_reader()  # Gracefully stop the serial reader
    
    print("Convertor stopped. Test complete!")


if __name__ == "__main__":
    test_converter()