class Linked_list:
    def __init__(self,head=None):
        self.head=head

    def repr(self):
        node=self.head
        nodes=[]
        while node is not None:
            nodes.append(node.value)
            node=node.next
        nodes.append('None')
        return ' -> '.join(map(str,nodes))


class Node:
    def __init__(self,value=0,next=None):
        self.value=value
        self.next=next
    
    def repr(self):
        return self.value

L=Linked_list()

a=Node('a')

L.head=a

b=Node('b')
c=Node('c')

a.next=b
b.next=c

print(a.repr())