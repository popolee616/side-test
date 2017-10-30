import street
import intersection


streetDB = street.StreetDB()

graphEdges = set()
#Edges
#add each line's edges into graphEdges
def addEdge(linesEdge):
    edgeinGraphEdges = False
    for e in graphEdges:
        if e.detail == linesEdge.detail:
            edgeinGraphEdges = True
    if not edgeinGraphEdges:
        graphEdges.add(linesEdge)
#    ##[check graphEdges]
#    print("in addEdge")
#    for e in graphEdges:
#        print(str(e))
    

def formatEdges(graphEdges):
    output = "E {"
#    for edge in edges:    
    for e in graphEdges:
        if (e!= list(graphEdges)[-1]):
            output += str(e) + ","
        else:
            output += str(e)
    output += "}"
    return output


    

def graphGenerator():
    #generate lines for each street
    for s in streetDB.data:
        s.linesGenerator()    
    #find intersection         
    for i in range(len(streetDB.data)):
        for j in range(i+1,len(streetDB.data)):
#                    ##
#            print(i,streetDB.data[i].name)
#            print(j,streetDB.data[j].name)
            for street1Line in streetDB.data[i].lines:
                for street2Line in streetDB.data[j].lines:
#                    ##
#                    print(str(street1Line))
#                    print(str(street2Line))
                    street1Line.intersect(street2Line)      
    
    for s in streetDB.data:
        for l in s.lines:
            #[add] dst and src to l's itsVertices
            if len(l.itsVertices) > 0:
                l.addVertexinLine(l.src)
                l.addVertexinLine(l.dst)
                
                l.itsVertices.sort(key=lambda v: (v.x, v.y))
                # arrange self.itsEdges
                # o------+----+----+--+------o
                for i in range(len(l.itsVertices)-1):
                    v0 = l.itsVertices[i]
                    v1 = l.itsVertices[i+1]
                    edge = intersection.Edge(v0, v1)
                    l.itsEdges.append(edge)
            #arrange graphEdges
    for s in streetDB.data:
        for l in s.lines:
            for e in l.itsEdges:
                addEdge(e)
#    ##[check]mei tiao jie d vertices

def build_graph():
    graphEdges.clear()
    intersection.graphVertices.clear()
    for i in range(len(streetDB.data)):
        streetDB.data[i].lines = []
    graphGenerator()
#    ##[check graphEdges]
#    print("in build_graph")
#    for e in graphEdges:
#        print(str(e))
    print(intersection.getVerticesNumber(intersection.graphVertices))
    print(formatEdges(graphEdges))
            
