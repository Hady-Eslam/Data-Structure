from HeapPriorityQueue import PriorityQueue

Queue = PriorityQueue()

# [9,5,6,2,3]
Queue.Insert_With_Priority(4, 2)
Queue.Insert_With_Priority(1, 9)
Queue.Insert_With_Priority(3, 6)
Queue.Insert_With_Priority(5, 3)
Queue.Insert_With_Priority(2, 5)

print(Queue.Pull_Lowest_Priority())
print(Queue.Pull_Lowest_Priority())
print(Queue.Pull_Lowest_Priority())
print(Queue.Pull_Lowest_Priority())
print(Queue.Pull_Lowest_Priority())
