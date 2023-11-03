def convert_to_base(n,b):
    s='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if b>len(s):
        raise()
    r=''
    while n:
        r=s[n%b]+r
        n//=b
    return r

print(convert_to_base(1221,16))