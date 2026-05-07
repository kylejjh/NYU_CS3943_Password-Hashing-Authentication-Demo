from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import bcrypt

app = Flask(__name__)

DATABASE = "users.db"


def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
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
    return redirect(url_for("register"))


@app.route("/register", methods=["GET", "POST"])
def register():
    message = ""

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        password_bytes = password.encode("utf-8")

        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password_bytes, salt)

        hashed_password_string = hashed_password.decode("utf-8")

        try:
            conn = get_db_connection()
            conn.execute(
                "INSERT INTO users (username, password_hash) VALUES (?, ?)",
                (username, hashed_password_string),
            )
            conn.commit()
            conn.close()

            message = "Registration successful. Your password was hashed before saving."

        except sqlite3.IntegrityError:
            message = "Username already exists. Please choose another username."

    return render_template("register.html", message=message)


@app.route("/login", methods=["GET", "POST"])
def login():
    message = ""

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        conn = get_db_connection()
        user = conn.execute(
            "SELECT * FROM users WHERE username = ?",
            (username,)
        ).fetchone()
        conn.close()

        if user is None:
            message = "Login failed. Username does not exist."
        else:
            stored_hash = user["password_hash"]

            password_bytes = password.encode("utf-8")
            stored_hash_bytes = stored_hash.encode("utf-8")

            if bcrypt.checkpw(password_bytes, stored_hash_bytes):
                return redirect(url_for("dashboard", username=username))
            else:
                message = "Login failed. Wrong password."

    return render_template("login.html", message=message)


@app.route("/dashboard/<username>")
def dashboard(username):
    return render_template("dashboard.html", username=username)


if __name__ == "__main__":
    init_db()
    app.run(debug=True)