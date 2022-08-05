
import random

class BinHeap:

    heapSize = 0
    A = []

    def insertIntoList(self,num):
        self.A.append(num)

    def printArray(self):
        print (self.A)

    def minHeapify(self,i):
        left = 2 * i + 1
        right = 2 * i + 2
        if(left <= self.heapSize and self.A[left]<self.A[i]):
            smallest = left
        else:
            smallest = i
        if(right <= self.heapSize and self.A[right]<self.A[smallest]):
            smallest = right
        if (smallest != i):
            temp = self.A[i]
            self.A[i] = self.A[smallest]
            self.A[smallest] = temp
            self.minHeapify(smallest)
    
    def deleteElement(self):
        print(self.A.pop(0))
        self.buildHeap()
   
    def buildHeap(self):
        self.heapSize = len(self.A)-1
        for i in range (int(len(self.A)/2-1),-1,-1):
           self.minHeapify(i)
        
    def heapSort(self):
        self.buildHeap()
        for i in range(len(self.A)-1,-1,-1):
            temp = self.A[0]
            self.A[0] = self.A[i]
            self.A[i] = temp
            self.heapSize = self.heapSize - 1
            self.minHeapify(0)

heapify = BinHeap()

print("inserting first 5 elements")
heapify.insertIntoList(2)
heapify.insertIntoList(1)
heapify.insertIntoList(4)
heapify.insertIntoList(3)
heapify.insertIntoList(5)
heapify.printArray()

print("inserting last 5 elements and rebuilding the heap")
for i in range(5,10):
    heapify.insertIntoList(random.randint(0,20))
heapify.buildHeap()
heapify.printArray()

print("deleting min element from minHeap")
heapify.deleteElement()

print("rebuilding the min Heap")
heapify.printArray()

print("sorting the final list")
heapify.heapSort()
heapify.printArray()
print("MAXheap sorts in ascending order while min heap in descending order")

