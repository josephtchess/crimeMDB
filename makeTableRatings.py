import sqlite3
import csv

conn = sqlite3.connect('myIMBD.db')
c = conn.cursor()

#c.execute("DROP TABLE RATINGS")
#conn.commit()

sql = """CREATE TABLE RATINGS (
            titleID int NOT NULL, 
            avgRating DECIMAL(2,1),
            numVotes int,
            PRIMARY KEY (titleID),
            FOREIGN KEY (titleID) REFERENCES TITLEBASICS(titleID)
            )"""
c.execute(sql)
conn.commit()

print("reading thing")
with open('reduced.title.ratings.csv', 'r', encoding='utf-8') as infile:
    reader = csv.DictReader(infile, delimiter=',')
    print("writing thing")
    for i, row in enumerate(reader):
        sql = "INSERT INTO RATINGS (titleID, avgRating, numVotes) VALUES (?, ?, ?)"
        values = row['tconst'], row['averageRating'], row['numVotes']
        c.execute(sql, values)

conn.commit()
conn.close()
