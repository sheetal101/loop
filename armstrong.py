n=int(input("enter a number: "))
sum=0
N=n
while n>0:
    i=n%10
    sum=sum+i**len(str(N))
    n=n//10
if N==sum:
    print("armstrong")
else:
    print("no")