# remove duplicates from SQL dataset using python!

import sqlite3
connection = sqlite3.connect('data.db')
cursor = connection.cursor()

cursor.execute("SELECT * FROM data")
results = cursor.fetchall()

for i in results:
    if results.count(i) > 1:
        for j in range(results.count(i) - 1):
            results.remove(i)

for i in results:
    print(i)

cursor.execute("DELETE FROM data")
for i in results:
    cursor.execute("INSERT INTO data VALUES (?, ?, ?)", (i[0], i[1], i[2]))

connection.commit()
connection.close()