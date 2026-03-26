# Secure Bank System

Simple educational Flask-based banking demo with user registration, login, deposit, withdraw, and transfers.

## Features
- User registration and authentication
- Dashboard showing account balance and transaction actions
- Deposit, withdraw, and transfer flows with HTML templates
- Lightweight SQLite database for local use (`bank.db`)

## Tech stack
- Python 3.8+
- Flask
- SQLite (local `bank.db`)

## Getting started
1. Clone the repository:

   git clone https://github.com/Siddesh3185/Secure-bank-system.git
2. Change into the project directory:

   cd "Secure Bank"
   cd "BANK SYSTEM"
3. (Optional) Create a virtual environment and install dependencies:

   python -m venv venv
   venv\Scripts\activate   # Windows
   pip install -r requirements.txt

   If `requirements.txt` is not present, install Flask:

   pip install Flask

4. Initialize or inspect the database:

   - The project includes a `bank.db` file for local testing. To recreate or seed test users, run `seed_test_user.py`.

5. Run the app:

   set FLASK_APP=app.py
   set FLASK_ENV=development
   flask run

   Or run directly with Python:

   python app.py

6. Open a browser at http://127.0.0.1:5000/ to access the app.

## Project layout
- `app.py` — Flask application entrypoint
- `bank.db` — SQLite database (local)
- `seed_test_user.py` — helper to create a test account
- `templates/` — HTML templates (home, login, register, dashboard, deposit, withdraw, transfer)
- `static/` — CSS and static assets

## Security notes (important)
- This project is a learning/demo application and is not production-ready.
- Do not use the included `bank.db` or code for real accounts or production data.
- Add proper password hashing, session management, CSRF protection, and secure database handling before production use.

## Contributing
Contributions are welcome. Please open issues or pull requests for enhancements or fixes.

## License
This project is provided under the MIT License. See LICENSE for details.

## Contact
Maintainer: Siddesh3185 — siddeshshinde3185@gmail.com
