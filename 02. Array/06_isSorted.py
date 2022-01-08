def isSorted(lst):
    sorted = "YES"
    if not lst or len(lst) == 1:
        return sorted 
    
    firstElement = lst[0]

    for i in lst[1:]:
        if i >= firstElement:
            firstElement = i
        else:
            sorted = "NO"
            return sorted

    return sorted


if __name__ == "__main__":
    # lst = [10,20,30] # OP: YES
    # lst = [10,20,20,30] # OP: YES
    # lst = [10,5,2] # OP: NO
    # lst = [10] # OP: YES
    lst = [] # OP: YES

    print(isSorted(lst))