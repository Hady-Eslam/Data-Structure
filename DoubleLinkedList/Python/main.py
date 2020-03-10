from DoubleLinkedList import Node

Head = Node('Hady')

Second_Node = Node('World')
Head.Next = Second_Node
Second_Node.Pre = Head

Third_Node = Node('Hello')
Second_Node.Next = Third_Node
Third_Node.Pre = Second_Node

print(Third_Node.Value)
print(Third_Node.Pre.Value)
print(Third_Node.Pre.Pre.Value)
