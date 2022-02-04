import serial
import binascii
print ("Active");
serialPort = serial.Serial(port = "COM5", baudrate=115200, bytesize=8, timeout=0, stopbits=serial.STOPBITS_ONE)    
serialString = 0;                          # Used to hold data coming over UART

while(1):

    # Wait until there is data waiting in the serial buffer
    if(serialPort.in_waiting > 0):
        f = open('dfs_uart.txt','a') 

        # Read data out of the buffer until a carraige return / new line is found
        serialString = serialPort.readline()
        #serialString = serialPort.read(128).replace("b'\\r\\r\\n","")
        # Print the contents of the serial data
        #print(serialString.decode('Ascii'))
        #print(binascii.hexlify(serialString))
        #print(int(binascii.hexlify(serialString),16))
        print (ord(serialString))

        #f.write(serialString.decode('Ascii'))

        # Tell the device connected over the serial port that we recevied the data!
        # The b at the beginning is used to indicate bytes!
        serialPort.write(b"Thank you for sending data \r\n")
        f.close()
    