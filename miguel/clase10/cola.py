class Cola(object):
    def __init__(self):
        self.cola = []

    def enqueue(self, x):
        self.cola.append(x)

    def dequeue(self, x):
        return self.cola.pop(0)

    def front(self):
        return self.cola[0]

    def is_empty(self):
        return not bool(self.cola)

    def size(self):
        return len(self.cola)
