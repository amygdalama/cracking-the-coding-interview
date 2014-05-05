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

if __name__ == '__main__':
    l = LinkedList()
    for i in range(10):
        l.append(i)
    for i in range(10):
        l.append(i)
    l = remove_duplicates(l)
    for e in l.elements():
        print e