import pymongo

# Connect to the MongoDB cluster using the SRV connection string
#client = pymongo.MongoClient("mongodb+srv://reut201112:Reut8091746@carzone.zijsrlp.mongodb.net/cars")
client = pymongo.MongoClient("mongodb://mongodb:27017/cars")
# Get the `cars` database
db = client["cars"]

# Get the `cars` collection
collection = db["cars_collection"]


collection.insert_many([
    {
        "image_name": "black.jpg",
        "image_heb":"שחור",
        "image_url":  "https://images.unsplash.com/photo-1618022325802-7e5e732d97a1?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1948&q=80"
    },
    {
        "image_name": "blue.jpg",
        "image_heb":"כחול",
        "image_url": "https://media.istockphoto.com/id/1138740533/photo/dark-blue-defocused-blurred-motion-abstract-background.jpg?s=612x612&w=0&k=20&c=QfnY1B69PD-FzeDCmwuJulHg1wawHotayzgeGjEuvCc="
    },
    {
        "image_name": "white.jpg",
        "image_heb":"שנהב לבן",
        "image_url": "https://images.unsplash.com/photo-1604147706283-d7119b5b822c?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=387&q=80"
    },
    {
        "image_name": "silver.jpg",
        "image_heb":"כסף",
        "image_url": "https://media.istockphoto.com/id/1287620067/photo/abstract-metal-background-silver-gray-background.jpg?s=612x612&w=0&k=20&c=PHPmWKV-dX7-kWyxRxyrgXZpqDImjC_n2rvPq-5GYVQ="
    },
    {
        "image_name": "bage.jpg",
        "image_heb":"בז",
        "image_url": "https://media.istockphoto.com/id/1182549107/photo/paper-texture-in-light-white-cream-color.jpg?s=612x612&w=0&k=20&c=6Yj6lVg_wsI9AjCX36W31zs3CmKOsfvv1ZWIBzHokSY="
    },
    {
        "image_name": "metalicSilver.jpg",
        "image_heb":"כסף מטלי",
        "image_url": "https://media.istockphoto.com/id/477679508/photo/gray-brushed-metal-texture-background-steel-or-aluminium.jpg?s=612x612&w=0&k=20&c=eaTrJihfJYPkpdIrVQP9W2qDvGYw6uLLMWQFOpDRkdA="
    }
])


