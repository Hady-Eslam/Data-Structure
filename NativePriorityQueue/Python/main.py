from NativePriorityQueue import PriorityQueue

Queue = PriorityQueue()

# [6, 7, 9, 4, 3, 5]
Queue.Insert_With_Priority(3, 9)
Queue.Insert_With_Priority(2, 7)
Queue.Insert_With_Priority(6, 5)
Queue.Insert_With_Priority(1, 6)
Queue.Insert_With_Priority(4, 4)
Queue.Insert_With_Priority(5, 3)

print(Queue.Pull_Highest_Priority_Element())
print(Queue.Pull_Highest_Priority_Element())
print(Queue.Pull_Highest_Priority_Element())
print(Queue.Pull_Highest_Priority_Element())
print(Queue.Pull_Highest_Priority_Element())
print(Queue.Pull_Highest_Priority_Element())
