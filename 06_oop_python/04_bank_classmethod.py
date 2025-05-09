class Bank:

    bank_name = "Bank of Python"
    
    @classmethod
    
    def change_bank_name(cls, name):
        cls.bank_name = name


customer1 = Bank()
customer2 = Bank()

print("customer1 bank ", customer1.bank_name)
print("customer2 bank ", customer2.bank_name)

Bank.change_bank_name("New Future Bank")

print("customer1 bank ", customer1.bank_name)
print("customer2 bank ", customer2.bank_name)



