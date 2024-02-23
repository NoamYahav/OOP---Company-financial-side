import copy

from Company import Company


class CompanyNode(Company):
    _comparison_type = "net value"
    def __init__(self, name, stocks_num, stock_price, comp_type):
        Company.__init__(self,name,stocks_num,stock_price,comp_type) #Inherites company instance
        self.__children = []
        self.__parent = None

    def get_parent(self):
        return self.__parent

    def get_children(self):
        return self.__children

    def is_leaf(self):
        if len(self) == 0:
            return True
        return False

    def add_child(self, child):
        if type(child) != CompanyNode:
            return False
        if self >= child:
            self.__children.append(child)
            child.__parent = self
            return True
        return False

    def total_net_worth(self):
        #Creating a sum valued 0
        total_sum = 0
        #The main lst. here we gonna add all the companies to sum.
        lst = []
        lst.append(self)
        while len(lst) != 0:
            n = len(lst)
            #If this company has childrens
            while n > 0:
                #Add the first company on the list net value to sum, and delete it from the list.
                current_company = lst[0]
                lst.pop(0)
                total_sum += current_company.net_worth()
                #Add all current company children to the lst
                for i in range(len(current_company)):
                    lst.append(current_company.__children[i])
                n -= 1
        return total_sum

    def set_stock_price(self, stock_price):
        m = self.net_worth()
        if (type(stock_price) != float and type(stock_price) != int) or stock_price < 0 or stock_price > m:
            return False
        current_company = copy.deepcopy(self) #Making a copy of self, and checking the company nude applies before updaiting self.
        current_company.stocks_num = int(m/stock_price)
        current_company.stock_price = stock_price
        if current_company.test_node_order_validity():
            self.stocks_num = int(m / stock_price)
            self.stock_price = stock_price
            return True
        return False

    def set_stocks_num(self, stocks_num):
        if type(stocks_num) != int or stocks_num < 0:
            return False
        m = self.net_worth()
        if m == 0:
            return True
        current_company = copy.deepcopy(self)#Making a copy of self, and checking the company nude applies before updaiting self.
        current_company.stock_price = m/stocks_num
        if current_company.test_node_order_validity():
            self.stock_price = m / stocks_num
            self.stocks_num = stocks_num
            return True
        return False

    def update_net_worth(self, net_worth):
        if (type(net_worth) != float and type(net_worth) != int) or net_worth <= 0:
            return False
        current_company = copy.deepcopy(self)#Making a copy of self, and checking the company nude applies before updaiting self.
        current_company.stock_price = net_worth / current_company.stocks_num
        if current_company.test_node_order_validity():
            self.stock_price = net_worth / self.stocks_num
            return True
        return False

    def add_stocks(self, number):
        if type(number) != int:
            return False
        if number + self.stocks_num <= 0:  # checking the number of stocks bigger then 0
            return False
        current_company = copy.deepcopy(self)#Making a copy of self, and checking the company nude applies before updaiting self.
        current_company.stocks_num += number
        if current_company.test_node_order_validity():
            self.stocks_num += number
            return True
        return False

    def test_node_order_validity(self):
        lst_of_children = self.__children
        for x in lst_of_children:#Checking all self children follow company node rule
            if self < x:
                return False
        main_lst = []
        temp_lst = [self]
        while temp_lst != []:#Building a list contain all of self ancestors
            if temp_lst[0].__parent == None:
                break
            main_lst.append(temp_lst[0].__parent)
            temp_lst.append(temp_lst[0].__parent)
            temp_lst.pop(0)
        for y in main_lst:#Checking self ancestor follow company node rule
            if self > y:
                return False
        return True

    def is_ancestor(self, other):
        main_lst = []
        temp_lst = [other]
        while temp_lst != []: #Building a list of parents, untill hitting None.
            if temp_lst[0].__parent == None:
                break
            main_lst.append(temp_lst[0].__parent)
            temp_lst.append(temp_lst[0].__parent)
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

    def in_order_tree(self,res=[]): #Recursive function building the inorder traversel using companytree
        self.left = []
        self.right = []
        child_lst = self.get_children()
        if child_lst == []:
            res.append(self)
            for company in res:
                if self.get_parent() is company:
                    return res
            # res.append(self.get_parent())
            return res
        m = len(child_lst)
        if m % 2 == 0:
            for i in range(int(len(child_lst) / 2)):
                self.left.append(child_lst[i])
            for x in range(int(len(child_lst) / 2), len(child_lst)):
                self.right.append(child_lst[x])
        if m % 2 == 1:
            for i in range(int(len(child_lst) / 2) + 1):
                self.left.append(child_lst[i])
            for x in range(int(len(child_lst) / 2) + 1, len(child_lst)):
                self.right.append(child_lst[x])
        left_before_changes = copy.deepcopy(self.left)
        while len(self.left) != 0:
            x = self.left[0].in_order_tree()
            # if len(self.left) == 1:
            #     res.append(self.get_parent())
            self.left.pop(0)
        m = left_before_changes[0].get_parent()
        res.append(m)
        while len(self.right) != 0:
            m = self.right[0].in_order_tree()
            self.right.pop(0)
        return res



    @classmethod
    def change_comparison_type(cls,comparison_type):
        if comparison_type != "net value" and comparison_type != "stock num" and comparison_type != "stock price" and comparison_type != "total sum":
            return False
        cls._comparison_type = comparison_type

    def __len__(self):
        return len(self.__children)


    def __repr__(self):
        children = self.__children
        lst = []
        for child in children:
            lst.append(child)
        result = '[{}, {}]'.format(self.__str__(),lst)
        return result

    def __add__(self, other):
        if other.is_ancestor(self):
            return False
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
        if type(other) != CompanyNode:
            return False
        if self.comparison_value() < other.comparison_value():
            return True
        else:
            return False

    def __gt__(self, other):
        if type(other) != CompanyNode:
            return False
        if self.comparison_value() > other.comparison_value():
            return True
        else:
            return False

    def __eq__(self, other):
        if type(other) != CompanyNode:
            return False
        if self.comparison_value() == other.comparison_value():
            return True
        else:
            return False

    def __ge__(self, other):
        if type(other) != CompanyNode:
            return False
        if self.comparison_value() >= other.comparison_value():
            return True
        else:
            return False

    def __le__(self, other):
        if type(other) != CompanyNode:
            return False
        if self.comparison_value() <= other.comparison_value():
            return True
        else:
            return False

    def __ne__(self, other):
        if type(other) != CompanyNode:
            return False
        if self.comparison_value() != other.comparison_value():
            return True
        else:
            return False
