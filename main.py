from collections import deque

def calc(s):
    a=s.split(' ')
    stack=deque()
    for i in a:
        if i.isdigit():
            stack.append(int(i))
        elif i.replace('.','').isdigit():
            stack.append(float(i))
        else:
            if len(stack)>1:
                t,p=stack.pop(),stack.pop()
                stack.append(eval(f'{p}{i}{t}'))
    return stack.pop() if stack else 0


print(calc('5 1 2 + 4 * + 3 -'))
print(calc("3.5"))