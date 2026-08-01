class Graph:
    
    def __init__(self):
        self.adjacencyList = dict()

    def addEdge(self, src: int, dst: int) -> None:
        if src not in self.adjacencyList:
            self.adjacencyList[src] = set()
        if dst not in self.adjacencyList:
            self.adjacencyList[dst] = set()
        self.adjacencyList[src].add(dst)

    def removeEdge(self, src: int, dst: int) -> bool:
        if src not in self.adjacencyList or dst not in self.adjacencyList or dst not in self.adjacencyList[src]:
            return False
        self.adjacencyList[src].remove(dst)
        return True

    def hasPath(self, src: int, dst: int) -> bool:
        if src == dst:
            return True

        visited = set()
        visited.add(src)
        
        queue = deque()
        queue.append(src)

        while queue:
            for _ in range(len(queue)):
                currentNode = queue.popleft()
                for neighbor in self.adjacencyList[currentNode]:
                    if neighbor not in visited:
                        if neighbor == dst:
                            return True
                        visited.add(neighbor)
                        queue.append(neighbor)
        
        return False
