i=1
count=0
sum=0
while i<=4:
    A=int(input("enter a weight: "))
    sum=sum+A
    count=count+1
    i=i+1
print(sum)
print(sum/count)
average=sum/count
if average%5==0:
    print("divisible")
else:
    print("not divisible")