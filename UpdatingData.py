import sqlite3
connection = sqlite3.connect('data.db')
cursor = connection.cursor()

cursor.execute('''UPDATE data SET vid_name="video1" WHERE vid_name = "video15";''')
connection.commit()

connection.close()