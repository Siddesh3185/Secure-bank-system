from flask import Flask, render_template, request, redirect, session, flash
import sqlite3

app = Flask(__name__)
app.secret_key = "banksecret"

# Database Initialization
def init_db():
    conn = sqlite3.connect("bank.db")
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT UNIQUE,
            password TEXT,
            balance REAL DEFAULT 0
        )
    """)
    conn.commit()
    conn.close()

init_db()

# Home
@app.route('/')
def home():
    return render_template("home.html")

# Register
@app.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']

        conn = sqlite3.connect("bank.db")
        cur = conn.cursor()
        try:
            cur.execute("INSERT INTO users(name,email,password) VALUES(?,?,?)",
                        (name,email,password))
            conn.commit()
            flash("Registration Successful!")
            return redirect('/login')
        except:
            flash("Email already exists!")
        conn.close()

    return render_template("register.html")

# Login
@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        conn = sqlite3.connect("bank.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM users WHERE email=? AND password=?",
                    (email,password))
        user = cur.fetchone()
        conn.close()

        if user:
            session['user_id'] = user[0]
            session['name'] = user[1]
            return redirect('/dashboard')
        else:
            flash("Invalid Credentials!")

    return render_template("login.html")

# Dashboard
@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect('/login')

    conn = sqlite3.connect("bank.db")
    cur = conn.cursor()
    cur.execute("SELECT balance FROM users WHERE id=?",
                (session['user_id'],))
    balance = cur.fetchone()[0]
    conn.close()

    return render_template("dashboard.html", balance=balance)

# Deposit
@app.route('/deposit', methods=['GET','POST'])
def deposit():
    if 'user_id' not in session:
        return redirect('/login')

    if request.method == 'POST':
        amount = float(request.form['amount'])
        conn = sqlite3.connect("bank.db")
        cur = conn.cursor()
        cur.execute("UPDATE users SET balance = balance + ? WHERE id=?",
                    (amount, session['user_id']))
        conn.commit()
        conn.close()
        return redirect('/dashboard')

    return render_template("deposit.html")

# Withdraw
@app.route('/withdraw', methods=['GET','POST'])
def withdraw():
    if 'user_id' not in session:
        return redirect('/login')

    if request.method == 'POST':
        amount = float(request.form['amount'])

        conn = sqlite3.connect("bank.db")
        cur = conn.cursor()
        cur.execute("SELECT balance FROM users WHERE id=?",
                    (session['user_id'],))
        balance = cur.fetchone()[0]

        if balance >= amount:
            cur.execute("UPDATE users SET balance = balance - ? WHERE id=?",
                        (amount, session['user_id']))
            conn.commit()
        conn.close()
        return redirect('/dashboard')

    return render_template("withdraw.html")

# Transfer
@app.route('/transfer', methods=['GET','POST'])
def transfer():
    if 'user_id' not in session:
        return redirect('/login')

    if request.method == 'POST':
        receiver_email = request.form['email']
        amount = float(request.form['amount'])

        conn = sqlite3.connect("bank.db")
        cur = conn.cursor()

        cur.execute("SELECT balance FROM users WHERE id=?",
                    (session['user_id'],))
        sender_balance = cur.fetchone()[0]

        cur.execute("SELECT id FROM users WHERE email=?",
                    (receiver_email,))
        receiver = cur.fetchone()

        if receiver and sender_balance >= amount:
            cur.execute("UPDATE users SET balance = balance - ? WHERE id=?",
                        (amount, session['user_id']))
            cur.execute("UPDATE users SET balance = balance + ? WHERE email=?",
                        (amount, receiver_email))
            conn.commit()

        conn.close()
        return redirect('/dashboard')

    return render_template("transfer.html")

# Logout
@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)