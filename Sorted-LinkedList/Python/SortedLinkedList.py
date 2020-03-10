from SortedLinkedListNode import Node

class SortedLinkedList:

    def __init__(self):
        self.__Head = None
    
    def Search(self, Item):
        cur = self.__Head

        while cur:
            if cur.Value == Item:
                return True
            cur = cur.Next
        
        return False
    
    def Add(self, Item):
        cur = self.__Head
        pre = None
        Stop = False

        while cur:
            if cur.Value > Item:
                Stop = True
                break
            pre = cur
            cur = cur.Next
        
        if Stop:
            if pre is None:
                Temp = Node(Item)
                self.__Head = Temp
                Temp.Next = cur
            else:
                Temp = Node(Item)
                pre.Next = Temp
                Temp.Next = cur
        else:
            if pre is None:
                self.__Head = Node(Item)
            else:
                pre.Next = Node(Item)
    
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
    
    def Print(self):
        cur = self.__Head
        while cur:
            print(cur.Value)
            cur = cur.Next
