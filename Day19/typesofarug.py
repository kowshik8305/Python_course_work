#positional arugments are used when the input in the depend on the position 
'''def display(name,email,password):
    print(f'name: {name},email: {email},password:{password}')

display("kowshik","kowshik@11222","aqsw123")

#keyword arugments
def display(name,email,password):
    print(f"name:{name} email: {email},password:{password}")

display (name="xyz",email="awsq123222@",password="djdjdjjd")
display (password="dddhhdh",name="jdjfj",email='djdjd')

#
def dispaly(name=" ",email,password):
    print(f"name:{name}")
    print(f"email:{email}")
    print(f"password:{password}")
dispaly("xyz","djjdjdj")
display("jjdjdjjd")
#the output will comes in tuple formate
def display(*names):
    print(names)
display("kowshik")
display("kowshik","benarji")
display("ksddjfjn","jdsjfjf","hhjsfhd",'ajdhfdjsh')'''

#in this output comes in dict format
def display(**products):
    print(products)
display(bag=5000)
display(bag=500,book=30)
display(bag=4567,book=38,bottel=33)