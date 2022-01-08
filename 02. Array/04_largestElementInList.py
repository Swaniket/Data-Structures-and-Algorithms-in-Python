def largest(lst):
    if not lst:
        return None
    else: 
        max = lst[0]
        for i in range(1, len(lst)):
            if lst[i] > max:
                max = lst[i]
        return max

if __name__ == "__main__":
    lst = [2, 40, 4, 21, 14, 8]
    # lst = []
    print(largest(lst))