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