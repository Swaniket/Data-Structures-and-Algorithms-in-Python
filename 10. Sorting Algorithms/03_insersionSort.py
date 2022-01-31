# - Divide the given array into two parts
# - Take first element from unsorted array and find its correct position in sorted array
# - Repeat until unsorted array is empty

# Pros:
#   - Uses O(1) space, so when space is a concern, it's a great choise
#   - When we have continuous inflow of numbers and we want to keep them sorted

# Cons:
#   - Poor time complexity: O(n^2)


# Time Complexity -> O(n^2)
# Space Complexity -> O(1)
def insersionSort(customList):
    for i in range(1, len(customList)):
        key = customList[i]
        j = i - 1
        while j >= 0 and key < customList[j]:
            customList[j+1] = customList[j]
            j -= 1
        customList[j+1] = key
    print(customList) 

if __name__ == "__main__":
    cList = [2,1,7,6,5,3,4,9,8]

    insersionSort(cList)