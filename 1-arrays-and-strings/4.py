def replace_spaces(s):
    """Replace spaces in a string with '%20'."""

    s = list(s)
    for i in xrange(len(s)):
        if s[i] == ' ':
            s[i] = '\%20'
    return ''.join(s)

if __name__ == '__main__':
    test_strings = (
        ('', ''),
        (' ', '\%20'),
        ('  ', '\%20\%20')
        )
    for s, expected in test_strings:
        print expected == replace_spaces(s)