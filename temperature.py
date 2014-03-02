#/home/pi/temperature.py
tfile = open("/sys/bus/w1/devices/28-000004f13577/w1_slave")
text = tfile.read()
tfile.close()
secondline = text.split("\n")[1]
temperaturedata = secondline.split(" ")[9]
temperature = float(temperaturedata[2:])
temperature = temperature / 1000
res = '{"value":%f}' %temperature
output = open('/home/pi/ehome_data/datafile.txt', 'w')
output.write(res)
output.close
