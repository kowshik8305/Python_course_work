'''def display(name,email,password):
    print(f"hello {name}")
    print(f"your email {email}")
    print(f"your password {password}")

display('kowshik',"kowshik@gmail.com","pass123")
display("benarji","benarji@gmail.com","pass12")
display("pavan","pavan@gmail.com","passs123")

def isleapyear(year):
    if year%400==0 or (year%4==0 and year%100!=0):
        print(f"{year} is an leap year")
    else:
        print(f"{year} is not an leap year")

for year in range(2001,2029):
    isleapyear(year)

def sumofdigit(n):
    sum=0
    while n>0:
        sum +=n%10
        n=n//10
    return sum
n=int(input("enter the number:"))
print(f"sum of {n} digit is {sumofdigit(n)}")

def proofdigit(n):
    pro=1
    while n>0:
        pro +=n%10
        n=n//10
    return pro
n=int(input("enter the number:"))
print(f"pro of {n} digit is {proofdigit(n)}")

def checkpassword(password):
    if len(password)>8:
        check=set()
        for i in password:
            if i.isupper():
               check.add("u")
            elif i.islower():
                check.add("l")
            elif i.isdigit():
                check.add("d")
            else:
                check.add("s")
        if len(check)==4:
            return "strong password"
    return "weak password"
password=input()
print(f"{checkpassword(password)}")
n=int(input())
def table(n):
    print(f"--------------table-{n}----------------------")
    for i in range(1,11):
        print(f"{n} * {i} = {n*i}")
for i in range (n):
    table(i)'''
