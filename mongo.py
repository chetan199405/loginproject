from pymongo import MongoClient

# Your connection string (make sure the password is correct)
client = MongoClient("mongodb://chetan:Limit%123456789@ac-Cluster1-shard-00-00.cluster0.mongodb.net:27017,ac-Cluster1-shard-00-01.cluster0.mongodb.net:27017,ac-Cluster1-shard-00-02.cluster0.mongodb.net:27017/?ssl=true&replicaSet=atlas-Cluster1-shard-0&authSource=admin&retryWrites=true&w=majority")

# Access a database
db = client["students_data"]  # replace 'test' with your database name

# Example operation
print(db.list_collection_names())
