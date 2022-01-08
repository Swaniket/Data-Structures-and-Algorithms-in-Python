def oddEven(lst):
    oddList = []
    evenList = []

    for i in lst:
        if i % 2 == 0:
            evenList.append(i)
        else:
            oddList.append(i)

    print("The List of Odd Numbers:", oddList)
    print("The List of Even Numbers:", evenList)


if __name__ == "__main__":
    lst = [10,41,30,15,80]

    oddEven(lst)