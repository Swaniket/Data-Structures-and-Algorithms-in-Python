def reverseUsingLibrary(lst):
    new_list = list(reversed(lst))
    return new_list

def reverseUsingSlicing(lst):
    new_list = lst[::-1]
    return new_list

def customReverse(lst):
    start = 0
    end = len(lst) - 1
    while start < end:
        lst[start], lst[end] = lst[end], lst[start]
        start = start + 1
        end = end - 1
    return lst


if __name__ == "__main__":
    lst = [10,20,30]

    print(reverseUsingLibrary(lst))
    print(reverseUsingSlicing(lst))
    print(customReverse(lst))