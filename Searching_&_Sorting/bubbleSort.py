def bubbleSort(arr):
    n=len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j]>arr[j+1]:
               arr[j],arr[j+1]=arr[j+1],arr[j]
arr=[7,4,6,99,12,17,26]
print("Before Bubble sort:")
print(arr)
bubbleSort(arr)
print("After Bubble sort:")
print(arr)