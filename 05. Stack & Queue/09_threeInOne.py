# Describe how you could use a single Python list to implememt three stacks

# For a list of size 9 - 
# Stack 1 - [0], [1], [2] -> [0, n/3)
# Stack 2 - [3], [4], [6] -> [n/3, 2n/3)
# Stack 3 - [7], [8], [9] -> [2n/3, n)

class MultiStack:
    def __init__(self, stackSize) -> None:
        self.numberOfStacks = 3
        self.customList = [0] * (stackSize * self.numberOfStacks)
        self.stackSize = stackSize
        # To keep size of each stack
        self.sizes = [0] * self.numberOfStacks

    def isFull(self, stackNumber):
        if self.sizes[stackNumber] == self.stackSize:
            return True
        return False

    def isEmpty(self, stackNumber):
        if self.sizes[stackNumber] == 0:
            return True
        return False

    # Returns the top element index from a given stack
    def indexOfTop(self, stackNumber):
        offset = stackNumber * self.stackSize
        return offset + self.sizes[stackNumber] - 1

    # Insert an element by stack number
    def push(self, item, stackNumber):
        if self.isFull(stackNumber):
            return "This stack is full"
        else:
            # Increase the size for that perticular stack in the sizes array by 1
            self.sizes[stackNumber] += 1
            # Add the item into the customList
            self.customList[self.indexOfTop(stackNumber)] = item

    # Returns the top element from a given stack and removes it
    def pop(self, stackNumber):
        if self.isEmpty(stackNumber):
            return "The stack is already empty!"
        else:
            # Extract the value of the top element of the perticular stack
            value = self.customList[self.indexOfTop(stackNumber)]
            # Setting the top element to 0
            self.customList[self.indexOfTop(stackNumber)] = 0
            # Decreasing the sizes array for that index by 1
            self.sizes[stackNumber] -= 1
            return value

    def peek(self, stackNumber):
        if self.isEmpty(stackNumber):
            return "The stack is already empty!"
        else:
            # Extract the value of the top element of the perticular stack
            value = self.customList[self.indexOfTop(stackNumber)]
            return value

if __name__ == "__main__":
    customStack = MultiStack(6)

    # print(customStack.isFull(0))
    # print(customStack.isEmpty(1))

    customStack.push(1, 0)
    customStack.push(2, 0)
    customStack.push(3, 0)

    customStack.push(10, 1)
    customStack.push(20, 1)

    customStack.push(100, 2)

    print(customStack.peek(0))
    print(customStack.peek(1))

    print(customStack.pop(2))
    print(customStack.peek(2))
