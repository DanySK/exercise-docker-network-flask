from flask import Flask, jsonify
import psycopg2
import os

app = Flask(__name__)

def get_connection():
    return psycopg2.connect(
        dbname=os.getenv("POSTGRES_DB"),
        user=os.getenv("POSTGRES_USER"),
        password=os.getenv("POSTGRES_PASSWORD"),
        host="db"
    )

@app.route("/")
def index():
    return "OK"

@app.route("/users")
def users():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS users(id SERIAL PRIMARY KEY, name TEXT UNIQUE);")
    cur.execute("INSERT INTO users(name) VALUES('Alice') ON CONFLICT DO NOTHING;")
    cur.execute("SELECT * FROM users;")
    data = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
