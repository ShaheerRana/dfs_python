import matplotlib.pyplot as plt
import csv
  
Names = []
Values = []
  
with open('dfs_uart.csv','r') as csvfile:
    lines = csv.reader(csvfile, delimiter=',')
    for row in lines:
        Names.append(row[0])
        Values.append(float(row[1]))
  
plt.plot(Names, Values, color = 'g')
plt.xticks(rotation = 90)
plt.xlabel('Reading')
plt.ylabel('Raw Value')
plt.title('ADC Sampling Report', fontsize = 20)
  
plt.show()
