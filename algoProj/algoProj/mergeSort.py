


def mergeSort(A,head,tail):
    if(head<tail):
        mid = int((head+tail)/2)
        mergeSort(A,head,mid)
        mergeSort(A,mid+1,tail)
        merge(A,head,mid,tail)

def merge(A,head,mid,tail):
    lenX = mid - head
    lenY = tail - mid - 1
    x = []
    y = []
    for i in range(0,lenX+1):
        x.append(A[head + i])
    for j in range(0,lenY+1):
        y.append(A[mid+1+j])
    x.append(999)
    y.append(999)
    i = 0 
    j = 0
    for k in range(head,tail+1):
        if x[i]<=y[j]:
            A[k] = x[i]
            i = i+1
        else:
            A[k] = y[j]
            j = j+1

A = []
print('input numbers')
for i in range(0,5):
    a = int(input())
    A.append(a)
print(" ")
mergeSort(A,0,4)
print(A)


ss