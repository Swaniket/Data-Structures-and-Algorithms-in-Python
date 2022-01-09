def rotateUsingSlicing(lst, d):
    lst = lst[d:] + lst[:d]
    return lst

def rotateUsingDeque(lst, d):
    from collections import deque

    dq = deque(lst)
    dq.rotate(-d)
    lst = list(dq)

    return lst

def simpleRotate(lst, d): # -> Time complexity is O[nd]
    for i in range(0,d):
        lst.append(lst.pop(0))
    return lst

def reverseHelper(lst, start, end):
    while start < end:
        lst[start], lst[end] = lst[end], lst[start]
        start = start + 1
        end = end - 1

def leftRotate(lst, d): # -> Time complexity is O[n]
    n = len(lst)

    reverseHelper(lst, 0, d-1)
    reverseHelper(lst, d, n-1)
    reverseHelper(lst, 0, n-1)

    return lst

if __name__ == "__main__":
    lst = [1,2,3,4,5]
    d = 2
    # OP: [3,4,5,1,2]

    lst2 = [10,20,30,40]
    d2 = 3
    # OP: [40,10,20,30]

    print(rotateUsingSlicing(lst, d))
    print(rotateUsingDeque(lst, d))
    print(simpleRotate(lst, d))
    print(leftRotate(lst2, d2))