# delete data from SQL using Python
import sqlite3
connection = sqlite3.connect('data.db')
cursor = connection.cursor()

cursor.execute('''DELETE FROM data WHERE vid_name = "video15";''')

connection.commit()
connection.close()