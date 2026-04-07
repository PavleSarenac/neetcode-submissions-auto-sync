class TreeNode:
    def __init__(self, key=-1, value=-1, left=None, right=None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right

class TreeMap:
    
    def __init__(self):
        self.root = None

    def insert(self, key: int, val: int) -> None:
        if not self.root:
            self.root = TreeNode(key, val)
            return

        currentNode = self.root
        while True:
            if currentNode.key == key:
                currentNode.value = val
                break
            elif currentNode.key > key:
                if not currentNode.left:
                    currentNode.left = TreeNode(key, val)
                    break
                currentNode = currentNode.left
            else:
                if not currentNode.right:
                    currentNode.right = TreeNode(key, val)
                    break
                currentNode = currentNode.right

    def get(self, key: int) -> int:
        result = -1
        currentNode = self.root
        while currentNode:
            if currentNode.key == key:
                result = currentNode.value
                break
            elif currentNode.key > key:
                currentNode = currentNode.left
            else:
                currentNode = currentNode.right
        return result

    def getMin(self) -> int:
        if not self.root:
            return -1
        currentNode = self.root
        while currentNode.left:
            currentNode = currentNode.left
        return currentNode.value

    def getMax(self) -> int:
        if not self.root:
            return -1
        currentNode = self.root
        while currentNode.right:
            currentNode = currentNode.right
        return currentNode.value

    def remove(self, key: int) -> None:
        previousNode = None
        currentNode = self.root
        while currentNode:
            if currentNode.key == key:
                break
            previousNode = currentNode
            if currentNode.key > key:
                currentNode = currentNode.left
            else:
                currentNode = currentNode.right

        if not currentNode:
            return

        if not currentNode.left and not currentNode.right:
            if not previousNode:
                self.root = None
                return
            if previousNode.left and previousNode.left.key == currentNode.key:
                previousNode.left = None
            else:
                previousNode.right = None
            return

        if not currentNode.left:
            nodeForDeletion = currentNode
            previousNode = None
            currentNode = currentNode.right
            while currentNode.left:
                previousNode = currentNode
                currentNode = currentNode.left
            nodeForDeletion.key = currentNode.key
            nodeForDeletion.value = currentNode.value
            if not previousNode:
                nodeForDeletion.right = currentNode.right
            else:
                previousNode.left = currentNode.right
            return

        nodeForDeletion = currentNode
        previousNode = None
        currentNode = currentNode.left
        while currentNode.right:
            previousNode = currentNode
            currentNode = currentNode.right
        nodeForDeletion.key = currentNode.key
        nodeForDeletion.value = currentNode.value
        if not previousNode:
            nodeForDeletion.left = currentNode.left
        else:
            previousNode.right = currentNode.left
        
    def getInorderKeys(self) -> List[int]:
        inorderKeys = []
        def inorder(node):
            if not node:
                return None
            inorder(node.left)
            inorderKeys.append(node.key)
            inorder(node.right)
        inorder(self.root)
        return inorderKeys