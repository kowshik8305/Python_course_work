
True
n = 20
n += 10
n
30
n-=5
n
25
n/2
12.5
n//=2
n
12
n%=1
n
0
n*=2
n
0
n**=3
n
0
n=10
n
10
n%2==0 and n%3==0
False
n%2==0 or n%3==0
True
n%9==0  %3==0
n%9==0 or n%3==0
False
n
10
n<5
False
n<5
True
# str, list, tuple, set, dirct
s='sai'
s in s
True

'b' in s
True
'z' in s
False
'w' not in s
True
l =[1,2,3,4]
'1' in l
False
1 in l
True
t =(1,2,3,4,5,6)
2 in t
True
9 not in t
True
s ={1,2,3,4,5,6,7}
1 in s
True
0 not in s
True
d = {'name':"sai",'age':"21"}
'name' in d
True
"sai" not in d
True
l = [1,2,3,4]
m=[1,2,3,4]
id(l)
2385282068352
id(m)
2385327749312
l is m
False
n = l
id(n)
2385282068352
n is l
True
l is not m
True
l is not m
True
l is not n
False
s = {1,2,3,4}
id(s)
2385327579744
s.add(5)
s
{1, 2, 3, 4, 5}
id(s)
2385327579744
9&10
8
9|10
11
9^10
3
8>>3
1
8<<3
64
6
-71
-2
0
-1
a = 10
b = 20.2
