from Heap import Heap

heap = Heap()

# heap.BuildHeap([9,5,6,2,3])
heap.Insert(9)
heap.Insert(5)
heap.Insert(6)
heap.Insert(2)
heap.Insert(3)

heap.Print()

print(heap.DeleteMin())
heap.Print()

print(heap.DeleteMin())
heap.Print()

print(heap.DeleteMin())
heap.Print()
