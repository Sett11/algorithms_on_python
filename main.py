"""
>>> check_braces_sequence('[((()))]')
True
>>> check_braces_sequence('[(((()))]')
False
>>> check_braces_sequence('[(((())))]')
True
"""

import A_stack

def check_braces_sequence(s:str)->bool:
    A_stack.clear()
    for i in range(len(s)):
        if s[i] in '[(':
            A_stack.push(s[i])
        else:
            if not A_stack._stack:
                return False
            t=A_stack.pop()+s[i]
            if t not in '()[]':
                return False
    return A_stack.is_empty()


if __name__=="__main__":
    from doctest import testmod
    print(testmod(verbose=True))