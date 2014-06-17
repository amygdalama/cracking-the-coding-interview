class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return str(self.data)


class LinkedList(object):
    def __init__(self):
        self.head = None

    def __repr__(self):
        l = []
        n = self.head
        while n:
            l.append(n.data)
            n = n.next
        return str(l)

    def append(self, data):
        end = Node(data)
        n = self.head
        if n:
            while n.next:
                n = n.next
            n.next = end
        else:
            self.head = end

    def delete(self, data):
        current = self.head
        previous = None
        while current:
            if current.data == data:
                if previous:
                    previous.next = current.next
                else:
                    self.head = current.next
                break
            previous = current
            current = current.next

    def reverse(self):
        previous = None
        current = self.head
        while current:
            next = current.next
            current.next = previous
            previous = current
            current = next
        self.head = previous

if __name__ == '__main__':
    l = range(8)
    linked = LinkedList()
    for elem in l:
        linked.append(elem)
    n = linked.head
    for elem in l:
        assert elem == n.data
        n = n.next
    linked.delete(4)
    l.remove(4)
    assert repr(linked) == repr(l)
    linked.delete(0)
    l.remove(0)
    assert repr(linked) == repr(l)
    linked.delete(7)
    l.remove(7)
    assert repr(linked) == repr(l)
    linked.append(14)
    l.append(14)
    assert repr(linked) == repr(l)
    print linked
    linked.reverse()
    print linked