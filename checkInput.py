import intersection
import street
import re
from ast import literal_eval
import graph

           
class Check():
    def __init__(self, str):
        """

        :rtype:
        """
        self.str = str
        self.cmd = ""
        self.street = street.Street("",list())
    
    def splitandSetPoints(self, str):
        #re.sub()split strs with ")[ ]*("
        #literal_eval() convert string to its original type(,useless in my code)
        #trasnform tuple to list to assign values to self,(casue tuple is immutable)
        # self.street.points = list(literal_eval(re.sub(r'(\))(\s+)(\()','\g<1>,\g<3>',str.strip())))
        tmpPoints = list()
        points = list(literal_eval(re.sub(r'(\))(\s*)(\()','\g<1>,\g<3>',str.strip())))
        for p in points:
            x = p[0]
            y = p[1]
            tmpPoint = intersection.Point(x, y)
            self.street.points.append(tmpPoint)
        
    def checkandOperate(self):
        #split the userInput with ' " ', and 2 is the largest index of the return list
        inputInfoSplit = self.str.split("\"", 2)
        # #print("cmd:", inputInfoSplit[0])
        #inputInfoSplit contains [cmd, streetname, streetpoints] which is not verified yet
        if len(inputInfoSplit) == 1:
            #g
            stdGraph = re.compile(r'[g][ ]*')
            graphMatchResult = re.match(stdGraph, inputInfoSplit[0])
            if not graphMatchResult:
                raise Exception("Error: Wrong command.")
            else:
                #graph
                graph.build_graph()
#                print("graph")
        elif len( inputInfoSplit )==0:
            raise Exception("Error: Not enough arguments.")
        elif len(inputInfoSplit)==3 or len(inputInfoSplit)==2:
            #verify Command using regular expression 
            #(permitting cmd entered with blank(s))
            stdCmds = re.compile(r'[acr][ ]*')
            cmdMatchResult = re.match(stdCmds, inputInfoSplit[0])
            if not cmdMatchResult:
                raise Exception("Error: Wrong command.")
            else:
                self.cmd = inputInfoSplit[0]
                
                #verify Streetname
                stdStreetName = re.compile(r'^([a-zA-Z ])+$')
                nameMatchResult = re.match(stdStreetName, inputInfoSplit[1])
                if not nameMatchResult:
                    raise Exception("Error: Wrong name format.(accept letters and blanks)")
                else:
                    self.street.name = inputInfoSplit[1]
                    #add
                    stdAdd = re.compile(r'[a][ ]*')
                    addMatchResult = re.match(stdAdd, self.cmd)
                    #change
                    stdChang = re.compile(r'[c][ ]*')
                    changMatchResult = re.match(stdChang, self.cmd)
                    #remove
                    stdRemove = re.compile(r'[r][ ]*')
                    removeMatchResult = re.match(stdRemove, self.cmd)
                    
                    if addMatchResult:
                        self.checkandAdd(inputInfoSplit)
                    elif changMatchResult:
                        self.checkandChange(inputInfoSplit)
                    elif removeMatchResult:
                        self.checkandRemove(inputInfoSplit)
                    else:
                        pass
        else:
            raise Exception("Error: Wrong command and arguments.")
    
    def checkandRemove(self, inputInfoSplit):
        # #check same name
        findName = -1
        for s in graph.streetDB.data:
            if s.name.lower() == self.street.name.lower():
                findName = 1                
                graph.streetDB.removeStreet(s)
        if findName == -1:
            raise Exception("Error: street's name doesnot exist")
    
    def checkandChange(self, inputInfoSplit):   
        # #check same name
        findName = -1
        for s in graph.streetDB.data:
            if s.name.lower() == self.street.name.lower():
                findName = 1
                #verify points format
                stdPoint = re.compile(r'([ ]*\([ ]*[-]?[0-9]+[ ]*,[ ]*[-]?[0-9]+[ ]*\)[ ]*)+')
                pointMatchResult = re.match(stdPoint, inputInfoSplit[2])
                if not pointMatchResult:
                    raise Exception("Error: Wrong coordinate format")
                else:
                    #split points
                    self.splitandSetPoints(inputInfoSplit[2])
                    #save this street in streetDB
                    graph.streetDB.changeStreet(s, self.street)
                    break
        if findName == -1:
            raise Exception("Error: street's name doesnot exist")
                
    def checkandAdd(self, inputInfoSplit):
        for s in graph.streetDB.data:
            if s.name.lower() == self.street.name.lower():
                raise Exception("Error: street's name aleady exists")
        #verify points format
        stdPoint = re.compile(r'([ ]*\([ ]*[-]?[0-9]+[ ]*,[ ]*[-]?[0-9]+[ ]*\)[ ]*)+')
        pointMatchResult = re.match(stdPoint, inputInfoSplit[2])
        if not pointMatchResult:
            raise Exception("Error: Wrong coordinate format")
        else:
            #split points
            self.splitandSetPoints(inputInfoSplit[2])
            #save this street in streetDB
            graph.streetDB.addStreet(self.street)
                                    
if __name__ == "__main__":
    
#    userInput1 = Check("a \"Weber Street\" (2,-1) (2,2) (5,5) (5,6) (3,8)")    
#    userInput1.checkandOperate()
#    
#    userInput2 = Check("a \"Kings Street\" (4,2) (4,8)")
#    userInput2.checkandOperate()
#    
#    userInput3 = Check("a \"Davenport Road\" (1,4) (5,8)")
#    userInput3.checkandOperate()
#    
#    userInput4 = Check("c \"Weber Street\" (2,1) (2,2)")
#    userInput4.checkandOperate()
    userInput4 = Check("a \"a\" (4,2)(4,7)")
    userInput4.checkandOperate()
    
    userInput5 = Check("a \"b\" (4,4)(4,8)")
    userInput5.checkandOperate()
    
    userInput6 = Check("g")
    userInput6.checkandOperate()
    
#    graphGenerator()                                  
#    print(formatVertices(graphVertices))                    
#    print(formatEdges(graphEdges))
#    graph.build_graph()
