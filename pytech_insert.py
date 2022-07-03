from pymongo import MongoClient
conn = MongoClient()
db = conn.pytech
collection = db.students
cursor = collection.find()

for record in cursor:
    print(record)

result = collection.update_one(

{"student_id":1007},
{
"$set":{
"first_name":"Matt", 
"last_name":"Smith"
}
}
)

result = collection.update_one(

{"student_id":1008},
{
"$set":{
"first_name":"John",
"last_name":"Doe"
}
}
)

result = collection.update_one(

{"student_id":1009},
{
"$set":{
"first_name":"Tim",
"last_name":"Allen"
}
}
)

cursor = collection.find()

for record in cursor:
    print(record)