import numpy as np

def addColumn(arr, position, newCol): # Time Complexity -> O(mn)
    newArray = np.insert(arr, position, newCol, axis=1)
    print(newArray)
    return newArray

def addColumnEnd(arr, newCol): # Time Complexity -> O(1)
    newArray = np.append(arr, newCol, axis=1)
    print(newArray)
    return newArray

def deleteColumn(arr, deletionIndex):
    deletedArray = np.delete(arr, deletionIndex, axis=1)
    print(deletedArray)
    return deletedArray

def addRow(arr, position, newCol): # Time Complexity -> O(mn)
    newArray = np.insert(arr, position, newCol, axis=0)
    print(newArray)
    return newArray

def addRowEnd(arr, newCol): # Time Complexity -> O(1)
    newArray = np.append(arr, newCol, axis=0)
    print(newArray)
    return newArray

def deleteRow(arr, deletionIndex):
    deletedArray = np.delete(arr, deletionIndex, axis=0)
    print(deletedArray)
    return deletedArray

def accessElements(array, rowIndex, columnIndex): # Time & Space Complexity -> O(1)
    if rowIndex >= len(array) and columnIndex >= len(array[0]):
        print('Incorrect Index!')

    print(array[rowIndex][columnIndex])
    return array[rowIndex][columnIndex]

def traverseTDArray(array): # Time Complexity -> O(mn), if m=n, then O(n^2)
    numberOfRows = len(array)
    numberOfColumns = len(array[0])

    for i in range(numberOfRows):
        for j in range(numberOfColumns):
            print(array[i][j])

def linearSearchForTDArray(array, element): # Time Complexity -> O(mn), if m=n, then O(n^2)
    numberOfRows = len(array)
    numberOfColumns = len(array[0])

    for i in range(numberOfRows):
        for j in range(numberOfColumns):
            if array[i][j] == element:
                return "Found at: ({i}, {j})".format(i=i, j=j)
            
    return "Element not found!"


if __name__ == "__main__":
    twoDArray = np.array([[11, 15, 10, 6], [10, 14, 11, 5], [12, 17, 12, 8], [15, 18, 14, 9]])
    print("The original array is:\n", twoDArray)

    # addColumn(twoDArray, 0, [[1,2,3,4]])
    # addRow(twoDArray, 0, [[1,2,3,4]])

    # addColumnEnd(twoDArray,[[1,2,3,4]])
    # addRowEnd(twoDArray,[[1,2,3,4]])

    # accessElements(twoDArray, 3, 3)

    # traverseTDArray(twoDArray)

    # print(linearSearchForTDArray(twoDArray, 55))
    # print(linearSearchForTDArray(twoDArray, 14))
    deleteColumn(twoDArray, 0)
