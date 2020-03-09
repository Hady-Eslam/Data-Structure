class Node:
    def __init__(self, Value):
        self.Value = Value
        self.Next = None


class Deque:

    def __init__(self):
        self.__Head = None

    def Pop_Front(self):
        if self.__Head is None:
            return None
        
        cur = self.__Head
        pre = None

        while cur.Next is not None:
            pre = cur
            cur = cur.Next
        
        if pre is None:
            self.__Head = None
            return cur.Value
        else:
            pre.Next = None
            return cur.Value

    def Pop_Back(self):
        if self.__Head:
            temp = self.__Head
            self.__Head = temp.Next
            return temp.Value
        return None

    def Push_Front(self, Value):
        if self.__Head is None:
            self.__Head = Node(Value)
        else:
            cur = self.__Head
            while cur:
                if cur.Next is None:
                    cur.Next = Node(Value)
                    break
                cur = cur.Next
            cur.Next = Node(Value)

    def Push_Back(self, value):
        temp = Node(value)
        temp.Next = self.__Head
        self.__Head = temp

    def Front(self):
        cur = self.__Head
        value = None

        while cur:
            value = cur.Value
            cur = cur.Next
        return value
    
    def Back(self):
        return self.__Head.Value if self.__Head else None
