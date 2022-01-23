# Implement Queue class which implements a queue using 2 stacks

class Stack:
    def __init__(self) -> None:
        self.list = []

    def __len__(self):
        return len(self.list)

    def push(self, item):
        self.list.append(item)

    def pop(self):
        if len(self.list) == 0:
            return None
        return self.list.pop()

class QueueViaStack:
    def __init__(self) -> None:
        self.inStack = Stack()
        self.outStack = Stack()

    def enqueue(self, item):
        self.inStack.push(item)

    def dequeue(self):
        # If there are elements in the instack we will push it to outstack
        # it will reverse the order of the elements
        while len(self.inStack):
            self.outStack.push(self.inStack.pop())
        result = self.outStack.pop()
        # Pushing all elements back to instack
        while len(self.outStack):
            self.inStack.push(self.outStack.pop())
        return result

if __name__ == "__main__":
    customQueue = QueueViaStack()

    customQueue.enqueue(1)
    customQueue.enqueue(2)
    customQueue.enqueue(3)

    print(customQueue.dequeue())

    customQueue.enqueue(4)
    print(customQueue.dequeue())