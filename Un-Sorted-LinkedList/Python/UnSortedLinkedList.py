from UnSortedLinkedListNode import Node

class UnSortedLinkedList:

    def __init__(self):
        self.__Head = None
    
    def Add(self, Value):
        Temp = Node(Value)
        Temp.Next = self.__Head
        self.__Head = Temp
    
    def Search(self, Value):
        cur = self.__Head

        while cur:
            if cur.Value == Value:
                return True
            cur = cur.Next
        return False
    
    def Remove(self, Value):
        cur = self.__Head
        pre = None
        Found = False

        while True:
            if cur.Value == Value:
                Found = True
                break
            pre = cur
            cur = cur.Next
        
        if Found:
            if pre is None:
                self.__Head = cur.Next
            else:
                pre.Next = cur.Next
