from pymongo import MongoClient
conn = MongoClient()
db = conn.pytech
collection = db.students
cursor = collection.find()

for record in cursor:
    print(record)

doc = db.students.find_one({"student_id": 1007})
 
print(doc["student_id"])

doc = db.students.find_one({"student_id": 1008})
 
print(doc["student_id"])

doc = db.students.find_one({"student_id": 1009})
 
print(doc["student_id"])