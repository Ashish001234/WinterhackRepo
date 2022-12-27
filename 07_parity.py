def getParity( n ):
    parity = 0
    while n:
        parity = ~parity
        n = n & (n - 1)
    return parity
            
n = 7
n_bin=bin(n)
print ("Parity of no ", n," = ",
     ( "odd" if getParity(n) else "even"))
c1=0
for i in str(n_bin):
    if i=='1':
        c1=c1+1
if(getParity(n)):
    if(c1%2!=0):
        print((str(n_bin)+"0").replace("0b",""))
    else:
        print((str(n_bin)+"1").replace("0b",""))
else:
    if(c1&1):
        print((str(n_bin)+"1").replace("0b",""))
    else:
        print((str(n_bin)+"0").replace("0b",""))