# We will be using collections.deque as a FIFO Queue
# Internally Deque is implemented using doubly linked list which gives us excellent perfomance

from collections import deque

# Create Queue
customQueue = deque(maxlen=3)
# print(customQueue)

# Add elements
customQueue.append(1)
customQueue.append(2)
customQueue.append(3)
# Inserting more elements than the max size will override the top most elements
customQueue.append(4) # OP [2, 3, 4]
# print(customQueue)

# Remove elements
customQueue.popleft()
# print(customQueue)

# Delete Queue
customQueue.clear()
print(customQueue)