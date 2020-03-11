from HashTable import HashTable
from HashFunctions import SimpleHash

Hash = HashTable(SimpleHash)

Hash.Insert('Hello')
Hash.Insert('World')
Hash.Insert('Hady')

print(Hash.Search('Hello'))

Hash.Delete('World')

print(Hash.Search('World'))
