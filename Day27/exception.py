try:
    a= int(input('enter the number :'))
    #k=(1.12,123)
    #print(k[2])
    #l=[22,644]
   # print(i[10])
   # print(1/0)
    print('1'+1)
except ValueError:
    print("enter the correct data type")
except IndexError:
    print("enter the correct index")
except ZeroDivisionError:
    print("enter the correct data type")
except TypeError:
    print("enter the correct type")
except NameError:
    print("enter the correct Name")

finally:
    print("end of the program")

try:
    a= int(input('enter the number :'))
    #k=(1.12,123)
    #print(k[2])
    #l=[22,644]
   # print(i[10])
   # print(1/0)
    #print('1'+1)
except(ValueError,IndexError,ZeroDivisionError,TypeError,NameError) as e:
    print("error occur")
else:
    print("Error free program")
finally:
    print("end of the program")
try:
    a= int(input('enter the number :'))
    #k=(1.12,123)
    #print(k[2])
    #l=[22,644]
   # print(i[10])
   # print(1/0)
   # print('1'+1)
except Exception as e:
    print("error occur")
else:
    print('Error free program')
finally:
    print("end of the program")
try:
    amount=int(input('enter the amount'))
    balance=5000
    if amount <0:
        raise Exception("amount needs to be positive")
except Exception as e:
    print("error occured:",e)
else:
    print('Error free program')
finally:
    print("end of the program")