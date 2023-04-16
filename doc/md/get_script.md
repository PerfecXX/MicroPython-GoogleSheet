# How to get Google Apps Script 
We have to 2 method to get the Google Apps Script.
1. Copy the script from 
here: https://github.com/PerfecXX/MicroPython-GoogleSheet/blob/main/script.gs
2. Use the gen_scriptFile() function to generate the script file.
```python
from ggsheet import MicroGoogleSheet

# Google Sheet Credential 
google_sheet_url = "https://docs.google.com/spreadsheets/d/xxxxxxxxx/edit#gid=0"
google_sheet_name = "Sheet1"

ggsheet = MicroGoogleSheet(google_sheet_url,google_sheet_name)
ggsheet.gen_scriptFile()
```
After running the script, it will be saved at root (/) on your ESP32 or ESP8266, then copied to Google Apps Script.
