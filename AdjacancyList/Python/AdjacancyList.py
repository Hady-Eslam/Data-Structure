from AdjacancyListNode import FromNode

class AdjacancyList:

    def __init__(self):
        self.__FromList = None
    
    def Add_Edge(self, From, To, Cost):
        cur = self.__FromList

        while cur:
            if cur.From == From: # Found From Node
                cur.Add_To_Node(To, Cost)
                return
            cur = cur.Next
        
        # Not Found
        Temp = FromNode(From)
        Temp.Add_To_Node(To, Cost)
        Temp.Next = self.__FromList
        self.__FromList = Temp
    
    def Search(self, From, To):
        cur = self.__FromList
        
        while cur:
            if cur.From == From:
                return cur.Search(To)
            cur = cur.Next
        
        return None
