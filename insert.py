#!/usr/bin/python
import json
from bson import json_util
import bottle
from bottle import route, run, request, abort, response, post, get, put, delete
from pymongo import MongoClient
import pprint

# Set target db & collection
connection = MongoClient('localhost', 27017)
db = connection['market']
collection = db['stocks']

#############################################
#           PyMongo CRUD Methods            #
#############################################


# Inserts a new document into Collection.
# 
# @param document
#   - JSON-type document to be inserted into the collection
# 
# @var result
#   - Indicates success/failure of inserting document
#    
# @throws TypeError
#   - Thrown if document is incorrect format
#   
# @return result
#   - Created document on successful creation

document = { "Ticker" : "Test", "Profit Margin" : 0.013, "Institutional Ownership" : 0.599, "EPS growth past 5 years" : -0.439, 
            "Total Debt/Equity" : 0.65, "Current Ratio" : 1.2, "Return on Assets" : 0.008, "Sector" : "Test Sector", 
            "P/S" : 0.41, "Change from Open" : -0.0022, "Performance (YTD)" : 0.0502, "Performance (Week)" : -0.0694, 
            "Quick Ratio" : 0.7, "Insider Transactions" : 0.1031, "P/B" : 0.75, "EPS growth quarter over quarter" : 1.143, 
            "Payout Ratio" : 0.429, "Performance (Quarter)" : 0.1058, "Forward P/E" : 21.35, "P/E" : 35.96, 
            "200-Day Simple Moving Average" : 0.0823, "Shares Outstanding" : 1070, "Earnings Date" : { "date" : 1381264200000 }, 
            "52-Week High" : -0.0925, "P/Cash" : 9.460000000000001, "Change" : 0.0033, "Analyst Recom" : 3.1, 
            "Volatility (Week)" : 0.0345, "Country" : "USA", "Return on Equity" : 0.023, "50-Day Low" : 0.1579, 
            "Price" : 9.02, "50-Day High" : -0.0925, "Return on Investment" : 0.007, "Shares Float" : 1068.5, 
            "Dividend Yield" : 0.0133, "EPS growth next 5 years" : 0.1747, "Industry" : "Aluminum", "Beta" : 2.02, 
            "Sales growth quarter over quarter" : -0.012, "Operating Margin" : 0.049, "EPS (ttm)" : 0.25, "PEG" : 2.06, 
            "Float Short" : 0.1129, "52-Week Low" : 0.1899, "Average True Range" : 0.3, "EPS growth next year" : 0.231, 
            "Sales growth past 5 years" : -0.041, "Company" : "Test Company", "Gap" : 0.0056, "Relative Volume" : 0.6, 
            "Volatility (Month)" : 0.0336, "Market Cap" : 9619.299999999999, "Volume" : 14600992, "Gross Margin" : 0.163, 
            "Short Ratio" : 4.51, "Performance (Half Year)" : 0.06519999999999999, "Relative Strength Index (14)" : 49.61, 
            "Insider Ownership" : 0.0007, "20-Day Simple Moving Average" : -0.0192, "Performance (Month)" : 0.0766, 
            "P/Free Cash Flow" : 33.17, "Institutional Transactions" : 0.0252, "Performance (Year)" : 0.0963, 
            "LT Debt/Equity" : 0.6, "Average Volume" : 26728.11, "EPS growth this year" : -0.673, 
            "50-Day Simple Moving Average" : 0.052 }

def insert_document(document):
  try:
    collection.save(document)
  except TypeError as te:
    abor(400, str(te))
  else:
    for result in collection.find({"Sector" : "Test Sector", "Company" : "Test Company"}):
      print (result)
        
insert_document(document)


  
 