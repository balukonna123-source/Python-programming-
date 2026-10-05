#Removing duplicate chars from a string
m=input("enter the string")
j=''
count=0
for i in m:
    if i in j:
        count+=1
    else:
        j+=i
print(j)
print(count)
