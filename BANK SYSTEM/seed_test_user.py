import sqlite3

def seed():
    conn = sqlite3.connect('bank.db')
    cur = conn.cursor()
    try:
        cur.execute("INSERT OR IGNORE INTO users(name,email,password,balance) VALUES (?,?,?,?)",
                    ('Test User','harshada@gmail.com','KKW@123',1000.0))
        conn.commit()
        print('Seeded user: harshada@gmail.com / KKW@123')
    except Exception as e:
        print('Error seeding user:', e)
    finally:
        conn.close()

if __name__ == '__main__':
    seed()
