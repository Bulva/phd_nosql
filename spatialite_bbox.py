from pyspatialite import dbapi2 as db

conn = db.connect('phd.sqlite')
cur = conn.cursor()

roads = cur.execute('SELECT * FROM roads')
for row in roads:
    print(row[0], row[1], row[2])