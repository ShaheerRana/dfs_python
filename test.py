'''import serial
print("Conversion Open")
while (1):
    string = input();


    string = string.replace(",", " +")
    print('=', string[1:-1])'''
f = open('dfs_uart.txt','wb') 
a = 1
#while(1):
#f.write(a.to_bytes(1, byteorder='big'))
x = 1
while (x < 100):
    f.write((a).to_bytes(1, byteorder='big', signed=True))
    x+=1
f.close()
print ("done")