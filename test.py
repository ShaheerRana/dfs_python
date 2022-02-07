'''import serial
print("Conversion Open")
while (1):
    string = input();


    string = string.replace(",", " +")
    print('=', string[1:-1])'''
f = open('dfs_uart.txt','wb') 
while(1):
    f.write(b"0x100")
f.close()
