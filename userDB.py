import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()

# Create a table
cursor.execute('''CREATE TABLE IF NOT EXISTS users
                  (id INTEGER PRIMARY KEY AUTOINCREMENT,
                   username TEXT,
                   password TEXT)''')


#cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", ("", ""))
conn.commit()
conn.close()

#retrieve data from the table
conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()

#sql_del = cursor.execute("DELETE FROM users WHERE id = 5")
#conn.commit()
#conn.close()


#display the retrieved rows
for row in rows:
    print(f"ID: {row[0]}, Username: {row[1]}, Password: {row[2]}")

#Close the connection
conn.close()