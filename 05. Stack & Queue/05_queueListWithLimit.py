# Also known as Circular Queue

class Queue:
    def __init__(self, maxSize) -> None:
        self.items = maxSize * [None] # Create list with maxSize number of Nones
        self.maxSize = maxSize
        self.start = -1
        self.top = -1

    def __str__(self) -> str:
        values = [str(x) for x in self.items]
        return ' '.join(values)

    # Returns true if the queue is full
    def isFull(self): # Time Complexity -> O(1)
        if self.top + 1 == self.start:
            return True
        elif self.start == 0 and self.top + 1 == self.maxSize:
            return True
        else:
            return False

    # Returns true if the queue is empty
    def isEmpty(self): # Time Complexity -> O(1)
        if self.top == -1:
            return True
        return False

    # Insert element to the queue
    def enqueue(self, value): # Time Complexity -> O(1)
        if self.isFull():
            return "The Queue is Full!"
        else:
            # Top element points to the last element
            if self.top + 1 == self.maxSize:
                self.top = 0
            else:
                self.top += 1
                # Inserting the 1st element
                if self.start == -1:
                    self.start = 0
            self.items[self.top] = value
            return "The element is inserted at the end of the queue!"

    # Delete element from the queue
    def dequeue(self): # Time Complexity -> O(1)
        if self.isEmpty():
            return "There is no element in the dequeue"
        else:
            firstElement = self.items[self.start]
            start = self.start
            # This is the only element in the queue
            if self.start == self.top:
                self.start = -1
                self.top = -1
            # When the 1st element points to the last element
            elif self.start + 1 == self.maxSize:
                self.start = 0
            else:
                self.start += 1
            self.items[start] = None
            return firstElement

    # Return the first element
    def peek(self): # Time Complexity -> O(1)
        if self.isEmpty():
            return "There is no element in the dequeue"
        else:
            return self.items[self.start]

    def delete(self): # Time Complexity -> O(1)
        self.items = self.maxSize * [None]
        self.top = -1
        self.start = -1


if __name__ == "__main__":
    customQueue = Queue(3)
    # print(customQueue.isFull())
    # print(customQueue.isEmpty())

    customQueue.enqueue(1)
    customQueue.enqueue(2)
    customQueue.enqueue(3)

    print(customQueue.dequeue())
    print(customQueue)
    print(customQueue.peek())

    customQueue.delete()
    print(customQueue)
