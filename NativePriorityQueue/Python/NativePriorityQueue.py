from PriorityQueueNode import Node

class PriorityQueue:

    def __init__(self):
        self.__Head = None
    
    def is_Empty(self):
        return True if self.__Head else False
    
    def Insert_With_Priority(self, Priority, Value):
        if self.__Head is None:
            self.__Head = Node(Priority, Value)
        else:
            cur = self.__Head
            Found = False
            pre = None

            while cur:
                if cur.Priority < Priority:
                    Found = True
                    break
                pre = cur
                cur = cur.Next
            
            if not Found:
                pre.Next = Node(Priority, Value)
            else:
                if pre is None:
                    self.__Head = Node(Priority, Value)
                    self.__Head.Next = cur
                else:
                    Temp = Node(Priority, Value)
                    pre.Next = Temp
                    Temp.Next = cur
    
    def Pull_Highest_Priority_Element(self):
        Item = self.__Head
        self.__Head = Item.Next
        return Item.Value
