import sqlite3
import csv

DBNAME = 'myIMBD.db'

conn = sqlite3.connect(DBNAME)
c = conn.cursor()

#c.execute("DROP TABLE PRINCIPALS")
#conn.commit()

sql = """CREATE TABLE PRINCIPALS (
            titleID int NOT NULL, 
            ordering int NOT NULL,
            nameID int NOT NULL,
            job VARCHAR(50),
            character VARCHAR(50),
            PRIMARY KEY (titleID, ordering),
            FOREIGN KEY (titleID) REFERENCES TITLEBASICS(titleID),
            FOREIGN KEY (nameID) REFERENCES NAMEBASICS(nameID)
            )"""
c.execute(sql)
conn.commit()

print("reading in csv")
with open('reduced.title.principals.csv', 'r', encoding='utf-8') as infile:
    reader = csv.DictReader(infile, delimiter=',')
    print('writing to table')
    for i, row in enumerate(reader):
        sql = "INSERT INTO PRINCIPALS (titleID, ordering, nameID, job, character) VALUES (?, ?, ?, ?, ?)"
        values = row['tconst'], row['ordering'], row['nconst'], row['category'], row['characters']
        c.execute(sql, values)
        #if i == 10000000:
           #break

conn.commit()
conn.close()