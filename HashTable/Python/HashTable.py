class HashTable:

    def __init__(self, HashFunction):
        self.__HashFunction = HashFunction
        self.__Hash = {}
    
    def Insert(self, Item):
        index = self.__HashFunction(Item)
        self.__Hash[index] = Item
    
    def Delete(self, Item):
        index = self.__HashFunction(Item)
        self.__Hash[index] = None
    
    def Search(self, Item):
        index = self.__HashFunction(Item)
        try:
            return self.__Hash[index]
        except:
            return None
