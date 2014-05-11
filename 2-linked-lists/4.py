from singly import LinkedList

def partition_linked_list(l, x):
    """Partition a linked list l around a value x, such that all
    elements of the list less than x come before all elements of
    the list greater than or equal to x."""
    less_than_x = LinkedList()
    greater_than_x = LinkedList()
    head = l.head
    while head:
        if head.cargo < x:
            less_than_x.append(head.cargo)
        else:
            greater_than_x.append(head.cargo)
        head = head.next
    return l

def partition_list(l, x):
    """Partition a Python list l around a value x, such that all
    elements of the list less than x come before all elements of
    the list greater than or equal to x."""
    less_than_x = []
    greater_than_x = []
    for element in l:
        if element < x:
            less_than_x.append(element)
        else:
            greater_than_x.append(element)
    less_than_x.extend(greater_than_x)
    return less_than_x

def partition_list_in_place(l, x):
    """Partition a Python list l around a value x, such that all
    elements of the list less than x come before all elements of
    the list greater than or equal to x."""
    count = 0
    index = 0
    while count < len(l):
        if l[index] >= x:
            element = l.pop(index)
            l.append(element)
        else:
            index += 1
        count += 1
    return l

def print_test(preserved_test, expected, result):
    if expected == result:
        print "Kittens!"
    else:
        print "=========="
        print "Nope!"
        print "Test: ", preserved_test
        print "Expected: ", expected
        print "Result: ", result

def test_list():
    tests = (
        [],
        [0],
        range(10),
        list(reversed(range(10)))
        )
    for test in tests:
        preserved_test = test[:]
        expected = partition_list(test, 6)
        result = partition_list_in_place(test, 6)
        print_test(preserved_test, expected, result)

def test_linked_list():
    tests = (
        LinkedList(),
        LinkedList().append(0),
        LinkedList()
        )

if __name__ == '__main__':
    test_list()
    test_linked_list()
