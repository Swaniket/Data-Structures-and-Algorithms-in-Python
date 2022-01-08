# Calculate the power of a number using recursion

def calcPower(base, exp):
    assert exp >= 0 and int(exp) == exp, 'The exponent has to be a possitive integer'
    if exp == 0: return 1
    if exp == 1: return base
    return base * calcPower(base, exp-1)

if __name__ == "__main__":
    # print(calcPower(5, 2))
    print(calcPower(3.2, 2))
    # print(calcPower(5, 1.2))
    # print(calcPower(2, -1))
    # print(calcPower(-1, 2))

