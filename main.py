import gmpy2
import inspect
import networkx as nx
import matplotlib.pyplot as plt
import re
from math import ceil, inf
from collections import defaultdict, deque, Counter
from string import ascii_uppercase, digits
from gen_graph import matrix,dfs_a,dfs_b,seq,seq_b,generate_chess_knight_grafh,p_graph as g,d_graph as dg,f_grapf as fg, ff_g,exp,exp_dict,net_g
from functools import reduce
from itertools import product,zip_longest
from operator import mul,add,sub,truediv
from random import shuffle,choice#,randint
q=list(range(1,1503))
shuffle(q)

class TreeNode:
    def __init__(self,key=None,val=None,left=None,right=None,parent=None):
        self.key=key
        self.val=val
        self.left=left
        self.right=right
        self.parent=parent

    def has_left_child(self):
        return self.left
    
    def has_right_child(self):
        return self.right
    
    def is_left_child(self):
        return self.parent and self.parent.left==self
    
    def is_right_child(self):
        return self.parent and self.parent.right==self
    
    def is_root(self):
        return not self.parent
    
    def is_leaf(self):
        return not (self.left or self.right)
    
    def has_any_children(self):
        return (self.left or self.right)
    
    def has_both_children(self):
        return (self.left and self.right)
    
    def replace_node_data(self,k,v,lc,rc):
        self.key=k
        self.payload=v
        self.left=lc
        self.right=rc
        if self.is_left_child():
            self.left.parent=self
        if self.is_right_child():
            self.right.parent=self

class BinarySearchTree:
    def __init__(self):
        self.root=None
        self.size=0

    def length(self):
        return self.size
    
    def __len__(self):
        return self.length()
    
    def put(self,k,v):
        if self.root:
            self._put_(k,v,self.root)
        else:
            self.root=TreeNode(k,v)
        self.size+=1

    def _put_(self,k,v,cur):
        if k<cur.key:
            if cur.has_left_child():
                self._put_(k,v,cur.left)
            else:
                cur.left=TreeNode(k,v,parent=cur)
        else:
            if cur.has_right_child():
                self._put_(k,v,cur.right)
            else:
                cur.right=TreeNode(k,v,parent=cur)

    def __setitem__(self,k,v):
        self.put(k,v)

    def get(self,k):
        if self.root:
            r=self._get_(k,self.root)
            if r:
                return r.val

    def _get_(self,k,cur):
        if not cur:
            return
        elif cur.key==k:
            return cur
        elif k<cur.key:
            return self._get_(k,cur.left)
        else:
            return self._get_(k,cur.right)
        
    def __getitem__(self,k):
        return self.get(k)
    
    def __contains__(self,k):
        return bool(self._get_(k,self.root))

    def delete(self,k):
        if self.size>1:
            n=self._get_(k,self.root)
            if n:
                self.remove(n)
                self.size-=1
            else:
                raise KeyError('Error: key not in tree')
        elif self.size==1 and self.root.key==k:
            self.root=None
            self.size-=1
        else:
            raise KeyError('Error: key not in tree')

    def __delitem__(self,k):
        self.delete(k)

    def splice_out(self):
        if self.is_leaf():
            if self.is_left_child():
                self.parent.left=None
            else:
                self.parent.right=None
        elif self.has_any_children():
            if self.has_left_child():
                if self.is_left_child():
                    self.parent.left=self.left
                else:
                    self.parent.right=self.right
                self.left.parent=self.parent
            else:
                if self.is_left_child():
                    self.parent.left=self.right
                else:
                    self.parent.right=self.right
                self.right.parent=self.parent

    def find_successor(self):
        succ=None
        if self.has_right_child():
            succ=self.right.findmin()
        else:
            if self.parent:
                if self.is_left_child():
                    succ=self.parent
                else:
                    self.parent.right=None
                    succ=self.parent.find_successor()
                    self.parent.right=self
        return succ

    def find_min(self):
        curr=self
        while curr.has_left_child():
            curr=curr.left
        return curr

    def remove(self,cur):
        if cur.is_leaf():
            if cur==cur.parent.left:
                cur.parent.left=None
            else:
                cur.parent.right=None
        elif cur.has_both_children():
            succ=cur.find_successor()
            succ.splice_out()
            cur.k=succ.k
            cur.payload=succ.payload
        else:
            if cur.has_left_child():
                if cur.is_left_child():
                    cur.left.parent=cur.parent
                    cur.parent.left=cur.left
                elif cur.is_right_child():
                    cur.right.parent=cur.parent
                    cur.parent.right=cur.right
                else:
                    cur.replace_node_data(cur.left.key,cur.left.payload,cur.left.left,cur.left.right)
            else:
                if cur.is_left_child():
                    cur.right.parent=cur.parent
                    cur.parent.left=cur.right
                elif cur.is_right_child():
                    cur.right.parent=cur.parent
                    cur.parent.right=cur.right
                else:
                    cur.replace_node_data(cur.right.key,cur.right.payload,cur.right.left,cur.right.right)


m=BinarySearchTree()
m[3]="red"
m[4]="blue"
m[6]="yellow"
m[2]="at"

m[0]=1
print(m[6])
print(m[2])
del m[0]
print(m[0])

m[3]='pink'

print(m[3])