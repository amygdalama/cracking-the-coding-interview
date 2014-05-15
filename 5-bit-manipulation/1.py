def all_ones(num):
    bits = 0
    for i in range(num):
        bits = bits | 1 << i
    return bits

def bit_length(num):
    return len(bin(num)) - 2        # account for 0b prefix

def clear_bits(N, i, j):
    n_length = bit_length(N)
    left_mask = all_ones(n_length-j-1)
    left_mask = left_mask << j+1
    right_mask = all_ones(i)
    mask = left_mask | right_mask
    return N & mask

def bit_swap(N, M, i, j):
    """Replace bits j through i in N with M.
    Arguments:
    N, M -- 32-bit integers
    i, j -- integers representing bit indices
    """
    m_length = bit_length(M)
    n_length = bit_length(N)
    if m_length != j - i + 1:
        raise IndexError("The length of M must be equal to j - i")
    N = clear_bits(N, i, j)
    N = N | M << i
    return N

if __name__ == '__main__':
    N = int('10000000000', 2)
    M = int('10011', 2)
    i = 2
    j = 6
    output = int('10001001100', 2)
    assert bit_swap(N, M, i, j) == output
    N = int('10000000000', 2)
    M = int('11011', 2)
    i = 6
    j = 10
    output = int('11011000000', 2)
    assert bit_swap(N, M, i, j) == output
