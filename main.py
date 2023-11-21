def fib(n):

    def f(x):
        if not x:
            return [0,1]
        if x==1:
            return [1,1]
        a,b=f(x//2)
        p,t=a*(2*b-a),a*a+b*b
        return [p,t] if x%2==0 else [t,t+p]
    
    return f(n)[0] if n>=0 else -f(-n)[0] if n%2==0 else f(-n)[0]

print(fib(-96))
print(fib(10))