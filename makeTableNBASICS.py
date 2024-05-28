import sqlite3
import csv

DBNAME = 'myIMBD.db'

conn = sqlite3.connect(DBNAME)
c = conn.cursor()

#c.execute("DROP TABLE NAMEBASICS")
#conn.commit()

sql = """CREATE TABLE NAMEBASICS (
            nameID int NOT NULL, 
            name VARCHAR(50),
            birthYear int,
            deathYear int,
            professions VARCHAR(50),
            PRIMARY KEY (nameID)
            )"""
c.execute(sql)
conn.commit()

print("reading in csv")
with open('name.basics.tsv', 'r', encoding='utf-8') as infile:
    reader = csv.DictReader(infile, delimiter='\t')
    print("writing to table")
    for i, row in enumerate(reader):
        sql = "INSERT INTO NAMEBASICS (nameID, name, birthYear, deathYear, professions) VALUES (?, ?, ?, ?, ?)"
        values = row['nconst'], row['primaryName'], row['birthYear'], row['deathYear'], row['primaryProfession']
        c.execute(sql, values)
        #if i == 10000000:
            #break

conn.commit()
conn.close()