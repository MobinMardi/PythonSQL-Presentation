import sqlite3
connection = sqlite3.connect('data.db')
cursor = connection.cursor()
# each video is a list of data - name, views, date (YYYY-MM-DD)
videos = [['video1', 100, '2022-10-25'],
          ['video2', 200, '2021-12-29'],
          ['video3', 300, '2022-03-31'],
          ['video4', 400, '2022-05-19']]

for i in range(len(videos)):
    name = videos[i][0]
    views = videos[i][1]
    date = videos[i][2]
    cursor.execute("INSERT INTO data VALUES (?, ?, ?)", (name, views, date))

# MUST commit data or no changes will be saved
connection.commit()
connection.close()