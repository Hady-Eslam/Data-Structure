from BinaryTree import BinaryTreeNode

Root = BinaryTreeNode(5)

LeftNode = BinaryTreeNode(3)
Root.Left = LeftNode

RightNode = BinaryTreeNode(7)
Root.Right = RightNode

print(Root.Value)
print(Root.Left.Value)
print(Root.Right.Value)
