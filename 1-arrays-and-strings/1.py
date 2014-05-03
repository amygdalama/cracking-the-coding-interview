def sorted_list_has_unique_characters(l):
    """Determines if a sorted list has unique characters."""
    if len(l) < 2:
        return True
    elif l[0] == l[1]:
        return False
    else:
        return sorted_list_has_unique_characters(l[1:])


def string_has_unique_characters(s, other_data_structures=True):
    """Determines if a string has all unique characters."""

    l = sorted(s.lower())
    return sorted_list_has_unique_characters(l)

if __name__ == '__main__':
    test_strings = (
        ("", True),
        ("a", True),
        ("aA", False),
        ("abcdefghijk", True),
        ("abcdefghijka", False)
        )
    for s, expected in test_strings:
        print expected == string_has_unique_characters(s)