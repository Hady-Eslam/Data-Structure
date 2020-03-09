from Deque import Deque

The_Deque = Deque()

# ['Hello']
The_Deque.Push_Back('Hello')
# ['World', 'Hello']
The_Deque.Push_Back('World')
# ['Hady', 'World', 'Hello']
The_Deque.Push_Back('Hady')


# ['Hady', 'World', 'Hello', 'Me']
The_Deque.Push_Front('Me')
# ['Hady', 'World', 'Hello', 'Me', 'is']
The_Deque.Push_Front('is')
# ['Hady', 'World', 'Hello', 'Me', 'is', 'This']
The_Deque.Push_Front('This')


print(The_Deque.Front())
print(The_Deque.Back())
print('___________')

print(The_Deque.Pop_Back())
print(The_Deque.Pop_Back())
print(The_Deque.Pop_Back())
print('___________')

print(The_Deque.Front())
print(The_Deque.Back())
print('___________')

print(The_Deque.Pop_Front())
print(The_Deque.Pop_Front())
print(The_Deque.Pop_Front())
