# Find the sum of N natural numbers

def sumN(n):
    if n == 1:
        return 1
    return sumN(n-1) + n

if __name__ == "__main__":
    n = int(input())
    print(sumN(n))