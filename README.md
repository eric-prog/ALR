# ALR - 📽️ Autonomous Lecture Recorder 

Recorded lectures serve as invaluable learning resources for university students. As of today, the mere positioning of a camera at the back of a hall to capture the entire board falls short of delivering an optimal viewing experience of the recorded lectures, since deciphering the professor's writing can be a challenge. Thus, what holds the potential to be an exceptional educational tool instead morphs into a source of frustration and ineffectiveness for learners. <br>

The Autonomous Lecture Recorder (ALR), can be placed in the front row, thus removing the need to zoom in and increasing video quality.

### 🌊 Get Started

1. Clone the repo on your Raspberry Pi:
```
git clone https://github.com/eric-prog/ALR.git
```

2. Navigate to the project in the terminal: 

```
sudo apt-get update    
sudo apt-get upgrade
pip install opencv-python
pip3 install opencv-python
```

3. Input the following in a Python file and run on [Geany](https://raspberrytips.com/use-geany-on-raspberry-pi/):

```
import os
os.system("sudo apt update")
os.system("sudo apt upgrade")
os.system("python3 --version")
os.system("sudo apt-get install python3-pip")
os.system("pip3 install numpy")
os.system("pip3 install opencv-python")
os.system("pip3 install pyserial")
os.system("sudo apt install fswebcam")
os.system("sudo apt install linux-tools-virtual hwdata")
os.system("sudo update-alternatives --install /usr/local/bin/usbip usbip ls /usr/lib/linux-tools/*/usbip | tail -n1 20")
```
> **_NOTE:_**  After installation may need to reboot/restart the Raspberry Pi

3. Open the main.py using [Geany](https://raspberrytips.com/use-geany-on-raspberry-pi/) and run the [detect.py file](https://github.com/eric-prog/ALR/blob/main/detect.py)! 

</br>

###### SE101 Final Project Group 9 (2023) / Code by Eric Sheen
