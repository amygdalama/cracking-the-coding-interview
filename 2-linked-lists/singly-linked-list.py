class Node(object):
    def __init__(self, cargo=None, next=None):
        self.cargo = cargo
        self.next = next

    def __str__(self):
        return str(self.cargo)

class LinkedList(object):
    def __init__(self):
        self.head = None

    def append(self, cargo):
        n = self.head
        end = Node(cargo)
        if n == None:
            self.head = end
        else:
            while n.next:
                n = n.next
            n.next = end

    def add(self, cargo):
        n = Node(cargo)
        n.next = self.head
        self.head = n

    def delete(self, cargo):
        n = self.head
        if n.cargo == cargo:
            self.head = self.head.next
            return
        while n.next:
            if n.next.cargo == cargo:
                n.next = n.next.next
                return
            n = n.next

    def size(self):
        count = 0
        n = self.head
        while n:
            count += 1
            n = n.next
        return count

    def search(self, target):
        n = self.head
        while n:
            if n.cargo == target:
                return True
            n = n.next
        return False

    def insert(self, cargo, index=0):
        pass

    def index(self, cargo):
        pass

    def pop(self, index=0):
        pass

    def elements(self):
        node = self.head
        while node:
            yield node.cargo
            node = node.next

    
if __name__ == '__main__':
    l = LinkedList()
    assert l.search("thing") == False
    assert l.size() == 0
    l.append("thing")
    l.append("cat")
    l.append("bird")
    l.add("first")
    assert l.size() == 4
    l.delete("cat")
    assert l.size() == 3
    assert l.search("cat") == False
    assert l.search("bird") == True

    for element in l.elements():
        print element