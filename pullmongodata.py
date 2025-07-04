from pymongo import MongoClient

# Replace with your Atlas connection string
client = MongoClient("mongodb+srv://chetan:Limit%123456789@cluster0.mongodb.net/?retryWrites=true&w=majority")

# Switch to your database
db = client["students"]   # Replace 'mydatabase' with your actual DB name

# Switch to your collection
collection = db["addmission"]  # Replace 'students' with your collection name

# Fetch all documents
students = collection.find()

# Print each record
for admission_date in addmission:
    print(admission_date)
