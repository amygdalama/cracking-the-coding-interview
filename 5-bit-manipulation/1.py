def bit_swap(N, M, i, j):
    """Replace bits j through i in N with M.
    Arguments:
    N, M -- strings of the form '0b010001'
    i, j -- integers representing bit indices
    """
    m_length = len(M)
    if m_length != j - i:
        raise IndexError("The length of M must be equal to j - i")
    mask = int('1' * m_length)
