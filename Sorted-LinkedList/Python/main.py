from SortedLinkedList import SortedLinkedList

List = SortedLinkedList()

List.Add(10)
List.Add(60)
List.Add(30)
List.Add(50)
List.Add(40)
List.Add(20)

List.Print()

List.Remove(60)

print(List.Search(60))

List.Print()
