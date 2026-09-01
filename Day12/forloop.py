#str list set tuple dict range()

''' 
for var in seq:
    print (var)
'''
'''s="kowshik"
for ch in s:
    if ch in "aeiouAEIOU":
        print(ch)'''

'''i=[23,45,2,3,11,245,2,3,33,677]
for i in i:
    if i%2==0:
        print(i,"even")
    else:
        print(i,"odd")'''

'''mar=(36,1,36,67,87,98,56,44)
for mark in mar:
    if mark>35:
        print(mark,"pass")
    else:
        print(mark,"fail")'''

'''follower={'kowshik','benarji','srinivas'}
for i in follower:
    print(i)'''

'''bus={'s1':'booked','s2':'available','s3':'available','s4':'booked'}
for seat in bus:
    if bus.get(seat)=='available':
        print (seat,bus.get(seat))'''

#range (start,end,step)=>(0,nodef,i)

'''for i in range(1,11):
    print(i)'''

'''for i in range(2,51,2):
    print(i,end=" ")'''

   
'''for i in range(2,51,2):
    print(i,end=" ")'''

n=int(input("enter the table"))
for i in range(1,11):
    print(f'{n}*{i}={n*i}')