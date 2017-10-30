import intersection


class Street:
    #confirm the name and coordinate, before make a street object
    def __init__(self, name, points):
        self.name = str(name)
        self.points = points
        self.lines = list()
    
    def __str__(self):
        streetInfo = "\"" + self.name + "\""
        for p in self.points:
            streetInfo += " "+ str(p)
        return streetInfo
        
    def linesGenerator(self):
        for i in range(len(self.points)-1):
            line = intersection.Line(self.points[i],self.points[i+1])
            self.lines.append(line)
        

class StreetDB:
    
    def __init__(self):
        self.data = []
        
    def findStreet(self, name):
        if len(self.data) > 0:
            for i in range(len(self.data)):
                #use case insensitive string comparison in STREET'S NAME
                if self.data[i].name.lower() == name.lower():
                    return i
            return -1
        else:
            return -2
                
    # def addStreet(self, street):
        # if self.findStreet(street.name) <= -1:
            # self.data.append(street)
            # return 1
        # else:
            # return -1
    def addStreet(self, street):
        self.data.append(street)
                
    def removeStreet(self, street):
        self.data.remove(street)
        
    def changeStreet(self,street0,street1):
        self.removeStreet(street0)
        self.addStreet(street1)

if __name__ == "__main__":
    streetDB = StreetDB()
    # street1 = Street("Weber Street", [(2,-1),(2,2),(5,5),(5,6),(3,8)])
    # streetDB.data.append(street1)
    point1 = Point(4, 2)
    point2 = Point(4, 8)
    points = []
    points.append(point1)
    points.append(point2)
    
    
    street2 = Street("King Street", points)
    print(streetDB.findStreet(street2))
    print(streetDB.addStreet(street2))
    print(len(streetDB.data))
    print(streetDB.removeStreet(street2))
    print(len(streetDB.data))
    
    
    
