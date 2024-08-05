import gmpy2
import inspect
import re
from math import ceil, inf
from collections import defaultdict, deque, Counter
from string import ascii_uppercase, digits
from gen_graph import matrix,dfs_a,dfs_b,seq,seq_b,generate_chess_knight_grafh,p_graph as g,d_graph as dg,f_grapf as fg, ff_g,exp,exp_dict,LazyInit
from functools import reduce
from itertools import product
from operator import mul,add,sub,truediv
from random import shuffle,choice#,randint
q=list(range(1,1503))
shuffle(q)

class LazyInit:
    @classmethod
    def lazy_init(msc,init):
        def wrap(*args):
            p=inspect.getfullargspec(init).args
            self=args[0]
            for i in range(1,len(p)):
                setattr(self,p[i],args[i])
        return wrap
    
    def __new__(msc,name,bases,attrs):
        cls=type(name,bases,attrs)
        setattr(cls,'__init__',LazyInit.lazy_init(attrs['__init__']))
        return cls
    
class MyClass(metaclass=LazyInit):
    def __init__(self,name,age):
        pass

m=MyClass('John',23)

print(m.name)