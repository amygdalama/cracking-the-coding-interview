from singly import LinkedList

def delete_node(node):
    if node and node.next:
        node.cargo = node.next.cargo
        node.next = node.next.next
    else:
        raise IndexError("Node out of range!")

if __name__ == '__main__':
    l = LinkedList()
    for i in range(10):
        l.append(i)
    delete_node(l.head.next.next.next.next.next.next.next.next)
    for e in l.elements():
        print e