from Company import Company
from CompanyNode import CompanyNode
from CompantTree import CompanyTree


def main():
    print("#################CompanyTree tests#################")
    c0_node = CompanyNode("BGU Zero", 2000, 20.284, "High Tech")
    c1_node = CompanyNode("BGU One", 1100, 20.284, "High Tech")
    c11_node = CompanyNode("BGU One One", 1100, 20.284, "High Tech")
    c12_node = CompanyNode("BGU One Two", 1100, 20.284, "High Tech")
    c13_node = CompanyNode("BGU One Three", 1100, 20.284, "High Tech")
    c2_node = CompanyNode("BGU Two", 1100, 20.284, "High Tech")
    print(c0_node.add_child(c1_node))
    print(c1_node.add_child(c2_node))
    print(c2_node.add_child(c11_node))
    print(c11_node.add_child(c12_node))
    print(c12_node.add_child(c13_node))
    comp_tree = CompanyTree(c0_node)
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
