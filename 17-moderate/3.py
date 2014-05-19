import math

def naive_trailing_zeros(n):
    n_fact = math.factorial(n)
    num_zeros = 0
    while n_fact % 10 == 0:
        n_fact /= 10
        num_zeros += 1
    return num_zeros

def trailing_zeros(n):
    num_zeros = 0
    i = 5
    while i <= n:
        num_zeros += n / i
        i *= 5
    return num_zeros

if __name__ == '__main__':
    inputs = (0, 1, 10, 25, 30, 100)
    for n in inputs:
        assert trailing_zeros(n) == naive_trailing_zeros(n)