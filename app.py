from flask import Flask, request, jsonify
from pymongo import MongoClient
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from flask_cors import CORS
import ssl

app = Flask(__name__)
CORS(app)

# Replace with your MongoDB Atlas URI
MONGO_URI = "mongodb+srv://experimentalsolution:0NpbKpk1ZcAKGWEN@cluster0.jhdtvgm.mongodb.net/?retryWrites=true&w=majority"

# Initialize MongoDB client
client = MongoClient(
    MONGO_URI,
    connectTimeoutMS=30000,
    socketTimeoutMS=None,
    connect=False,
    maxPoolsize=1,

)
db = client.chatbot_db
collection = db.qa_pairs  # Replace with your collection name

# Fetch all documents from the MongoDB collection
all_documents = list(collection.find())

# Extract questions and responses
questions = [doc['question'] for doc in all_documents]
print(questions)
responses = [doc['response'] for doc in all_documents]
print(responses)

# Create a TF-IDF vectorizer
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(questions)
print(tfidf_matrix)

@app.route('/chatbot', methods=['POST'])
def chatbot():
    print('request came')
    data = request.get_json()

    # Extract user's query from the request
    user_query = data.get('query', '')

    # Calculate TF-IDF vector for the user's query
    user_query_tfidf = vectorizer.transform([user_query])

    # Calculate cosine similarity between the user's query and all questions
    similarities = cosine_similarity(user_query_tfidf, tfidf_matrix)

    # Find the index of the most similar question
    most_similar_index = similarities.argmax()

    similarity_score = similarities[0, most_similar_index] * 100

    if similarity_score > 30:
        response = responses[most_similar_index]
    else:
        response ='Not sure I understood you and my knowledge is limited as of now.My boss has not allowed me for advance search from internet.Please ask him to enable so that I can help you'

    # Retrieve the response corresponding to the most similar question
    
    print('response is')
    print(similarity_score)
    print(response)

    return jsonify({'response': response})

if __name__ == '__main__':
    app.run()
