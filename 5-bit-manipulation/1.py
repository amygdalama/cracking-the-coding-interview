def all_ones(num):
    bits = 0
    for i in range(num):
        bits = bits | 1 << i
    return bits

def bit_swap(N, M, i, j):
    """Replace bits j through i in N with M.
    Arguments:
    N, M -- 32-bit integers
    i, j -- integers representing bit indices
    """
    m_length = len(M)
    if m_length != j - i:
        raise IndexError("The length of M must be equal to j - i")
    left_mask = all_ones(32-j)
    left_mask = left_mask << j
    print bin(left_mask)
    right_mask = all_ones(i)

