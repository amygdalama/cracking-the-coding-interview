from singly import LinkedList

def nth_to_last(l, n):
    """Find nth to last element of the singly linked list, l."""

    current = l.head
    runner = current
    for i in range(n):
        if runner.next:
            runner = runner.next
        else:
            raise ValueError("%s is larger than the list!" % n)
    while runner.next:
        current = current.next
        runner = runner.next
    return current.cargo

if __name__ == '__main__':
    l = LinkedList()
    for i in range(10):
        l.append(i)
    for i in range(10):
        print nth_to_last(l, i)
