# In the list implementation
# left child = cell[2x]
# right child = cell[2x+1]
# Where x is the index of the root node.
# We we skip the index 0 inorder to work with this formula

class BinaryTree:
    def __init__(self, size) -> None: # Time Complexity -> O(1), Space Complexity -> O(n)
        self.customList = size * [None]
        self.lastUsedIndex = 0
        self.maxSize = size

    def insertNode(self, value): # Time Complexity -> O(1), Space Complexity -> O(1)
        if self.lastUsedIndex + 1 == self.maxSize:
            return "The Binary Tree is full"
        self.customList[self.lastUsedIndex+1] = value
        self.lastUsedIndex += 1
        return "The value has been successfully inserted"

    # Searching by level order traversal
    def searchNode(self, nodeValue): # Time Complexity -> O(n), Space Complexity -> O(1)
        for i in range(len(self.customList)):
            if self.customList[i] == nodeValue:
                return "Success!"
        return "Not found!"

    # Root Node -> Left Subtree -> Right Subtree
    def preOrderTraversal(self, index): # Time Complexity -> O(n), Space Complexity -> O(n)
        if index > self.lastUsedIndex:
            return
        print(self.customList[index])
        # Visiting Left sub tree
        self.preOrderTraversal(index * 2)
        # Visiting right subtree
        self.preOrderTraversal(index * 2 + 1)

    # Left Subtree -> Root Node -> Right Subtree
    def inOrderTraversal(self, index): # Time Complexity -> O(n), Space Complexity -> O(n)
        if index > self.lastUsedIndex:
            return
        # Visit left subtree
        self.inOrderTraversal(index * 2)
        # print the root node
        print(self.customList[index])
        # Visiting right subtree
        self.inOrderTraversal(index * 2 + 1)

    # Left Subtree -> Right Subtree -> Root Node
    def postOrderTraversal(self, index): # Time Complexity -> O(n), Space Complexity -> O(n)
        if index > self.lastUsedIndex:
            return
        # Visit left subtree
        self.postOrderTraversal(index * 2)
        # Visiting right subtree
        self.postOrderTraversal(index * 2 + 1)
        # print the root node
        print(self.customList[index])

    # Traverse level by level- in list implementation, it's same as printing the list
    def levelOrderTraversal(self, index): # Time Complexity -> O(n), Space Complexity -> O(n)
        for i in range(index, self.lastUsedIndex + 1):
            print(self.customList[i])

    # It will replace the deepest node value with the value to be deleted & delete the deepest node
    def deleteNode(self, value): # Time Complexity -> O(n), Space Complexity -> O(1)
        if self.lastUsedIndex == 0:
            return "There is no node to delete"
        for i in range(1, self.lastUsedIndex + 1):
            if self.customList[i] == value:
                # Replacing the value with the deepest node value
                self.customList[i] = self.customList[self.lastUsedIndex]
                # Delete the deepest node
                self.customList[self.lastUsedIndex] = None
                self.lastUsedIndex -= 1
                return "The node has been successfully deleted!"

    # Deletes the entire tree
    def deleteBT(self): # Time Complexity -> O(1), Space Complexity -> O(1)
        self.customList = None
        return "The BT has been successfully deleted"




if __name__ == "__main__":
    newBT = BinaryTree(8)

    newBT.insertNode("Drinks")
    newBT.insertNode("Hot")
    newBT.insertNode("Cold")
    newBT.insertNode("Tea")
    newBT.insertNode("Coffee")

    # print(newBT.searchNode("abc"))

    # newBT.preOrderTraversal(1)
    # newBT.inOrderTraversal(1)
    # newBT.postOrderTraversal(1)

    print(newBT.deleteNode('Hot'))

    # print(newBT.deleteBT())

    newBT.levelOrderTraversal(1)
        