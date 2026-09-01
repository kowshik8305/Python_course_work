'''def display(n):
    n=n+10
    print("inside",n)

n=10
display(n)
print("outside",n)

def display():
    print('inside',n)

n=10 
display()
print("outside",n)

def display():
    n=n=10
    print('inside',n)

n=10 
display()
print("outside",n)

def display():
    global n
    n=n+12
    print('inside',n)

n=10 
n=4+n
display()
print("outside",n)

def display():
    n='pfs'
    print('inside',n)

n='jfs'
display()
print("outside",n)

def display():
    n='jfs'
    def update():
        nonlocal n
        n='pfs'
        print("updated course",n)
    update()
    print("final course",n)
display()'''

#if we use bulit in function as a variables then a act as a variable and it loses it property and act as variable




