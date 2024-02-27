import copy

from Company import Company


class CompanyNode(Company):
    _comparison_type = "net value"

    def __init__(self, name, stocks_num, stock_price, comp_type):
        Company.__init__(self, name, stocks_num, stock_price, comp_type)
        self.__children = []
        self.__parent = None

    def get_parent(self):
        return self.__parent

    def get_children(self):
        return self.__children

    def add_child(self, child):
        if not isinstance(child, CompanyNode) or self < child:
            return False

        self.__children.append(child)
        child.__parent = self
        return True

    # Calculate net worth including children - Recursive
    def total_net_worth(self):
        total_sum = self.net_worth()
        for child in self.get_children():
            total_sum += child.total_net_worth()
        return total_sum

    def set_stock_price(self, stock_price):
        if not isinstance(stock_price, (float, int)) or stock_price < 0:
            return False

        net_worth = self.net_worth()
        current_company = copy.deepcopy(self)
        current_company.stocks_num = int(net_worth / stock_price)
        current_company.stock_price = stock_price
        return self.set_company_stock_values(current_company, current_company.stocks_num)

    def set_stocks_num(self, stocks_num):
        if not isinstance(stocks_num, (int)) or stocks_num < 0:
            return False

        net_worth = self.net_worth()
        if net_worth == 0:
            return True

        current_company = copy.deepcopy(self)
        current_company.stock_price = net_worth / stocks_num
        return self.set_company_stock_values(current_company, stocks_num)

    def set_company_stock_values(self, current_company, stocks_num):
        if not current_company.test_node_order_validity():
            return False

        self.stock_price = current_company.stock_price
        self.stocks_num = stocks_num
        return True

    def update_net_worth(self, net_worth):
        if not isinstance(net_worth, (float, int)) or net_worth <= 0:
            return False

        current_company = copy.deepcopy(self)
        current_company.stock_price = net_worth / current_company.stocks_num
        if current_company.test_node_order_validity():
            self.stock_price = net_worth / self.stocks_num
            return True
        return False

    def add_stocks(self, number):
        if not isinstance(number, int) or number + self.stocks_num <= 0:
            return False

        current_company = copy.deepcopy(self)
        current_company.stocks_num += number
        if current_company.test_node_order_validity():
            self.stocks_num += number
            return True
        return False

    def test_node_order_validity(self):
        list_of_children = self.get_children()
        for children in list_of_children:
            # Checking all self children follow companynode rule
            if self < children:
                return False

        main_lst = self.get_parents_companies(self)
        for company in main_lst:  # Checking self ancestor follow company node rule
            if self > company:
                return False
        return True

    def is_ancestor(self, other):
        main_lst = self.get_parents_companies(other)
        for parent in main_lst:
            if parent == self:
                return True
        return False

    def get_parents_companies(self, base_company):
        main_lst = []
        temp_lst = [base_company]
        while temp_lst != []:  # Building a list of parents, untill hitting None.
            if temp_lst[0].get_parent() == None:
                break
            main_lst.append(temp_lst[0].get_parent())
            temp_lst.append(temp_lst[0].get_parent())
            temp_lst.pop(0)

        return main_lst

    def is_leaf(self):
        return len(self) == 0

    # -----------------------      Class Methods     -----------------------------

    @classmethod
    def change_comparison_type(cls, comparison_type):
        if comparison_type in ["net value", "stock num", "stock price", "total sum"]:
            cls._comparison_type = comparison_type

    def __len__(self):
        return len(self.__children)

    # Repr the company as asked : (Ancestor Comp, [Children, [Grandchildren e.g]]])
    def __repr__(self):
        children = self.__children
        result = '[{}, {}]'.format(self.__str__(), children)  # As defined in Company class
        return result

    # Merging other Company to Self including other childrens
    def __add__(self, other):
        if other.is_ancestor(self):
            raise ValueError

        if self.is_ancestor(other):
            other.__parent.__children.remove(other)

        new_node = copy.deepcopy(self)
        new_node.stocks_num = self.stocks_num + other.stocks_num
        value = self.net_worth() + other.net_worth()
        new_node.stock_price = value / new_node.stocks_num

        for child in other.__children:
            new_node.__children.append(child)

        if not new_node.test_node_order_validity():
            raise ValueError

        other.__children = []
        other.__parent = None
        return new_node

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