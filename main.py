def late_ride(n):
    a,b=divmod(n,60)
    return sum(map(int,str(a)))+sum(map(int,str(b)))

print(late_ride(808))
print(late_ride(1439))