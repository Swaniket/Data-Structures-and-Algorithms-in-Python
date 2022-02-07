# - Merge sort is a divide and conquer algorithm.
# - Divide the i/p array in two halves and we keep having recursively until they become too small
#   that cannot be broken further.
# - Merge halves by sorting them.

# Pros:
#   - It's a stable sorting Algorithm
#   - Time complexity O(NlogN)

# Cons:
#   - Bad Space complexity O(n)

def mergeTwoSortedArray(a,b, arr):
    i = j = k = 0

    lenA = len(a)
    lenB = len(b)

    # Iterate through both of the list till reach end in any of 'em
    while i < lenA and j < lenB:
        if a[i] <= b[j]:
            arr[k] = a[i]
            i += 1
        else:
            arr[k] = b[j]
            j += 1
        k += 1

    while i < lenA:
        arr[k] = a[i]
        i += 1
        k += 1
    while j < lenB:
        arr[k] = b[j]
        j += 1
        k += 1


def mergeSort(arr):
    if len(arr) <= 1:
        return

    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]

    mergeSort(left)
    mergeSort(right)

    mergeTwoSortedArray(left, right, arr)

if __name__ == "__main__":
    test_cases = [
        [10, 3, 15, 7, 8, 23, 98, 29],
        [],
        [3],
        [9,8,7,2],
        [1,2,3,4,5]
    ]

    for arr in test_cases:
        mergeSort(arr)
        print(arr)