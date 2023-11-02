class Linked_list:
    def __init__(self,head=None):
        self.head=head
    
    def repr(self):
        h=self.head
        r=[]
        while h is not None:
            r.append(h.val)
            h=h.next
        return ' -> '.join(map(str,r[:-1]))

class Node:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next

a=list(range(1,101))

L=Linked_list()
n=Node()
c=n

for i in a:
    c.val=i
    c.next=Node()
    c=c.next

L.head=n

print(L.repr())