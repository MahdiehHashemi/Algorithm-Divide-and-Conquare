def merge(a,b):
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
l1=[1,8,12,90]
l2=[4,5,10,24,32]
print(merge(l1,l2))