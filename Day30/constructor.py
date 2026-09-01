#A constructor is a special method in a class that is automatically called when you create an object.

class Flipkart:
    def __init__(self,name,phone):
        self.name=name
        self.phone=phone
        print(f"Hello {self.name},welcomr to the Flipkart")

kowshik=Flipkart('kowshik',123454321)
