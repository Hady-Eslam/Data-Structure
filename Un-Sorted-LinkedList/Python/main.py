from UnSortedLinkedList import UnSortedLinkedList

List = UnSortedLinkedList()

List.Add(10)
List.Add(10)
List.Add(20)
List.Add(30)
List.Add(40)
List.Add(50)
List.Add(60)

print(List.Search(40))
print(List.Search(100))

List.Remove(10)
print(List.Search(10))

List.Remove(10)
print(List.Search(10))
