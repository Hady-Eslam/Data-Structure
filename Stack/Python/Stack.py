class Node:
    def __init__(self, Value):
        self.Value = Value
        self.Next = None


class Stack:

    def __init__(self):
        self.__Head = None

    def Push(self, value):
        temp = Node(value)
        temp.Next = self.__Head
        self.__Head = temp

    def Pop(self):
        if self.__Head is None:
            return None
        temp = self.__Head
        self.__Head = temp.Next
        return temp.Value

    def Top(self):
        return self.__Head.Value if self.__Head else None
