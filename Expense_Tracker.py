from Tax_Calculation import tax_calculation

class ExpenseTracker:
    def __init__(self, income=100000):
        self.expenses = {}
        self.income = income

    def add_expense(self, category, amt, prnt=True):
        """Will add an expense name and amount (string, float) to a dictionary of expenses, 
        append it, and will calculate and return the new total expense amount"""
        if category in self.expenses:
            self.expenses[category].append(amt)
        else:
            self.expenses[category] = [amt]

        if prnt: print(f"The new total expense for {category} is {sum(self.expenses[category])}")
        return sum(self.expenses[category])

    def delete_expense(self, category, amt, prnt=True):
        """Will delete an expense name and amount (string, float) from a dictionary of expenses,
        append it, and will calculate and return the new total expense amount"""
        
        if amt not in self.expenses[category]:
            if prnt: print(f"Error: the expense of amount {amt} was not found in category {category}")
            return 0
        else:
             self.expenses[category].remove(amt)
             if prnt: print(f"The new total expense for {category} is {sum(self.expenses[category])}")
             return sum(self.expenses[category])


    def average_expense_by_category(self, category, prnt = True):
        """Calculates the average price for expenses by category for each
            month of the year"""
        
        if category not in self.expenses:
            if prnt: print("Category not found.")
            return 0
        else:
            avg = sum(self.expenses[category])/len(self.expenses[category])
            if prnt: print(f"The average expense for {category} per month is {avg}")
            return avg

    def total_expenses(self, prnt=True):
        """Calculates the overall amount spent monthly, regardless of category"""
        s = 0
        for category, expenses in self.expenses.items():
            s += sum(expenses)
        if prnt: print(f"Your total expenses for the month is {s}")
        return s


    def expense_by_category(self, category, prnt=True):
        """Calculates how much money the user spends on each category on a monthly basis"""
        if category not in self.expenses:
            if prnt: print("Category not found")
        else:
            if prnt: print(sum(self.expenses[category]))
        return sum(self.expenses[category])


    def expense_projection(self, num_of_months = -1, prnt=True):
        """Projects expenses for the upcoming months"""
        monthly_expenses = sum([sum(expenses) for expenses in self.expenses.values()])

        if num_of_months == -1:
            num_of_months = int(input("Please enter the number of months you would like to project your expenses for: "))
        
        projected_expenses = monthly_expenses * num_of_months
        if prnt: print(f"Your projected expenses for the next {num_of_months} months is {projected_expenses}")
        return projected_expenses


    def set_savings(self, prnt=True):
        """"""
        total_expenses = self.total_expenses(prnt=prnt)
        savings = self.income - total_expenses
        if prnt: print(f"You are expected to have {savings:.2f} leftover at the end")
        return savings

def main():
    """Main function of the program"""
    
    Continue = True

    print("Welcome to the Expense Tracker!")

    while Continue:
        income = input("Please enter your monthly income: ")
        if income.isnumeric():
            Continue = False
        else:
            print("Please enter a numeric value.")
        
    tracker = ExpenseTracker(float(income))

    Continue = True
    while Continue:
        
        print("Please select an option from the menu below:")
        print("1. Add an expense")
        print("2. Delete an expense")
        print("3. Calculate yearly tax")
        print("4. Calculate average expense by category")
        print("5. Calculate total expenses")
        print("6. Calculate expenses by category")
        print("7. Expense Projection")
        print("8. Set Savings")
        print("9. Exit")
        option = input("Please enter your selection: ")
        if option == "1":
            name = input("Please Enter a category: ")
            amount = input("Please enter the amount of the expense: ")
            tracker.add_expense(name, float(amount))
        elif option == "2":
            category = input("Please enter your category: ")
            amt = input("Please enter the amount of the expense: ")
            tracker.delete_expense(category, float(amt))
        elif option == "3":
            tax_calculation(tracker)
        elif option == "4":
            category = input("Please enter a category: ")
            tracker.average_expense_by_category(category)
        elif option == "5":
            tracker.total_expenses()
        elif option == "6":
            category = input("Please enter your category: ")
            tracker.expense_by_category(category)
        elif option == "7":
            tracker.expense_projection()
        elif option == "8":
            tracker.set_savings()
        elif option == "9":
            Continue = False
            print("Thank you for using the Expense Tracker!")
        else:
            print("Invalid option, please try again.")
if __name__ == "__main__":
    main()
