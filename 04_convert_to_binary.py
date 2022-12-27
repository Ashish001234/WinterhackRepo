a = 4352
b = 543.25
def decimal_to_binary(num, k):
    final = ""
    int_part = int(num)
    frac = num - int_part

    while int_part:
        rem = int_part % 2
        final += str(rem)
        int_part //= 2

    final = final[:: -1]
    final += '.'

    while k:
        frac *= 2
        fract_bit = int(frac)
        if fract_bit == 1:
            frac -= fract_bit
            final += '1'
        else:
            final += '0'
        k -= 1

    return final
print(decimal_to_binary(a,0))
print(decimal_to_binary(b,3))

a0= decimal_to_binary(a,0).count("0")
print(a0)
a1= decimal_to_binary(a,0).count("1")
print(a1)
b0 = decimal_to_binary(b,3).count("0")
print(b0)
b1 = decimal_to_binary(b,3).count("1")
print(b1)