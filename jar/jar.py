class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        if self.capacity < 0:
            raise ValueError

    def __str__(self):
        return "🍪"*self.size

    def deposit(self, n):
        self.size += n

    def withdraw(self, n):
        self.size -= n

    @property
    def capacity(self):
        return self.capacity

    @property
    def size(self):
        return self.size