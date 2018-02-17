import psycopg2
from basin.basin_postgresql import Basin


def iterate_over_rivers(sum, city=None, start_counting=False, river_act=None, basin=None, finish_river=None):
    parts = basin.find_touching_ids(basin.get_river_by_id(river_act.objectid))
    print('Nejbližší vodní úseky: {} pro úsek: {}'.format(parts, river_act.objectid))
    for river in basin.find_touching(basin.get_river_by_id(river_act.objectid), prohibited=None):
        print('Vybral jsem vodni tok s ID: {}'.format(river.objectid))
        print('Srovnávam ID: {}'.format(river_act.objectid == river.objectid))
        print('finish: {}'.format(repr(finish_river.objectid)))
        print('parts: {}'.format(parts))
        print('length: {}'.format(len(parts)))
        if len(river.cities) > 0:
            for river_city in river.cities:
                if city == river_city:
                    start_counting = True
                    print('Začínám počítat')
                    finish_river = river
                elif (start_counting):
                    if river.objectid not in basin.it_rivers:
                        print("suma před: {}".format(sum))
                        city.inhabitants_count += int(river_city.inhabitants)
                        print("suma po: {}".format(sum))
        print('Přidávám river_act řeku s ID: {} do iterovaných řek'.format(river_act.objectid))
        basin.it_rivers.add(river_act.objectid)
        print('Přidávám river řeku s ID: {} do iterovaných řek'.format(river.objectid))
        basin.it_rivers.add(river.objectid)
        #print('Seznam iterovaných řek: {}'.format(basin.it_rivers))
        prohibited = basin.find_touching_ids(basin.get_river_by_id(river_act.objectid))
        #print('Seznam zakázaných IDs: {}'.format(prohibited))
        print('Pro další iteraci použiju řeku s ID: {}'.format(river.objectid))
        print('\n')
        iterate_over_rivers(sum, city=city, start_counting=start_counting, river_act=river, basin=basin, finish_river=finish_river)



try:
    conn = psycopg2.connect("dbname='phd_nosql' user='postgres' host='localhost' password='postgres'")
except:
    print('I am unable to connect to the database')

# populate objects from database
basin = Basin(conn)

# populate cities to nearest rivers
basin.nearest_cities()

# select first river and find touching rivers
sum = 0

for city in basin.cities:
    print('Mesto: {}'.format(city.name))
    print('Suma pro {} je {}'.format(city.name, iterate_over_rivers(sum, city=city, river_act=basin.get_river_by_id(7), basin=basin, finish_river=basin.get_river_by_id(7))))
    basin.it_rivers.clear()

for city in basin.cities:
    print('Zapisuje výsledek pro {}: {}'.format(city, sum))
    f = open('sum_postgresql.csv', 'a')
    f.write(city.name + '\t' + str(city.inhabitants_count) + '\n')
    f.close()