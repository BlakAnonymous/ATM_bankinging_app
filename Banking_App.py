
class User:
    def __init__(self,name,age,gender):
        self.name = name
        self.age =  age
        self.gender = gender
   
    def  show_details(self):
         print("Personal Details") 
         print("")
         print("Name ", self.name)
         print("Age ", self.age)
         print("Gender ", self.gender)

    

class Bank(User):
    def __init__(self,name,age,gender):
        super().__init__(name,age,gender)
        self.balance = 0

    def deposit(self, amount):
        self.amount = amount
        self.balance = self.balance + self.amount
        print("Account balance has been updated : R ", self.balance)

    def withdraw(self, amount):
        self.amount = amount
        if self.amount > self.balance:
            print("Insuficient Funds / Balance Available : R", self.balance)
        else:
            self.balance = self.balance - self.amount
            print("Account balance has been updated : R ", self.balance)

    def view_balance(self):
            self.show_details()
            print("Account balance has been updated : R ", self.balance)
               
               
  
   

    
               
   
       
        
