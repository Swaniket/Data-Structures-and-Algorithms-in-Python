def smaller(lst, x):
    elements = []

    for i in lst:
        if i < x:
            elements.append(i)

    return elements

if __name__ == "__main__":
    lst = [8, 100, 20, 40, 3, 7]
    x = 10

    print(smaller(lst, x))