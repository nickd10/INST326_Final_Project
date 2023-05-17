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
        
    def test_total_expenses(self):
        expenses = {
            'groceries': [50, 30, 20],
            'utilities': [60],
            'rent': [900]
        }
        expected_total = 1060

        result = total_expenses(expenses, printresult=False)

        self.assertEqual(result, expected_total)

    def test_expense_by_category(self):
        self.assertEqual(self.expense_tracker.expense_by_category("Groceries"), 125)
        
        self.assertEqual(self.expense_tracker.expense_by_category("Leisure"), None)
    def test_set_savings(self):
         self.expense_tracker.add_expense("Groceries", 50.0)
         self.expense_tracker.add_expense("Entertainment", 30.0)
         self.expense_tracker.add_expense("Utilities", 20.0)


         self.expense_tracker.income = 200.0
         expected_savings = self.expense_tracker.income - self.expense_tracker.total_expenses()
         self.assertAlmostEqual(self.expense_tracker.set_savings(), expected_savings, places=2)
         


if __name__ == '__main__':
        unittest.main()
        
