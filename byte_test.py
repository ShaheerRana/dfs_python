import serial
import binascii
print ("Active");
serialPort = serial.Serial(port = "COM5", baudrate=115200, bytesize=8, timeout=0, stopbits=serial.STOPBITS_ONE)    
serialString = b'\x00';                          # Used to hold data coming over UART
#f = open('dfs_uart.txt','wb') 
#f.write(b"0x100")

while(1):

    # Wait until there is data waiting in the serial buffer
    if(serialPort.in_waiting > 0):

        # Read data out of the buffer until a carraige return / new line is found
        #serialString = serialPort.readline()
        serialString = (serialPort.read(1)[0] << 8) | serialPort.read(1)

        #print (bin(int.from_bytes(serialString, byteorder='big')))
        print (serialString)
        #f.write(serialString)

        # Tell the device connected over the serial port that we recevied the data!
        # The b at the beginning is used to indicate bytes!
        #serialPort.write(b"Thank you for sending data \r\n")
#f.close()
