from LinkedList import Node

Head_Node = Node('Hello')

Second_Node = Node('World')
Head_Node.Next = Second_Node

Third_Node = Node('Hady')
Second_Node.Next = Third_Node

print(Head_Node.Value)
print(Head_Node.Next.Value)
print(Head_Node.Next.Next.Value)
