import serial.tools.list_ports


# Find the Arduino port
arduino_port = "/dev/ttyUSB0"

if arduino_port:
    try:
        # Open the serial connection
        serial_connection = serial.Serial(arduino_port, 9600)  # Adjust the baud rate if needed

        # Sending data to the Arduino
        data_to_send = " Indri"
        serial_connection.write(data_to_send.encode())
        print(f"Sent: {data_to_send}")

        # Close the serial connection
        serial_connection.close()
    except Exception as e:
        print(f"Error: {e}")
else:
    print("Arduino not found. Make sure it is connected and recognized by your computer.")
