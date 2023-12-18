class Income:
    
    def __init__(self,rent_income = 0,total_income = 0,total_expenses = 0,annual_cash_flow = 0 , total_investment = 0):
        print("Please type in as a number")
        self.total_income = int(input("Your total income is: "))
        self.rent_income = rent_income
        self.total_expenses = 0
        self.annual_cash_flow = 0
        self.total_investment = 0
        

    def Expenses(self):
        self.total_expenses += int((input("What is your total tax: "))) 
        self.total_expenses += int((input("What is your total insurance: ")))
        self.total_expenses += int((input("What is your total utilites: ")))
        self.total_expenses += int((input("What is your total repairs fee: ")))
        print (f"Your total expenses equals to {self.total_expenses}")


    def Cash_flow(self):
        cash_flow = self.total_income - self.total_expenses
        self.annual_cash_flow = cash_flow * 12
        print (f"Your cash flow is {cash_flow}")
        print (f"Your annual cash flow is: {self.annual_cash_flow}")
    

    def Investment(self,down_payment = 0,closing_cost = 0,rehab = 0):
        self.down_payment = down_payment
        self.closing_cost = closing_cost
        self.rehab = rehab
        self.total_investment += int((input("What is your down payment: ")))
        self.total_investment += int((input("What is your closing costs: ")))
        self.total_investment += int((input("what is your Rehab budget: ")))
        print(f" your total investment is {self.total_investment}")


        
        #  ROI
        return self.annual_cash_flow/self.total_investment