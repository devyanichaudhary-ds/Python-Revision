class Expensetracker:
    def __init__ (self, food=0, travel=0, study=0):
        self.food= food
        self.travel= travel
        self.study = study
    
    def total_expense(self):
        return self.food + self.travel + self.study
    
    def display(self):
        print("\n----- Expense Report -----")
        print(f"Food Expense: {self.food}")
        print(f"Travel Expense: {self.travel}")
        print(f"Study Expense: {self.study}")
        print(f"Total Expense: {self.total_expense()}")
    
tracker = Expensetracker()
while True:
    category = input("\n Enter Category or exit:").lower()
    if category == "exit":
        break

    if category not in ["food", "travel", "study"]:
        print("Invalid category!")
        continue
    amount = float(input("enter expense amount: "))
    if category == "food":
        tracker.food +=amount
    elif category =="travel":
        tracker.travel +=amount
    elif category == "study":
        tracker.study +=amount
    print("Expense aded Successfully!!")
tracker.display()