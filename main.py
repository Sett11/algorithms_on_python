from random import shuffle

def bubble_sort(arr):
    a=arr.copy()
    l=len(a)
    shuffle(a)
    for i in range(1,l):
        for j in range(l-i):
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
    return a


print(bubble_sort(list(range(101))))