# Chatbot Web Application

## Overview
This project is a **web-based chatbot** built using **Flask**, **MongoDB**, and **TF-IDF based similarity matching**.  
The chatbot answers user queries by finding the most similar question in the database.  
Queries that cannot be answered are logged for future improvements.

---

## Features
- Flask-based web API for chatbot interaction  
- Stores questions and answers in **MongoDB**  
- Uses **TF-IDF vectorization** and **cosine similarity** for query matching  
- Handles unanswered queries automatically  
- CORS enabled for front-end integration  

---

## Project Structure
- `app.py` — Main Flask application  
- `mongodb.py` — Script to insert QA pairs into MongoDB  
- `requirements.txt` — Python dependencies  
- `README.md` — Project documentation  

---

## Installation

### Prerequisites
- Python 3.8+  
- MongoDB Atlas account or local MongoDB instance  
- pip package manager  

### Clone the repository
Open your terminal and run:

```
git clone https://github.com/experimentalsolution/chatbot-experimental-solution.git
cd my-project
```

### Install dependencies
```bash
pip install -r requirements.txt
```

## Setup MongoDB

- Create a database named chatbot_db.
- Create collections:
- qa_pairs → standard QA pairs
- qa_pairs_experimental_solution → experimental QA pairs
- qa_pairs_not_answered → unanswered queries
- Update the MongoDB URI in app.py and mongodb.py:
- MONGO_URI = "your_mongodb_connection_string"

## Insert initial QA pairs
```python
python mongodb.py
```
### Running the Application

Start the Flask server:
```python
python app.py
```
Default server: http://127.0.0.1:5000/
POST request to /chatbot with JSON payload:

{
  "query": "Hello"
}


Response example:

{
  "response": "Morning, Afternoon, Evening to whatever time zone you are! How can I help you?"
}

## How It Works

- Fetches all questions and responses from MongoDB.
- Converts questions into vectors using TF-IDF.
- Compares the user query to stored questions with cosine similarity.
- Returns the matched response if similarity > 50%.
- Logs queries that cannot be answered to qa_pairs_not_answered.

### Future Improvements

- Add machine learning models for better query understanding
- Implement intent classification
- Build a frontend UI for live interaction
- Enable real-time learning from unanswered queries

## Dependencies

- Flask
- Flask-CORS
- pymongo
- scikit-learn

## Install dependencies:
```python
pip install flask flask-cors pymongo scikit-learn
```
## Demo
[Live demo is created here](https://experimentalsolution.github.io/explore/#/home)  on a angular front end .It is deployed .
Please  check it out and share your feedback .

## License

MIT License
