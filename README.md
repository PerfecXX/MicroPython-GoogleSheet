# MicroPython-GoogleSheet

[![Version](https://img.shields.io/badge/version-0.0.3-blue.svg)](https://github.com/PerfecXX/MicroPython-GoogleSheet)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)

Update or append the data to Google Sheet, or get the data on Google Sheet.  
By using HTTP to execute the Google Apps Script API.  
Compatible with ESP32 and ESP8266.

# Getting Started
- [Installation](https://github.com/PerfecXX/MicroPython-GoogleSheet/blob/main/doc/md/installation.md)
- [How to get your google credential](https://github.com/PerfecXX/MicroPython-GoogleSheet/blob/main/doc/md/get_google_credential.md)
- [API](https://github.com/PerfecXX/MicroPython-GoogleSheet/wiki)

# Quick Example 
```python
# Import Library 
from ggsheet import MicroGoogleSheet
from network import WLAN,STA_IF

# Network Creadential 
ssid = "Change_SSID"    
password = "Change_Password"

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

# Update the data to a specific cell (Row,Column,Data)
ggsheet.updateCell(1,1,"Hello this is my first data")

# Get the data from a specific cell (Row,Column)
print(ggsheet.getCell(1,1))

# Delete the data from a specific cell (Row,Column)
ggsheet.deleteCell(1,1)

# Append the data to a specific row (Row, Data List)
ggsheet.appendRow(1,[1,2,3,"Row 1 Appended!"])

# Update the data in a specific row (Row, Data List) 
ggsheet.updateRow(1,[3,2,1,"Row 1 Updated!"])

# Get all of the data from a specific row (Row)
print(ggsheet.getRow(1))

# Delete the data in a specific row (Row)
ggsheet.deleteRow(1)

# Append the data to a specific column (Column, Data List)
ggsheet.appendColumn(1,[1,2,3,"Column 1 Appended!"])

# Update the data to a specific column (Column, Data List)
ggsheet.updateColumn(1,[3,2,1,"Column 1 Updated!"])

# Get all of the data from a specific column (Column)
print(ggsheet.getColumn(1))

# Delete the data in a specific column (Column)
ggsheet.deleteColumn(1) 
```
