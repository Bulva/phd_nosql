class River:

    def __init__(self, objectid, name, conn=None):
        self.objectid = objectid
        self.nazev = name
        self.cities = []

        self.cur = conn.cursor()

