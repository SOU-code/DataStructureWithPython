def insertionSort(arr):
    n=len(arr)
    for i in range(1,n):
        key=arr[i]
        j=i-1
        while j>=0 and arr[j]>key:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key       
arr=[7,4,6,99,12,17,26]
print("Before insertion sort:")
print(arr)
insertionSort(arr)
print("After insertion sort:")
print(arr)

