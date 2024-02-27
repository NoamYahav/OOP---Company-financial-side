import unittest
from Company import Company

class TestCompany(unittest.TestCase):
    def setUp(self):
        # Create a Company object with default values for testing
        self.company = Company("Company A", 100, 10.0, "Type A")

    def test_initialization(self):
        # Test valid initialization
        self.assertEqual(self.company.name, "Company A")
        self.assertEqual(self.company.stocks_num, 100)
        self.assertEqual(self.company.stock_price, 10.0)
        self.assertEqual(self.company.comp_type, "Type A")

        # Test invalid initialization scenarios
        with self.assertRaises(ValueError):
            Company("company B", 100, 10.0, "Type B")  # Name starts with lowercase letter

        with self.assertRaises(ValueError):
            Company("Company B-", 100, 10.0, "Type B")  # Name contains non-alphabetic characters

        with self.assertRaises(ValueError):
            Company("Company C", -100, 10.0, "Type C")  # Negative stocks number

        with self.assertRaises(ValueError):
            Company("Company D", 100, -10.0, "Type D")  # Negative stock price

    def test_net_worth(self):
        # Test net worth calculation
        self.assertEqual(self.company.net_worth(), 1000.0)

    def test_set_name(self):
        # Test valid name change
        self.assertTrue(self.company.set_name("New Company Name"))
        self.assertEqual(self.company.name, "New Company Name")

        # Test invalid name change
        self.assertFalse(self.company.set_name("invalid company"))

    def test_set_stocks_num(self):
        # Test setting stocks number
        self.assertTrue(self.company.set_stocks_num(150))
        self.assertEqual(self.company.stocks_num, 150)
        self.assertEqual(self.company.stock_price, 1000.0 / 150)  # Check if stock price is adjusted

        # Test invalid stocks number
        self.assertFalse(self.company.set_stocks_num(-50))
        self.assertEqual(self.company.stocks_num, 150)  # Stocks number should remain unchanged

    def test_set_stock_price(self):
        # Test setting stock price
        self.assertTrue(self.company.set_stock_price(20.0))
        self.assertEqual(self.company.stock_price, 20.0)
        self.assertEqual(self.company.stocks_num, 50)  # Check if stocks number is adjusted

        # Test invalid stock price
        self.assertFalse(self.company.set_stock_price(-5.0))
        self.assertEqual(self.company.stock_price, 20.0)  # Stock price should remain unchanged

    def test_set_comp_type(self):
        # Test setting company type
        self.assertTrue(self.company.set_comp_type("New Type"))
        self.assertEqual(self.company.comp_type, "New Type")

        # Test invalid company type
        self.assertFalse(self.company.set_comp_type("invalid type"))
        self.assertEqual(self.company.comp_type, "New Type")  # Company type should remain unchanged

    def test_update_net_worth(self):
        # Test updating net worth
        self.assertTrue(self.company.update_net_worth(1500.0))
        self.assertEqual(self.company.stock_price, 15.0)  # Check if stock price is adjusted

        # Test invalid net worth update
        self.assertFalse(self.company.update_net_worth(-100.0))
        self.assertEqual(self.company.stock_price, 15.0)  # Stock price should remain unchanged

    def test_add_stocks(self):
        # Test adding stocks
        self.assertTrue(self.company.add_stocks(50))
        self.assertEqual(self.company.stocks_num, 150)  # Check if stocks number is increased

        # Test invalid adding of stocks
        self.assertFalse(self.company.add_stocks(-10000000))
        self.assertEqual(self.company.stocks_num, 150)  # Stocks number should be 100 again


    def test_change_comparison_type(self):
        # Test changing comparison type
        self.assertTrue(Company.change_comparison_type("stock num"))
        self.assertEqual(Company._comparison_type, "stock num")

        # Test invalid comparison type change
        self.assertFalse(Company.change_comparison_type("invalid type"))
        self.assertEqual(Company._comparison_type, "stock num")  # Comparison type should remain unchanged

    def test_comparison_methods(self):
        # Test comparison methods
        company2 = Company("Company B", 200, 5.0, "Type B")
        Company.change_comparison_type("stock num")
        self.assertTrue(self.company < company2)
        self.assertFalse(self.company > company2)
        Company.change_comparison_type("stock price")
        self.assertTrue(self.company > company2)
        self.assertFalse(self.company < company2)
        Company.change_comparison_type("net value")
        self.assertTrue(self.company == company2)


    def test_str_representation(self):
        # Test string representation of Company object
        self.assertEqual(str(self.company), "(Company A, 100 stocks, Price: 10.0, Type A, Net Worth: 1000.0)")

    def test_repr_representation(self):
        # Test representation of Company object
        self.assertEqual(repr(self.company), "(Company A, 100 stocks, Price: 10.0, Type A, Net Worth: 1000.0)")

    def test_add_method(self):
        # Test "+" method represtning merging company B to A
        company2 = Company("Company B", 200, 15.0, "Type B")
        combined_company = self.company + company2

        # Check if the combined Company object has the correct values
        self.assertEqual(combined_company.name, "Company A")
        self.assertEqual(combined_company.stocks_num, 300)  # 100 + 200
        self.assertEqual(combined_company.stock_price, 40/3)  # (1000.0 + 3000.0) / 300
        self.assertEqual(combined_company.comp_type, "Type A")
        self.assertEqual(combined_company.net_worth(), 4000.0)  # 1000.0 + 3000.0

if __name__ == '__main__':
    unittest.main()
