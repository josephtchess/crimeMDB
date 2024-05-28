import sqlite3
import csv

DBNAME = 'myIMBD.db'

conn = sqlite3.connect(DBNAME)
c = conn.cursor()

#c.execute("DROP TABLE TITLEBASICS")
#conn.commit()

sql = """CREATE TABLE TITLEBASICS (
            titleID int NOT NULL, 
            movieName VARCHAR(50),
            year int,
            runtime int,
            genres VARCHAR(50),
            PRIMARY KEY (titleID)
            )"""
c.execute(sql)
conn.commit()
print("reading in csv")
with open('reduced.title.basics.csv', 'r', encoding='utf-8') as infile:
    reader = csv.DictReader(infile, delimiter=',')
    print("writing to table")
    for i, row in enumerate(reader):
        if row['primaryTitle'] == 'Harry Potter and the Deathly Hallows: Part 2':
            print("hp 2 made it")
        sql = "INSERT INTO TITLEBASICS (titleID, movieName, year, runtime, genres) VALUES (?, ?, ?, ?, ?)"
        values = row['tconst'], row['primaryTitle'], row['startYear'], row['runtimeMinutes'], row['genres']
        c.execute(sql, values)
        #if i == 10000000:
            #break

conn.commit()
conn.close()