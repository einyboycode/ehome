sudo python /home/pi/ehome/PiCamera.py
curl --request POST --data-binary @"/home/pi/img/capture.jpg" --header "U-ApiKey:f790aa8e585cc5ce0cda6015a6563cec"  http://api.yeelink.net/v1.0/device/7909/sensor/12695/photos
