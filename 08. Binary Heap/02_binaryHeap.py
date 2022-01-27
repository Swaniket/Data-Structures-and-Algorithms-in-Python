class Heap:
    def __init__(self, size) -> None: # Time Complexity -> O(1), Space Complexity -> O(n)
        self.customList = (size + 1) * [None]
        self.heapSize = 0
        self.maxSize = size + 1

# Return the value of the root - The highest/lowest value
def peekForHeap(rootNode): # Time Complexity -> O(1), Space Complexity -> O(1)
    if not rootNode:
        return
    else:
        return rootNode.customList[1] 

# Returns the number of elements in the heap
def sizeOfHeap(rootNode): # Time Complexity -> O(1), Space Complexity -> O(1)
    if not rootNode:
        return
    else:
        return rootNode.heapSize

# All 4 traversal is possible in Binary heap. Its same as BST
def levelOrderTraversal(rootNode): # Time Complexity -> O(n), Space Complexity -> O(1)
    if not rootNode:
        return
    else:
        for i in range(1, rootNode.heapSize + 1):
            print(rootNode.customList[i])

# Method to make adjustments when the binary heap property is violated
def heapifyTreeInsert(rootNode, index, heapType): # Time Complexity -> O(logN), Space Complexity -> O(logN)
    # find the parent node (will be same from left & right child)
    parentIndex = int(index/2)
    if index <= 1:
        return
    if heapType == "min":
        # if current value is smaller than parent we will swap'em
        if rootNode.customList[index] < rootNode.customList[parentIndex]:
            # Swap
            temp = rootNode.customList[index]
            rootNode.customList[index] = rootNode.customList[parentIndex]
            rootNode.customList[parentIndex] = temp
        heapifyTreeInsert(rootNode, parentIndex, heapType)
    elif heapType == "max":
        # if current value is larger than parent we will swap'em
        if rootNode.customList[index] > rootNode.customList[parentIndex]:
            # Swap
            temp = rootNode.customList[index]
            rootNode.customList[index] = rootNode.customList[parentIndex]
            rootNode.customList[parentIndex] = temp
        heapifyTreeInsert(rootNode, parentIndex, heapType)

# Insert a value in the binary heap
def insertNode(rootNode, nodeValue, heapType): # Time Complexity -> O(logN), Space Complexity -> O(logN)
    if rootNode.heapSize + 1 == rootNode.maxSize:
        return "The Binary Heap is full!"
    rootNode.customList[rootNode.heapSize + 1] = nodeValue
    rootNode.heapSize += 1
    heapifyTreeInsert(rootNode, rootNode.heapSize, heapType)
    return "The value has been successfully inserted"

# Heapify method for extracting a node from Heap
def heapifyTreeRemove(rootNode, index, heapType):
    leftIndex = index * 2
    rightIndex = index * 2 + 1
    swapChild = 0
    # We dont have any child for current node
    if rootNode.heapSize < leftIndex:
        return
    # We have only left child
    elif rootNode.heapSize == leftIndex:
        if heapType == "min":
            if rootNode.customList[index] > rootNode.customList[leftIndex]:
                temp = rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[leftIndex]
                rootNode.customList[leftIndex] = temp
            return
        elif heapType == "max":
            if rootNode.customList[index] < rootNode.customList[leftIndex]:
                temp = rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[leftIndex]
                rootNode.customList[leftIndex] = temp
            return
    # We have both children
    else:
        if heapType == "min":
            if rootNode.customList[leftIndex] < rootNode.customList[rightIndex]:
                swapChild = leftIndex
            else:
                swapChild = rightIndex
            if rootNode.customList[index] > rootNode.customList[swapChild]:
                temp = rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[swapChild]
                rootNode.customList[swapChild] = temp
        else:
            if rootNode.customList[leftIndex] > rootNode.customList[rightIndex]:
                swapChild = leftIndex
            else:
                swapChild = rightIndex
            if rootNode.customList[index] < rootNode.customList[swapChild]:
                temp = rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[swapChild]
                rootNode.customList[swapChild] = temp
    heapifyTreeRemove(rootNode, swapChild, heapType)

# Only the root element can be extracted from a heap
def extractNode(rootNode, heapType): # Time Complexity -> O(logN), Space Complexity -> O(logN)
    if rootNode.heapSize == 0:
        return
    else:
        extractedNode = rootNode.customList[1]
        rootNode.customList[1] == rootNode.customList[rootNode.heapSize]
        rootNode.customList[rootNode.heapSize] = None
        rootNode.heapSize -= 1
        heapifyTreeRemove(rootNode, 1, heapType)
        return extractedNode

def deleteEntireBP(rootNode):
    rootNode.customList = None


if __name__ == "__main__": 
    newHeap = Heap(5)

    # print(sizeOfHeap(newHeap))

    insertNode(newHeap, 4, "min")
    insertNode(newHeap, 5, "min")
    insertNode(newHeap, 2, "min")
    insertNode(newHeap, 1, "min")

    print(extractNode(newHeap, "min"))

    deleteEntireBP(newHeap)
    
    levelOrderTraversal(newHeap)