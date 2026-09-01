import sys
#print(sys.path)
#print(sys.version)
print("start")
sys.exit()
print("end")

import platform
print(platform.system())
print(platform.release())
print(platform.processor())

import math
print(math.pi)
print(math.e)

print(math.sqrt(36))
print(math.pow(2,56))

print(math.ceil(12.00001))
print(math.ceil(12.3))
print(math.ceil(12.5))
print(math.ceil(12.89999))

print(math.floor(12.00001))
print(math.floor(12.3))
print(math.floor(12.5))
print(math.floor(12.89999))

print(math.fabs(-12))
print(math.factorial(5))
print(math.gcd(8,24))
print(math.log(2,2))
print(math.sin(90))
print(math.cos(45))
print(math.tan(180))
print(math.degrees(45))
print(math.radians(30))

import random 
random.seed(12)
print(random.randint(1,12))
print(random.randint(10000,90000))
print(random.random())
print(random.uniform(1,6))

l=['s','p','c']
print(random.choice(l))
print(random.choices(l,k=4))

random.shuffle(l)
print(l)

from collections import Counter

s="python programming"
m='this is that is is this is this a this '.split()
l=[1,2,1,2,3,4,5,4,3,5,5,4,5,5,66,44,33,66,33,5,45,4,45,45,454454,]

print(Counter(s))
print(Counter(m))
print(Counter(l))

from collections import defaultdict

s="python programming"
m='this is that is is this is this a this '.split()
l=[1,2,1,2,3,4,5,4,3,5,5,4,5,5,66,44,33,66,33,5,45,4,45,45,454454,]

d=defaultdict(int)
for i in s:
    d[i]+=1
print(d)
from collections import Counter,defaultdict,deque

i=deque([])
i.append(10)
i.append(23)
i.append(45)
i.append(23)
i.popleft()
i.popleft()
i.append(34)
i.append(12)
i.popleft()

print(i)

from collections import Counter,defaultdict,deque

i=deque([])
i.appendleft(10)
i.appendleft(23)
i.appendleft(45)
i.appendleft(23)
i.pop()
i.pop()
i.appendleft(34)
i.appendleft(12)
i.pop()

print(i)

from itertools import combinations,permutations

resl=list(combinations('abc',2))
res2=list(permutations('abc',2))

print(''.join(i) for i in resl)
print("".join(i) for i in res2)