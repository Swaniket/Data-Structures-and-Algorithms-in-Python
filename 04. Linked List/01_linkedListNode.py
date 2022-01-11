class Node:
    def __init__(self, key):
        self.key = key
        self.next = None

if __name__ == "__main__":
    # temp1 = Node(10)
    # temp2 = Node(20)
    # temp3 = Node(30)

    # temp1.next = temp2
    # temp2.next = temp3

    # head = temp1

    # --------OR----------

    head = Node(10)
    head.next = Node(20)
    head.next.next = Node(30)