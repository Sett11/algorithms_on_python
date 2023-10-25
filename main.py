from random import shuffle

def insert_sort(arr):
    a=arr.copy()
    shuffle(a)
    for i in range(1,len(a)):
        k=i
        while k>0 and a[k-1]>a[k]:
            a[k],a[k-1]=a[k-1],a[k]
            k-=1
    return a


print(insert_sort(list(range(101))))