"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, contract, hours, rate, number_of_contracts, commision_rate, bonus_commission):
        self.name = name
        self.contract = contract
        self.hours = hours
        self.rate = rate
        self.number_of_contracts = number_of_contracts
        self.commision_rate = commision_rate
        self.bonus_commission = bonus_commission

    def get_pay(self):
        pay = 0;
        if self.contract == "monthly":
            pay = int(self.rate)
        elif self.contract == "contract":
            pay = int(self.hours) * int(self.rate)
        if int(self.number_of_contracts) > 0:
            pay += int(self.number_of_contracts) * int(self.commision_rate)
        pay += int(self.bonus_commission)
        return pay

    def __str__(self):
        return f"{self.name} works on a{self.get_contract_info()}{self.get_commission_info()}{self.get_bonus_info()}. Their total pay is {self.get_pay()}."

    def get_contract_info(self):
        if self.contract == "monthly":
            return " monthly salary of " + self.rate
        else:
            return " contract of " + self.hours + " hours at " + self.rate + "/hour"
        
    def get_commission_info(self):
        if int(self.number_of_contracts) > 0:
            return " and receives a commission for " + self.number_of_contracts + " contract(s) at " + self.commision_rate + "/contract"
        else:
            return ""
        
    def get_bonus_info(self):
        if int(self.bonus_commission) > 0:
            return " and receives a bonus commission of " + self.bonus_commission
        else:
            return ""    

# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', "monthly", "0", "4000", "0", "0", "0")

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', "contract", "100", "25", "0", "0", "0")

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', "monthly", "0", "3000", "4", "200", "0")

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', "contract", "150", "25", "3", "220", "0")

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', "monthly", "0", "2000", "0", "0", "1500")

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', "contract", "120", "30", "0", "0", "600")
