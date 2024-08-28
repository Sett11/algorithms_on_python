import gmpy2
import inspect
import networkx as nx
import matplotlib.pyplot as plt
import re
from math import ceil,inf,factorial
from collections import defaultdict,deque,Counter
from string import ascii_uppercase,digits
from gen_graph import matrix,dfs_a,dfs_b,seq,seq_b,generate_chess_knight_grafh,p_graph as g,d_graph as dg,f_grapf as fg, ff_g,exp,exp_dict,net_g,options,back,sudoku,kad
from functools import reduce
from itertools import product,zip_longest,permutations
from copy import deepcopy
from operator import mul,add,sub,truediv,mod
from decimal import Decimal
from random import shuffle,choice#,randint
q=list(range(1,1503))
shuffle(q)
def fucken_indentations():
   ...

def tokenize(s):
   if not s:
      return []
   r=re.compile("\s*(=>|[-+*\/\%=\(\)]|[A-Za-z_][A-Za-z0-9_]*|[0-9]*\.?[0-9]+)\s*")
   return [i for i in r.findall(s) if not i.isspace()]

def is_number(n):
   return bool(re.compile(r'\A[-]?\d+(?:\.\d+)?\Z').search(n))

class Envirinment(dict):
   def __init__(self,ops={},funcs={},vars={},keys={}):
      self.update(ops=ops,funcs=funcs,vars=vars,keys=keys)

class Func:
   def __init__(self,params,expr,interp):
      self.params,self.expr=params,expr
      self.env=Envirinment(interp.env['ops'],interp.env['funcs'])
      self.ary=len(params)
      self.interp=interp

   def __call__(self,*args):
      self.env['vars'].update(zip(self.params,args))
      return self.interp.eval_postfix(self.interp.shunting_yard(self.expr,self.env),self.env)

class Interpreter:
   def __init__(self):
      vars={}
      funcs={}
      ops={'+':add,'-':sub,'*':mul,'/':truediv,'%':mod,'=':self._assign_var}
      keys=['fn']
      self.env=Envirinment(ops,funcs,vars,keys)

   def input(self,expr):
      t=tokenize(expr)
      if not t:
         return ''
      if t[0] in self.env['keys']:
         if t[0]=='fn':
            new_f_n=t[1]
            if new_f_n in self.env['vars']:
               raise Exception('Cannot overwrite variable with function!')
            opi=t.index('=>')
            params=t[2:opi]
            if len(params)!=len(set(params)):
               raise Exception('Duplicate parameters specified!')
            ex=t[opi+1:]
            for i in ex:
               if i.isalpha() and i not in params:
                  raise Exception('Function body contains unknown variables!')
            new_f=Func(params,ex,self)
            self.env['funcs'][new_f_n]=new_f
            return ''
      else:
         val=self.eval_expr(t)
      return val

   def eval_expr(self,t):
      return self.eval_postfix(self.shunting_yard(t))

   def _assign_var(self,name,value):
      if name in self.env['funcs']:
         raise Exception('Cannot overwrite function with variable!')
      self.env['vars'][name]=value
      return value
   
   def shunting_yard(self,expr,env=None):
      env=env or self.env
      out,ops=[],[]

      def prec(op):
         if op in '+-':
            return 2
         if op in '/*%':
            return 3
         if op=='=':
            return 1
         else:
            raise Exception(f'{op} is not a valid operator.')
      
      def is_left_assoc(op):
         return False if op=='=' else True
    
      for i in expr:
         if is_number(i):
            out.append(int(i) if isinstance(i,int) else float(i))
         elif i in env['funcs']:
            ops.append(i)
         elif i in env['vars']:
            out.append(i)
         elif i in env['ops']:
            if ops and ops[-1] in env['ops']:
               o1,o2=i,ops[-1]
               while ops and o2 in env['ops'] and ((is_left_assoc(o1) and prec(o1)<=prec(o2)) or (not is_left_assoc(o1) and prec(o1)<prec(o2))):
                  out.append(env['ops'][ops.pop()])
                  if ops:
                     o2=ops[-1]
                  else:
                     break
            ops.append(i)
         elif i=='(':
            ops.append(i)
         elif i==')':
            while ops and ops[-1]!='(' and ops[-1] in env['ops']:
               out.append(env['ops'][ops.pop()])
            try:
               ops.pop()
            except IndexError:
               raise Exception('ERROR: Mismatched parentheses!')
            if ops and ops[-1] in env['funcs']:
               out.append(env['funcs'][ops.pop()])
         else:
            out.append(i)
      while ops:
         if ops[-1] in env['ops']:
            out.append(env['ops'][ops.pop()])
         elif ops[-1] in env['funcs']:
            out.append(env['funcs'][ops.pop()])
         else:
            raise Exception('Invalid function!')
      return out

   def eval_postfix(self,tokens,env=None):
      env=env or self.env
      if tokens is None:
         return ''
      out=[]
      for _,i in enumerate(tokens):
         if isinstance(i,(int,float)):
            out.append(i)
         elif isinstance(i,Func):
            try:
               args=[env['vars'][out.pop()] if out[-1] in env['vars'] else out.pop() for _ in range(i.ary)]
            except IndexError:
               raise Exception('ERROR: Incorrect number of arguments passed to function!')
            out.append(i(*args))
         elif callable(i):
            r,l=out.pop(),out.pop()
            if r in env['vars']:
               r=env['vars'][r]
            if isinstance(r,str):
               raise Exception('ERROR: Variable referenced before assignment!')
            if l in env['vars'] and i!=env['ops']['=']:
               l=env['vars'][l]
            out.append(i(l,r))
         elif isinstance(i,str):
            out.append(i)
      if len(out)>1:
         raise Exception('ERROR: Invalid syntax!')
      try:
         if out[0] in env['vars']:
            return env['vars'][out[0]]
         elif isinstance(out[0],str):
            raise Exception('Undeclared variable referenced!')
         else:
            return out[0]
      except IndexError:
         return ''

         
I=Interpreter()
I.input("fn avg x y => (x + y) / 2")
print(I.input("avg 4 2"))

print(I.input('1 + 1'))
print(I.input('2 * 3'))