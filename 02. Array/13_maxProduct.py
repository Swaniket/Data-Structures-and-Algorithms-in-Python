# Find the maximum product of two integeres in the array where all elements are possitive
def myMaxProduct(lst):
    lst.sort()
    return lst[-1] * lst[-2]

def maxProduct(lst): # -> Time Complexity: O(n^2)
    maxProduct = 0
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[i] * lst[j] > maxProduct:
                maxProduct = lst[i] * lst[j]
                pairs = str(lst[i]) + ", " + str(lst[j])
    return pairs, maxProduct

if __name__ == "__main__":
    myArray = [1,20,30,44,5,56,57,8,9,10,31,12,13,14,35,16,27,58,19,21]

    print(myMaxProduct(myArray))

    pairs, maxProduct = maxProduct(myArray)
    print(pairs)
    print(maxProduct)
