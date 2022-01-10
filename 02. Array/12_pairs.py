# Write a program to find all pairs of integers whose sum is equal to a given number

# Assumptions: 
# - Distinct pair, i.e, [2,2] or [3,3] not allowed

def findPairs(lst, sum): # -> Time Complexity n^2
    pairs = []
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[i] + lst[j] == sum:
                pairs.append([lst[i], lst[j]])

    return pairs

    

if __name__ == "__main__":
    myList = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    sum = 10

    print(findPairs(myList, sum))