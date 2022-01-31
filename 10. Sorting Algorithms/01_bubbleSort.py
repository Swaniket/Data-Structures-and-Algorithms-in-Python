# Repeatedly compare each pair of adjacent items and swap them if they are in the wrong order

# When to use Bubble Sort?
#   - When Space is a concern
#   - It's easy to implement

# When NOT to use it?
#   - O(n^2) time complexity is not suitable for fast sorting
#   - Perfomance will be very slow for large inputs


# Time Complexity -> O(n^2)
# Space Complexity -> O(1)
def bubbleSort(customList):
    for i in range(len(customList) - 1):
        for j in range(len(customList) - i - 1):
            if customList[j] > customList[j+1]:
                customList[j], customList[j+1] = customList[j+1], customList[j]
    print(customList)

if __name__ == "__main__":
    cList = [2,1,7,6,5,3,4]
    bubbleSort(cList)