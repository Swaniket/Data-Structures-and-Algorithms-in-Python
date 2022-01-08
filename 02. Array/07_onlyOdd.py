def onlyOdd(lst):
    result = None
    for i in lst:
        count = lst.count(i)
        if count%2 != 0:
            result = i
            break
    return result
    
def onlyOddXOR(lst):
    result = 0
    for i in lst:
        result = result ^ i
    return result

if __name__ == "__main__":
    # lst = [10,30,30,10,30,30,20] #OP: 20
    # lst = [10,10,10,10,10,20,20] #OP: 10
    # lst = [10,10,20,30,30,20,40] #OP: 40
    lst = [10] #OP: 10

    print(onlyOdd(lst))
    print(onlyOddXOR(lst))