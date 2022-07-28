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

# test document 
test_doc = {
    "_id": 1010,
    "First Name": "Martin",
    "Last Name": "Freeman"
}

# insert the test document into MongoDB atlas 
test_doc_id = students.insert_one(test_doc).inserted_id

# insert statements with output 
print("\n  -- INSERT STATEMENTS --")
print("  Inserted student record into the students collection with ID: ", str(test_doc_id))

# call the find_one() method by student_id 1010
student_test = students.find_one({"_id": 1010})

# display the results 
print("\n  -- DISPLAYING STUDENT TEST DOC -- ")
print("  Student ID: ", student_test["_id"], "\n  First Name: ", student_test["First Name"], "\n  Last Name: ", student_test["Last Name"], "\n")

# call the delete_one method to remove the student_test_doc
deleted_student_test_doc = students.delete_one({"_id": 1010})

# find all students in the collection 
new_student_list = students.find({})

# display message 
print("\n  -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")

# loop over the collection and output the results 
for doc in new_student_list:
    print("  Student ID: ", doc["_id"], "\n  First Name: ", doc["First Name"], "\n  Last Name: " + doc["Last Name"], "\n")

# exit message 
input("\n\n  End of program, press any key to continue...")