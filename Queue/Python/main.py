from Queue import Queue

The_Queue = Queue()

The_Queue.Enqueue('Hello')
The_Queue.Enqueue('World')
The_Queue.Enqueue('Hady')

print(The_Queue.Top())

print(The_Queue.Dequeue())
print(The_Queue.Dequeue())
print(The_Queue.Dequeue())

print(The_Queue.Dequeue())
