i=1
while i<=100:
    sum=0
    n=i
    while n>0:
        R=n%10
        sum=sum+R
        n=n//10
    if i%sum==0:
        print(i)
    i=i+1