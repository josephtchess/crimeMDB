import sqlite3
import csv

conn = sqlite3.connect('myIMBD.db')
c = conn.cursor()

#c.execute("DROP TABLE CRIMEDATA")
#conn.commit()

sql = """CREATE TABLE CRIMEDATA (
            crimeID int NOT NULL,
            date DATETIME NOT NULL,
            crime int,
            crimeDesc varchar(128),
            PRIMARY KEY (crimeID)
            )"""
c.execute(sql)
conn.commit()
print("reading in csv1")
with open('Crime_Data_from_2010_to_2019.csv', 'r', encoding='utf-8') as infile1:
    reader1 = csv.DictReader(infile1, delimiter=',')
    print("writing to table1")
    for i, row in enumerate(reader1):
        sql = "INSERT INTO CRIMEDATA (crimeID, date, crime, crimeDesc) VALUES (?, ?, ?, ?)"
        values = row['DR_NO'], row['DATE OCC'], row['Crm Cd'], row['Crm Cd Desc']
        c.execute(sql, values)

print("reading in csv2")
with open('Crime_Data_from_2020_to_Present.csv', 'r', encoding='utf-8') as infile2:
    reader2 = csv.DictReader(infile2, delimiter=',')
    print("writing to table2")
    for j, row in enumerate(reader2):
        sql = "INSERT INTO CRIMEDATA (crimeID, date, crime, crimeDesc) VALUES (?, ?, ?, ?)"
        values = row['DR_NO'], row['DATE OCC'], row['Crm Cd'], row['Crm Cd Desc']
        c.execute(sql, values)

conn.commit()
conn.close()