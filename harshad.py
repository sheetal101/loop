num=int(input("enter a number: "))
sum=0
while num>0:
    n=num%10
    sum=sum+n
    num=num//10
if num%sum==0:
    print("harshad number")
else:
    print("NOO!!!")