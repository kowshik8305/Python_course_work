class Whatsappv1:
    def __init__(self,name):
        self.name=name
        print(f"welcome to the whatsappv1 {self.name}")
    def massaging(self):
        print("you can do massaging")
class Whatsappv2(Whatsappv1):
    def __init__(self,name):
        self.name=name
        print(f"welcome to the whatsappv1 {self.name}")
    def calls(self):
        print("you can do audio and video calls")
kowshik=Whatsappv1("kowshik")
kowshik.massaging()

asd=Whatsappv2("asd")
asd.massaging()
asd.calls()