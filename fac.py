n=int(input("enter a number: "))
while n>0:
    j=1
    fac=1
    rem=n%10
    while j<=rem:
        fac=fac*j
        j=j+1
        n=n//10
print(fac)
