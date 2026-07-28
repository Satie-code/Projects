# Contains all the functions used in the Customer Order Analysis System

# Get Customer Data
def get_customer_data():
    customers = []
    orders = []

    num_customers = int(input("Enter the number of customers: "))

    print()

    for i in range(num_customers):

        print("=" * 50)
        print(f"Customer {i + 1}")
        print("=" * 50)

        customer = input("Enter Customer Name: ").strip().title()

        customers.append(customer)

        num_products = int(input("How many products did this customer purchase? "))

        print()

        for j in range(num_products):

            print(f"Product {j + 1}")

            product = input("Product Name: ").strip().title()

            price = float(input("Product Price ($): "))

            print("\nSelect Category")
            print("1. Electronics")
            print("2. Clothing")
            print("3. Home Essentials")

            choice = input("Enter Choice: ")

            if choice == "1":
                category = "Electronics"

            elif choice == "2":
                category = "Clothing"

            elif choice == "3":
                category = "Home Essentials"

            else:
                category = "Other"

            orders.append(
                (customer, product, price, category)
            )

            print()

    return customers, orders

# Customer -> Products Dictionary
def create_customer_product_dict(orders):

    customer_products = {}

    for customer, product, price, category in orders:

        if customer not in customer_products:
            customer_products[customer] = []

        customer_products[customer].append(product)

    return customer_products

# Product -> Category Dictionary
def create_product_category_dict(orders):

    product_category = {}

    for customer, product, price, category in orders:
        product_category[product] = category

    return product_category

# Unique Categories
def get_unique_categories(product_category):

    return set(product_category.values())

# Customer Spending
def calculate_customer_spending(orders):

    customer_spending = {}

    for customer, product, price, category in orders:

        if customer not in customer_spending:
            customer_spending[customer] = 0

        customer_spending[customer] += price

    return customer_spending

# Customer Classification
def classify_customers(customer_spending):

    customer_classification = {}

    for customer, total in customer_spending.items():

        if total > 100:
            customer_classification[customer] = "High-Value Buyer"

        elif total >= 50:
            customer_classification[customer] = "Moderate Buyer"

        else:
            customer_classification[customer] = "Low-Value Buyer"

    return customer_classification

# Revenue Per Category
def calculate_category_revenue(orders):

    category_revenue = {}

    for customer, product, price, category in orders:

        if category not in category_revenue:
            category_revenue[category] = 0

        category_revenue[category] += price

    return category_revenue

# Unique Products
def get_unique_products(orders):

    unique_products = set()

    for customer, product, price, category in orders:
        unique_products.add(product)

    return unique_products

# Electronics Customers
def get_electronics_customers(orders):

    return list({
        customer
        for customer, product, price, category in orders
        if category == "Electronics"
    })

# Top 3 Customers
def get_top_three_customers(customer_spending):

    return sorted(
        customer_spending.items(),
        key=lambda x: x[1],
        reverse=True
    )[:3]

# Customer Categories
def get_customer_categories(orders):

    customer_categories = {}

    for customer, product, price, category in orders:

        if customer not in customer_categories:
            customer_categories[customer] = set()

        customer_categories[customer].add(category)

    return customer_categories

# Multiple Category Customers
def get_multiple_category_customers(customer_categories):

    result = {}

    for customer, categories in customer_categories.items():

        if len(categories) > 1:
            result[customer] = categories

    return result

# Electronics & Clothing Customers
def get_common_customers(orders):

    electronics = set()
    clothing = set()

    for customer, product, price, category in orders:

        if category == "Electronics":
            electronics.add(customer)

        elif category == "Clothing":
            clothing.add(customer)

    return electronics.intersection(clothing)

# Product Frequency
def get_product_frequency(orders):

    product_frequency = {}

    for customer, product, price, category in orders:

        if product not in product_frequency:
            product_frequency[product] = 0

        product_frequency[product] += 1

    return product_frequency

# Most Purchased Products
def get_most_purchased_products(product_frequency):

    highest = max(product_frequency.values())

    return {
        product: count
        for product, count in product_frequency.items()
        if count == highest
    }

# Highest Revenue Category
def get_highest_revenue_category(category_revenue):

    return max(
        category_revenue,
        key=category_revenue.get
    )

# Highest Spending Customer
def get_highest_spending_customer(customer_spending):

    return max(
        customer_spending,
        key=customer_spending.get
    )