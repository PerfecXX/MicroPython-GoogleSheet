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
