class Queue:
    def __init__(self, val) -> None:
        self.content = [val]

    def enqueue(self, val):
        self.content.append(val)
    def dequeue(self):
        temp = self.content[0]
        self.content.pop(0)
        return temp
    def peek(self):
        return self.content[0]
    def isEmpty(self):
        return len(self.content) == 0
    def length(self):
        return len(self.content)    

myQueue = Queue(5)

myQueue.enqueue(6)
myQueue.enqueue(7)

print(myQueue.length(), myQueue.dequeue(), myQueue.dequeue())
print(myQueue.dequeue(), myQueue.isEmpty())