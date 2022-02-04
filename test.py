import serial
print("Conversion Open")
while (1):
    string = input();


    string = string.replace(",", " +")
    print('=', string[1:-1])