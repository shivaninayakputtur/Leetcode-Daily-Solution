def reverse(x):
    rev=0
    if x<0:
        negative=True
    else:
        negative=False
    x=abs(x)
    rev=int(str(x)[::-1])
    if negative:
        rev=-rev
    return rev
x=1321
print(reverse(x))