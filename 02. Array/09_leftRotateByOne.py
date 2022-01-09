def myLeftRotator(lst):
    firstElement = lst[0]
    lst.remove(firstElement)
    lst.append(firstElement)

    return lst

def leftRotationSlicing(lst):
    lst = lst[1:] + lst[0:1]
    return lst

def leftRotatorMethods(lst):
    lst.append(lst.pop(0))
    return lst

def rotateByOne(lst):
    n = len(lst)
    x = lst[0]
    for i in range(1, n):
        lst[i-1] = lst[i]
    lst[n-1] = x

    return lst

if __name__ == "__main__":
    lst = [10,20,30,40]
    lst2 = [1,2,3]
    lst3 = [11,22,33]

    print(myLeftRotator(lst))
    print(leftRotationSlicing(lst2))
    print(leftRotatorMethods(lst2))
    print(rotateByOne(lst3))