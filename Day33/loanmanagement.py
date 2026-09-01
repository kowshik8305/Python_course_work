from abc import ABC,abstractmethod
class customer:
    def __init__(self,customer_id,name,age,email,phone,income,creadit_scr):
        self.customer_id=customer_id
        self.name=name
        self.age=age
        self.email=email
        self.phone=phone
        self.income=income
        self.creadit_scr=creadit_scr

    def check_eligibility(self):
        if self.age<21 or self.creadit_scr<650 or self.income<25000:
            return False
        return True

    def display_customer(self):
        print("\n Customer details")
        print("---------------------")
        print("customer id: ",self.customer_id)
        print("Name:  ",self.name)
        print("Age: ",self.age)
        print("Phone Number: ",self.phone)
        print("Email: ",self.email)
        print("Income: ",self.income)
        print("credits_score: ",self.creadit_scr)
kowshik=customer(1,'kowshik',22,789456120,'kowshik@gmail.com',26000,750)
kowshik.display_customer()
print("Loan eligibility",kowshik.check_eligibility())

class Loan(ABC):
    def __init__(self,loan_id,customer, loan_amount, interest_rate,loan_tenure):
        self.load_id=self.load_id
        self.customer=customer
        self.loan_id=loan_id
        self.loan_amount=loan_amount
        self.interest_rate=interest_rate
        self.loan_tenure=loan_tenure
        self.repayment_history=[]
        self.status="Applied"
    def calculate_emi(self):
        pass
    def check_loan_eligibility(self):
        if not self.Customer.check_eligibility():
            self.status="Rejected"
            return False
        return True
    def sanction_loan(self):
        if self.status=="Rejected":
            print("Loan application was rejected")
            return
        if not self.check_loan_eligibility():
            print("customer is not eligible for the loan")
            return
        self.status="scanctioned"
        print("\nLoan sanctioned successfully")
    def repay(self,amount):
        if self.status!="Scanctioned":
            print("Repayment is not allowed")
            print("Loan status:",self.status)
            return
        if amount<=0:
            print("Invalid repayment amount")
            return
        if amount > self.__balance:
            print("Repayment amount is greater than outstanding balance")
            return
        self.__balance-=amount
        self.__toatl_paid+=amount

        self.repayment_history.append(amount)
        print("\n Repayment successful:")
        print("Amounrt paid           :",amount)
        print("Outstanding Balance    :",self.__balance)

        if self.__balance==0:
            self.status="Closed"
            print("Loan Closed sucessfully")
    def get_balance(self):
        return self.__balance
    def get_loan_amount(self):
        return self.__loan_amount
    def get_toatl_paid(self):
        return self.__toatl_paid
    def display_statement(self):
        print("\n")
        print("="*40)
        print("LOAN STATEMENT")
        print("="*40)

        print("Loan Id                         :",self.loan_id)
        print("Customer Name                   :",self.Customer.name)
        print("loan amount                     :",self.loan_amount)
        print("Interest rate                   :",self.interest_rate)
        print("Tenure                          :",self.tenure)
        print("Loan status                     :",self.status)

        print("\n Repayment history")
        if not self.repayment_history:
            print("No repayment made")
        else:
            for i in range(len(self.repayment_history)):
                print(f"payment{i+1}     : {self.repayment_history {i} }")
        print("="*40)
    def __str__(self):
        return (
            f"Loan Id : {self.loan_id}"
            f" Customer: {self.customer.name}"
            f"Loan Amount:{self.__loan_amount}"
            f"Outstanding:{self.__balance}"
            f""
        )

