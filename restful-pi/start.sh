source mic/bin/activate
fuser -k 5000/tcp
sudo killall pigpiod
sudo pigpiod
python restful-pi/camera.py