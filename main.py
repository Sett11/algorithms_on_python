from random import shuffle,choice

def hoar_sort(a):
    if len(a)<2:
        return a
    t=choice(a)
    l=[]
    m=[]
    r=[]
    [l.append(i) if i<t else r.append(i) if i>t else m.append(i) for i in a]
    return hoar_sort(l)+m+hoar_sort(r)


arr=list(range(101))
shuffle(arr)
print(hoar_sort(arr))