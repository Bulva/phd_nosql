from basin.river import River
from basin.city import City


client = MongoClient()
db = client.phd

class Basin:
    OBJECTID_START_RIVER = 7

    def __init__(self, conn=None):
        self.rivers = []
        self.cities = []

        self.it_rivers = {Basin.OBJECTID_START_RIVER,}

        self.cur = conn.cursor()

        self.cur.execute('SELECT * FROM cities')
        cities = self.cur.fetchall()
        for city in cities:
            self.cities.append(City(city[2], city[4], city[23]))

        self.cur.execute('SELECT * FROM rivers')
        rivers = self.cur.fetchall()
        for river in rivers:
            self.rivers.append(River(river[2], river[4], conn=conn))

    def nearest_cities(self):
        for city in self.cities:
            self.cur.execute(
                """SELECT objectid, St_Distance((SELECT geom FROM cities WHERE objectid='{}'), rivers.geom) 
                   FROM rivers ORDER BY 2""".format(city.objectid))
            river_near = self.cur.fetchone()
            for river in self.rivers:
                if river.objectid == river_near[0]:
                    river.cities.append(city)

    def get_river_by_id(self, objectid):
        for river in self.rivers:
            if river.objectid == objectid:
                return river
        return None

    def find_touching(self, river, prohibited):
        rivers_list = []
        self.cur.execute("""SELECT objectid FROM rivers WHERE 
          st_touches((SELECT geom FROM rivers WHERE objectid={}), rivers.geom)""".format(river.objectid))
        touching_rivers = self.cur.fetchall()
        if len(touching_rivers) > 0:
            for objectid in touching_rivers:
                if objectid[0] not in self.it_rivers:
                    if prohibited is None:
                        rivers_list.append(self.get_river_by_id(objectid[0]))
                    else:
                        if objectid[0] not in prohibited:
                            rivers_list.append(self.get_river_by_id(objectid[0]))
            return rivers_list
        return None


    def find_touching_ids(self, river):
        rivers_list = []
        self.cur.execute("""SELECT objectid FROM rivers WHERE 
          st_touches((SELECT geom FROM rivers WHERE objectid={}), rivers.geom)""".format(river.objectid))
        touching_rivers = self.cur.fetchall()
        if len(touching_rivers) > 0:
            for objectid in touching_rivers:
                if objectid[0] not in self.it_rivers:
                    rivers_list.append(objectid[0])
            return rivers_list
        return None
