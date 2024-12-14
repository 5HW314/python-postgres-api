import os
import psycopg2
from dotenv import load_dotenv
from flask import Flask, jsonify

load_dotenv()

app = Flask(__name__)
url = os.getenv("DATABASE_URL")
connection = psycopg2.connect(url)

@app.get('/')
def home():
    return "Hello, world!"
    
#Insert New User
@app.post('/users')
def add_user():
    with connection.cursor() as cursor:
        cursor.execute("INSERT INTO users (name, email) VALUES (%s, %s), (Maharaj, maharaj@example.com), (Surbhi, subhu@example.com)")
        connection.commit()
    return "User Added!"

#Query Data
@app.route('/users')
def get_user():
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM users")
        rows = cursor.fetchall()
        column_names = [desc[0] for desc in cursor.description]
        # Map rows to dictionaries
        result = [dict(zip(column_names, row)) for row in rows]
    return jsonify(result)

# Run the app
if __name__=='_main_':
    ap.run(debug=True)