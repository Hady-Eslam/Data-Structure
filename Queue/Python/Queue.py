class Node:
    def __init__(self, Value):
        self.Value = Value
        self.Next = None


class Queue:

    def __init__(self):
        self.__Head = None

    def Enqueue(self, Value):
        if self.__Head is None:
            self.__Head = Node(Value)
        else:
            cur = self.__Head
            while cur:
                if cur.Next is None:
                    break
                cur = cur.Next
            cur.Next = Node(Value)

    def Dequeue(self):
        if self.__Head is None:
            return None
        else:
            temp = self.__Head
            self.__Head = temp.Next
            return temp.Value
    
    def Top(self):
        return self.__Head.Value if self.__Head else None
