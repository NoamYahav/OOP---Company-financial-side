from Company import Company
from CompanyNode import CompanyNode


def main():
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



if __name__ == "__main__":
    main()
