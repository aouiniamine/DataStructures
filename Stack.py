class Node:
    def __init__(self, val) -> None:
        self.val = val 
        self.prev = None

class Stack:
    def __init__(self, val) -> None:
        self.content = Node(val)

    def push(self, val):
        temp = self.content
        head = Node(val)
        head.prev = temp
        self.content = head
    
    def pop(self):
        val = self.content.val
        if self.content.prev != None:
            self.content.val = self.content.prev.val
            self.content.prev = self.content.prev.prev
        else:
            self.content = None
        return val


myStack = Stack(5)
myStack.push(6)
myStack.push(7)
print(myStack.content.val, "->", myStack.content.prev.val, "->", myStack.content.prev.prev.val)
print("rm:", myStack.pop(),"curr -> ", myStack.content.val)


