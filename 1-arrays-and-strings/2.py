def permutations_by_sorting(s1, s2):
    """Determine if s1 and s2 are permutations of each other, meaning
    they have the same characters but possibly in different order.
    Whitespace and capitalization are significant.
    Use the sorting method."""

    if len(s1) != len(s2):
        return False
    s1 = sorted(s1)
    s2 = sorted(s2)
    for i in xrange(len(s1)):
        if s1[i] != s2[i]:
            return False
    return True

def count_chars(s):
    """Assuming that s is a string of ASCII characters, count
    the number of times that each character appears in the string.
    Return a list of length 256 of the counts."""

    count = [0] * 256
    for char in s:
        count[ord(char)] += 1
    return count


def permutations_by_char_count(s1, s2):
    """Determine if s1 and s2 are permutations of each other, meaning
    they have the same characters but possibly in different order.
    Whitespace and capitalization are significant.
    Use the sorting method."""

    s1_count = count_chars(s1)
    s2_count = count_chars(s2)
    return s1_count == s2_count


if __name__ == '__main__':
    test_strings =(
        ("", "", True),
        ("cat", "tac", True),
        ("CAT", "tac", False),
        ("cat", "", False),
        )
    for s1, s2, expected in test_strings:
        print expected == permutations_by_char_count(s1, s2)
