def is_rotation(s1, s2):
    """Check if s2 is a rotation of s1."""

    if len(s1) != len(s2):
        return False
    for i in xrange(len(s2)):
        if s2[i] == s1[0]:
            if s2[i:] + s2[:i] == s1:
                return True
    return False

def is_rotation_better(s1, s2):
    if len(s1) != len(s2):
        return False
    if s2 in s1 + s1:
        return True
    else:
        return False

if __name__ == '__main__':
    test_strings = (
        ('erbottlewat', 'waterbottle', True),
        ('waterbottle', 'erbottlewat', True),
        ('ttlewaterbo', 'waterbottle', True),
        ('ttlewaterbo', 'waterbottl', False)
        )
    for s1, s2, expected in test_strings:
        result = is_rotation_better(s1, s2)
        if result == expected:
            print "Success!"
        else:
            print "=========="
            print "Failure!"
            print "Expected:"
            print expected
            print "Result:"
            print result