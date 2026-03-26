)

🏦 Secure Bank System

A simple, educational Flask-based banking system that demonstrates core banking operations such as user authentication, deposits, withdrawals, and fund transfers.

⚠️ This project is intended for learning purposes only and is not production-ready.

🚀 Features
🔐 User Registration & Login Authentication
📊 Dashboard with Account Balance
💰 Deposit Money
💸 Withdraw Money
🔁 Transfer Funds Between Users
🗄️ SQLite Database (bank.db) for Local Storage
🎨 HTML Templates for UI (Flask Jinja)
🛠️ Tech Stack
Backend: Python 3.8+, Flask
Database: SQLite
Frontend: HTML, CSS (Flask Templates)
📂 Project Structure
Secure-bank-system/
│
├── app.py                # Main Flask application
├── bank.db              # SQLite database
├── seed_test_user.py    # Script to create test user
│
├── templates/           # HTML templates
│   ├── home.html
│   ├── login.html
│   ├── register.html
│   ├── dashboard.html
│   ├── deposit.html
│   ├── withdraw.html
│   └── transfer.html
│
├── static/              # CSS and assets
│
└── README.md
⚙️ Getting Started
1️⃣ Clone the Repository
git clone https://github.com/Siddesh3185/Secure-bank-system.git
2️⃣ Navigate to Project Folder
cd "Secure Bank"
cd "BANK SYSTEM"
3️⃣ Create Virtual Environment (Optional but Recommended)
python -m venv venv

Activate environment:

Windows
venv\Scripts\activate
4️⃣ Install Dependencies
pip install -r requirements.txt

If requirements.txt is not available:

pip install Flask
5️⃣ Setup Database
Prebuilt database: bank.db
To create a test user:
python seed_test_user.py
6️⃣ Run the Application
Option 1: Flask Command
set FLASK_APP=app.py
set FLASK_ENV=development
flask run
Option 2: Direct Run
python app.py
🌐 Access the App

Open your browser:

http://127.0.0.1:5000/
🔐 Security Notice

This project is NOT secure for real-world usage.

Before using in production, you must implement:

Password Hashing (e.g., bcrypt)
CSRF Protection
Secure Session Management
Input Validation & Sanitization
Proper Database Security
HTTPS Deployment
🤝 Contributing

Contributions are welcome!

Fork the repo
Create a new branch
Submit a pull request
📄 License

This project is licensed under the MIT License.
See the LICENSE file for details.

📧 Contact

Maintainer: Siddesh Shinde
📩 Email: siddeshshinde3185@gmail.com

🔗 GitHub: https://github.com/Siddesh3185
