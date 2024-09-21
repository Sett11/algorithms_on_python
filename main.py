x=1000000
a,b,c='012'*x,'000111222'*x,('0'*9+'1'*9+'2'*9)*x

def get_positions(n):
    return int(a[n]),int(b[n]),int(c[n])

print(get_positions(98))