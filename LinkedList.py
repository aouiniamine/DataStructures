
class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self, val) -> None:
        self.head = Node(val)

    def add(self, val):
        temp = self.head
        while temp.next != None:
            temp = temp.next
        temp.next = Node(val)
        return val
        
    def find(self, val):
        temp = self.head
        while temp.next != None and val != temp.val:
            temp = temp.next
        if temp.val == val:
            return val
        return 0
        
    def rm(self, val):
        temp = self.head
        prev = None
        while temp.next != None and val != temp.val:
            prev = temp
            temp = temp.next
        if temp.val == val:
            if temp.next != None:
                temp.val = temp.next.val
                temp.next = temp.next.next
            else:
                prev.next = None

            return val
        return 0


myLinked = LinkedList(5)

print(myLinked.head.val, myLinked.add(6), myLinked.add(7), myLinked.add(8))
print(myLinked.head.next.val, myLinked.head.next.next.val)

print(myLinked.find(10), myLinked.find(6))
print(myLinked.rm(6), myLinked.head.next.val)
print(myLinked.rm(8), myLinked.head.next.val)
myLinked.add(99)
print(myLinked.rm(7), myLinked.head.next.val)
