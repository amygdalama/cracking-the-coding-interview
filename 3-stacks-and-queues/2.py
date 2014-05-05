from structures import Stack

class MinStack(Stack):
    def __init__(self):
        super(MinStack, self).__init__()
        self.min = None

    def push(self, item):
        if self.min == None or item < self.min:
            self.min = item
        super(MinStack, self).push(item)

if __name__ == '__main__':
    m = MinStack()
    for i in range(10):
        m.push(i)
        m.push(-i)
        print m.min
