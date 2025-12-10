from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS messages (id INTEGER PRIMARY KEY AUTOINCREMENT, text TEXT)')
    conn.commit()
    conn.close()

@app.route('/')
def home():
    return "Hello, this is Flask app running in Docker!"

@app.route('/add', methods=['POST'])
def add_message():
    data = request.json
    text = data.get('text')
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute('INSERT INTO messages (text) VALUES (?)', (text,))
    conn.commit()
    conn.close()
    return jsonify({"status": "success", "message": text})

@app.route('/messages', methods=['GET'])
def get_messages():
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute('SELECT * FROM messages')
    rows = c.fetchall()
    conn.close()
    return jsonify(rows)

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000)
