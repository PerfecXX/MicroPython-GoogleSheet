import urequests as requests
import ujson
import os

class MicroGoogleSheet():
    def __init__(self, googleSheetURL, sheet_name="Sheet1", deploymentID=""):
        self.sheetID = self.get_googleSheetID(googleSheetURL)
        self.sheetName = sheet_name
        self.deploymentID = deploymentID
        
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
        self.deploymentID = deployment_id
        
    def updateCell(self, row=1, column=1, data=""):
        sheet_name = self.encoding_url(self.sheetName)
        mode = "updateCell"
        url = "https://script.google.com/macros/s/{}/exec?sheet_id={}&sheet_name={}&mode={}&row={}&column={}&data={}".format(
            self.deploymentID, self.sheetID, sheet_name, mode, row, column, self.encoding_url(str(data))
        )
        response = requests.get(url)
        response.close()
        return response.status_code    
    
    def appendRow(self,row=0,data=[]):
        sheet_name = self.encoding_url(self.sheetName)
        mode = "appendRow"
        url = "https://script.google.com/macros/s/{}/exec?sheet_id={}&sheet_name={}&mode={}&row={}".format(
            self.deploymentID, self.sheetID, sheet_name, mode, row)
        for i in range(len(data)):
            url += "&data{}={}".format(i,self.encoding_url(str(data[i])))
        print(url)
        response = requests.get(url)
        response.close()
        return response.status_code  
    
    def appendColumn(self,column=0,data=[]):
        sheet_name = self.encoding_url(self.sheetName)
        mode = "appendColumn"
        url = "https://script.google.com/macros/s/{}/exec?sheet_id={}&sheet_name={}&mode={}&row={}".format(
            self.deploymentID, self.sheetID, sheet_name, mode, column)
        for i in range(len(data)):
            url += "&data{}={}".format(i,self.encoding_url(str(data[i])))
        print(url)
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
            start_index = html_code.find('<body>')
            end_index = html_code.find('</body>')
            script_content = html_code[start_index:end_index]
            start_index = script_content.find('script type="text/javascript"')
            end_index = script_content.find('</script>')
            script_content = script_content[start_index:end_index]
            script_content = script_content[script_content.find('body')+18:script_content.find('/body')-21]
            return script_content
        else:
            return "Error Code:{}".format(responseCode)
        
    def gen_scriptFile(self):
        code = """
function doGet(e) {
  var sheet_id = e.parameter.sheet_id;
  var sheet_name = e.parameter.sheet_name;
  var mode = e.parameter.mode;

  var ss = SpreadsheetApp.openById(sheet_id);
  var sheet = ss.getSheetByName(sheet_name);

  if (mode == "updateCell") {
    var row = e.parameter.row;
    var column = e.parameter.column;
    var data = e.parameter.data;

    var cell = sheet.getRange(row, column);
    cell.setValue(data);
  }
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

  else if (mode == "getCell") {
    var row = e.parameter.row;
    var column = e.parameter.column;

    var cell = sheet.getRange(row, column);
    var value = cell.getValue();

    var html = "<html><head><title>Get The data </title></head><body><h1>" + value + "</h1></body></html>";
    return HtmlService.createHtmlOutput(html);
  }
}
        """
        with open('script.txt', 'w') as file:
            file.write(code)