from singly import LinkedList

def remove_duplicates(l):
    """Remove duplicates from a linked list.

    -- l: a singly linked list"""

    node = l.head
    if node:
        elements = {node.cargo}
    else:
        return
    while node.next:
        print "==============="
        print "Current element: ", node.cargo
        print "Next element: ", node.next.cargo
        if node.next.cargo in elements:
            print "It's a dupe!"
            node.next = node.next.next
        else:
            elements.add(node.next.cargo)
        node = node.next
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