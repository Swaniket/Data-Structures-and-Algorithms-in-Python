# Convert a number from decimal to binary using recursion

def convertDToB(n):
    assert int(n) == n, "Decimal number should be an integer"
    if n == 0: return 0
    return n%2 + 10*convertDToB(int(n/2)) 

if __name__ == "__main__":
    print(convertDToB(23))
    # print(convertDToB(13))
    # print(convertDToB(-34))
    # print(convertDToB(45.4))