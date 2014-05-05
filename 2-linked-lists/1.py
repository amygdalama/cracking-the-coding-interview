from singly import LinkedList

def remove_duplicates(l):
    """Remove duplicates from a linked list.

    -- l: a singly linked list"""

    n = l.head
    previous = None
    elements = set()
    while n:
        if n.cargo in elements:
            previous.next = n.next
        else:
            elements.add(n.cargo)
            previous = n
        n = n.next
    return l

def remove_duplicates_without_buffer(l):
    """Remove duplicates from a linked list.

    -- l: a singly linked list"""
    current = l.head
    if current == None:
        return
    while current:
        runner = current
        while runner.next:
            if runner.next.cargo == current.cargo:
                runner.next = runner.next.next
            else:
                runner = runner.next
        current = current.next
    return l


if __name__ == '__main__':
    l = LinkedList()
    for i in range(10):
        l.append(i)
    for i in range(10):
        l.append(i)
    l = remove_duplicates_without_buffer(l)
    for e in l.elements():
        print e