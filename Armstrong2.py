i=1
while i<=2000:
    sum=0
    j=i
    while j>0:
        N=j%10
        sum=sum+N**len(str(i))
        j=j//10
    if i==sum:
        print(i)
    i=i+1