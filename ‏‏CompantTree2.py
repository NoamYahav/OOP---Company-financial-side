import copy

from CompanyNode import CompanyNode
class CompanyTree:

    def __init__(self, root=None):
        if type(root) is not CompanyNode and root is not None and root.get_parent() != None:
            raise ValueError
        self.__root = root


    def set_root(self, root):
        if type(root) is not CompanyNode and root is not None:
                False
        self.__root = root
        return True

    def get_root(self):
        return str(self.__root)

    def __str__(self):
        if self.__root is None:
            return ""
        # Creating a empty string
        final_str = ""
        # The main lst. here we gonna add all the companies.
        lst = []
        lst.append(self.__root)
        while len(lst) != 0:
            if len(lst) == 1:#Adding the companies to string by the rules defined in the job.(cosmetics)
                final_str += (str(lst[0]) + "\n")
            elif len(lst) > 1:
                empty_str = ""
                for i in range(len(lst)):
                    if i == 0:
                        empty_str = empty_str + str(lst[i])
                    else:
                        empty_str = empty_str + " * " + str(lst[i])
                empty_str += "\n"
                final_str += (empty_str)
            n = len(lst)
            # If this company has childrens
            while n > 0:
                #Focus on one company each time and add it to the main list.
                current_company = lst[0]
                lst.pop(0)
                # Add all current company children to the lst
                for i in range(len(current_company)):
                    lst.append(current_company.get_children()[i])
                n -= 1 #Making asure while loop stop (could have use for loop)
        return final_str[0:len(final_str)-1] #Slicing the last /n from the final str


    def __iter__(self):
        if self.__root == None:
            m=[]
            return iter(m)
        try:
            m = self.final_result
        except:
            m = self.inorder_comp_tree()
        return iter(m)

    def __next__(self):
        pass

    def insert_node(self, node):
        #First checking rules defined in work
        if self.__root == None:
            return False
        if type(node) is not CompanyNode and node is not None:
            return False
        if node.get_parent() != None:
            return False
        if node.test_node_order_validity() != True:
            return False
        if node is None:
            return True
        if node == self.__root or self.__root.is_ancestor(node):
            return False
        try:
            lst_inorder = self.final_result
        except:
            lst_inorder = self.inorder_comp_tree()
        for i in range(len(lst_inorder)):
            current_node = lst_inorder[i]
            current_node_copy = copy.deepcopy(current_node)
            current_node_copy.get_children().append(node)
            if current_node_copy.test_node_order_validity():
                current_node.get_children().append(node)
                return True
        return False

    def remove_node(self, name):
        if self.__root == None:
            return None
        for company in self:
            current_company = company.name
            if current_company == name:
                lst_of_children = company.get_children()
                for child in lst_of_children:
                    if company.get_parent() is self.__root:
                        self.__root.get_children().append(child)
                    company.get_parent().get_children().append(child)
                    lst_of_children.remove(child)
                if company.get_parent() is self.__root:
                    self.__root.get_children().remove(company)
                company_parent = company.get_parent()
                company_parent_children =company_parent.get_children()
                company_parent_children.remove(company)
                self.final_result.remove(company)
                return company
        return None


    def inorder_comp_tree(self):
        node = self.__root
        final_result = node.in_order_tree()
        for i in final_result:
            if i is None:
                final_result.remove(None)
        self.final_result = final_result
        return final_result