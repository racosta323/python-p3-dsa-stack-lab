import ipdb

class Stack:

    def __init__(self, items = [], limit = 100):
        self.items = items
        self.limit = limit

    def isEmpty(self):
        if self.items: 
            return False
        else:
            return True
        

    def push(self, item):
        return self.items.append(item) if not self.full() else False

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()

    def peek(self):
        i = len(self.items)-1
        return self.items[i]
    
    def size(self):
        return len(self.items)

    def full(self):
        if self.size() >= self.limit:
            return True
        else:
            False

    def search(self, target):
        if target in self.items:
            return self.peek() - target
        else:
            return -1

# stk = Stack([5,6,7,8,9,10])
# ipdb.set_trace()