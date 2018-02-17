class City:

    def __init__(self, objectid, name, inhabitants):
        self.objectid = objectid
        self.name = name
        self.inhabitants = inhabitants
        self.inhabitants_count = 0

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.objectid == other.objectid
        return NotImplemented