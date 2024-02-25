import copy

from Company import Company


class CompanyNode(Company):
    _comparison_type = "net value"
    def __init__(self, name, stocks_num, stock_price, comp_type):
        Company.__init__(self,name,stocks_num,stock_price,comp_type) #Inherites company instance
        # Define children, parent as protected attributes (Name mangaling)
        self.__children = []
        self.__parent = None

    def get_parent(self):
        return self.__parent

    def get_children(self):
        return self.__children

    def add_child(self, child):
        if not isinstance(child, CompanyNode):
            return False
        if self >= child:
            self.__children.append(child)
            child.__parent = self
            return True
        return False

    def total_net_worth(self):
        #Calculte net worth including children - Recursive
        total_sum = self.net_worth()
        for child in self.get_children():
            total_sum += child.total_net_worth()
        return total_sum

    def set_stock_price(self, stock_price):
        m = self.net_worth()
        if not isinstance(stock_price, (float, int)) or stock_price < 0:
            return False
        current_company = copy.deepcopy(self)
        # Making a copy of self, and checking the companynode applies before updaiting self.
        current_company.stocks_num = int(m/stock_price)
        current_company.stock_price = stock_price
        if current_company.test_node_order_validity():
            self.stocks_num = int(m / stock_price)
            self.stock_price = stock_price
            return True
        return False

    def set_stocks_num(self, stocks_num):
        if not isinstance(stocks_num, (int)) or stocks_num < 0:
            return False
        m = self.net_worth()
        if m == 0:
            return True
        current_company = copy.deepcopy(self)
        #Making a copy of self, and checking the companynode applies before updaiting self.
        current_company.stock_price = m/stocks_num
        if current_company.test_node_order_validity():
            self.stock_price = m / stocks_num
            self.stocks_num = stocks_num
            return True
        return False

    def update_net_worth(self, net_worth):
        if not isinstance(net_worth, (float, int)) or net_worth <= 0:
            return False
        current_company = copy.deepcopy(self)
        # Making a copy of self to ensure node order validity
        current_company.stock_price = net_worth / current_company.stocks_num
        if current_company.test_node_order_validity():
            self.stock_price = net_worth / self.stocks_num
            return True
        return False

    def add_stocks(self, number):
        if not isinstance(number, int) or number + self.stocks_num <= 0:
            return False
        current_company = copy.deepcopy(self)  # Making a copy of self to ensure node order validity
        current_company.stocks_num += number
        if current_company.test_node_order_validity():
            self.stocks_num += number
            return True
        return False

    def test_node_order_validity(self):
        lst_of_children = self.get_children()
        for x in lst_of_children:
            #Checking all self children follow companynode rule
            if self < x:
                return False
        main_lst = []
        temp_lst = [self]
        while temp_lst != []:
            #Building a list contain all of self ancestors
            if temp_lst[0].get_parent() == None:
                break
            main_lst.append(temp_lst[0].get_parent())
            temp_lst.append(temp_lst[0].get_parent())
            temp_lst.pop(0)
        for y in main_lst:#Checking self ancestor follow company node rule
            if self > y:
                return False
        return True

    def is_ancestor(self, other):
        main_lst = []
        temp_lst = [other]
        while temp_lst != []: #Building a list of parents, untill hitting None.
            if temp_lst[0].get_parent() == None:
                break
            main_lst.append(temp_lst[0].get_parent())
            temp_lst.append(temp_lst[0].get_parent())
            temp_lst.pop(0)
        for parent in main_lst:
            if parent == self:
                return True
        return False

    def comparison_value(self): #Helping function connecting between the comparison_type string to math function.
        if self._comparison_type == "net value":
            return self.net_worth()
        if self._comparison_type == "stock num":
            return self.stocks_num
        if self._comparison_type == "stock price":
            return self.stock_price
        if self._comparison_type == "total sum":
            return self.total_net_worth()

    def is_leaf(self):
        if len(self) == 0:
            return True
        return False

    # -----------------------      Class Methods     -----------------------------
    @classmethod
    def change_comparison_type(cls,comparison_type):
        if comparison_type != "net value" and comparison_type != "stock num" and comparison_type != "stock price" and comparison_type != "total sum":
            return False
        cls._comparison_type = comparison_type

    def __len__(self):
        return len(self.__children)


    def __repr__(self):
        #Repr the company as asked : (Ancestor Comp, [Children, [Grandchildren e.g]]])
        children = self.__children
        lst = []
        for child in children:
            lst.append(child)
        result = '[{}, {}]'.format(self.__str__(),lst) #As defined in Company class
        return result

    def __add__(self, other):
        #Merging other Company to Self including other childrens
        if other.is_ancestor(self):
            raise ValueError
        if self.is_ancestor(other):
            m = other.__parent
            m.__children.remove(other)
        new_node = copy.deepcopy(self)
        new_node.stocks_num = self.stocks_num + other.stocks_num
        value = self.net_worth() + other.net_worth()
        new_node.stock_price = value/new_node.stocks_num
        for x in other.__children:
            new_node.__children.append(x)
        if new_node.test_node_order_validity():
            other.__children = []
            other.__parent = None
            return new_node
        else:
            raise ValueError

    def __lt__(self, other):
        if not isinstance(other, CompanyNode):
            return False
        return self.comparison_value() < other.comparison_value()

    def __gt__(self, other):
        if not isinstance(other, CompanyNode):
            return False
        return self.comparison_value() > other.comparison_value()

    def __eq__(self, other):
        if not isinstance(other, CompanyNode):
            return False
        return self.comparison_value() == other.comparison_value()

    def __ge__(self, other):
        if not isinstance(other, CompanyNode):
            return False
        return self.comparison_value() >= other.comparison_value()

    def __le__(self, other):
        if not isinstance(other, CompanyNode):
            return False
        return self.comparison_value() <= other.comparison_value()

    def __ne__(self, other):
        if not isinstance(other, CompanyNode):
            return False
        return self.comparison_value() != other.comparison_value()