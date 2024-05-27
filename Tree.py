class Node: 
    def __init__(self, val) -> None:
        self.val = val
        self.right = None
        self.left = None

class Tree:
    def __init__(self, val) -> None:
        self.root = Node(val)

    def add(self, val):
        temp = self.root
        while ((val > temp.val and temp.right != None) or (val < temp.val and temp.left != None)):
            if val > temp.val:
                temp = temp.right
            else:
                temp = temp.left

        if val > temp.val:
            temp.right = Node(val)
        else:
            temp.left = Node(val)
        return val
    
    def find(self, val):
        temp = self.root
        while (temp.val != val) and ((val > temp.val and temp.right != None) or (val < temp.val and temp.left != None)):
            if val > temp.val:
                temp = temp.right
            else:
                temp = temp.left
        if temp.val == val:
            return val
        return 0
    
    def rm(self, val):
        temp = self.root    
        prev = None
        while (temp.val != val) and ((val > temp.val and temp.right != None) or (val < temp.val and temp.left != None)):
            prev = temp
            if val > temp.val:
                temp = temp.right
            else:
                temp = temp.left
        print("rm", val, ":", temp.val, prev.val)
        if temp.val == val:
            if temp.right != None:
                temp.val = temp.right.val
                temp.right = temp.right.right

            elif temp.left != None:
                temp.val = temp.left.val
                temp.left = temp.left.left

            else: 
                if val > prev.val:
                    prev.right = None
                else:
                    prev.left = None
            return val
        return 0
        


myTree = Tree(10)

print(myTree.add(20), myTree.add(30), myTree.add(15), myTree.add(5), myTree.add(8), myTree.add(2))
print(myTree.root.right.val, myTree.root.right.right.val, myTree.root.left.right.val, myTree.root.left.left.val)
print(myTree.find(30), "is found!")
print(myTree.rm(5), myTree.rm(30))
print(myTree.root.left.val, myTree.root.right.val, myTree.root.right.val, myTree.root.left.left.val)
print(myTree.find(20), myTree.find(15), myTree.find(5), myTree.find(30))

