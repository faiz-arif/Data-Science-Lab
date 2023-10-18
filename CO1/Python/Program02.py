text=input("enter the text:")
uppercase=0
lowercase=0
for char in text:
    if char.isupper():
        uppercase+=1
    elif char.islower():
        lowercase+=1
print("upper case letters:",uppercase)
print("lower case letters:",lowercase)
