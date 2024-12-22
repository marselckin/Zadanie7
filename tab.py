import sqlite3

conn = sqlite3.connect('example.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS TPresent (
id INTEGER PRIMARY KEY,
name TEXT NOT NULL,
present TEXT NOT NULL,
cost INTEGER,
status BLOB)''')

data = [
['Иванов Иван Иванович', 'торт', 10, 1],
['Петров Петр Петрович', 'конфета', 11, 1],
['Кузнецов Василий Петрович', 'медаль', 12, 0],
['Песков Андрей Борисович', 'ноутбук', 13, 0],
['Андреев Иван Васильевич', 'стол', 14, 0],
['Быков Михаил Иванович', 'колонки', 15, 1],
['Грозный Владимир Борисович', 'Коврик', 16, 1],
['Петров Александр Максимович', 'Кружка', 17, 0],
['Селедцов Евгений Евгеньевич', 'Часы', 18, 1],
['Селеванов Виктор Владимирович', 'Шапка', 19, 1]
]

cursor.executemany('INSERT INTO TPresent (name, present, cost, status) VALUES (?, ?, ?, ?)', data)

cursor.execute('SELECT * FROM TPresent')
tpresent = cursor.fetchall()

for tpresent in tpresent:
 print(tpresent)

conn.commit()
conn.close()
