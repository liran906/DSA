class Vertex:
    def __init__(self, key, value=None):
        self.key = key
        self.value = value
        self.connectTo = {}
        self.connectBy = {}
        self.connections = 0
    
    def connect(self, toV, weight=0):
        self.connectTo[toV.key] = weight
        toV.connectBy[self.key] = weight
        self.connections += 1
    
    def disconnect(self, toV):
        if not toV in self.connectTo:
            print(f'vertex is not connected')
            return False
        else:
            self.connectTo.pop(toV.key)
            toV.connectBy.pop(self.key)
            self.connections -= 1
            return True
    
    def getKey(self):
        return self.key
    
    def getValue(self):
        return self.value

    def getToConnections(self):
        return self.connectTo.keys()
    
    def getByConnections(self):
        return self.connectBy.keys()
    
    def getWeight(self, nbr):
        return self.connectTo[nbr.key]


class Graph:
    def __init__(self):
        self.verDict = {}
        self.size = 0
    
    def addVertex(self, key):
        self.size += 1
        newVrtx = Vertex(key)
        self.verDict[key] = newVrtx
    
    def delVertex(self, key):
        if not key in self.verDict:
            raise IndexError(f'key {key} not in graph {self}')
        else:
            vrtx = self.getVertex(key)
            # 在遍历 connectTo 和 connectBy 时直接修改它们，可能导致遍历出错，所以复制出一个 list
            for neighbor_key in list(vrtx.connectTo):
                neighbor = self.getVertex(neighbor_key)
                neighbor.connectBy.pop(key)
            for neighbor_key in list(vrtx.connectBy):
                neighbor = self.getVertex(neighbor_key)
                neighbor.connectTo.pop(key)
            self.verDict.pop(key)
            self.size -= 1
    
    def addEdge(self, fromV, toV, weight=0):
        # if parameter input is key
        if not isinstance(fromV, Vertex):
            if fromV in self.verDict:
                fromV = self.verDict[fromV]
            else:
                fromV = Vertex(fromV)
        if not isinstance(toV, Vertex):
            if toV in self.verDict:
                toV = self.verDict[toV]
            else:
                toV = Vertex(toV)
        
        if not fromV.key in self.verDict:
            self.addVertex(fromV.key)
        if not toV.key in self.verDict:
            self.addVertex(toV.key)
        fromV.connect(toV, weight)
    
    def delEdge(self, fromV, toV):
        fromV.disconnect(toV)
    
    def __str__(self):
        result = ["Graph Structure:"]
        for v in self.verDict.values():
            result.append(f'    Vertex {v.getKey()} - value: {v.getValue()}')
            result.append('      Connections:')
            for ck, cv in v.connectTo.items():
                result.append(f'      to key: {ck} ; weight: {cv}')
        return "\n".join(result)

    def __getitem__(self, key):
        return self.getVertex(key).key, self.getVertex(key).value

    def __contains__(self, key):
        if not isinstance(key, Vertex):
            return key in self.verDict
        else:
            return key.key in self.verDict
    
    def getVertex(self, key):
        if key in self.verDict:
            return self.verDict[key]
        else:
            raise IndexError(f'key {key} not found in graph {self}')
    
    def __iter__(self):
        for i in self.verDict.values():
            yield i.key, i.value

if __name__ == '__main__':
    g = Graph()
    for i in range(6):
        g.addVertex(i)
    g.addEdge(1,2,1)
    g.addEdge(2,3,1)
    g.addEdge(1,3,1)
    g.addEdge(3,4,1)
    g.addEdge(4,5,1)
    print(g)

    g.delVertex(2)
    print(g)
    