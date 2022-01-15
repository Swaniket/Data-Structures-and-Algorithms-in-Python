# You have two numbers represented by a linked list, where each node contains a single digit
# The digits are stored in reverse order, such that 1's digit is at the head of the list.
# Write a function that adds the two numbers and returns the sum as a Linked List
# 
# list1 = 7 -> 1 -> 6 = 617
# list2 = 5 -> 9 -> 2 = 295 
# Sum, 617 + 295 = 912
# OP = 2 -> 1 -> 9

from GeneralLinkedList import LinkedList

# Time Complexity: O(n)
# Space Complexity: O(n)
def sumLL(llA, llB):
    n1 = llA.head
    n2 = llB.head
    carry = 0
    # This will hold the sum of 2 LL
    llTemp = LinkedList() 

    while n1 or n2:
        result = carry
        # Summing the values for 1st and 2nd LL
        if n1:
            result += n1.value
            n1 = n1.next
        if n2:
            result += n2.value
            n2 = n2.next
        # Only adding the 1's digit to the temp LL
        llTemp.add(int(result % 10)) 
        # Carry the 10's digit
        carry = result / 10

    return llTemp

if __name__ == "__main__":
    llA = LinkedList()
    llA.add(7)
    llA.add(1)
    llA.add(6)

    llB = LinkedList()
    llB.add(5)
    llB.add(9)
    llB.add(2)

    print(llA)
    print(llB)

    print(sumLL(llA, llB))