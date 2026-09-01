'''def display(n):
    if n>10:
        return
    print(n)
    display(n+1)
display(1)

def display(n):
    if n>10:
        return
    display(n+1)
    print(n)
display(1)

def displaysum(n):
    if n==1:
        return 1
    return n+displaysum(n-1)
print(displaysum(8))

def displaypro(n):
    if n==1:
        return 1
    return n*displaypro(n-1)
print(displaypro(3))

def string(ind):
    if ind==len(s):
        return
    print(s[ind],end="") 
    string(ind+1)
s="kowshik"
string(0)   
def string(ind):
    if ind==len(s):
        return
    string(ind+1)
    print(s[ind],end="")
s="kowshik"
string(0)  

def display(n):
    if n>len(s):
        return
    print(s[:n])
    display(n+1)

s="kowshik"
display(1)

def display(ind,w):
    if ind>len(s)-w:
        return
    print(s[ind:ind+w])
    display(ind+1,w)
s='kowshik'
display(0,7)'''

def display(n):
    if n==0:
        return
    display(n//10)
    print(n%10)
n=987654
display(n)
