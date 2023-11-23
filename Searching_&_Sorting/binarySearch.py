def binarySearch(arr,findEle):
    n=len(arr)
    first,last=0,n-1
    while first<=last:
        mid=(first+last)//2
        if arr[mid]==findEle:
            return mid
        elif arr[mid]<findEle:
            first=mid+1
        else:
            last=mid-1
    return -1
arr=[4,7,9,11,14,17,19]
findEle=17
position=binarySearch(arr,findEle)
print(position)