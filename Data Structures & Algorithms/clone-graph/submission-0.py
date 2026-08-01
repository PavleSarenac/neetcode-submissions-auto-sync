"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        self.visited = dict()

        def dfs(node: Node) -> Node:
            deepCopyNode = Node(node.val)
            self.visited[deepCopyNode.val] = deepCopyNode
            for neighbor in node.neighbors:
                if neighbor.val not in self.visited:
                    deepCopyNode.neighbors.append(dfs(neighbor))
                else:
                    deepCopyNode.neighbors.append(self.visited[neighbor.val])
            return deepCopyNode

        return dfs(node)
        
