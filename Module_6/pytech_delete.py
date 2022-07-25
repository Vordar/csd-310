from pymongo import MongoClient
conn = MongoClient()
db = conn.pytech
collection = db.students
cursor = collection.find()

for record in cursor:
    print(record)

result = collection.update_one(

{"student_id":1010},
{
"$set":{
"first_name":"Rick", 
"last_name":"Flare"
}})

cursor = collection.find()

for record in cursor:
    print(record)

result = collection.delete_one({"student_id":1010})

cursor = collection.find()

for record in cursor:
    print(record)