from BinarySearchTreeNode import Node

class BTS: # Binary Search Tree

    def __init__(self):
        self.__Head = None

    def Insert(self, Value):
        if self.__Head is None:
            self.__Head = Node(Value)
        else:
            self.__insert(Value, self.__Head)

    def __insert(self, Value, root):
        if Value < root.Value:
            if root.Left is None:
                root.Left = Node(Value)
            else:
                self.__insert(Value, root.Left)
        else:
            if root.Right is None:
                root.Right = Node(Value)
            else:
                self.__insert(Value, root.Right)

    def Delete(self, Value):
        if self.__Head:
            self.__Delete(self.__Head, Value)
    
    def __Delete(self, Root, Value):
        if Root is None:
            return None
        
        elif Root.Value > Value:
            Root.Left = self.__Delete(Root.Left, Value)
        
        elif Root.Value < Value:
            Root.Right = self.__Delete(Root.Right, Value)
        
        else:
            if Root.Right is None:
                return Root.Left
            elif Root.Left is None:
                return Root.Right
            else:
                Temp = Root.Right
                Mini_Value = Temp.Value
                while Temp.Left:
                    Temp = Temp.Left
                    Mini_Value = Temp.Value
                Root.Value = Mini_Value
                Root.Right = self.__Delete(Root.Right, Root.Value)
        return Root

    def Preorder(self):
        if self.__Head:
            self.__Preorder(self.__Head)
    
    def __Preorder(self, Root):
        print(Root.Value)
        self.__Preorder(Root.Left)
        self.__Preorder(Root.Right)

    def Inorder(self):
        if self.__Head:
            self.__Inorder(self.__Head)
    
    def __Inorder(self, Root):
        if Root:
            self.__Inorder(Root.Left) 
            print(Root.Value) 
            self.__Inorder(Root.Right)

    def Postorder(self):
        if self.__Head:
            self.__Postorder(self.__Head)
    
    def __Postorder(self, Root):
        self.__Preorder(Root.Left)
        self.__Preorder(Root.Right)
        print(Root.Value)

    def Search(self, Value):
        root = self.__Head
        while root:
            if Value < root.Value:
                root = root.Left
            elif Value > root.Value:
                root = root.Right
            else:
                return Value
