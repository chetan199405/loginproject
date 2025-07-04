from pymongo import MongoClient

# Replace with your Atlas connection string
client = MongoClient("mongodb+srv://chetan:Limit%123456789@cluster0.mongodb.net/?retryWrites=true&w=majority")

# Switch to your database
db = client["students"]  # Replace with your database name

# Switch to your collection
collection = db["addmission"]  # Replace with your collection name

# Sample data to insert
student = {
    "name": "Alice Smith",
    "age": 25,
    "email": "alice.smith@example.com",
    "admission_date": "2024-07-04"
}

# Insert the document
result = collection.insert_one(addmission)

# Print inserted ID
print(f"Data inserted with ID: {result.inserted_id}")
