import json
from bson import json_util
from pymongo import MongoClient

connection = MongoClient('localhost', 27017)
db = connection['market']
collection = db['stocks']

# Updates documents based on search criteria.
# Updated documents are then returned.
# 
# @param criteria
#   - Key,value pair used to identify documents to be updated
#   
# @param document
#   - Set of key,value pairs for updating documents
#   
# @var result
#   - Cursor containing updated documents
#   
# @throws TypeError
#   - Thrown if criteria is incorrect format
#   
# @throws Exception
#   - Thrown if document is incorrect format
#   
# @return result
#   - Cursor containing updated documents, undefined if update fails

def edit_document(criteria, document):
  try:
    collection.update_one(criteria,{"$set" : document})
    result = collection.find(criteria)
  except TypeError as te:
    abort(400, str(te))
  except Exception as we:
    abort(400, str(we))
  except:
    abort(400, "Bad Request")
  else:
    return result

        
def main():
  
        myQuery = { "Ticker" : "Test", "Volume" : 14600992 }
        newValues = { "$set" : {"Volume" : 1234567}}
  
        collection.update_one(myQuery, newValues)
    
        for result in collection.find({"Ticker" : "Test", "Volume" : 1234567}):
        
          print(result)
        
        
main()    