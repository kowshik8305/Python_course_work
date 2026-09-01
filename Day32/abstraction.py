from abc import ABC,abstractmethod

class Phonepy(ABC):
    def senderinfo(self):
        print("you can enter their moblie number or scanner ")
    def amount(self):
        print("you can enter amount")
    def pin(self):
        print("you need to enter pin")
    @abstractmethod
    def transaction(self):
        pass

class HDFC(Phonepy):
    def transaction(self):
        print('payment using Hdfc bank')
class SBI(Phonepy):
    def transaction(self):
        print('payment using sbi bank')
class AXIS(Phonepy):
    def transaction(self):
        print('payment using axis bank')
class UNION(Phonepy):
    def transaction(self):
        print("payment using union bank")
class ICIC(Phonepy):
    def transaction(self):
        print('payment using Hdfc bank')
kowshik=SBI()
kowshik.senderinfo()
kowshik.amount()
kowshik.pin()
kowshik.transaction()
