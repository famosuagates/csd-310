import pymongo
from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.mbglzal.mongodb.net/pytech"
client = MongoClient(url)
db = client["pytech"]
students = db["students"]

# find all students in the collection 
student_list = students.find({})

# display message 
print("\n  -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")

# loop over the collection and output the results 
for x in student_list:
    print("  Student ID: ", x["_id"], "\n  First Name: ", x["First Name"], "\n  Last Name: ", x["Last Name"], "\n")

# update student_id 1007
result = students.update_one({"_id": 1007}, {"$set": {"Last Name": "Mckellan II"}})

# find the updated student document 
ian = students.find_one({"_id": 1007})

# display message
print("\n  -- DISPLAYING STUDENT DOCUMENT 1007 --")

# output the updated document to the terminal window
print("  Student ID: ", ian["_id"], "\n  First Name: ", ian["First Name"], "\n  Last Name: ", ian["Last Name"], "\n")

# exit message 
input("\n\n  End of program, press any key to continue...")