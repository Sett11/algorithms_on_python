"""
>>> is_empty()
True
>>> push(1)
>>> push(2)
>>> push(3)
>>> is_empty()
False
>>> pop()
3
>>> pop()
2
>>> pop()
1
>>> is_empty()
True
"""
_stack=[]

def is_empty():
    return not len(_stack)

def push(n):
    _stack.append(n)

def pop():
    return _stack.pop()

def clear():
    _stack.clear()

if __name__=="__main__":
    from doctest import testmod
    testmod(verbose=True)