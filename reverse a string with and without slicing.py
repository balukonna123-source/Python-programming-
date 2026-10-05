#Reverse a given string without slicing

name=input("enter the string")
count=len(name)
for  i in range(count,0,-1):
    print(name[i-1],end="")

#Reverse a given string with slicing
print()
str=input("enter the string")
print(str[::-1])
