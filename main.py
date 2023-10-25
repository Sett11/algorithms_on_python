from random import shuffle

def choise_sort(arr):
    a=arr.copy()
    l=len(a)
    shuffle(a)
    for i in range(l):
        for j in range(i+1,l):
            if a[j]<a[i]:
                a[i],a[j]=a[j],a[i]
    return a


print(choise_sort(list(range(101))))