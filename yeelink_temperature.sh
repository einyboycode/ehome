sudo python /home/pi/ehome/temperature.py
curl --request POST --data-binary @"/home/pi/ehome_data/datafile.txt" --header "U-ApiKey:f790aa8e585cc5ce0cda6015a6563cec" http://api.yeelink.net/v1.0/device/7909/sensor/12707/datapoints
