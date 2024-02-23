from Company import Company
from CompanyNode import CompanyNode
from CompantTree import CompanyTree


def main():
    """
    Note: This file contains only partial tests
    """
    print("#################Company tests#################")
    print("1. create Company instance:")
    c1 = Company("Google", 1000, 20.284, "High Tech")
    print(c1)

    print("2. test net_worth method:")
    print(c1.net_worth())

    print("3. test set_name method:")
    print(c1.set_name("Google2"))
    print(c1.set_name("Google Two"))
    print(c1)

    print("4. test set_stocks_num method:")
    print(c1.set_stocks_num(2000))
    print(c1)

    print("5. test set_stock_price method:")
    print(c1.set_stock_price(25))
    print(c1)

    print("6. test set_comp_type method:")
    print(c1.set_comp_type("General"))
    print(c1)

    print("7. test update_net_worth method:")
    print(c1.update_net_worth(0))
    print(c1)
    print(c1.update_net_worth(2027.5))
    print(c1)

    print("8. test add_stocks method:")
    print(c1.add_stocks(-850))
    print(c1)
    print(c1.add_stocks(8000))
    print(c1)

    print("9. test Operator Overloading:")
    c2 = Company("Lenovo", 1000, 5, "High Tech")
    print(c2)
    print(c1 > c2)
    print(c1 < c2)
    print(c1 == c2)
    print(c1 + c2)

    print("#################CompanyNode tests#################")
    print("1. create CompanyNode instances and connect them, and test repr:")
    c0_node = CompanyNode("BGU Zero", 1000, 20.284, "High Tech")
    c1_node = CompanyNode("BGU One", 1100, 20.284, "High Tech")
    c2_node = CompanyNode("BGU Two", 2000, 20.284, "High Tech")
    print(c2_node.add_child(c1_node))
    print(c1_node.add_child(c0_node))
    print(repr(c2_node))

    print("2. test len:")
    print(len(c2_node))

    print("3. test total_net_worth:")
    print(c2_node.total_net_worth())

    print("4. test is_ancestor:")
    print(c2_node.is_ancestor(c1_node))
    print(c1_node.is_ancestor(c2_node))

    print("5. add operator:")
    c3_node = c2_node + c0_node
    print(repr(c3_node))

    print("#################CompanyTree tests#################")
    c0_node = CompanyNode("BGU Zero", 1000, 20.284, "High Tech")
    c1_node = CompanyNode("BGU One", 1100, 20.284, "High Tech")
    c11_node = CompanyNode("BGU One One", 1100, 20.284, "High Tech")
    c12_node = CompanyNode("BGU One Two", 1100, 20.284, "High Tech")
    c13_node = CompanyNode("BGU One Three", 1100, 20.284, "High Tech")
    c2_node = CompanyNode("BGU Two", 2000, 20.284, "High Tech")
    c2_node.add_child(c1_node)
    c2_node.add_child(c11_node)
    c2_node.add_child(c12_node)
    c2_node.add_child(c13_node)
    c1_node.add_child(c0_node)
    comp_tree = CompanyTree(root=c2_node)
    print("1. test str:")
    print(comp_tree)
    print("2. test iterator design pattern implementation:")
    for node in comp_tree:
        print(node)

    print("3. test insert_node method:")
    c_new_node = CompanyNode("BGU added", 500, 20.284, "High Tech")
    print(comp_tree.insert_node(c_new_node))
    print(comp_tree)

    print("4. test remove_node method:")
    print(repr(comp_tree.remove_node("BGU One")))
    print(comp_tree)


if __name__ == "__main__":
    main()
