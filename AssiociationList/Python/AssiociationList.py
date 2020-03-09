class Node:

    def __init__(self, Key, Value):
        self.Key = Key
        self.Value = Value
        self.Next = None


class AssiociationList:

    def __init__(self):
        self.__Head = None

    def Insert(self, Key, Value):
        temp = Node(Key, Value)
        temp.Next = self.__Head
        self.__Head = temp

    def Delete(self, Key):
        if self.__Head is None:
            return
        else:
            cur = self.__Head
            pre = None

            while cur.Next is not None:
                if cur.Key == Key:
                    break
                pre = cur
                cur = cur.Next

            if pre is None:
                if cur.Key == Key:
                    self.__Head = None
                    return cur.Value
                else:
                    return None
            else:
                pre.Next = cur.Next
                return cur.Value

    def Get(self, Key):
        cur = self.__Head
        value = None

        while cur:
            if cur.Key == Key:
                value = cur.Value
                break
            cur = cur.Next
        return value
