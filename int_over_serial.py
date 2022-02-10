import serial
print ("Active");
serialPort = serial.Serial(port = "COM5", baudrate=115200, bytesize=8, timeout=0, stopbits=serial.STOPBITS_ONE)    
serialString = b'\x00';                          # Used to hold data coming over UART

while(1):
    if(serialPort.in_waiting > 0):
        serialString = serialPort.read(1)
        print (int.from_bytes(serialString, byteorder='big'))