import datetime as dt
import serial.tools.list_ports

# Function to find the Arduino COM port
arduino_port = "/dev/ttyUSB0"

def Recolte(FeoTenaMitovy, FeoNampidirina, PercentResult):
    current_date_and_time = dt.datetime.now()
    # print( "%s , %s et %s%"%(FeoTenaMitovy, FeoNampidirina, PercentResult))
    DataAlefa= (f"{FeoTenaMitovy}, {FeoNampidirina} , {str(PercentResult)}% et {str(current_date_and_time)}")
    if arduino_port:
        try:
        # Open the serial connection
            serial_connection = serial.Serial(arduino_port, 9600)  # Adjust the baud rate if needed

            # Sending data to the Arduino
            data_to_send = DataAlefa+"\n"
            serial_connection.write(data_to_send.encode())
            print(f"Sent: {data_to_send}")

            # Close the serial connection
            serial_connection.close()
        except Exception as e:
            print(f"Error: {e}")
    else:
        print("Arduino not found. Make sure it is connected and recognized by your computer.")
    #Configure port serie arduino et envoyer data port serie
    
    
