class User:
    def __init__(self, identification, lastname, balance):
        super().__init__()
        self.identification = identification
        self.lastname = lastname
        self.balance = balance
    
    def debit(self, ammount):
        self.balance = self.balance + ammount
        print(self.balance)
        return self.balance
    
    def credit(self, ammount):
        if(self.balance >= ammount):
            self.balance = self.balance - ammount
            print(self.balance)
            return self.balance
        else:
            print("Saldo insuficiente")
            return 0

antonio = User(1, "Fernandez", 1000000)
antonio.credit(1000)
antonio.debit(1000)