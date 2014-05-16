def multiply(a, b):
    total = 0
    for i in xrange(abs(b)):
        total += a
    if b < 0:
        total = negate(total)
    return total

def multiply2(a, b):
    if b < 0:
        return negate(sum(a for i in range(b)))
    return sum(a for i in range(b))

def negate(a):
    if a == 0:
        return a
    step = -1 if a > 0 else 1
    neg_a = 0
    for i in xrange(abs(a)):
        neg_a += step
    return neg_a

def negate2(a):
    if a == 0:
        return a
    step = -1 if a > 0 else 1
    return sum(step for i in xrange(abs(a)))

def subtract(a, b):
    return a + negate(b)

def divide(a, b):
    if b == 0:
        raise ValueError("Can't divide by zero")
    count = 0
    product = 0
    abs_a = abs(a)
    abs_b = abs(b)
    while abs_a > product + abs_b:
        product += abs_b
        count += 1
    if (a < 0 and b > 0) or (a > 0 and b < 0):
        return negate(count)
    return count

if __name__ == '__main__':
    assert negate(0) == 0
    assert negate2(0) == 0
    assert multiply(0, 5) == 0
    assert multiply(4, 5) == 20
    assert multiply2(0, 5) == 0
    assert multiply2(4, 5) == 20
    assert subtract(4, 5) == -1
    assert subtract(6, -7) == 13
    assert divide(4, 3) == 1
    assert divide(234, 16) == 234/16