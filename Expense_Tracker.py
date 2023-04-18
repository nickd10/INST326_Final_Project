def add_expense():
    pass

def delete_expense():
    pass

def tax_calculation():
    """Calculates the yearly tax expense of the user based on their
        income and the tax rate of their country."""
    pass

def average_expense():
    """Calculates the average price for expenses by category for each
        month of the year"""
    pass

def total_expenses():
    pass

def expense_by_category():
    pass

def expense_per_month():
    pass

def pay_credit():
    pass

def main():
    """Main function of the program"""
    Continue = True
    while Continue:
        print("Welcome to the Expense Tracker!")
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
            add_expense()
        elif option == "2":
            delete_expense()
        elif option == "3":
            tax_calculation()
        elif option == "4":
            average_expense()
        elif option == "5":
            total_expenses()
        elif option == "6":
            expense_by_category()
        elif option == "7":
            expense_per_month()
        elif option == "8":
            pay_credit()
        elif option == "9":
            Continue = False
        else:
            print("Invalid option, please try again.")
