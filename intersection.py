from math import sqrt
import graph


graphVertices = set()

def addVertex(p):
    pointinVertices = False
    for interp in graphVertices:
        if interp.x==p.x and interp.y==p.y:
            pointinVertices = True
            p.strNum = interp.strNum
            break
    if not pointinVertices:
        num = len(graphVertices)+1
        if p.strNum == "":
            p.strNum = str(num)
        graphVertices.add(p)

#def formatVertices(graphVertices):
#    output = "V = {" + "\n"
#    for vertex in graphVertices:
#        output += "  "
#        output += vertex.strNum + ":" + " " + str(vertex)
#        output += "\n"
#    output += "}"
#    return output

def getVerticesNumber(graphVertices):
    return len(graphVertices)

class Point(object):
    def __init__ (self, x, y):
        self.x = float(x)
        self.y = float(y)
        self.strNum = ""

    def __str__ (self):
        return '(' + str("{0:.2f}".format(self.x)) + ',' + str("{0:.2f}".format(self.y)) + ')'
        
    def length(self):
    #functionality:get length for a line's direction
        return sqrt(self.x*self.x + self.y*self.y)
    
class Line():
    def __init__(self, src, dst):
        self.src = src
        self.dst = dst
        self.itsEdges = []
        self.itsVertices = []
        
    def __str__(self):
        return str(self.src) + '-->' + str(self.dst)
    
    def dir(self):
        dir = Point((self.dst.x - self.src.x),(self.dst.y - self.src.y))
        return dir
    
    def addVertexinLine(self, v):
		 pointinVertices = False
		 for vl in self.itsVertices:
			 if vl.x==v.x and vl.y==v.y:
				 pointinVertices = True
				 break
		 if not pointinVertices:
			 self.itsVertices.append(v)
	
    def intersect(self, l):
    # functionality: find intersections in segment:self with segment:l
        direction1 = self.dir()
#        ##[check]
#        print("l",str(l))
        direction2 = l.dir()
        
        len1 = direction1.length()
        len2 = direction2.length()
#        ##[check]
#        print("len2",str(len2))
        #normalize direction1 and direction2
#        ##[check]
#        print("direction1",str(direction1))
#        print("direction2",str(direction2))
        
        direction1.x /= len1; direction1.y /= len1
        direction2.x /= len2; direction2.y /= len2
#        ##[check]
#        print("direction1\'",str(direction1))
#        print("direction2\'",str(direction2))
        #(dot product)functionality: 
        dot_prod = direction1.x*direction2.x + direction1.y*direction2.y
        candidates = []
        #
        if dot_prod == 1.0 or dot_prod == -1.0:
            #
            if  is_in_segment(l.src, self.src, self.dst) or is_in_segment(l.dst, self.src, self.dst):
                #overlap              
                candidates.append(self.src)
                candidates.append(self.dst)
                candidates.append(l.src)
                candidates.append(l.dst)
                
                if is_in_segment(l.src, self.src, self.dst):
                    #self.itsVertices.add(l.src)
                    self.addVertexinLine(l.src)
					
                if is_in_segment(self.src, l.src, l.dst):
                    #l.itsVertices.add(self.src)
                    l.addVertexinLine(self.src)
                
                if is_in_segment(l.dst, self.src, self.dst):
#                    self.itsVertices.add(l.dst)
                    self.addVertexinLine(l.dst)
                
                if is_in_segment(self.dst, l.src, l.dst):
#                    l.itsVertices.add(self.dst)
                    l.addVertexinLine(self.dst)
                    
            #else:
                #parallel, no intersection at all
        else:
            interPoint = regularIntersect(self, l)
            
            if interPoint:
                candidates.append(interPoint)
                
#                self.itsVertices.add(interPoint)
                self.addVertexinLine(interPoint)
#                l.itsVertices.add(interPoint)
                l.addVertexinLine(interPoint)
                
                candidates.append(self.src)
                candidates.append(self.dst)
                candidates.append(l.src)
                candidates.append(l.dst)
        #add vertex to whole Vertices
        for c in candidates:
            addVertex(c)
#END OF INTERSECT                

# class Vertex():
    # def __init__(self, num, point):
        # self.num  = num
        # self.point = point
        
    # def __str__(self):
        # return str(self.num) + ":  " + str(self.point) 

class Edge():
    def __init__(self,point1,point2):
        self.src = point1
        self.dst = point2
        self.split = False
        self.detail = set([self.src.strNum, self.dst.strNum])
    def __str__(self):
        return "<"+self.src.strNum+","+self.dst.strNum+">"

def findRangeforInterPoint(l1, l2):
    x_list = []
    y_list = []
    points = []
    lines = [l1,l2]
    for l in lines:
        points.append(l.src)
        points.append(l.dst)
    for p in points:
        x_list.append(p.x)
        y_list.append(p.y)
    #[second biggest, second smallest]
    x_range = [sorted(x_list, reverse=True)[1], sorted(x_list, reverse=True)[len(x_list)-2]]
    y_range = [sorted(y_list, reverse=True)[1], sorted(y_list, reverse=True)[len(y_list)-2]]
    return [x_range, y_range]
        

def regularIntersect(l1, l2):
    x1, y1 = l1.src.x, l1.src.y
    x2, y2 = l1.dst.x, l1.dst.y
    x3, y3 = l2.src.x, l2.src.y
    x4, y4 = l2.dst.x, l2.dst.y
    
    xnum = (x1*y2-x2*y1)*(x3-x4) - (x1-x2)*(x3*y4 - x4*y3)
    xden = (x1-x2)*(y3-y4) - (y1-y2)*(x3-x4)
    if xden == 0:
        return None
    else:
        xcoor = xnum / xden        
        ynum = (x1*y2-x2*y1)*(y3-y4) - (y1-y2)*(x3*y4 - x4*y3)
        ycoor = ynum / xden
        
        points=list()
        listsofXYRange = findRangeforInterPoint(l1, l2)
        #check if intersection is on these two segments
        if (xcoor < listsofXYRange[0][0] and xcoor >listsofXYRange[0][1]) or (ycoor < listsofXYRange[1][0] and ycoor >listsofXYRange[1][1]):
            point = Point(xcoor,ycoor)
            return point
        else:
            return None
def is_in_segment(p, src, dst):
    x1 = p.x - src.x
    y1 = p.y - src.y
    x2 = p.x - dst.x
    y2 = p.y - dst.y
    dir1 = Point(x1, y1)
    dir2 = Point(x2, y2)
    return (dir1.x * dir2.x + dir1.y * dir2.y) <= 0
    
if __name__ == "__main__":
    point = Point(1,4)
    point2 = Point(5,8)
    l1 = Line(point,point2)

    point3 = Point(2,-1)
    point4 = Point(2,2)
    l2 = Line(point3,point4)
    print(findRangeforInterPoint(l1, l2))
    points = [point,point2]
    search = Point(1,4)
    print(any((p.x == search.x and p.y==search.y)for p in points))
    
