# In case of selection sort we repeatedly find the min element and move it to the sorted part
# of array to make unsorted part sorted

# Pros:
#   - It works well on small array
#   - It's in place sorting algo, no additional space is required

# Cons:
#   - Performs poorly when given big number of elements in array
#   - time complexity O(n^2)
#   - Performance is depended on initial sorting state of the elements


# Time Complexity -> O(n^2)
# Space Complexity -> O(1)
def selectionSort(customList):
    for i in range(len(customList)):
        # Finding minimum element
        minIndex = i
        for j in range(i+1, len(customList)):
            if customList[minIndex] > customList[j]:
                minIndex = j
        # Swap
        customList[i], customList[minIndex] = customList[minIndex], customList[i]
    print(customList)
        


if __name__ == "__main__":
    cList = [2,1,7,6,5,3,4,9,8]

    selectionSort(cList)
