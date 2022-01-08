def findSecondLargest(lst):
    if len(lst) <= 1:
        return None
    else:
        largest = lst[0]
        secondLargest = None
        for i in lst[1:]:
            if i > largest:
                secondLargest = largest
                largest = i
            elif i < largest:
                if secondLargest == None or i > secondLargest:
                    secondLargest = i

        return secondLargest

                
if __name__ == "__main__":
    lst = [20,10,20,8,12]
    # lst = [10,10,10]
    print(findSecondLargest(lst))