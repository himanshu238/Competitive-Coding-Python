def is_leap(n):
    t=False
    if n%4==0:
        t=True
        if (n%100==0 and n%400!=0):
            t=False
    return t
n=int(input())
print(is_leap(n))
