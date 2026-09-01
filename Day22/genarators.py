'''def retrivdata():
    d=['1','100','388','euruwyr','77575fgfhf']
    for i in d:
        yield i
reels=retrivdata()

while True:
    status=input("[s]crol or [q]uit")
    if status =="s":
        print(next(reels))
    else:
        break

def factors(n):
    for i in range(1, n + 1):
        if n % i == 0:
            yield i

n = int(input("Enter a number: "))

for factor in factors(n):
    print(factor, end=" ")'''

def isprime(n):
    for i in range(2,n//2+1):
        if n%i==0:
            return False
    return True
def prime(n):
    for j in range(2,n+1):
        if isprime(j):
            yield j
n=50
res =prime(n)
for j in res:
    print (j)
