def replace_spaces(s):
    """Replace spaces in a string with '%20'."""

    s = list(s)
    for i in xrange(len(s)):
        if s[i] == ' ':
            s[i] = '%20'
    return ''.join(s)

def replace_spaces_using_char_array(s):
    """Replace spaces in a string with '%20' using lists with entries
    that are only length one, like a character array in Java."""

    space_count = 0
    for char in s:
        if char == ' ':
            space_count += 1
    new_length = len(s) + space_count * 2
    new_string = [''] * new_length
    for i in xrange(len(s)-1, -1, -1):
        if s[i] == ' ':
            new_string[new_length - 1] = '0'
            new_string[new_length - 2] = '2'
            new_string[new_length - 3] = '%'
            new_length -= 3
        else:
            new_string[new_length - 1] = s[i]
            new_length -= 1
    return ''.join(new_string)


if __name__ == '__main__':
    test_strings = (
        ('', ''),
        (' ', '%20'),
        ('  ', '%20%20')
        )
    for s, expected in test_strings:
        print expected == replace_spaces_using_char_array(s)
        print replace_spaces_using_char_array(s)