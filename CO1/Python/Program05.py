def sum_of_cubes_of_even_numbers(n):
    sum=0
    for i in range(2,n+1,2):
        cube=i**3
        sum+=cube
    return sum
n=int(input("enter a postive integer"))
if n<=0:
    print("enter a postive integer")
else:
    result=sum_of_cubes_of_even_numbers(n)
print(result)
