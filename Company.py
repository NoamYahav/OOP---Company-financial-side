class Company:
    _comparison_type = "net value"

    def __init__(self, name, stocks_num, stock_price, comp_type):
        # Validate and initialize attributes
        if not self._validate_name(name):
            raise ValueError("Invalid name")
        self.name = name

        if not self._validate_stocks_num(stocks_num):
            raise ValueError("Invalid number of stocks")
        self.stocks_num = stocks_num

        if not self._validate_stock_price(stock_price):
            raise ValueError("Invalid stock price")
        self.stock_price = stock_price

        if not self._validate_comp_type(comp_type):
            raise ValueError("Invalid company type")
        self.comp_type = comp_type

    def net_worth(self):
        return self.stocks_num * self.stock_price

    def set_name(self, name):
        # Set name if valid
        if self._validate_name(name):
            self.name = name
            return True
        return False

    def set_stocks_num(self, stocks_num):
        # Set stocks number if valid
        if self._validate_stocks_num(stocks_num):
            m = self.net_worth()
            if m == 0:
                self.stocks_num = stocks_num
            else:
                self.stock_price = m / stocks_num
                self.stocks_num = stocks_num
            return True
        return False

    def set_stock_price(self, stock_price):
        # Set stock price if valid
        if self._validate_stock_price(stock_price):
            m = self.net_worth()
            self.stocks_num = int(m / stock_price)
            self.stock_price = stock_price
            return True
        return False

    def set_comp_type(self, comp_type):
        # Set company type if valid
        if self._validate_comp_type(comp_type):
            self.comp_type = comp_type
            return True
        return False

    def update_net_worth(self, net_worth):
        # Update net worth by changing stock price only if valid
        if not self._validate_net_worth(net_worth):
            return False
        self.stock_price = net_worth / self.stocks_num
        return True

    def add_stocks(self, number):
        # Add stocks if valid
        if not self._validate_add_stocks(number):
            return False
        self.stocks_num += number
        return True

    def comparison_value(self):
        # Get comparison value based on comparison type (helping function)
        if self._comparison_type == "net value":
            return self.net_worth()
        if self._comparison_type == "stock num":
            return self.stocks_num
        if self._comparison_type == "stock price":
            return self.stock_price

# -----------------------      Validate Methods    -----------------------------
    def _validate_name(self, name):
        return (
            isinstance(name, str)
            and name[0].isupper()
            and len(name) >= 2
            and all(x.isalpha() or x.isspace() for x in name)
            and "  " not in name
        )

    def _validate_stocks_num(self, stocks_num):
        return isinstance(stocks_num, int) and stocks_num > 0

    def _validate_stock_price(self, stock_price):
        return isinstance(stock_price, (float, int)) and stock_price > 0

    def _validate_comp_type(self, comp_type):
        return (
            isinstance(comp_type, str)
            and comp_type[0].isupper()
            and len(comp_type) >= 2
            and "  " not in comp_type
        )

    def _validate_net_worth(self, net_worth):
        return isinstance(net_worth, (float, int)) and net_worth > 0

    def _validate_add_stocks(self, number):
        return isinstance(number, int) and number + self.stocks_num > 0

    @classmethod
    def _validate_comparison_type(cls, comparison_type):
        return comparison_type in ["net value", "stock num", "stock price"]

# -----------------------      Class Methods    -----------------------------

    @classmethod
    def change_comparison_type(cls, comparison_type):
        if cls._validate_comparison_type(comparison_type):
            cls._comparison_type = comparison_type
            return True
        return False

    def __str__(self):
        result = '(' + self.name + ', ' + str(self.stocks_num) + ' stocks, Price: ' + str(
            self.stock_price) + ', ' + self.comp_type + ', Net Worth: ' + str(self.net_worth()) + ')'
        return result

    def __repr__(self):
        return self.__str__()
## All of the equilty function using the helping function comparison_value.
    def __lt__(self, other):
        if isinstance(other, Company):
            return self.comparison_value() < other.comparison_value()
        return False

    def __gt__(self, other):
        if isinstance(other, Company):
            return self.comparison_value() > other.comparison_value()
        return False

    def __eq__(self, other):
        if isinstance(other, Company):
            return self.comparison_value() == other.comparison_value()
        return False

    def __ge__(self, other):
        if isinstance(other, Company):
            return self.comparison_value() >= other.comparison_value()
        return False

    def __le__(self, other):
        if isinstance(other, Company):
            return self.comparison_value() <= other.comparison_value()
        return False

    def __ne__(self, other):
        if isinstance(other, Company):
            return self.comparison_value() != other.comparison_value()
        return False

    def __add__(self, other):
        stocks = self.stocks_num + other.stocks_num
        value = self.net_worth() + other.net_worth()
        price = value/stocks
        return Company(self.name,stocks,price,self.comp_type)