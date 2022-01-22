# It's the most secure queue implementation with support for multitasking
# It has 3 types of Queues:
# 1. FIFO Queue, 2. LIFO Queue - Stack, 3. Priority Queue

import queue as q

# Creating/ Initializing queue
customQueue = q.Queue(maxsize=3)

# Check if the queue is empty
print(customQueue.empty())

# Inser elements at the end of the queue
customQueue.put(1)
customQueue.put(2)
customQueue.put(3)

# Number of elements in the queue
print(customQueue.qsize())

# Check if the queue is full
print(customQueue.full())

# Dequeue the 1st element from the queue
print(customQueue.get())