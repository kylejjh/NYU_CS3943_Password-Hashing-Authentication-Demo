from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import bcrypt

app = Flask(__name__)

DATABASE = "users.db"


def get_db_connection():
    """
    Connect to the SQLite database.
    If users.db does not exist, SQLite will create it automatically.
    """
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    """
    Create the users table if it does not already exist.
    I store username and password_hash.
    I do NOT store the plain password.
    """
    conn = get_db_connection()
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL
        )
        """
    )
    conn.commit()
    conn.close()


@app.route("/")
def home():
    return "Database is ready. Register page will be added next."


if __name__ == "__main__":
    init_db()
    app.run(debug=True)