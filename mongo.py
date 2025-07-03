from pymongo import MongoClient

# Your connection string (make sure the password is correct)
client = MongoClient("mongodb+srv://chetan:Limit%123456789@cluster1.ccggsge.mongodb.net/")

# Access a database
db = client["test"]  # replace 'test' with your database name

# Example operation
print(db.list_collection_names())
