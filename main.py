class Heap:
    def __init__(self):
        self.heap_list=[]
        self.current_size=0

    def perc_up(self,i):
        while i//2>0:
            if self.heap_list[i]<self.heap_list[i//2]:
                self.heap_list[i],self.heap_list[i//2]=self.heap_list[i//2],self.heap_list[i]
            i//=2

    def add(self,k):
        self.heap_list.append(k)
        self.current_size+=1
        self.perc_up(self.current_size)

    def perc_down(self,i):
        while i*2<=self.current_size:
            m=self.min_child(i)
            if self.heap_list[i]>self.heap_list[m]:
                self.heap_list[i],self.heap_list[m]=self.heap_list[m],self.heap_list[i]
            i=m

    def min_child(self,i):
        if i*2+1>self.current_size or self.heap_list[i*2]>self.heap_list[i*2+1]:
            return i*2
        return i*2+1
    
    def del_min(self):
        rv=self.heap_list[1]
        self.heap_list[1]=self.heap_list[self.current_size]
        self.current_size-=1
        self.heap_list.pop()
        self.perc_down(1)
        return rv
    
    def build_heap(self,a):
        n=len(a)
        i=n//2
        self.current_size=n
        self.heap_list=[0]+a[:]
        while i>0:
            self.perc_down(i)
            i-=1


H=Heap()

H.build_heap([1,5,2,3,9,17,4])

H.add(22)
H.add(6)
H.add(7)

H.del_min()

print(H.heap_list)