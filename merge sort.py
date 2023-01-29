def merge_sort(arr):
    if len(arr)>1:
        mid=len(arr)//2
        left=arr[:mid]
        right=arr[mid:]
        merge_sort(left)
        merge_sort(right)
        return merge_two_sorted_lists(left, right)
def merge_two_sorted_lists(a,b):
    aux=[]
    i=0
    j=0
    while i<len(a) and j<len(b):
        if a[i]<b[j]:
            aux.append(a[i])
            i=i+1
        else:
            aux.append(b[j])
            j=j+1
    while i<len(a):
        aux.append(a[i]) 
        i=i+1
    while j<len(b):
        aux.append(b[j]) 
        j=j+1   
    return(aux)   
l=[1,8,12,90,4,5,10,24,32]
print(merge_sort(l))