'''greater = lambda a,b: a if a>b else b

print(greater(12,34))

wish=lambda name : f'welcome to the course {name}'

print(wish("pfs"))

iseven=lambda n: 'even' if n%2==0 else 'odd'

print(iseven(12))

avg=lambda a,b,c:(a+b+c)/3
print(avg(2,34,56))

domain =lambda mail: (mail.split("@")[-1]).split('.')[0]

print(domain('kowshikcode.com'))
print(domain("kowshikgmail.com"))

gst=lambda price :price +price*0.18

print(gst(1000))
print(gst(3000))
print(gst(2345))

p=[123.33425,224,4452,23534654]
re=list(map(lambda p: p +p*0.18,p))
print(re)

names=["kowshik",'kdssd','jdsjkdks']
re=list(map(lambda name: name.title(),names))
print(re)

prices=[1211,313,1344,34234,3435]
res = list(map(lambda price: price - price*0.3,prices))
print(res)

prices=[1211,313,1344,34234,3435,5467]
res = list(filter(lambda price: price>5000,prices))
print(res)

name=("kowshik",'kjfkjsf,jdfjsfsj,hguygduyg')
res =list(filter(lambda name : len(name)>5,name))
print(res)

name=['sjdfjs','zdhfjf','shsjshf',"jhffhj"]
res=reduce(lambda res,1:res+" +1,name")
print(res)'''

products= {"super":60,
           "salt":30,
           'eggs':40}
print(dict(sorted(products.items())))
print(dict(sorted(products.items(),reverse=True)))

print(dict(sorted(products.item)))