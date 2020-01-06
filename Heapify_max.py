
import Tools


class Heap:

    def __init__(self, a):
        self.a = a
        self.heap_size = len(a)

    def heapify_max(self, i):
        left = 2*i + 1
        right = 2*i + 2
        if (left < self.heap_size) and (self.a[left] > self.a[i]):
            largest = left
        else:
            largest = i
        if (right < self.heap_size) and (self.a[right] > self.a[largest]):
            largest = right
        if largest != i:
            temp = self.a[i]
            self.a[i] = self.a[largest]
            self.a[largest] = temp
            self.heapify_max(largest)

    def build_max_heap(self):
        self.heap_size = len(self.a)
        for i in range(int((len(self.a))/2), -1, -1):
            self.heapify_max(i)

    def heap_sort(self):
        self.build_max_heap()
        for i in range(len(self.a)-1, 0, -1):
            temp = self.a[0]
            self.a[0] = self.a[i]
            self.a[i] = temp
            self.heap_size -= 1
            self.heapify_max(0)


a = []
Tools.fill_random_array(a)
print(a)
heap = Heap(a)
heap.heap_sort()
print(a)







