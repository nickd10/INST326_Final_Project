class Expense:
    def __init__(self, category, amount):
        self.category = category
        self.amount = amount
        self.list_of_items = {}
        self.input = input("Please select an option from the menu below: ")

    def __str__(self):
        return
    
    
def add_expense():
    """Will add an expense name and amount to a dictionary of expenses, 
    append it, and will calculate and return the new total expense amount"""
    pass

def delete_expense():
    """Will delete an expense name and amount from a dictionary of expenses,
    append it, and will calculate and return the new total expense amount"""
    pass

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
def average_expense_by_category(expenses):
    """Calculates the average price for expenses by category for each
        month of the year"""
    pass

def total_expenses():
    """Calculates the overall amount spent monthly, regardless of category"""
    pass

def expense_by_category():
    """Calculates how much money the user spends on each category on a monthly basis"""
    pass

def expense_per_month():
    pass

def pay_credit():
    pass

def main():
    """Main function of the program"""
    category = input("Please enter the category: ")
    amount = input("Please enter the amount: ")
    expense = Expense(category, amount)
    print(expense)
    # Continue = True

    # while Continue:
    #     print("Welcome to the Expense Tracker!")
    #     income = input("Please enter your monthly income: ")
    #     print("Please select an option from the menu below:")
    #     print("1. Add an expense")
    #     print("2. Delete an expense")
    #     print("3. Calculate yearly tax")
    #     print("4. Calculate average expense by category")
    #     print("5. Calculate total expenses")
    #     print("6. Calculate expenses by category")
    #     print("7. Calculate expenses per month")
    #     print("8. Pay credit")
    #     print("9. Exit")
    #     option = input("Please enter your selection: ")
    #     if option == "1":
    #         add_expense()
    #     elif option == "2":
    #         delete_expense()
    #     elif option == "3":
    #         tax_calculation(income)
    #     elif option == "4":
    #         average_expense_by_category()
    #     elif option == "5":
    #         total_expenses()
    #     elif option == "6":
    #         expense_by_category()
    #     elif option == "7":
    #         expense_per_month()
    #     elif option == "8":
    #         pay_credit()
    #     elif option == "9":
    #         Continue = False
    #         print("Thank you for using the Expense Tracker!")
    #     else:
    #         print("Invalid option, please try again.")
if __name__ == "__main__":
    main()
