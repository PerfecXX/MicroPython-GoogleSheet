# What we need 
1. Google Sheet URL. 
2. Google Sheet Page Name (not the name of file inside the Google Drive).
3. Google App Script Deployment ID. 

# How to get Google Sheet URL and Page Name
1. Create your Google Sheet https://docs.google.com/spreadsheets.
2. Copy the full URL of your sheet (for example: https://docs.google.com/spreadsheets/d/id/edit#gid=0).
3. Copy the name of your page sheet (the default is `Sheet1`).

# How to get the Google Apps Script Deployment ID
1. At the `Extensions` menu, select the `Apps Script`, and then the new Google Apps Script should be created.
2. In the Google Apps Script window, copy all of the script from `script.gs` and paste them into Google Apps Script.
3. Save the script.
4. Click the `Deploy` button, then select `New Deployment`. After that, the new deployment window should appear. 
5. On the select type menu on the left-side of the window, select `Web app`. 
6. On the configuration menu on the right-side of the window, make sure the scripts are executed by `Me (Your Email)` and who has access is set to `Anyone`.
7. Click `Deploy`.
8. Then authorize the aceess with your email (the same email as the owner of google sheet)
9. If the window shows `Google hasn’t verified this app`, select the `Advanced` menu and click Go to `<your script name> (unsafe)`. and continue to authorize the access.
10. After that, the window will show the `Deployment ID`. 
11. Copy it.

# Final Step 
Put all three credentials in your code.

