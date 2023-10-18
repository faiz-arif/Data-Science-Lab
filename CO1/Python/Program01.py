n=int(input("enter the number:"))
rev=0
sum=0
while n>0:
    number=n%10
    rev=rev*10+number
    sum=sum+number
    n=n//10
print("reversed number:",rev)
print("sum of digits:",sum)
