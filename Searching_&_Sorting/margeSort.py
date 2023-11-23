def marge(arr1,arr2):
    m=len(arr1)
    n=len(arr2)
    i,j=0,0
    arr3=[]
    while i<m and j<n:
        if(arr1[i]<arr2[j]):
            arr3.append(arr1[i])
            i+=1
        else:
            arr3.append(arr2[j])
            j+=1
    while i<m:
        arr3.append(arr1[i])
        i+=1
    while j<n:
        arr3.append(arr2[j])
        j+=1
    return arr3

def margeSort(arr):
    n=len(arr)
    if n==1:
        return arr
    arr1=margeSort(arr[:n//2])
    arr2=margeSort(arr[n//2:])
    return marge(arr1,arr2)
arr=[7,4,6,99,12,17,26]
print(margeSort(arr))