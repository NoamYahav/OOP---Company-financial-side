import unittest
from Company import Company
from CompanyNode import CompanyNode

class TestCompanyNode(unittest.TestCase):
    def setUp(self):
        # Create CompanyNode objects for testing
        self.company1 = CompanyNode("Company A", 300, 20.0, "Type A")
        self.company2 = CompanyNode("Company B", 200, 15.0, "Type B")
        self.company3 = CompanyNode("Company C", 50, 10.0, "Type C")

    def test_initialization(self):
        # Ensure CompanyNode objects inherit from Company class
        self.assertTrue(isinstance(self.company1, Company))

    def test_add_child(self):
        # Test adding child companies to a parent company
        self.assertTrue(self.company1.add_child(self.company2))
        self.assertIn(self.company2, self.company1.get_children())

        # Test invalid addition of non-CompanyNode object as a child
        invalid_child = CompanyNode("Invalid Company", 500, 50, "Invalid Type")
        self.assertFalse(self.company1.add_child(invalid_child))

    def test_total_net_worth(self):
        # Test calculation of total net worth for a company and its children
        self.company1.add_child(self.company2)
        expected_total_net_worth = self.company1.net_worth() + self.company2.net_worth()
        self.assertEqual(self.company1.total_net_worth(), expected_total_net_worth)

    def test_set_stock_price(self):
        # Test setting stock price
        new_stock_price = 20.0
        self.assertTrue(self.company1.set_stock_price(new_stock_price))
        self.assertEqual(self.company1.stock_price, new_stock_price)

        # Test invalid stock price
        invalid_stock_price = -5.0
        self.assertFalse(self.company1.set_stock_price(invalid_stock_price))

    def test_set_stocks_num(self):
        # Test setting stocks number
        new_stocks_num = 150
        self.assertTrue(self.company1.set_stocks_num(new_stocks_num))
        self.assertEqual(self.company1.stocks_num, new_stocks_num)

        # Test invalid stocks number
        invalid_stocks_num = -50
        self.assertFalse(self.company1.set_stocks_num(invalid_stocks_num))

    def test_update_net_worth(self):
        # Test updating net worth
        new_net_worth = 2000.0
        self.assertTrue(self.company1.update_net_worth(new_net_worth))
        self.assertAlmostEqual(self.company1.net_worth(), new_net_worth)

        # Test invalid net worth
        invalid_net_worth = -500.0
        self.assertFalse(self.company1.update_net_worth(invalid_net_worth))

    def test_add_stocks(self):
        # Test adding stocks to certain company
        added_stocks = 50
        self.assertTrue(self.company1.add_stocks(added_stocks))
        self.assertEqual(self.company1.stocks_num, 300 + added_stocks)

        # Test invalid addition of stocks
        invalid_stocks = -400
        self.assertFalse(self.company1.add_stocks(invalid_stocks))


    def test_is_ancestor(self):
        #Test that company ancestor define well (2 levels down)
        self.company1.add_child(self.company2)
        self.company2.add_child(self.company3)
        self.assertTrue(self.company1.is_ancestor(self.company3))
        self.assertFalse(self.company3.is_ancestor(self.company1))


    def test_node_repr(self):
        #Test that company ancestor define well (2 levels down)
        self.company1.add_child(self.company2)
        self.company2.add_child(self.company3)
        self.assertEqual(self.company3.__repr__(),('[(Company C, 50 stocks, Price: 10.0, Type C, Net Worth: 500.0), []]'))
        self.assertEqual(self.company1.__repr__(),('[(Company A, 300 stocks, Price: 20.0, Type A, Net Worth: 6000.0), [[(Company '
        'B, 200 stocks, Price: 15.0, Type B, Net Worth: 3000.0), [[(Company C, 50 '
        'stocks, Price: 10.0, Type C, Net Worth: 500.0), []]]]]]'))


    def test_node_add(self):
        #Test the adding func. cant add ancestor to children, keeping net value after adding.
        self.company2.add_child(self.company3)
        with self.assertRaises(ValueError):
            self.company3.__add__(self.company2)
        self.assertEqual(self.company1.__add__(self.company2).net_worth(),9000.0)



if __name__ == '__main__':
    unittest.main()