# Given 2 lists, write a method to decide if one is a permutation of other.
# Permutations - Same characters, but in reverse orders
# Example: peek <-> keep, rail <-> liar

def isPermutation(lst1, lst2):
    lst2.reverse()
    if lst1 == lst2:
        return True
    return False 

if __name__ == "__main__":
    list1 = ['p', 'e', 'e', 'k']
    list2 = ['k', 'e', 'e', 'p']

    print(isPermutation(list1, list2))