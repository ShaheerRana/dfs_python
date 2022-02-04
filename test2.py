import serial

def sendSerialConsoleCmds():
    s=serial.Serial('COM5', 115200, timeout=1)
    if(serialPort.in_waiting > 0):
        s.write(('\r').encode())
        print(str(s.read(128)).replace("b'\\r\\r\\n",""))
        print(str(s.read(1000000)).replace("\\r\\n","").replace("b'","").replace("\\r",""))


while(1):
    sendSerialConsoleCmds()
