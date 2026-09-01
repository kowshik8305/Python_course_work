'''s='python programming'
for i in range (len(s)):
    if s[i] in 'aeiouAEIOU':
        print(i,s[i])'''

'''l=[23,44,34,2,57,21,46,89,13]
sum=0
for i in range(len(l)):
    if l[i]%2==0:
        sum=sum+i
        print(i,l[i])
print(sum)'''

'''n=int(input("enter the number"))
fact=1
for i in range(1,n+1):
    fact*=i
print(f"factorial of {n} is {fact}")'''

'''data={}
n=int(input("enter the no of students: "))
max_marks=0
for i in range(n):
    name=input("enter the name: ")
    marks=int(input("enter the marks "))
    if marks > max_marks:
        max_marks=marks
    data[name]=marks
print(data)
print("maximum marks",max_marks)'''

'''name of item,price,quantity we need to print total amount '''

data={}
n=int(input("enter the no of items: "))
bill=0
sum=0
for i in range(n):
    name =input("enter the name of item: ")
    price=int(input("enter the price"))
    qun=int(input("enter the quntity"))
    sum=price*qun
    print("Total price:",sum)
    bill+=sum
print("Total Bill:",bill)
