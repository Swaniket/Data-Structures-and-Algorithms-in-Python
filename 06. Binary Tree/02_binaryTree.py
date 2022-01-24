# Depth First Search
#   - Preorder Traversal
#   - Inorder Traversal
#   - Post order Traversal
# Breadth First Search
#   - Level Order Traversal

import QueueLinkedListHelper as queue

class TreeNode:
    def __init__(self, data) -> None:
        self.data = data
        self.leftChild = None
        self.rightChild = None

# Root Node -> Left Subtree -> Right Subtree
def preOrderTraversal(rootNode): # Time Complexity -> O(n), Space Complexity -> O(n)
    if not rootNode:
        return
    print(rootNode.data)
    preOrderTraversal(rootNode.leftChild) #O(n/2)
    preOrderTraversal(rootNode.rightChild) #O(n/2)

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

# Visit level by level (start from left)
def levelOrderTraversal(rootNode): # Time Complexity -> O(n), Space Complexity -> O(n)
    if not rootNode:
        return
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            print(root.value.data)
            if root.value.leftChild is not None:
                customQueue.enqueue(root.value.leftChild) # Value comes from queue class
            if root.value.rightChild is not None:
                customQueue.enqueue(root.value.rightChild)

# Perfrom search in BT using Level Order Traversal
def searchBT(rootNode, nodeValue): # Time Complexity -> O(n), Space Complexity -> O(n)
    if not rootNode:
        return "The BT doesn't exists"
    else: 
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            if root.value.data == nodeValue:
                return "Success"
            if root.value.leftChild is not None:
                customQueue.enqueue(root.value.leftChild)
            if root.value.rightChild is not None:
                customQueue.enqueue(root.value.rightChild)
        return "Not Found"


if __name__ == "__main__":
    newBT = TreeNode("Drinks")
    leftChild = TreeNode("Hot")
    tea = TreeNode("Tea")
    coffee = TreeNode("Coffee")
    leftChild.leftChild = tea
    leftChild.rightChild = coffee
    rightChild = TreeNode("Cold")
    newBT.leftChild = leftChild
    newBT.rightChild = rightChild

    # print("PRE ORDER")
    # preOrderTraversal(newBT)

    # print("IN ORDER")
    # inOrderTraversal(newBT)

    # print("POST ORDER")
    # postOrderTraversal(newBT)

    # levelOrderTraversal(newBT)

    print(searchBT(newBT, "Tea"))
