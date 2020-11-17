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
def insert_document(document):
  try:
    collection.save(document)
  except TypeError as te:
    abor(400, str(te))
  else:
    result = collection.find(document)
    return result
  
  
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


#############################################
#     Set up URI paths for REST service     #
#############################################

  
# URI path for creating a new document in db
# Accepts a JSON object and adds to collection
#   by calling insert_document()
#   
# @param data
#   - Request JSON object
# 
# @param result
#   - Cursor containing new document
#   
# @throws NameError
#   - Thrown if document creation fails
#   
# @return
#   - Returns list conversion of result, parsed into a JSON object
@post('/create')
def create_document():
  try:
    data = request.json
  except:
    abort(404, "Bad data")
    
  try:
    result = insert_document(data)
    
    response.headers['Content-Type'] = 'application/json'
    return json.dumps(list(result), indent=4, default=json_util.default)
  except NameError as ne:
    abort(400, str(ne))


# URI path for searching for a document
# Uses the business_name query parameter
#   to search MongoDb using find_document()
# 
# @param name
#   - Ticker request query parameter
# 
# @param cursor
#   - Cursor returned from find_document()
#   
# @throws NameError
#   - Thrown if search fails
#   
# @return
#   - Returns list conversion of cursor, parsed into a JSON object
@get('/read')
def read_document():
  try:
    name = request.query.Company
    cursor = find_document({"Company" : name})
    
    if cursor:
      response.content_type = 'application/json'
      return json.dumps(list(cursor), indent=4, default=json_util.default)
    else:
      abort(404, "No documents found")
  except NameError as ne:
    abort(404, str(ne))
    
# URI path for updating an existing documents
# Uses the id query parameter to search MongoDb using edit_document(),
#   then updates the returned documents with the result query parameter
#   
# @param stock_ticker
#   - id request query parameter
#   
# @param stock_volume
#   - result request query parameter
#   
# @param criteria
#   - Key, value pair used to query MongoDb
#   
# @param change
#   - Key, value pair of data to update returned documents
#   
# @param cursor
#   - Updated documents returned from edit_document()
@get('/update')
def update_document():
  try:
    stock_ticker = request.query.Ticker
    stock_volume = request.query.Volume
    criteria = {"Ticker" : stock_ticker}
    change = {"Volume" : stock_volume}
    cursor = edit_document(criteria, change)
    
    if cursor:
      response.content_type = 'application/json'
      return json.dumps(list(cursor), indent=4, default=json_util.default)
    else:
      abort(404, "No documents found")
  except NameError as ne:
    abort(404, str(ne))
    
# URI path for deleting a documents
# Uses the id query parameter to search MongoDb using remove_document(),
#   matching documents are deleted
#   
# @param stock_ticker
#   - id request query parameter
#   
# @param result
#   - Return from remove_document(), returns True if successful
#   
# @throws exception
#   - Thrown if remove_document() fails
@get('/delete')
def delete_document():
  
  try:
    stock_ticker = request.query.Ticker
    result = remove_document({"Ticker" : stock_ticker})
    
    if result == "True":
      return "delete success\n"
    else:
      abort(404, "File not found")
  except:
    abort(400, "Bad Request")
    

# Application entry point
# Starts REST service
if __name__ == '__main__':
  #app.run(debug=True)
  run(host='localhost',port=8080, debug=True)
