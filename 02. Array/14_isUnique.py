# Implement an algorithm to determine if a list has all unique chracters
# return True if all unique, else return false
def myUniqueClassifier(lst):
    uniqueList = set(lst)
    if len(uniqueList) == len(lst):
        return True
    return False

def isUnique(lst): # -> Time Complexity: O(n)
    visited = []
    for i in lst:
        if i in visited:
            print(i)
            return False
        else:
            visited.append(i)
    return True

if __name__ == "__main__":
    myArray = [1,20,30,44,5,56,57,8,9,10,31,12,13,14,35,16,27,58,19,21]

    if myUniqueClassifier(myArray):
        print("YES")
    else:
        print("NO")

    print(isUnique(myArray))