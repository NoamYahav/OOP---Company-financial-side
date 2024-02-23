from Company import Company

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


if __name__ == "__main__":
    main()