# MicroPython-GoogleSheet
Update or append the data to Google Sheet, or get the data on Google Sheet.  
By using HTTP to execute the Google Apps Script API.  
Compatible with ESP32 and ESP8266.

# Quick Example 
```python
# Import Library 
from ggsheet import MicroGoogleSheet
from network import WLAN,STA_IF

# Network Creadential 
ssid = "Change SSID"    
password = "Change Password"

# Connect to Network
sta_if = WLAN(STA_IF)
sta_if.active(True)
if not sta_if.isconnected():
    print("Connecting to wifi: ", ssid)
    sta_if.connect(ssid, password)
    while not sta_if.isconnected():
        pass
print("Connection successful")

# Google Sheet Credential 
google_sheet_url = "https://docs.google.com/spreadsheets/d/xxxxxxxxx/edit#gid=0"
google_sheet_name = "Sheet1"
google_app_deployment_id = "xxxxxxxx"

# Create Instance 
ggsheet = MicroGoogleSheet(google_sheet_url,google_sheet_name)
ggsheet.set_DeploymentID(google_app_deployment_id)

# create the Google App Script file (not necessary if it already exists).
ggsheet.gen_scriptFile()

# Update the cell (single data into a single cell)
ggsheet.updateCell(1,1,"Hello this is my first data")

# Get the data from specific cell 
print(ggsheet.getCell(1,1))

# Append the row (many data into a single row)
ggsheet.updateRow(1,[1,2,3,"Hello","สวัสดีครับ"])

# Get all the data from a specific row
print(ggsheet.getRow(1))
```

# Getting Started
- [Installation](https://github.com/PerfecXX/MicroPython-GoogleSheet/blob/main/doc/md/installation.md)
- [How to get your google credential](https://github.com/PerfecXX/MicroPython-GoogleSheet/blob/main/doc/md/get_google_credential.md)
- [Example]()
