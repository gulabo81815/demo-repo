from flask import Flask, render_template, request, jsonify
import mysql.connector
import os

app = Flask(__name__)

# MySQL Configuration (from environment variables)
db_config = {
    'host': os.getenv('MYSQL_HOST', 'localhost'),
    'user': os.getenv('MYSQL_USER', 'root'),
    'password': os.getenv('MYSQL_PASSWORD', 'root'),
    'database': os.getenv('MYSQL_DB', 'flasknotes') 
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/notes', methods=['GET'])
def get_notes():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM notes ORDER BY id DESC;")
    notes = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(notes)

@app.route('/api/notes', methods=['POST'])
def add_note():
    data = request.get_json()
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO notes (title, content) VALUES (%s, %s);", 
                   (data['title'], data['content']))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"message": "Note added successfully!"}), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
