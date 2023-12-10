class BinaryTree:
    def __init__(self,data):
        self.data = data
        self.lchild = None
        self.rchild = None

    def insertion(self,key):
        if self.data == None:
            self.data = key
            return  
        if self.data > key:
            if self.lchild:
                self.lchild.insertion(key)
            else:
                self.lchild = BinaryTree(key)
        else:
            if self.rchild:
                self.rchild.insertion(key)
            else:
                self.rchild = BinaryTree(key)
    
    def search(self,key):
        if self.data == key:
            print("node found")
            return
        if self.data > key:
            if self.lchild:
                self.lchild.search(key)
            else:
                print("node not found")
        else:
            if self.rchild:
                self.rchild.search(key)
            else:
                print("node not found")
            
    def preorder(self):
        print(self.data)
        if self.lchild:
            self.lchild.preorder()
        if self.rchild:
            self.rchild.preorder()

    def inorder(self):
        if self.lchild:
            self.lchild.inorder()
        print(self.data)
        if self.rchild:
            self.rchild.inorder()
    def postorder(self):
        if self.lchild:
            self.lchild.postorder()
        if self.rchild:
            self.rchild.postorder()
        print(self.data)


node = BinaryTree(None)
list = [60,20,30,40,50,70,80]
for i in list:
    node.insertion(i)
print("preorder")
node.preorder()
print("inorder")
node.inorder()
print("postorder")
node.postorder()
node.search(60)
node.search(100)
print(node.data)
print(node.lchild.data)
print(node.rchild.data)
print(node.lchild.lchild.data)
print(node.lchild.rchild.data)



