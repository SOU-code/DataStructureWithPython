def selectionSort(arr):
    n=len(arr)
    for i in range(n):
        minimum=i
        for j in range(i,n):
            if arr[minimum]>arr[j]:
                minimum=j
        arr[i],arr[minimum]=arr[minimum],arr[i]
arr=[7,4,6,99,12,17,26]
print("Before selection sort:")
print(arr)
selectionSort(arr)
print("After selection sort:")
print(arr)