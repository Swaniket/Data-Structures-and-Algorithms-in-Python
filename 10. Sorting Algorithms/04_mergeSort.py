# - Merge sort is a divide and conquer algorithm.
# - Divide the i/p array in two halves and we keep having recursively until they become too small
#   that cannot be broken further.
# - Merge halves by sorting them.

# Pros:
#   - It's a stable sorting Algorithm
#   - Time complexity O(NlogN)

# Cons:
#   - Bad Space complexity O(n)

# It's a helper function which merges two subarray of custom list
# l = left index
# m = middle of the list
# r = last of the list
def merge(customList, l, m, r): # Time Complexity -> O(n)
    # No. of elements in the 1st sub array
    n1 = m - l + 1
    # No. of elements in the 2nd sub array
    n2 = r - m

    L = [0] * (n1)
    R = [0] * (n2)

    # Copy elements to subarray
    for i in range(0, n1):
        L[i] = customList[l+i]
    for j in range(0, n2):
        R[j] = customList[m+1+j]

    # Merge temp sub arrays into the list in a sorted array
    i = 0
    j = 0
    k = l
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            customList[k] = L[i]
            i += 1
        else:
            customList[k] = R[j]
            j += 1
        k += 1
    while i < n1:
        customList[k] = L[i]
        i += 1
        k += 1
    while j < n2:
        customList[k] = R[j]
        j += 1
        k += 1

# l = left index - start index, r = right index - end index
# Time Complexity -> O(NlogN)
# Space Complexity -> O(n)
def mergeSort(customList, l, r):
    if l < r:
        m = (l+(r-1))//2
        mergeSort(customList, l, m)
        mergeSort(customList, m + 1, r)
        merge(customList, l, m, r)
    return customList

if __name__ == "__main__":
    cList = [2,1,7,6,5,3,4,9,8]

    print(mergeSort(cList, 0, 8))