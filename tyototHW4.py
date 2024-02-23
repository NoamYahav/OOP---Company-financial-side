from Company import Company
from CompanyNode import CompanyNode
from CompantTree import CompanyTree

c6_node = CompanyNode("BGU Six", 100000, 200000, "High Tech")
c3_node = CompanyNode("BGU Three", 1000, 2000, "High Tech")
c5_node = CompanyNode("BGU Five", 10, 20, "High Tech")
c9_node = CompanyNode("BGU Nine", 10000, 20000, "High Tech")
c1_node = CompanyNode("BGU One", 100, 20, "High Tech")
c2_node = CompanyNode("BGU Two", 100, 20, "High Tech")
c4_node = CompanyNode("BGU Four", 200, 20, "High Tech")
c8_node = CompanyNode("BGU Eight", 100, 20, "High Tech")
c10_node = CompanyNode("BGU Ten", 100, 20, "High Tech")
c7_node = CompanyNode("BGU Seven", 100, 20, "High Tech")

c6_node.add_child(c3_node)
c6_node.add_child(c5_node)
c6_node.add_child(c9_node)
c3_node.add_child(c1_node)
c3_node.add_child(c2_node)
c3_node.add_child(c4_node)
c9_node.add_child(c8_node)
c9_node.add_child(c10_node)
c8_node.add_child(c7_node)


comp_tree = CompanyTree(root=c6_node)
print(repr(comp_tree.remove_node("BGU ")))

for child in comp_tree:
    print(child)
