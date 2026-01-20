import os
import psycopg2
from flask import Flask, jsonify

app = Flask(__name__)

def conn():
    return psycopg2.connect(
        host=os.getenv("DB_HOST", "db"),
        dbname=os.getenv("DB_NAME", "appdb"),
        user=os.getenv("DB_USER", "appuser"),
        password=os.getenv("DB_PASSWORD", "apppass"),
    )

@app.get("/users")
def users():
    c = conn()
    cur = c.cursor()
    cur.execute("SELECT id, name FROM users ORDER BY id;")
    rows = cur.fetchall()
    cur.close()
    c.close()
    return jsonify([{"id": r[0], "name": r[1]} for r in rows])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
