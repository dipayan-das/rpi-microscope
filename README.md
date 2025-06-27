# Restful PI microscope
## Setup
**Use debian bullseye lite 64 bit**  
  
![image](https://github.com/user-attachments/assets/3a6092ba-0380-4876-9e7e-2a3715e8dd50)  
  
**Use the settings as follows:**  
make sure the wifi network you are choosing is not a 5ghz, and please choose wireless lan country as US  
  
![image](https://github.com/user-attachments/assets/d0276d44-c9e8-4fb3-aa3b-0aeb7f66b4fc)

## Sending the files
open a command prompt, establish a connection and then type the following to send the files to raspberry pi from PC. This will send all the files in that folder

<code>scp -r F:\rpi\rpi-microscope\restful-pi dip@raspberrypi.local:~/ </code>

to move from raspberrypi to your pc

<code>scp -r pi@raspberrypi.local:~/*.py F:\rpi\micro\restful-pi\ </code>

to delete a folder use  
  
<code>sudo rm -r rpi-microscope/ </code>

Do an apt update and apt upgrade

<code>sudo apt update  
   sudo apt upgrade </code>

then install picamera2

<code>sudo apt install -y python3-picamera2 --no-install-recommends </code>

then install opencv

<code>sudo apt install build-essential cmake git libgtk-3-dev libavcodec-dev libavformat-dev libswscale-dev </code>

<code>pip install opencv-python </code>

## Finally run the code

<code>python camera.py </code>
