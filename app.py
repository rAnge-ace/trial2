from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="try"
    )

@app.route('/')
def index():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT 'Hello from MySQL!'")
    cursor.execute("SELECT 'Hello from heyheyhey'")
    data = cursor.fetchone()
    cursor.close()
    conn.close()
    return jsonify(message=data[0])

if __name__ == '__main__':
    app.run(debug=True)
