import unittest
from Expense_Tracker import ExpenseTracker
from Tax_Calculation import tax_calculation

class TestStringMethods(unittest.TestCase):
    
    def test_add_expense(self):
        """
        Tests adding expenses and making sure the total expense
        per category is calculated correctly
        """
        expense_tracker = ExpenseTracker()
        
        expense_tracker.add_expense("Groceries", 50.0, prnt=False)
        expense_tracker.add_expense("Groceries", 30.0, prnt=False)
        expense_tracker.add_expense("Groceries", 20.0, prnt=False)
        
        total_expense = expense_tracker.add_expense("Groceries", 25.0, prnt=False)
        self.assertEqual(total_expense, 125.0)
        
        expense_tracker.add_expense("Entertainment", 10.0, prnt=False)
        expense_tracker.add_expense("Entertainment", 15.0, prnt=False)
        
        total_expense = expense_tracker.add_expense("Entertainment", 20.0, prnt=False)
        self.assertEqual(total_expense, 45.0)
   
    def test_delete_expense(self): 
        """
        Tests deleting expenses and calculating expenses by category
        """
        expense_tracker = ExpenseTracker()
        expense_tracker.add_expense("Groceries", 50.0, prnt=False)
        expense_tracker.add_expense("Groceries", 50.0, prnt=False)
        expense_tracker.delete_expense("Groceries", 50.0, prnt=False)
        
        total_expense = expense_tracker.expense_by_category("Groceries", prnt=False)
        self.assertEqual(total_expense, 50.0)
        
        expense_tracker.add_expense("Entertainment", 15.0, prnt=False)
        expense_tracker.delete_expense("Entertainment", 15.0, prnt=False)
        
        total_expense = expense_tracker.expense_by_category("Entertainment", prnt=False)
        self.assertEqual(total_expense, 0)
        
    def test_total_expenses(self):
        """
        Tests adding expenses and calculating the total expenses
        (given multiple categories)
        """
        expense_tracker = ExpenseTracker()
  
        expense_tracker.add_expense("Groceries",50, prnt=False)
        expense_tracker.add_expense("Utilities",60, prnt=False)
        expense_tracker.add_expense("Rent",100, prnt=False)
        
        result = expense_tracker.total_expenses(prnt=False)

        self.assertEqual(result, 210)

        expense_tracker.delete_expense("Groceries",50, prnt=False)

        result = expense_tracker.total_expenses(prnt=False)
        self.assertEqual(result, 160)

    def test_expense_projection(self):
        """
        Tests calculating projections of expenses for future months
        """
        expense_tracker = ExpenseTracker()
        expense_tracker.add_expense("Groceries",50, prnt=False)
        expense_tracker.add_expense("Utilities",60, prnt=False)
        expense_tracker.add_expense("Rent",100, prnt=False)

        result = expense_tracker.expense_projection(3, prnt=False)
        self.assertEqual(result, 630)

    def test_savings(self):
        """
        Tests calculating monthly savings
        """
        expense_tracker = ExpenseTracker(income=500)
        expense_tracker.add_expense("Groceries",50, prnt=False)
        expense_tracker.add_expense("Utilities",60, prnt=False)
        expense_tracker.add_expense("Rent",100, prnt=False)
        
        result = expense_tracker.set_savings(prnt=False)

        self.assertEqual(result, 290)



if __name__ == '__main__':
        unittest.main()
        
