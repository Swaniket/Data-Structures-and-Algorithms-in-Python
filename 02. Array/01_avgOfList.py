def avgLst(lst):
    sum = 0

    for i in lst:
        sum = sum + i
        
    return sum/len(lst)

if __name__ == "__main__":
    lst = [10,20,30,40]

    print(avgLst(lst))