from pymongo import MongoClient
import csv, time

client = MongoClient()
db = client.phd

f = open('mongodb_bbox_time.csv', 'w')
with open('bboxs.csv') as file:
    reader = csv.reader(file, delimiter='\t')
    for row in reader:
        start = time.time()

        xmin, ymin, xmax, ymax = row[1].replace('SELECT * FROM roads WHERE Intersects(BuildMbr(','').replace('), geom);','').split(', ')
        query = {'geometry':
            {'$geoIntersects':
                {'$geometry': {
                    'type': 'Polygon',
                    'coordinates': [
                        [[xmin, ymin], [xmax, ymin], [xmax, ymax], [xmin, ymax], [xmin, ymin]]
                        ]
                    }
                }
            }
        }
        db.roads.find(query)

        end = time.time()
        diff = end - start
        f.write(str(query) + '\t' + str('{0:.10f}'.format(diff)) + '\n')

f.close()