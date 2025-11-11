from pymongo.mongo_client import MongoClient

// insert your mongo db uri
uri = ""

# Create a new client and connect to the server
client = MongoClient(uri)
# Send a ping to confirm a successful connection

db = client.chatbot_db

# Access a collection (e.g., qa_pairs)
collection = db.qa_pairs
qa_pairs = [
   {
      "question": "Greetings",
      "response": "Morning,Afternoon,Evening to whatever time zone you are !!How can I help you ? "
   }
   # Add more QA pairs as needed
]

# Insert the responses into the collection
collection.insert_many(qa_pairs)
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
