import csv

f = open('sensor_data', 'r')
'''
string dataset
0.56,0.56,0.56,0.56,0.56,0.56,0.56,0.56
0.56,0.56,0.56,0.56,0.56,0.56,0.56,0.56
0.56,0.56,0.56,0.56,0.56,0.56,0.56,0.56

to floating csv dataset:
ax,ay,az,gx,gy,gz
0.56,0.56,0.56,0.56,0.56,0.56,0.56,0.56
0.56,0.56,0.56,0.56,0.56,0.56,0.56,0.56
0.56,0.56,0.56,0.56,0.56,0.56,0.56,0.56
'''
with open('sensor_data.csv', 'w', newline='') as csvfile:
    fieldnames = ['aX','aY','aZ','gX','gY','gZ']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for line in f.readlines():
        values = line.split(',')
        values = [float(v) for v in values]
        writer.writerow({'aX': values[0],
                         'aY': values[1],
                         'aZ': values[2],
                         'gX': values[3],
                         'gY': values[4],
                         'gZ': values[5] })
