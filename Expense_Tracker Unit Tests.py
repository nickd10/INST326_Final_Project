import unittest
from Expense_Tracker import ExpenseTracker
from Tax_Calculation import tax_calculation

class TestStringMethods(unittest.TestCase):
    
    def test_add_expense(self):
        self.expense_tracker.add_expense("Groceries", 50.0)
        self.expense_tracker.add_expense("Groceries", 30.0)
        self.expense_tracker.add_expense("Groceries", 20.0)
        
        total_expense = self.expense_tracker.add_expense("Groceries", 25.0)
        self.assertEqual(total_expense, 125.0)
        
        self.expense_tracker.add_expense("Entertainment", 10.0)
        self.expense_tracker.add_expense("Entertainment", 15.0)
        
        total_expense = self.expense_tracker.add_expense("Entertainment", 20.0)
        self.assertEqual(total_expense, 45.0)
   
    def test_delete_expense(self): 
        self.expense_tracker.delete_expense("Groceries", 30.0)
        
        total_expense = self.expense_tracker.get_total_expense("Groceries")
        self.assertEqual(total_expense, 70.0)
        
        self.expense_tracker.delete_expense("Entertainment", 15.0)
        
        total_expense = self.expense_tracker.get_total_expense("Entertainment")
        self.assertEqual(total_expense, 30.0)

        
if __name__ == '__main__':
        unittest.main()
        