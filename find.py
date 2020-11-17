import json
from bson import json_util
from pymongo import MongoClient

connection = MongoClient('localhost', 27017)
db = connection['market']
collection = db['stocks']

# Searches Collection for documents matching passed criteria
# 
# @param document
#   - Key, value pair used as search criteria
#   
# @var result
#   - Returned cursor from find()
#   
# @throws TypeError
#   - Thrown if document is incorrect format
#   
# @return result
#   - Cursor from find(), undefined if search fails
def find_document(document):
  
  result = []

  try:
    data = collection.find(document)
    
    for document in data:
      result.append(document)
  except TypeError as te:
    abort(400, str(te))
  else:
    return result


        
def main():
  
        ## Part 3 Section 1
        ## myQuery = {"50-Day Simple Moving Average" : {"$gt" : 0, "$lt" : 2.6714}}
        ## result = collection.find(myQuery).count()
          ## print(result)
        
        
        ## Part 3 Section 2
        ## myQuery = {"Industry" : "Medical Laboratories & Research"}
        ## myDisplay = {"Ticker" : 1, "_id" : 0}
        ## result = collection.find(myQuery, myDisplay)
        ## for result in collection.find(myQuery, myDisplay):
          ## print(result)
       
  
main()  