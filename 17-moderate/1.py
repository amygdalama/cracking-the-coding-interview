def swap_numbers(a, b):
    """Swap the values of a and b."""
    a = a - b
    b = b + a
    a = b - a
    return a, b

if __name__ == '__main__':
    assert swap_numbers(3, 16) == (16, 3)
    assert swap_numbers(16, 3) == (3, 16)
    assert swap_numbers(16, 0) == (0, 16)