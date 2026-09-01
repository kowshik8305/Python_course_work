#1. Positive or Negative

'''n=int(input("enter the number:"))
if n>0:
    print("positive number")
else:
    print("Negative number")'''

#2. Even or Odd

'''n=int(input("enter the number:"))
if n%2==0:
    print("Even number")
else:
    print("odd number")'''

#3. Divisible by 5

'''n=int(input("enter the number:"))
if n%5==0:
    print("Divisible by 5")
else:
    print("not divisible by 5")'''

#4. Divisible by 3 and 7

'''n=int(input("enter the number:"))
if n%3==0 and n%7==0:
    print("Divisible by 3 and 7")
else:
    print("not divisible by 3 and 7")'''

#5. Check for Leap Year

'''n=int(input("enter the number:"))
if n%4==0 or n%400==0:
    print("leap year")
else:
    print("not an leap year")'''

#6. Check Pass or Fail (Passing marks = 35)

'''n=int(input("enter the number:"))
if n>35:
    print("pass")
else:
    print("fail")'''

#7. Check if number is 3-digit

'''n=int(input("enter the number:"))
if len([n])==3:
    print("3-digit number")
else:
    print(" not 3-digit number")'''


#8. Check if character is vowel

'''n=input("enter the number:")
if n in 'aeiouAEIOU':
    print("VOWEL")
else:
    print(" CONSONENT")'''

#9. Check greatest of two numbers

'''n=int(input("no 1"))
w=int(input("no 2"))
if n>w:
    print(n,"is greater")
elif w>n:
    print(w,"is greater")
else:
    print('please enter differnt no')'''

#10. Check smallest of two numbers

'''n=int(input("no 1"))
w=int(input("no 2"))
if n<w:
    print(n,"is smaller")
elif w<n:
    print(w,"is smaller")
else:
    print('please enter differnt no')'''

#11. Check if number is zero

'''n=int(input("enter the number:"))
if n==0:
    print("number is zero")
else:
    print(" not zero")'''

#12. Check if number is multiple of 10

'''n=int(input("enter the no: "))
if n%10:
    print("number is multiple of 10")
else:
    print("enter different")'''

#13. Check if age is eligible to vote (18+)

'''n=int(input("enter the no"))
if n>18:
    print("eligible to vote")
else:
    print("not eligible ")'''

#14. Check if number is between 1 and 100
'''n=int(input("enter the no"))
if 1<n<100:
    print("in range")
else:
    print("not in range")'''

#15. Check if number is square of another

'''n,s=map(int,input("enter the no").split())
if n ==s*s:
    print(n,"is squar of",s)
else:
    print("not squar")'''

#16. Check if two strings are equal

'''n,s=input().split()
if n==s:
    print("str is equal")
else:
    print("not equal")'''

#17. Check if a number is prime (basic logic)

'''n=int(input("enter the no"))
if n%2==1:
    print('prime')
else:
    print('not prime')'''

#18. Check if number is positive and even

'''n=int(input("enter the no"))
if n>0 and n%2==0:
    print("positive and even number")
else:
    print("positive and odd")'''

#19. Check if character is uppercase
'''n=input("enter the char")
if n==n.upper():
    print("uppercase letter")
else:
    print("not uppercase")'''

#20. Check if temperature is hot (>30°C)

'''n=int(input("enter the no"))
if n>35:
    print("it's hot")
else:
    print("cool")'''

#1. Check if a number is a 4-digit even number

'''n,s,w,e=map(int,input("enter 4 digit no").split())
if n%2==0 and  s%2==0 and  w%2==0 and  e%2==0:
    print("4 digit even number")
else:
    print("not 4 digit no")'''

#Check if a character is a consonant

'''n=input("enter char")
if n in 'aeiouAEIOU':
    print("vowel")
else:
    print("consonant")'''

#3. Check if a number is divisible by 2 or 3 but not both

n=int(input("enter the no"))
if n%2==0 and n%3==0:
    print("divisible by both 2 and 3")
elif n%2==0: 
    print("divisible by 2")
else:
    print('divisible by 3')


