from pyspatialite import dbapi2 as db
import csv, time

conn = db.connect('phd.sqlite')
cur = conn.cursor()

f = open('spatialite_bbox_time.csv', 'w')
with open('bboxs.csv') as file:
    reader = csv.reader(file, delimiter='\t')
    for row in reader:
        start = time.time()
        roads = cur.execute(row[1])
        end = time.time()
        diff = end - start
        f.write(row[1]+'\t'+str(diff)+'\n')
f.close()