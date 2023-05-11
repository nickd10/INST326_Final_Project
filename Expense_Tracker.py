class ExpenseTracker:
    def __init__(self, income):
        self.expenses = {}
        self.income = income

    def add_expense(self, category, amt):
        """Will add an expense name and amount (string, float) to a dictionary of expenses, 
        append it, and will calculate and return the new total expense amount"""
        if category in self.expenses:
            self.expenses[category].append(amt)
        else:
            self.expenses[category] = [amt]

        print(f"The new total expense for {category} is {sum(self.expenses[category])}")
        return sum(self.expenses[category])

    def delete_expense(self, name):
        """Will delete an expense name and amount (string, float) from a dictionary of expenses,
        append it, and will calculate and return the new total expense amount"""
        self.expenses.pop(name)
        total_expense = sum(int(self.expenses.values()))
        return total_expense

    def tax_calculation(self):
        """Calculates the yearly tax expense of the user based on their
        income and the tax rate of their country.

        Returns:
            tax (int): The user's yearly tax expense"""
        salary = self.income * 12
        if salary < 11000:
            tax = 0.10 * salary
        elif 11000 < salary < 44725:
            tax = 0.12 * salary
        elif 44725 < salary < 95375:
            tax = 0.22 * salary
        elif 95375 < salary < 182100:
            tax = 0.24 * salary
        elif 182100 < salary < 231250:
            tax = 0.32 * salary
        elif 231250 < salary < 578125:
            tax = 0.35 * salary
        elif salary > 578125:
            tax = 0.37 * salary
        print("Your yearly tax expense is:", tax)
        return tax

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
        total = sum(int(self.expenses.values()))
        return total

    def expense_by_category(self, amount):
        """Calculates how much money the user spends on each category on a monthly basis"""
        expense_category = {}
        for expenses in self.expenses:
            for category in expense_category:
                expense_category[category] += amount
            else: 
                expense_category[category] = amount
            return expense_category
 

    def expense_projection(self):
        """Projects expenses for the upcoming months"""
        monthly_expenses = sum([sum(expenses) for expenses in self.expenses.values()]) / len(self.expenses)
        num_of_months = int(input("Please enter the number of months you would like to project your expenses for: "))
        projected_expenses = monthly_expenses * num_of_months
        print(f"Your projected expenses for the next {num_of_months} months is {projected_expenses}")


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
        print("7. Expense Projection")
        print("8. Set Savings")
        print("9. Exit")
        option = input("Please enter your selection: ")
        if option == "1":
            name = input("Please Enter a category: ")
            amount = input("Please enter the amount of the expense: ")
            tracker.add_expense(name, float(amount))
        elif option == "2":
            name = input("Please Enter the category to delete: ")
            tracker.delete_expense(name)
        elif option == "3":
            tracker.tax_calculation()
        elif option == "4":
            tracker.average_expense_by_category()
        elif option == "5":
            tracker.total_expenses()
        elif option == "6":
            tracker.expense_by_category()
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
