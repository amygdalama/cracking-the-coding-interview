class Node(object):
    def __init__(self, cargo=None, previous=None, next=None):
        self.cargo = cargo
        self.next = next

    def __str__(self):
        return str(self.cargo)

class LinkedList(object):
    def __init__(self):
        self.n = 0
        self.last = Node()
        self.first = self.last

    def append(self, cargo):
        self.last.next = Node()
        self.last.next.cargo = cargo
        self.last = self.last.next
        if self.n == 0:
            self.first = self.last
        self.n += 1

    def size(self):
        return self.n

    def elements(self):
        node = self.first
        while node:
            yield node.cargo
            node = node.next

    
if __name__ == '__main__':
    l = LinkedList()
    print l.size()
    l.append("thing")
    print l.size()
    l.append("cat")
    print l.size()
    l.append("bird")
    print l.size()
    for cargo in l.elements():
        print cargo