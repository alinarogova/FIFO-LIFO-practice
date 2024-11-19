class Stack:
    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)

    def is_empty(self):
        return len(self.items) == 0

    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from empty stack.")
        val = self.items[-1]
        del self.items[-1]
        return val

    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from empty stack.")
        return self.items[-1]

stack1 = Stack()
stack1.push(1)
stack1.push(2)
stack1.push(3)
stack1.push(4)
stack1.push(8)
print(stack1.pop())

print(stack1.pop())
print(stack1.peek())

print("Task 2".center(40, '='))
class Queue:
    def __init__(self, max_size):
        self.items = []
        self.max_size = max_size

    def is_full(self):
        return self.max_size <= len(self.items)+1
    def push(self, value):
        if self.is_full():
            raise IndexError("the queue is full")
        self.items.append(value)

    def is_empty(self):
        return len(self.items) == 0

    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from empty stack.")
        val = self.items[0]
        del self.items[0]
        return val

    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from empty stack.")
        return self.items[0]

queue = Queue(15)
queue.push(1)
queue.push(2)
queue.push(3)

print(queue.pop())
print(queue.peek())
print(queue.pop())
print(queue.pop())
try:
    print(queue.pop())
except IndexError as e:
    print(e)

print("Task 3".center(40, "="))
class PriorityQueue:
    def __init__(self, max_size):
        self.items = []

        self.max_size = max_size

    def is_full(self):
        return self.max_size <= len(self.items)+1

    def push(self, value, prioritynum):
        if self.is_full():
            raise IndexError("the queue is full")
        self.items.append((value, prioritynum))
        self.items.sort(key = lambda x: x[1])

    def is_empty(self):
        return len(self.items) == 0

    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from empty stack.")
        val = self.items[0]
        del self.items[0]
        return val

    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from empty stack.")
        return self.items[0]

priorityqueue = PriorityQueue(10)
priorityqueue.push("Feed the cat", 1)
priorityqueue.push("Grow the flower", 10)
priorityqueue.push("Make breakfast", 0)
priorityqueue.push("Clean the room", 2)

print(priorityqueue.pop())
print(priorityqueue.pop())
print(priorityqueue.pop())
print(priorityqueue.pop())