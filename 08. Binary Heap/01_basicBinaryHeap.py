### What is Binary Heap?

# A Binary Heap is a binary tree with the following properties.
#   - A binary head is either a min heap or a max heap, the key at root must be min
#     among all keys present in Binary Heap. The same property must be recursively
#     true for all nodes in the Binary Tree
#   - It's a complete tree (All levels are completely filled except possibly the last level
#     has all keys as left as possible). This property of Binary Heap makes them suitable
#     to be stored in an array.


### Why we need a Binary Heap?

# Find the minimum or maximum number among a set of numbers in logN time. And also we want
# to make sure that inserting additional numbers does not take more than O(logN) time
#   - Why not to use sorted array? Find Min: O(1), Insersion: O(n)
#   - Why not use Linked List? Insersion: O(n)


### Practical Use:

#   - Prim's Algorithm
#   - Heap Sort
#   - Priority Queue


### Types of Binary Heap:

#   - Min Heap: The value of each node is less than or equal to the value of both it's children
#   - Max Heap: It's exactly the opposite of min heap, that is the value of each node is more than
#               or equal to the value of both it's children.


### Common Operations:
#   - Creation of Binary Heap
#   - Peek top of Binary Heap
#   - Extract Min/ Max
#   - Traversal of Binary Heap
#   - Size of Binary Heap
#   - Insert a value in Binary Heap
#   - Delete the entire binary heap


### Implementation Options:
#   - Array Implementation
#   - Reference/Pointer Implementation

class Heap:
    def __init__(self, size) -> None: # Time Complexity -> O(1), Space Complexity -> O(n)
        self.customList = (size + 1) * [None]
        self.heapSize = 0
        self.maxSize = size + 1

newBinaryHeap = Heap(5)