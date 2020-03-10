from CircularLinkedList import Node


Head = Node('Hello')
Second_Node = Node('World')
Third_Node = Node('Hady')

Head.Next = Second_Node
Second_Node.Next = Third_Node
Third_Node.Next = Head

print(Head.Value)
print(Head.Next.Value)
print(Head.Next.Next.Value)
print(Head.Next.Next.Next.Value)
