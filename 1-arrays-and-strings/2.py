def permutations(s1, s2):
    """Determine if s1 and s2 are permutations of eachother, meaning
    they have the same characters but possibly in different order.
    Whitespace and capitalization are significant."""
    if len(s1) != len(s2):
        return False
    s1 = sorted(s1)
    s2 = sorted(s2)
    for i in xrange(len(s1)):
        if s1[i] != s2[i]:
            return False
    return True


if __name__ == '__main__':
    test_strings =(
        ("", "", True),
        ("cat", "tac", True),
        ("CAT", "tac", False),
        ("cat", "", False),
        )
    for s1, s2, expected in test_strings:
        print expected == permutations(s1, s2)
