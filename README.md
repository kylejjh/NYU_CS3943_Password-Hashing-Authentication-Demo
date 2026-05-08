# Password Hashing Authentication Demo

## Project Overview

This project is a simple Flask web application that demonstrates how password hashing is used in user authentication.

Users can register an account and log in. The important part is that the application does not store the user's real password. Instead, it stores a bcrypt hashed version of the password in a SQLite database.

This project connects to cryptography because hash functions are one-way functions. They allow the system to verify a password without saving the original password.

## Main Features

- Register a new user
- Hash the user's password with bcrypt
- Store only the hashed password in SQLite
- Log in by checking the typed password against the stored hash
- Show a demo page that displays the stored password hash
- Explain why the real password should not be stored

## Technologies Used

- Python
- Flask
- SQLite
- bcrypt
- HTML
- CSS

## Project Structure

```text
NYU_CS3943_Password-Hashing-Authentication-Demo/
│
├── app.py
├── users.db
├── requirements.txt
├── README.md
│
├── templates/
│   ├── register.html
│   ├── login.html
│   ├── dashboard.html
│   └── demo.html
│
└── static/
    └── style.css
```

## How to Run the Project

### 1. Open the project folder

Open PowerShell or VS Code terminal and go into the project folder:

```powershell
cd C:\Users\kki\Desktop\NYU_CS3943_Password-Hashing-Authentication-Demo
```

### 2. Create a virtual environment

```powershell
python -m venv venv
```

### 3. Activate the virtual environment

```powershell
venv\Scripts\activate
```

If PowerShell blocks the script, run this first:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

Then activate again:

```powershell
venv\Scripts\activate
```

After it works, you should see:

```text
(venv) PS C:\Users\kki\Desktop\NYU_CS3943_Password-Hashing-Authentication-Demo>
```

### 4. Install dependencies

```powershell
pip install -r requirements.txt
```

### 5. Run the Flask app

```powershell
python app.py
```

You should see something like:

```text
Running on http://127.0.0.1:5000
```

### 6. Open the website

Open this link in your browser:

```text
http://127.0.0.1:5000
```

## How to Test the Project

### Test 1: Register a user

1. Open the register page.
2. Enter a username.
3. Enter a password.
4. Click **Create Account**.

The app should show:

```text
Registration successful. Your password was hashed before saving.
```

### Test 2: Login with the correct password

1. Go to the login page.
2. Enter the same username and password.
3. Click **Login**.

The app should take you to the dashboard page.

### Test 3: Login with the wrong password

1. Go to the login page.
2. Enter the correct username.
3. Enter a wrong password.
4. Click **Login**.

The app should show:

```text
Login failed. Wrong password.
```

### Test 4: View the stored hash demo

Open:

```text
http://127.0.0.1:5000/demo
```

This page shows the stored bcrypt password hash.

The real password is not shown because the app does not store the real password.

## Why Password Hashing Matters

A website should not store plain-text passwords. If a database is leaked, plain-text passwords can be stolen immediately.

With password hashing, the stored value is not the real password. bcrypt also uses salt, which makes the hash stronger and harder to guess using common password tables.

In this project, the login system checks the typed password against the stored hash. It does not decrypt the password, because hashing is one-way.

## Course Connection

This project connects to the course topic of cryptography and hash functions.

A hash function creates a fixed output from input data. A good hash function is one-way, deterministic, and hard to reverse.

In blockchain, hashes help protect data integrity and link blocks together. In this project, hashing is used in a website authentication system to protect user passwords.

## Important Note

The `/demo` page is only included for class explanation.