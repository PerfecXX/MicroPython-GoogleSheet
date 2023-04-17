# Prerequisite
1. In this documentation, we use the Thonny IDE. If you have not installed the Thonny IDE, click [here](https://github.com/PerfecXX/MicroPython-ESP32-AIoT-DevBoard-V1/blob/9f2c6fd7d80213c013d1d448a461d4a4ce00fc06/doc/md/setup-thonny.md)
2. ESP32/ESP8266 that already installed the MicroPython firmware and connected to your device. if you not sure how to do, click [here](https://github.com/PerfecXX/MicroPython-ESP32-AIoT-DevBoard-V1/blob/9f2c6fd7d80213c013d1d448a461d4a4ce00fc06/doc/md/setup-esp32.md)

# Installation 
1. Click on the `Tools` menu,then select `Manage Packages`, and the packages manager window should appear.
2. Enter `micropython-googlesheet` in the search bar and then press enter.
3. Select the highlighted `micropython-googlesheet` (if the author is Teeraphat Kullanankanjana).
4. Click `install` and wait until the installation is complete.
5. The installed library file will be install at /lib

# Verify and Test 
1. Create new file. 
2. Then copy this code into the new file. 
```python
from ggsheet import MicroGoogleSheet 
```
3. Save it and run. 
4. If there is no error message,  the installation is complete.
5. You can proceed to the next step.
