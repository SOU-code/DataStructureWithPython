def kSort(arr,low,high):
    if low>=high:
        return
    pivot=arr[low]
    i,j=low,high
    while i<=j:
        if(arr[i]>pivot and arr[j]<pivot):
            arr[i],arr[j]=arr[j],arr[i]
        if(arr[i]<=pivot):
            i+=1
        if(arr[j]>=pivot):
            j-=1
    partion=j
    arr[j],arr[low]=arr[low],arr[j]
    kSort(arr,low,partion-1)
    kSort(arr,partion+1,high)
arr=[7,4,6,99,12,17,26]
low=0
high=len(arr)-1
print("Before  sort:")
print(arr)
kSort(arr,low,high)
print("After  sort:")
print(arr)