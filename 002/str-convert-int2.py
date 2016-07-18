d={str(z):z for z in range(10)}
sum =0
a='-1'
#a=input(str('input num'))
if a[0]=='-':
    c = a.strip('-')
else:
    c = a

if '.' in c:
    x,y=c.split('.')
    for integer in x:
        sum+=d[integer]*10**(len(x)-1-x.index(integer))
    for decimals in y:
        sum+=d[decimals]*(0.1**((y.index(decimals)+1))) 
else:
    x = c
    for integer in x:
        sum+=d[integer]*10**(len(x)-1-x.index(integer))
if a[0]=='-':
    print(-sum)
else:
    print(sum)

