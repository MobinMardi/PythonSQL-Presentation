# read data from SQL!
import sqlite3
connection = sqlite3.connect('data.db')
cursor = connection.cursor()

# fetch all data from table in SQL db
cursor.execute("SELECT * FROM data")
# store all fetched data inside results variable
results = cursor.fetchall()
for i in results:
    print(i)

connection.close()