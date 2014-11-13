import sqlite3


def create_three_colons_table(table_name):
    db = sqlite3.connect(table_name + '.db')
    cursor = db.cursor()
    cursor.execute('''
        CREATE TABLE movies(id INTEGER PRIMARY KEY, name TEXT,
            rating INT)
        ''')
    db.commit()
    db.close()


def create_projections_table():
    db = sqlite3.connect('projections.db')
    cursor = db.cursor()
    cursor.execute('''
        CREATE TABLE projections(id INTEGER PRIMARY KEY, movie_id INT,
            type TEXT, date TEXT, time TEXT)
        ''')
    db.commit()
    db.close()


def create_reservations_table():
    db = sqlite3.connect('reservations.db')
    cursor = db.cursor()
    cursor.execute('''
        CREATE TABLE reservations(id INTEGER PRIMARY KEY, username TEXT, projection_id INT,
            row INT, col INT)
        ''')
    db.commit()
    db.close()


def main():
    #create_three_colons_table("movies")
    create_reservations_table()

if __name__ == '__main__':
    main()