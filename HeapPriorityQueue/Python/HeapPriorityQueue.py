from PriorityQueueNode import Node

class PriorityQueue:

    def __init__(self):
        self.__List = []
        self.__Size = 0
    
    def Insert_With_Priority(self, Priority, Value):
        self.__List.append(Node(Priority, Value))
        self.__Size += 1
        self.__PercUp()
    
    def __PercUp(self):
        i = self.__Size
        while i // 2 > 0:
            if self.__List[i - 1].Priority < self.__List[i//2 - 1].Priority:
                Temp = self.__List[i - 1]
                self.__List[i - 1] = self.__List[i//2 - 1]
                self.__List[i//2 - 1] = Temp
            i = i//2
    
    def Pull_Lowest_Priority(self):
        Item = self.__List[0]
        self.__List[0] = self.__List[self.__Size -1]
        self.__List.pop()
        self.__Size -= 1
        self.__PercDown()
        return Item.Value
    
    def __PercDown(self):
        i = 0
        while i * 2 < self.__Size:
            index_MiniChild = self.__MiniChild(i)
            if self.__List[i].Priority > self.__List[index_MiniChild].Priority:
                Temp = self.__List[i]
                self.__List[i] = self.__List[index_MiniChild]
                self.__List[index_MiniChild] = Temp
            if i == index_MiniChild:
                break
            i = index_MiniChild
    
    def __MiniChild(self, i):
        if i * 2 + 1 >= self.__Size:
            return i * 2
        else:
            if self.__List[i * 2].Priority < self.__List[i * 2 + 1].Priority:
                return i * 2
            else:
                return i * 2 + 1
