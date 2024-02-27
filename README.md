# OOP - Company Financial Side

This Python project provides implementations of the `Company` and `CompanyNode` classes, designed to manage and analyze financial data related to companies. The `Company` class represents individual companies, while the `CompanyNode` class extends this functionality to support hierarchical structures of companies.

## Features

### Company Class

The `Company` class provides the following features:

- **Initialization:** Allows creation of `Company` objects with a name, number of stocks, stock price, and company type.
- **Net Worth Calculation:** Computes the net worth of a company based on the number of stocks and stock price.
- **Data Modification:** Provides methods to update the name, number of stocks, stock price, and company type of a company.
- **Comparison:** Supports comparison operations based on net value, number of stocks, and stock price.
- **String Representation:** Generates a human-readable string representation of a company object.

### CompanyNode Class

The `CompanyNode` class extends the functionality of the `Company` class to support hierarchical structures of companies. It inherits all features of the `Company` class and adds the following:

- **Hierarchy Management:** Allows the creation of a tree-like structure of companies, where each node can have multiple child nodes.
- **Total Net Worth Calculation:** Computes the total net worth of a company and all its child companies recursively.
- **Ancestor Determination:** Determines whether a company is an ancestor of another company within the hierarchy.
- **String Representation:** Provides a string representation of a company node and its children in a hierarchical format.
- **Addition Operation:** Allows merging of two company nodes, preserving the hierarchical structure and financial data.

## Testing

The project includes built-in unit tests for both the `Company` and `CompanyNode` classes to ensure their correctness and reliability. The unit tests cover various aspects of the classes, including initialization, data modification, calculation, comparison, and hierarchical operations.

### Running Tests

To run the unit tests for the `Company` class, use the following command:
python -m unittest tests.test_company
To run the unit tests for the CompanyNode class, use the following command:
python -m unittest tests.test_companynode
These commands will automatically discover and execute all the unit tests defined in the respective test files within the tests directory.

For more detailed information on each test case and its implementation, please take a look at the test files in the test directory.
### Usage
To use the Company and CompanyNode classes in your Python projects, simply import them from the provided modules and instantiate objects as needed. You can then utilize the various methods and features of these classes to manage and analyze financial data for individual companies and hierarchical structures of companies.
**code:**
from Company import Company
from CompanyNode import CompanyNode

# Example usage of Company class
company1 = Company("Company A", 100, 10.0, "Type A")
print(company1.net_worth())  # Output: 1000.0

# Example usage of CompanyNode class
parent_company = CompanyNode("Parent Company", 200, 15.0, "Type B")
child_company = CompanyNode("Child Company", 50, 10.0, "Type C")
parent_company.add_child(child_company)
print(parent_company.total_net_worth())  # Output: Total net worth of parent and child companies


