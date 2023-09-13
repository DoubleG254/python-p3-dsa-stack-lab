class Stack:
    def __init__(self,items=[], capacity=None):
        self.items = items
        self.capacity = capacity

    def push(self, item):
        if self.capacity is not None and len(self.items) >= self.capacity:
            return "Stack is full"
        self.items.append(item)

    def pop(self):
        if self.isEmpty():
            return None
        return self.items.pop()

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return len(self.items) == 0

    def full(self):
        if self.capacity is None :
            return False
        else:
            return len(self.items) == self.capacity

    def search(self, target):
        for i, item in enumerate(self.items[::-1]):
            if item == target:
                return i
        return -1
