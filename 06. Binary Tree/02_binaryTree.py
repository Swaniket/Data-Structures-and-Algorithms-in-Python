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
    

if __name__ == "__main__":
    newBT = TreeNode("Drinks")

    newBT.leftChild = TreeNode("Hot")
    newBT.rightChild = TreeNode("Cold")

    # print("PRE ORDER")
    # preOrderTraversal(newBT)

    # print("IN ORDER")
    # inOrderTraversal(newBT)

    # print("POST ORDER")
    # postOrderTraversal(newBT)

    levelOrderTraversal(newBT)