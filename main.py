class Heap:
    def __init__(self):
        self.heap=[]

    def push(self,v):
        self.heap.append(v)
        self.check()
    
    def check(self):
        i=len(self.heap)-1
        while i:
            if self.heap[i]<self.heap[(i-1)//2]:
                self.heap[i],self.heap[(i-1)//2]=self.heap[(i-1)//2],self.heap[i]
            i-=1


H=Heap()

H.push(46)
H.push(15)
H.push(3)
H.push(4)
H.push(21)
H.push(79)

H.push(61)

print(H.heap)