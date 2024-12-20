import os
import psycopg2
from dotenv import load_dotenv
from flask import Flask, jsonify, request
from flask_cors import CORS

load_dotenv()

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes
url = os.getenv("DATABASE_URL")
connection = psycopg2.connect(url)

@app.get('/')
def home():
    return "Hello, world!"
    
#Insert New User
@app.post('/users')
def add_user():
    data = request.get_json()
    name = data['name']
    email = data['email']
    with connection:
        with connection.cursor() as cursor:
            cursor.execute('INSERT INTO users (name, email) VALUES (%s, %s)', (name, email))
    return {}, 201

#Query Data
@app.get('/users')
def get_user():
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM users")
        rows = cursor.fetchall()
        column_names = [desc[0] for desc in cursor.description]
        # Map rows to dictionaries
        result = [dict(zip(column_names, row)) for row in rows]
    return jsonify(result)

# # Run the app
# if __name__=='_main_':
#     ap.run(debug=True)