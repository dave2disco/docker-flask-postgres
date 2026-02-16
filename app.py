from flask import Flask, request, render_template, redirect
import psycopg2
import time
import os

app = Flask(__name__)

DB_HOST = os.getenv("DB_HOST", "db")
DB_NAME = os.getenv("POSTGRES_DB", "mydb")
DB_USER = os.getenv("POSTGRES_USER", "user")
DB_PASSWORD = os.getenv("POSTGRES_PASSWORD", "password")


def get_connection():
    while True:
        try:
            return psycopg2.connect(
                host=DB_HOST,
                database=DB_NAME,
                user=DB_USER,
                password=DB_PASSWORD
            )
        except Exception as e:
            print("Database non pronto, riprovo...", e)
            time.sleep(2)


def init_db():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS messages (
            id SERIAL PRIMARY KEY,
            text TEXT
        )
    """)

    conn.commit()
    cur.close()
    conn.close()


@app.route("/")
def home():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT text FROM messages")
    rows = cur.fetchall()

    cur.close()
    conn.close()

    messages = [r[0] for r in rows]

    return render_template("index.html", messages=messages)


@app.route("/add", methods=["POST"])
def add():
    text = request.form.get("text")

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("INSERT INTO messages (text) VALUES (%s)", (text,))
    conn.commit()

    cur.close()
    conn.close()

    return redirect("/")


if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=5000)
