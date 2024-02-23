class Company:
    _comparison_type = "net value"

    def __init__(self, name, stocks_num, stock_price, comp_type):
        if type(name) != str or not (name[0].isupper()) or len(name) <2: #Varify name rules
            raise ValueError
        if not all(x.isalpha() or x.isspace() for x in name):#Varify name rules
            raise ValueError
        if "  " in name:#Varify name rules
            raise ValueError
        self.name = name
        if type(stocks_num) != int or stocks_num < 0: #Varify stocks num rules
            raise ValueError
        self.stocks_num = stocks_num
        if (type(stock_price) != float and type(stock_price) != int) or stock_price < 0: #Varify stock price rules
            raise ValueError
        self.stock_price = stock_price
        if type(comp_type) != str or not (comp_type[0].isupper()) or len(comp_type) <2:#Varify comp type rules
            raise ValueError
        if "  " in comp_type:
            raise ValueError
        self.comp_type = comp_type

    def net_worth(self):
        return self.stocks_num * self.stock_price

    def set_name(self, name): #First checking the rules apply, then update self.name.
        if type(name) != str or not (name[0].isupper()) or len(name) <2:
            return False
        if not all(x.isalpha() or x.isspace() for x in name):
            return False
        if "  " in name:
            return False
        self.name = name
        return True

    def set_stocks_num(self, stocks_num):#First checking the rules apply, then update self.stocks_num(keeping net worth the same).
        if type(stocks_num) != int or stocks_num < 0:
            return False
        m = self.net_worth()
        if m == 0:
            return True
        self.stock_price = m / stocks_num
        self.stocks_num = stocks_num
        return True

    def set_stock_price(self, stock_price):#First checking the rules apply, then update self.stock_price.
        m = self.net_worth()
        if (type(stock_price) != float and type(stock_price) != int) or stock_price < 0 or stock_price > m:
            return False
        self.stocks_num = int(m / stock_price)
        self.stock_price = stock_price
        return True

    def set_comp_type(self, comp_type): #First checking the rules apply, then update self.comp_type.
        if type(comp_type) != str or not (comp_type[0].isupper()) or len(comp_type) <2:
            return False
        if not all(x.isalpha() or x.isspace() for x in comp_type):
            return False
        if "  " in comp_type:
            return False
        self.comp_type = comp_type
        return True

    def update_net_worth(self, net_worth): #Updaiting net worth by changing stock price only.
        if (type(net_worth) != float and type(net_worth) != int) or net_worth <= 0:
            return False
        self.stock_price = net_worth / self.stocks_num
        return True

    def add_stocks(self, number):
        if type(number) != int:
            return False
        if number + self.stocks_num <= 0:  # checking the number of stocks bigger then 0
            return False
        self.stocks_num += number
        return True

    def comparison_value(self): #Helping fucntion to connect between comparison value string, to math action.
        if self._comparison_type == "net value":
            return self.net_worth()
        if self._comparison_type == "stock num":
            return self.stocks_num
        if self._comparison_type == "stock price":
            return self.stock_price


    @classmethod
    def change_comparison_type(cls, comparison_type):
        if comparison_type != "net value" and comparison_type != "stock num" and comparison_type != "stock price":
            return False
        cls._comparison_type = comparison_type
        return True

    def __str__(self):
        result = '(' + self.name + ', ' + str(self.stocks_num) + ' stocks, Price: ' + str(
            self.stock_price) + ', ' + self.comp_type + ', Net Worth: ' + str(self.net_worth()) + ')'
        return result

    def __repr__(self):
        return self.__str__()
## All of the equilty function using the helping function comparison_value.
    def __lt__(self, other):
        if type(other) != Company:
            return False
        if self.comparison_value() < other.comparison_value():
            return True
        else:
            return False

    def __gt__(self, other):
        if type(other) != Company:
            return False
        if self.comparison_value() > other.comparison_value():
            return True
        else:
            return False

    def __eq__(self, other):
        if type(other) != Company:
            return False
        if self.comparison_value() == other.comparison_value():
            return True
        else:
            return False

    def __ge__(self, other):
        if type(other) != Company:
            return False
        if self.comparison_value() >= other.comparison_value():
            return True
        else:
            return False

    def __le__(self, other):
        if type(other) != Company:
            return False
        if self.comparison_value() <= other.comparison_value():
            return True
        else:
            return False

    def __ne__(self, other):
        if type(other) != Company:
            return False
        if self.comparison_value() != other.comparison_value():
            return True
        else:
            return False

    def __add__(self, other):
        stocks = self.stocks_num + other.stocks_num
        value = self.net_worth() + other.net_worth()
        price = value/stocks
        return Company(self.name,stocks,price,self.comp_type)
