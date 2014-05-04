def compressed(s):
    if len(s) == 0:
        return s
    compression = [s[0]]
    count = 1
    for i in xrange(1, len(s)):
        if len(compression) >= len(s)-1:
            return s
        elif s[i] == s[i-1]:
            count += 1
        else:
            compression.extend([str(count), s[i]])
            count = 1
    compression.append(str(count))
    return ''.join(compression)

if __name__ == '__main__':
    test_strings = (
        ('abcdef', 'abcdef'),
        ('aabcdef', 'aabcdef'),
        ('aaaaab', 'a5b1'),
        ('aaaaabbb', 'a5b3')
        )
    for s, expected in test_strings:
        print expected == compressed(s)
        print compressed(s)