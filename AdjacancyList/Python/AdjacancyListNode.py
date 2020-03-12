class ToNode:
    def __init__(self, To, Cost):
        self.To = To
        self.Cost = Cost
        self.Next = None

class FromNode:
    def __init__(self, From):
        self.From = From
        self.ToList = None
    
    def Add_To_Node(self, To, Cost):
        Temp = ToNode(To, Cost)
        Temp.Next = self.ToList
        self.ToList = Temp
    
    def Search(self, To):
        cur = self.ToList
        while cur:
            if cur.To == To:
                return cur.Cost
            cur = cur.Next
        return None
