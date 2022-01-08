# Find the sum of digits of a positive integer number using recursion

def sumOfDigits(num):
    n = int(num)
    if n == 0: return 0
    return n%10 + sumOfDigits(n/10)

if __name__ == "__main__":
    print(sumOfDigits(int(input())))