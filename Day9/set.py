s=()
type(s)

set()
set()
s=set()
s
set()
s.add(22)
s.add(23.2)
s.add(2+3)
s
{5, 22, 23.2}
s={1,1,1,1,11}
s
{1, 11}
a={1,2,3,4,5}
b={3,5,7,9}
a
{1, 2, 3, 4, 5}
b
{9, 3, 5, 7}
a | b
{1, 2, 3, 4, 5, 7, 9}
a&b
{3, 5}
a-b
{1, 2, 4}
a^b
{1, 2, 4, 7, 9}
{1}<=a
True
a
{1, 2, 3, 4, 5}
{1, 2, 3, 4, 5}<a
False
{1, 2, 3, 4, 5}<=a
True
b
{9, 3, 5, 7}
a.isdijoint(b)
a.isdisjoint(b)
False
a.isdisjoint({9,10})
True
a.union(b)
{1, 2, 3, 4, 5, 7, 9}
a.intersection(b)
{3, 5}
a.issubset(b)
False
a.issubset(a)
True
a
{1, 2, 3, 4, 5}
5 in a
True
a.issuperset(b)
False
7 in a
False
8 not in a
True
max(a)
5
min(a)
1
sorted(a)
[1, 2, 3, 4, 5]
sum(a)
15
a
{1, 2, 3, 4, 5}
b=a
b
{1, 2, 3, 4, 5}
b.add(12)
b
{1, 2, 3, 4, 5, 12}
a
{1, 2, 3, 4, 5, 12}
c=a.copy()
c.add(12)
c.add(13)
c
{1, 2, 3, 4, 5, 12, 13}
a
{1, 2, 3, 4, 5, 12}
a.update({10,20,30})
a
{1, 2, 3, 4, 5, 10, 12, 20, 30}
a.pop()
1
a.pop()
2
a.remove(12)
a.discard(3)
a
{4, 5, 10, 20, 30}
a.discard({4,5})
a
{4, 5, 10, 20, 30}
a.clear()
a
set()
a={0,1,2,3,'sai',-22,0.2,}
len(a)
7
all(a)
False
any (a)
True
a = frozenset({1,22,30,44})
a
frozenset({1, 44, 22, 30})
a.ad(11)

d={'a':1, 'b':2, 'c':3}
   
d
   
{'a': 1, 'b': 2, 'c': 3}
id(d)
   
2709537587072
d['5']=d
   
d
   
{'a': 1, 'b': 2, 'c': 3, '5': {...}}
d[12.3]='flt'
   
d
   
{'a': 1, 'b': 2, 'c': 3, '5': {...}, 12.3: 'flt'}
d[2+3j]='comd[2+3j]='
   
d
   
{'a': 1, 'b': 2, 'c': 3, '5': {...}, 12.3: 'flt', (2+3j): 'com'}
d['str']='string'
   
d
   
{'a': 1, 'b': 2, 'c': 3, '5': {...}, 12.3: 'flt', (2+3j): 'com', 'str': 'string'}
d[(1,2,3)]='tuple'
   
d
   
{'a': 1, 'b': 2, 'c': 3, '5': {...}, 12.3: 'flt', (2+3j): 'com', 'str': 'string', (1, 2, 3): 'tuple'}
d={}
...    
d[2]=2
...    
d[3]=3
...    
d[5]=5
...    
d[6]=2+3
...    
d[7]='str'
...    
d[8]=(1,2,3)
...    
d
...    
{1: 1, 2: 2, 3: 3, 5: 5, 6: (2+3), 7: 'str', 8: (1, 2, 3)}
1 in d
...    
True
9 in d
...    
10  not in d
...    
True
'str' in d
...    
d[8]
...    
(1, 2, 3)
d.get(1)
...    
1
d.get(9,'key is not present')
...    
'key is not present'
d.get(7,'key is not present')   
{1: 1, 2: 2, 3: 3, 5: 10, 6: 100, 7: 'str', 8: (1, 2, 3)}