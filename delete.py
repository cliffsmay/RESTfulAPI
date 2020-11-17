import json
from bson import json_util
from pymongo import MongoClient

connection = MongoClient('localhost', 27017)
db = connection['market']
collection = db['stocks']

# Searches for documents based on passed criteria.
# If documents are found, they are printed.
# Documents are then deleted.
# 
# @param documen
#   - Key,value pair used to identify documents to be deleted
#   
#   
# @var result
#   - Cursor containing documents pending deletion
#   - If exception, result is set to False
#   - Otherwise, contents are printed then result is set to True
#   
# @throws TypeError
#   - Thrown if document is incorrect format
#   
# @return result
#   - True/False based on if documents were successfully deleted
#   - Undefined if deletion fails

def remove_document(document):
  try:
    collection.delete_one(document)
    result = "True"
  except TypeError as te:
    abort(400, str(te))
    
  return result

        
def main():
  
        myQuery = { "Ticker" : "BRLI" }

  
        deleteResult = collection.find_one_and_delete(myQuery)
        print(deleteResult)
    
main()  