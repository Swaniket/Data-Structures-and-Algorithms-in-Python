# Queue using python list without size limit

class Queue:
    def __init__(self) -> None:
        self.items = []

    def __str__(self) -> str:
        values = [str(x) for x in self.items]
        return ' '.join(values)

    def isEmpty(self): # Time Complexity -> O(1)
        if self.items == []:
            return True
        return False

    # Insert element to the queue is known as Enqueue
    def enqueue(self, value): # Time Complexity -> O(n^2)
        self.items.append(value)
        return "The element is inserted at the end of the queue"

    # Removing an element from the queue is known as Dequeue
    def dequeue(self): # Time Complexity -> O(n)
        if self.isEmpty():
            return "There is no element in the Queue!"
        return self.items.pop(0)

    def peek(self): # Time Complexity -> O(1)
        if self.isEmpty():
            return "There is no element in the Queue!"
        return self.items[0]

    def deleteQueue(self): # Time Complexity -> O(1)
        self.items = None

if __name__ == "__main__":
    customQueue = Queue()

    customQueue.enqueue(1)
    customQueue.enqueue(2)
    customQueue.enqueue(3)
    print(customQueue)
    # print(customQueue.isEmpty())   

    print(customQueue.dequeue())
    print(customQueue)