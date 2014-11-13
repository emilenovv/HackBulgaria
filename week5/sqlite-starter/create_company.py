import sqlite3


db = sqlite3.connect('company.db')
cursor = db.cursor()
cursor.execute('''
    CREATE TABLE company(id INTEGER PRIMARY KEY, name TEXT,
        monthly_salary TEXT, yearly_bonus TEXT, position TEXT)
    ''')
db.commit()
db.close()