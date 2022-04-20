import serial

print ("Active");
serialPort = serial.Serial(port = "COM5", baudrate=400000, bytesize=8, timeout=0, stopbits=serial.STOPBITS_ONE)   
serialPort.set_buffer_size(rx_size = 3) 
serialString = b'\x00';                          # Used to hold data coming over UART

#if you want to play audio in Audacity open the .txt file. if you want to graph the audio in Python, open the .csv file.
#f = open('dfs_uart.txt','wb') 
f = open('dfs_uart.csv','w') 
counter = 0



while(1):
    # Wait until there is data waiting in the serial buffer
    if(serialPort.in_waiting > 1):
        # Read data out of the buffer until a carraige return / new line is found
        serialString = serialPort.read(2)

        #if you want to play audio in Audacity, keep the next line uncommented
        #f.write(serialString)

        #if you want to graph the audio in Python, keep the next 2 lines uncommented then run faster_adc_plotting.py
        counter +=1;
        f.write(str(counter) + ","+str(int.from_bytes(serialString, byteorder='little') / 1.33)+",\n")
f.close()
