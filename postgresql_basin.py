import psycopg2
from river import River
import time

iterated_cities = []
iterated_rivers = []

OBJECTID_START_RIVER = 7

rivers = []

def get_kod(id):
    for riv2 in rivers:
        if riv2.objectid == id and len(riv2.cities) > 0:
            return riv2.cities[0]

# zacinam prochazet u rozvodnice a postupuju nahoru
# pridavam jednotlive useky do pole a kdyz narazim na reku s mestem tak zacnu pocitat
def compute_inhabitants(start, inhabitants, id=7, count=False):
    cur.execute("""SELECT objectid FROM rivers WHERE st_touches((SELECT geom FROM rivers WHERE objectid={}), rivers.geom)""".format(id))
    iterated_rivers.append(id)
    touch_rivers = cur.fetchall()
    if len(touch_rivers) > 0:
        for riv in touch_rivers:
            if riv[0] not in iterated_rivers:
                print(count)
                if count:
                    id_obec = get_kod(riv[0])
                    if id_obec is None:
                        inhabitants += compute_inhabitants(start, id=riv[0], inhabitants=inhabitants, count=True)
                    else:
                        cur.execute("""SELECT pocet_obyv FROM cities WHERE kod_obec='{}'""".format(id_obec))
                        inhabitants += cur.fetchall()[0][0]
                        inhabitants += compute_inhabitants(start, id=riv[0], inhabitants=inhabitants, count=True)
                else:
                    print('Start: {}'.format(start))
                    print('Riv0: {}'.format(riv[0]))
                    print('Inhabi: {}'.format(inhabitants))
                    if start == riv[0]:
                        print('rovna se')
                        id_obec = get_kod(riv[0])
                        print('Id obce: '+id_obec)
                        cur.execute("""SELECT pocet_obyv FROM cities WHERE kod_obec='{}'""".format(id_obec))#zjisti pocet obyvatel pro obec a pak ve vetvi count zjistuj dal
                        inhabitants = cur.fetchall()[0][0]
                        print('Inhabitants: {}'.format(inhabitants))
                        inhabitants += compute_inhabitants(start, id=riv[0], inhabitants=inhabitants, count=True)
                    else:
                        inhabitants = compute_inhabitants(start, id=riv[0], inhabitants=inhabitants, count=False)
    else:
        return inhabitants

try:
    conn = psycopg2.connect("dbname='phd_nosql' user='postgres' host='localhost' password='postgres'")
except:
    print('I am unable to connect to the database')


cur = conn.cursor()
cur.execute('SELECT * FROM cities')
cities = cur.fetchall()

#naplnim si objekty rek
cur.execute('SELECT objectid, nazev FROM rivers')
rivs = cur.fetchall()
for riv in rivs:
    rivers.append(River(riv[0], riv[1]))

for city in cities:
    cur.execute("""SELECT objectid, St_Distance((SELECT geom FROM cities WHERE kod_obec='{}'), rivers.geom) FROM rivers ORDER BY 2""".format(city[3]))
    river_near = cur.fetchone()
    for rivob in rivers:
        if rivob.objectid == river_near[0]:
            rivob.cities.append(city[3])

for city in cities:
    for riv in rivers:
        for kod in riv.cities:
            if city[3] == kod:
                print(riv.objectid)
                print(riv.cities)
                obyvatele = compute_inhabitants(start=riv.objectid, inhabitants=0)
    print('Obyvatele: {}'.format(obyvatele))






#SELECT objectid,Distance((SELECT geometry FROM cities WHERE kod_obec=510882), rivers.geometry) FROM rivers ORDER BY 2;
#SELECT objectid FROM rivers WHERE Touches((SELECT geometry FROM rivers WHERE objectid=16, rivers.geometry));

#SELECT objectid, Distance((SELECT geometry FROM cities WHERE kod_obec=510882), rivers.geometry) FROM rivers ORDER BY 2;

#SELECT Distance((SELECT geometry FROM rivers WHERE objectid=16), cities.geometry) FROM cities ORDER BY 1;

#SELECT objectid FROM rivers WHERE Touches((SELECT geometry FROM rivers WHERE objectid=7), rivers.geometry);

