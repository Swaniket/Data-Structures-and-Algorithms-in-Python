# Imagine a (literal) stack of plates. If the stack gets too high, it might toople.
# Therefore in real life, we would likely start a new stack when the previous stack exceeds some threshold.
# Implement a data structure- SetOfStacks that mimics this. SetOfStacks should be composed of
# several stacks and should create a new stack once the previous one exceeds capacity.
# .push() and .pop() should behave identiclly to a single stack (that is, .pop() should return the
# same value as it would if there were just a single stack).

# Follow Up:
# Implement a function popAt(int index) which performs a pop operation on a specific sub-stack.

class PlateStack:
    def __init__(self, capacity) -> None:
        self.capacity = capacity
        self.stacks = []

    def __str__(self):
        return self.stacks

    def print(self):
        print(self.stacks) 

    def push(self, item):
        # Check the length of stack list & see if the 1st one reached its capacity
        if len(self.stacks) > 0 and (len(self.stacks[-1])) < self.capacity:
            self.stacks[-1].append(item)
        # When the stack is empty
        else:
            self.stacks.append([item])

    def pop(self):
        # When len(stacks) > 0 and length of last stack = 0 then we will pop out of stacks
        while len(self.stacks) and len(self.stacks[-1]) == 0:
            self.stacks.pop()
        if len(self.stacks) == 0:
            return None
        # Otherwise pop out from the last stack
        else:
            return self.stacks[-1].pop()

    def popAt(self, stackNumber):
        if len(self.stacks[stackNumber]) > 0:
            return self.stacks[stackNumber].pop()
        else:
            return None

if __name__ == "__main__":
    customStack = PlateStack(2)
    # customStack = PlateStack(3)

    customStack.push(1)
    customStack.push(2)
    customStack.push(3)
    customStack.push(4)
    customStack.push(5)

    # print(customStack.pop())
    # print(customStack.popAt(1))
    customStack.print()
