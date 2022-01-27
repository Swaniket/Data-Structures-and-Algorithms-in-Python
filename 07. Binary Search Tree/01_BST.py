import QueueLinkedListHelper as queue

class BSTNode:
    def __init__(self, data) -> None: # Time Complexity -> O(1), Space Complexity -> O(1)
        self.data = data
        self.leftChild = None
        self.rightChild = None

def insertNode(rootNode, nodeValue): # Time Complexity -> O(logN), Space Complexity -> O(logN)
    if rootNode.data == None:
        rootNode.data = nodeValue
    # Checking for the leftchild
    elif nodeValue <= rootNode.data:
        # when the leftchild is none
        if rootNode.leftChild is None:
            rootNode.leftChild = BSTNode(nodeValue)
        else:
            insertNode(rootNode.leftChild, nodeValue)
    # Checking for the rightchild
    else:
        if rootNode.rightChild is None:
            rootNode.rightChild = BSTNode(nodeValue)
        else:
            insertNode(rootNode.rightChild, nodeValue)
    return "The node has been successfully inserted"

# Root Node -> Left Subtree -> Right Subtree
def preOrderTraversal(rootNode): # Time Complexity -> O(n), Space Complexity -> O(n)
    if not rootNode:
        return
    print(rootNode.data)
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)

# Left Subtree -> Root Node -> Right Subtree
def inOrderTraversal(rootNode): # Time Complexity -> O(n), Space Complexity -> O(n)
    if not rootNode:
        return
    inOrderTraversal(rootNode.leftChild)
    print(rootNode.data)
    inOrderTraversal(rootNode.rightChild)

# Left Subtree -> Right Subtree -> Root Node
def postOrderTraversal(rootNode): # Time Complexity -> O(n), Space Complexity -> O(n)
    if not rootNode:
        return
    postOrderTraversal(rootNode.leftChild)
    postOrderTraversal(rootNode.rightChild)
    print(rootNode.data)

# Visiting node level by level
def levelOrderTraversal(rootNode): # Time Complexity -> O(n), Space Complexity -> O(n)
    if not rootNode:
        return
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not (customQueue.isEmpty()):
            root = customQueue.dequeue()
            print(root.value.data)
            # When leftchild exists
            if root.value.leftChild is not None:
                customQueue.enqueue(root.value.leftChild)
            # When rightchild exists
            if root.value.rightChild is not None:
                customQueue.enqueue(root.value.rightChild)

# Search for a node in BST
def searchBST(rootNode, nodeValue): # Time Complexity -> O(logN), Space Complexity -> O(logN)
    if rootNode.data == nodeValue:
        print("The value is found")
    elif nodeValue < rootNode.data:
        if rootNode.leftChild.data == nodeValue:
            print("The value is found")
        else:
            searchBST(rootNode.leftChild, nodeValue)
    else:
        if rootNode.rightChild.data == nodeValue:
            print("The value is found")
        else:
            searchBST(rootNode.rightChild, nodeValue)
    return "The value is not found"

# Helper for delete - Find the successor - min value in the right subtree
def minValueNode(BSTNode):
    current = BSTNode
    while current.leftChild is not None:
        current = current.next
    return current

# Delete a node from BST
def deleteNode(rootNode, nodeValue): # Time Complexity -> O(logN), Space Complexity -> O(logN)
    if rootNode is None:
        return rootNode
    if nodeValue < rootNode.data:
        rootNode.leftChild = deleteNode(rootNode.leftChild, nodeValue)
    elif nodeValue > rootNode.data:
        rootNode.rightChild = deleteNode(rootNode.rightChild, nodeValue)
    else:
        # Delete for only 1 child
        if rootNode.leftChild is None:
            temp = rootNode.rightChild
            rootNode = None
            return temp
        if rootNode.rightChild is None:
            temp = rootNode.leftChild
            rootNode = None
            return temp
        # Delete a node which has 2 children
        temp = minValueNode(rootNode.rightChild)
        rootNode.data = temp.data
        rootNode.rightChild = deleteNode(rootNode.rightChild, temp.data)
    return rootNode

# Delete the entire BST
def deleteBST(rootNode): # Time Complexity -> O(1), Space Complexity -> O(1)
    rootNode.data = None
    rootNode.leftChild = None
    rootNode.rightChild = None
    return "The BST has been successfully deleted"


if __name__ == "__main__":
    newBST = BSTNode(None)

    insertNode(newBST, 70)
    insertNode(newBST, 50)
    insertNode(newBST, 90)
    insertNode(newBST, 30)
    insertNode(newBST, 60)
    insertNode(newBST, 80)
    insertNode(newBST, 100)
    insertNode(newBST, 20)
    insertNode(newBST, 40)

    # print(newBST.data)
    # print(newBST.leftChild.data)

    # preOrderTraversal(newBST)
    # inOrderTraversal(newBST)
    # postOrderTraversal(newBST)
    # levelOrderTraversal(newBST)

    # searchBST(newBST, 40)

    # deleteNode(newBST, 20)
    # deleteNode(newBST, 100)

    print(deleteBST(newBST))

    levelOrderTraversal(newBST)