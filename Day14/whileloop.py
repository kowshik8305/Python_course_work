'''i=1
while i<=10:
    print(i)
    i+=1'''

'''i=10
while i>0:
    print(i)
    i-=1
    '''
'''i=2
while i<=100:
    print(i,end=",")
    i+=2'''

'''s='python programming'
i=len(s)-1
while i>=0:
    print(s[i],end="")
    i-=1'''

'''i=[1,2,0,0,6,4,7,0,6,8,0,6,4,0]
while 0 in i:
    i.remove(0)
    print(i)'''

'''data={}
total_bill=0
while True:
    product=input('enter the product (for exit)')
    if product=='exit':
        break
    price=int(input("enter the price:"))
    total_bill+=price
    data[product]=price
print(data)
print("total bill",total_bill)'''

i=0
while i<=10:
    i+=1
    if i==15:
        break
    print(i)
else:
    print("end of the loop")
   