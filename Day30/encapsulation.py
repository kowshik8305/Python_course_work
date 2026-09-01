class Instagram:
    def __init__(self,username,password):
        self.username=username
        self.__password=password
        self._posts=[]
    def getpassword(self):
        return self.__password
    def setpassword(self,newpassword):
        self.__password=newpassword
    @property
    def accesspost(self):
        return self._posts
    @accesspost.setter
    def accesspost(self,newpost):
        self._posts.append(newpost)
    def display(self):
        print(self.username,self.__password,self._posts)
kowshik=Instagram('kowshik','asdfqwer@123')
kowshik.display()
print(kowshik.username)
print(kowshik.getpassword())
print(kowshik.accesspost)
kowshik.username='aqsw'
kowshik.setpassword("aqsw@123")
kowshik.accesspost="assd.png"
print(kowshik.username)
print(kowshik.getpassword())
print(kowshik.accesspost)
