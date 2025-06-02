from pymongo import MongoClient

# Connect to local MongoDB
client = MongoClient("mongodb://localhost:27017/")

# Create (or access) database and collection
db = client["spam_db"]
collection = db["spam_numbers"]

# List of spam numbers to insert
spam_numbers = [
    {"number": "1234567890"},
    {"number": "9999999999"},
    {"number": "8888888888"},
    {"number": "1122334455"},
    {"number": "0000000000"},
]

# Insert into collection
collection.insert_many(spam_numbers)

print("✅ Spam numbers inserted successfully!")

def is_suspicious(number):
    return len(set(number)) == 1 or number in "1234567890" * 2
