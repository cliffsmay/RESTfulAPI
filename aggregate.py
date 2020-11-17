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
def aggregate_document(document):
  
  result = []

  try:
    data = collection.aggregate(document)
    
    for document in data:
      result.append(document)
  except TypeError as te:
    abort(400, str(te))
  else:
    return result


        
def main():
  
       
        pipeline = ([{ '$match': { "Sector": "Healthcare" } },
                      { '$group': { '_id': "$Industry", 'Total Outstanding Shares:': { '$sum': "$Shares Outstanding" } } }])   
        cursor = collection.aggregate(pipeline)
        result = list (cursor)
        print(result)
  
main()  