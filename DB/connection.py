import pymongo

# Establish a connection to the MongoDB server
client = pymongo.MongoClient("mongodb+srv://reut201112:Reut8091746@carzone.zijsrlp.mongodb.net/cars")

# Connect to the database
db = client["cars_database"]

# Create a new collection
collection = db["cars_collection"]

collection.insert_many([
    {
        "image_name": "black.jpg",
        "image_url":  "https://images.unsplash.com/photo-1618022325802-7e5e732d97a1?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1948&q=80"
    },
    {
        "image_name": "blue.jpg",
        "image_url": "https://images.unsplash.com/photo-1588421357574-87938a86fa28?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2070&q=80"
    },
    {
        "image_name": "white.jpg",
        "image_url": "https://images.unsplash.com/photo-1604147706283-d7119b5b822c?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=387&q=80"
    }
])


