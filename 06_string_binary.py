def dtb(num):
    st = ''
    while num > 0:
        st = str(num % 2) + st
        num //= 2
    return st

a=input()
b=[ord(x) for x in a]
sto = ''
for i in b:
    sto += dtb(i)
print(sto)