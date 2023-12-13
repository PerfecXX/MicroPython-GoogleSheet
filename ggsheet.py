# Import Library
import urequests as requests
import ujson
import os

__version__ = '0.0.3'
__author__ = 'Teeraphat Kullanankanjana'

class MicroGoogleSheet():
    def __init__(self, googleSheetURL, sheet_name="Sheet1", deploymentID=""):
        self.sheetID = self.get_googleSheetID(googleSheetURL)
        self.sheetName = str(sheet_name)
        self.deploymentID = str(deploymentID)

    def get_googleSheetID(self, url):
        start_index = url.find('/d/') + 3
        end_index = url.find('/edit')
        sheet_id = url[start_index:end_index]
        return sheet_id

    def encoding_url(self, data):
        encoded_text = ujson.dumps(data)[1:-1]
        encoded_text = ujson.loads('"' + encoded_text + '"')
        encoded_text = encoded_text.replace('\\u', '%u')
        encoded_text = encoded_text.replace('"', '')
        encoded_text = encoded_text.replace('+', ' ')
        encoded_text = encoded_text.encode('utf-8')
        encoded_text = ''.join(['%' + ('%02X' % b) for b in encoded_text])
        return encoded_text

    def set_DeploymentID(self, deployment_id):
        self.deploymentID = str(deployment_id)

    def set_SheetName(self, sheetName):
        self.sheetName = str(sheetName)

    def updateCell(self, row=1, column=1, data=""):
        sheet_name = self.encoding_url(self.sheetName)
        mode = "updateCell"
        url = "https://script.google.com/macros/s/{}/exec?sheet_id={}&sheet_name={}&mode={}&row={}&column={}&data={}".format(
            self.deploymentID, self.sheetID, sheet_name, mode, row, column, self.encoding_url(
                str(data))
        )
        response = requests.get(url)
        response.close()
        return response.status_code

    def updateRow(self, row=1, data=[]):
        sheet_name = self.encoding_url(self.sheetName)
        mode = "updateRow"
        url = "https://script.google.com/macros/s/{}/exec?sheet_id={}&sheet_name={}&mode={}&row={}".format(
            self.deploymentID, self.sheetID, sheet_name, mode, row)
        for i in range(len(data)):
            url += "&data{}={}".format(i, self.encoding_url(str(data[i])))
        response = requests.get(url)
        response.close()
        return response.status_code

    def appendRow(self, row=0, data=[]):
        sheet_name = self.encoding_url(self.sheetName)
        mode = "appendRow"
        url = "https://script.google.com/macros/s/{}/exec?sheet_id={}&sheet_name={}&mode={}&row={}".format(
            self.deploymentID, self.sheetID, sheet_name, mode, row)
        for i in range(len(data)):
            url += "&data{}={}".format(i, self.encoding_url(str(data[i])))
        response = requests.get(url)
        response.close()
        return response.status_code

    def appendColumn(self, column=1, data=[]):
        sheet_name = self.encoding_url(self.sheetName)
        mode = "appendColumn"
        url = "https://script.google.com/macros/s/{}/exec?sheet_id={}&sheet_name={}&mode={}&column={}".format(
            self.deploymentID, self.sheetID, sheet_name, mode, column)
        for i in range(len(data)):
            url += "&data{}={}".format(i, self.encoding_url(str(data[i])))
        response = requests.get(url)
        response.close()
        return response.status_code

    def updateColumn(self, column=1, data=[]):
        sheet_name = self.encoding_url(self.sheetName)
        mode = "updateColumn"
        url = "https://script.google.com/macros/s/{}/exec?sheet_id={}&sheet_name={}&mode={}&column={}".format(
            self.deploymentID, self.sheetID, sheet_name, mode, column)
        for i in range(len(data)):
            url += "&data{}={}".format(i, self.encoding_url(str(data[i])))
        response = requests.get(url)
        response.close()
        return response.status_code

    def getCell(self, row=1, column=1):
        sheet_name = self.encoding_url(self.sheetName)
        mode = "getCell"
        url = "https://script.google.com/macros/s/{}/exec?sheet_id={}&sheet_name={}&mode={}&row={}&column={}".format(
            self.deploymentID, self.sheetID, sheet_name, mode, row, column
        )
        response = requests.get(url)
        responseCode = response.status_code

        if responseCode > 0:
            html_code = response.text
            start_index = html_code.find('start')
            end_index = html_code.find('finish')
            script_content = html_code[start_index:end_index]
            return script_content[29:-24]
        else:
            return "Error Code:{}".format(responseCode)

    def getRow(self, row=1):
        sheet_name = self.encoding_url(self.sheetName)
        mode = "getRow"
        url = "https://script.google.com/macros/s/{}/exec?sheet_id={}&sheet_name={}&mode={}&row={}".format(
            self.deploymentID, self.sheetID, sheet_name, mode, row)
        response = requests.get(url)
        responseCode = response.status_code
        if responseCode > 0:
            html_code = response.text
            start_index = html_code.find('start')
            end_index = html_code.find('finish')
            script_content = html_code[start_index:end_index]
            return script_content[29:-24]
        else:
            return "Error Code:{}".format(responseCode)

    def getColumn(self, column=1):
        sheet_name = self.encoding_url(self.sheetName)
        mode = "getColumn"
        url = "https://script.google.com/macros/s/{}/exec?sheet_id={}&sheet_name={}&mode={}&column={}".format(
            self.deploymentID, self.sheetID, sheet_name, mode, column)
        response = requests.get(url)
        responseCode = response.status_code
        if responseCode > 0:
            html_code = response.text
            start_index = html_code.find('start')
            end_index = html_code.find('finish')
            script_content = html_code[start_index:end_index]
            return script_content[29:-24]
        else:
            return "Error Code:{}".format(responseCode)
    
    def deleteCell(self,row=1,column=1):
        sheet_name = self.encoding_url(self.sheetName)
        mode = "deleteCell"
        url = "https://script.google.com/macros/s/{}/exec?sheet_id={}&sheet_name={}&mode={}&row={}&column={}".format(
            self.deploymentID, self.sheetID, sheet_name, mode, row, column)
        response = requests.get(url)
        response.close()
        return response.status_code
    
    def deleteRow(self,row=1):
        sheet_name = self.encoding_url(self.sheetName)
        mode = "deleteRow"
        url = "https://script.google.com/macros/s/{}/exec?sheet_id={}&sheet_name={}&mode={}&row={}".format(
            self.deploymentID, self.sheetID, sheet_name, mode, row)
        response = requests.get(url)
        response.close()
        return response.status_code
    
    def deleteColumn(self,column=1):
        sheet_name = self.encoding_url(self.sheetName)
        mode = "deleteColumn"
        url = "https://script.google.com/macros/s/{}/exec?sheet_id={}&sheet_name={}&mode={}&column={}".format(
            self.deploymentID, self.sheetID, sheet_name, mode, column)
        response = requests.get(url)
        response.close()
        return response.status_code

    def gen_scriptFile(self):
        code = """
/* 
Author: Teeraphat Kullanankanjana
Version: 0.0.3
*/

function doGet(e) {
  // Extract parameters from the request
  var sheet_id = e.parameter.sheet_id;
  var sheet_name = e.parameter.sheet_name;
  var mode = e.parameter.mode;
  
  // Open the spreadsheet and get the sheet
  var ss = SpreadsheetApp.openById(sheet_id);
  var sheet = ss.getSheetByName(sheet_name);
  
  // Update a single cell
  if (mode == "updateCell") {
    var row = e.parameter.row;
    var column = e.parameter.column;
    var data = e.parameter.data;
    var cell = sheet.getRange(row, column);
    cell.setValue(data);
  }
  
  // Update a row with multiple values
  else if (mode == "updateRow") {
    var row = e.parameter.row;
    var data = [];
    var count = 0;
    while (e.parameter["data" + count]) {
      count++;
    }
    for (var i = 0; i < count; i++) {
      var key = "data" + i;
      var value = e.parameter[key];
      data.push(value);
    }
    var range = sheet.getRange(row, 1, 1, data.length);
    range.setValues([data]);
  }
  
  // Append a row with multiple values
  else if (mode == "appendRow") {
    var data = [];
    var count = 0;
    while (e.parameter["data" + count]) {
      count++;
    }
    for (var i = 0; i < count; i++) {
      var key = "data" + i;
      var value = e.parameter[key];
      data.push(value);
    }

    var lastRow = sheet.getLastRow();
    var row = e.parameter.row || lastRow + 1; // If row parameter is not provided, append to last row + 1
    if (row > 0) {
      sheet.insertRowBefore(row);
      lastRow = row - 1;
    }
    sheet.getRange(lastRow + 1, 1, 1, data.length).setValues([data]);
  }
  
  // Append a column with multiple values
  else if (mode == "appendColumn") {
    var data = [];
    var count = 0;
    while (e.parameter["data" + count]) {
      count++;
    }
    for (var i = 0; i < count; i++) {
      var key = "data" + i;
      var value = e.parameter[key];
      data.push([value]); // wrap the value in an array to create a column
    }

    var lastColumn = sheet.getLastColumn();
    var column = e.parameter.column || lastColumn + 1; // If column parameter is not provided, append to last colum + 1
    if (column > 0) {
      sheet.insertColumnBefore(column);
      lastColumn = column - 1;
    }
    sheet.getRange(1, lastColumn + 1, data.length, 1).setValues(data);
  }
  
  // Update a column with multiple values
  else if (mode == "updateColumn") {
    var column = e.parameter.column;
    var data = [];
    var count = 0;
    while (e.parameter["data" + count]) {
      count++;
    }
    for (var i = 0; i < count; i++) {
      var key = "data" + i;
      var value = e.parameter[key];
      data.push([value]); // wrap the value in an array to create a column
    }
    var range = sheet.getRange(1, column, data.length, 1);
    range.setValues(data);
  }
  
  // Get the value of a specific cell
  else if (mode == "getCell") {
    var row = e.parameter.row;
    var column = e.parameter.column;

    var cell = sheet.getRange(row, column);
    var value = cell.getValue();

    var html = "<html><head><title>Get The data </title></head><body><h1>start</h1><h1>" + value + "</h1><h1>finish</h1></body></html>";
    return HtmlService.createHtmlOutput(html);
  }
  
  // Get the values of a specific row
  else if (mode == "getRow") {
  var row = e.parameter.row;
  var range = sheet.getRange(row, 1, 1, sheet.getLastColumn());
  var values = range.getValues()[0];

  var heading = "";
  for (var i = 0; i < values.length; i++) {
    heading += values[i] + " ";
  }

  var html = "<html><head><title>Get Row Data</title></head><body><h1>start</h1><h1>" + heading + "</h1><h1>finish</h1></body></html>";
  return HtmlService.createHtmlOutput(html);
}
 
 // Get the values of a specific column
else if (mode == "getColumn") {
  var column = e.parameter.column;
  var range = sheet.getRange(1, column, sheet.getLastRow(), 1);
  var values = range.getValues();
  var heading = "";
  for (var i = 0; i < values.length; i++) {
    heading += values[i] + " ";
  }

  var html = "<html><head><title>Get Column Data</title></head><body><h1>start</h1><h1>" + heading + "</h1><h1>finish</h1></body></html>";
  return HtmlService.createHtmlOutput(html);
  
}
  
  // Delete a specific row
else if (mode == "deleteRow") {
  var row = e.parameter.row;
  sheet.deleteRow(row);
}

// Delete a specific column
else if (mode == "deleteColumn") {
  var column = e.parameter.column;
  sheet.deleteColumn(column);
}

// Clear the content of a specific cell
else if (mode == "deleteCell") {
  var row = e.parameter.row;
  var column = e.parameter.column;
  var cell = sheet.getRange(row, column);
  cell.clearContent();
}
}
        """
        with open('script.txt', 'w') as file:
            file.write(code)

