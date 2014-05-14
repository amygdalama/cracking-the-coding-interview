def get_bit(num, i):
    """Get the ith bit of num."""
    return num & (1 << i) != 0

def set_bit(num, i):
    """Set the ith bit of num to 1."""
    return num | (1 << i)

def clear_bit(num, i):
    """Set the ith bit of num to 0."""
    return num & ~(1 << i)

def update_bit(num, i, v):
    """Set the ith bit of num to v."""
    return num & ~(1 << i) | (v << i)

if __name__ == '__main__':
    print get_bit(5, 1)
    print get_bit(6, 1)
    print get_bit(7, 1)