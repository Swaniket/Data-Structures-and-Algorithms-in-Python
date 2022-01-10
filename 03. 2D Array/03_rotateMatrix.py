# Given an image represented by a NxN matrix, write a method to rotate the image by 90 degrees
# It means that the 1st col -> 1st row, 2nd col -> 2nd row and so on...
import numpy as np

def rotateMatrix(matrix):
    numberOfRows = len(matrix)
    numberOfLayers = numberOfRows // 2 # This is number of layers of the matrix

    for layer in range(numberOfLayers):
        first = layer
        last = numberOfRows - layer - 1
        for i in range(first, last):
            # Save top element
            top = matrix[layer][i]
            # move left element to top
            matrix[layer][i] = matrix[-i-1][layer]
            # move buttom element to the left
            matrix[-i-1][layer] = matrix[-layer-1][-i-1]
            # move right element to buttom
            matrix[-layer-1][-i-1] = matrix[i][-layer-1]
            # move top element to right
            matrix[i][-layer-1] = top
    return matrix


if __name__ == "__main__":
    myArray = np.array([[1,2,3], [4,5,6], [7,8,9]])
    print('Original Matrix: \n', myArray)
    print('Transformed Matrix: \n')
    print(rotateMatrix(myArray))