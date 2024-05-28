import sqlite3

DBNAME = 'CrimeMDB Client/myIMBD.db'

conn = sqlite3.connect(DBNAME)
c = conn.cursor()

try:
    sql = "DROP INDEX titleName_idx"
    c.execute(sql)
except sqlite3.OperationalError:
    print("titleName_idx does not exist, skip drop")

try:
    sql = "DROP INDEX titleID_idx"
    c.execute(sql)
except sqlite3.OperationalError:
    print("titleID_idx does not exist, skip drop")

try:
    sql = "DROP INDEX titleYear_idx"
    c.execute(sql)
except sqlite3.OperationalError:
    print("titleYear_idx does not exist, skip drop")

try:
    sql = "DROP INDEX actorName_idx"
    c.execute(sql)
except sqlite3.OperationalError:
    print("actorName_idx does not exist, skip drop")

try:
    sql = "DROP INDEX nameID_idx"
    c.execute(sql)
except sqlite3.OperationalError:
    print("nameID_idx does not exist, skip drop")

try:
    sql = "DROP INDEX PtitleID_idx"
    c.execute(sql)
except sqlite3.OperationalError:
    print("PtitleID_idx does not exist, skip drop")

try:
    sql = "DROP INDEX PnameID_idx"
    c.execute(sql)
except sqlite3.OperationalError:
    print("PnameID_idx does not exist, skip drop")

try:
    sql = "DROP INDEX RnameID_idx"
    c.execute(sql)
except sqlite3.OperationalError:
    print("actorName_idx does not exist, skip drop")

try:
    sql = "DROP INDEX crimeID_idx"
    c.execute(sql)
except sqlite3.OperationalError:
    print("crimeID_idx does not exist, skip drop")

print("make index for movieName")
sql = "CREATE INDEX titleName_idx on TITLEBASICS (movieName)"
c.execute(sql)
print("make index for titleID")
sql = "CREATE INDEX titleID_idx on TITLEBASICS (titleID)"
c.execute(sql)
print("make index for year")
sql = "CREATE INDEX titleYear_idx on TITLEBASICS (year)"
c.execute(sql)
print("make index for name")
sql = "CREATE INDEX actorName_idx on NAMEBASICS (name)"
c.execute(sql)
print("make index for nameID")
sql = "CREATE INDEX nameID_idx on NAMEBASICS (nameID)"
c.execute(sql)
print("make index for titleID")
sql = "CREATE INDEX PtitleID_idx on PRINCIPALS (titleID)"
c.execute(sql)
print("make index for nameID")
sql = "CREATE INDEX PnameID_idx on PRINCIPALS (nameID)"
c.execute(sql)
print("make index for titleID")
sql = "CREATE INDEX RnameID_idx on RATINGS (titleID)"
c.execute(sql)
print("make index for crimeID")
sql = "CREATE INDEX crimeID_idx on CRIMEDATA (crimeID)"
c.execute(sql)

conn.commit()
conn.close()
print("indexing operation complete")