class ExpenseTracker:
    def __init__(self, income):
        self.expenses = {}
        self.income = income

    
        
    def add_expense(self, name, amount):
        """Will add an expense name and amount (string, float) to a dictionary of expenses, 
        append it, and will calculate and return the new total expense amount"""
        self.expenses[name] = amount
        total_expense = sum(self.expenses.values())
        return total_expense

    def delete_expense(self, name):
        """Will delete an expense name and amount (string, float) from a dictionary of expenses,
        append it, and will calculate and return the new total expense amount"""
        self.expenses.pop(name)
        total_expense = sum(self.expenses.values())
        return total_expense

    def tax_calculation(income):
        """Calculates the yearly tax expense of the user based on their
            income and the tax rate of their country.
            
            Args:
                income (int): The user's monthly income
                
            Returns:
                tax (int): The user's yearly tax expense"""
        salary = (int(income) * 12)
        if salary < 11000:
            tax = (.10 * salary)
        elif 11000 < salary < 44725:
            tax = (.12 * salary)
        elif 44725 < salary < 95375:
            tax = (.22 * salary)
        elif 95375 < salary < 182100:
            tax = (.24 * salary)
        elif 182100 < salary < 231250:
            tax = (.32 * salary)
        elif 231250 < salary < 578125:
            tax = (.35 * salary)
        elif salary > 578125:
            tax = (.37 * salary)
        print("Your yearly tax expense is: ", tax)
    def average_expense_by_category(self, category, prnt = True):
        """Calculates the average price for expenses by category for each
            month of the year"""
        
        if category not in self.expenses:
            print("Category not found.")
            return 0
        else:
            avg = sum(self.expenses[category])/len(self.expenses[category])
            if prnt: print(f"The average expense for {category} per month is {avg}")
            return avg

    def total_expenses(self, expenses):
        """Calculates the overall amount spent monthly, regardless of category"""
        total = sum(self.expenses.values())
        return total

    def expense_by_category():
        """Calculates how much money the user spends on each category on a monthly basis"""
        expense_category = {}
        for expenses in self.expenses():
            for category in expense_category:
                expense_category[category] += amount
            else: 
                expense_category[category] = amount
         return expense_category
 

    def expense_projection():
        """Gives the user a prediction of how much they are expected to spend over a certain period of time"""
        pass

    def set_savings():
        pass

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
        print("7. Calculate expenses per month")
        print("8. Pay credit")
        print("9. Exit")
        option = input("Please enter your selection: ")
        if option == "1":
            tracker.add_expense()
        elif option == "2":
            tracker.delete_expense()
        elif option == "3":
            tracker.tax_calculation(income)
        elif option == "4":
            tracker.average_expense_by_category()
        elif option == "5":
            tracker.total_expenses()
        elif option == "6":
            tracker.expense_by_category()
        elif option == "7":
            tracker.expense_per_month()
        elif option == "8":
            pass
        elif option == "9":
            Continue = False
            print("Thank you for using the Expense Tracker!")
        else:
            print("Invalid option, please try again.")
if __name__ == "__main__":
    main()
