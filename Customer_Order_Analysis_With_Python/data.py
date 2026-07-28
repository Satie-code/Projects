# Responsible for collecting customer order data

# Category Menu
CATEGORY_OPTIONS = {
    "1": "Electronics",
    "2": "Clothing",
    "3": "Home Essentials"
}

# Display Category Menu
def display_categories():
    print("\nAvailable Categories")
    print("-" * 30)

    for key, value in CATEGORY_OPTIONS.items():
        print(f"{key}. {value}")

# Get Valid Category
def get_category():

    while True:

        display_categories()

        choice = input("\nEnter Category Number: ").strip()

        if choice in CATEGORY_OPTIONS:
            return CATEGORY_OPTIONS[choice]

        print("Invalid category! Please try again.\n")

# Get Positive Price
def get_price():

    while True:

        try:
            price = float(input("Enter Product Price ($): "))

            if price > 0:
                return price

            print("Price must be greater than 0.")

        except ValueError:
            print("Please enter a valid number.")

# Collect Customer Orders
def collect_customer_orders():

    customers = []
    orders = []

    while True:

        try:
            number_of_customers = int(
                input("Enter Number of Customers: ")
            )

            if number_of_customers > 0:
                break

            print("Please enter at least one customer.")

        except ValueError:
            print("Invalid input. Enter a number.")

    print("\n" + "=" * 60)

    for customer_no in range(1, number_of_customers + 1):

        print(f"\nCustomer {customer_no}")
        print("-" * 40)

        customer_name = input("Enter Customer Name: ").strip().title()

        customers.append(customer_name)

        while True:

            try:

                number_of_products = int(
                    input("Number of Products Purchased: ")
                )

                if number_of_products > 0:
                    break

                print("Must purchase at least one product.")

            except ValueError:
                print("Enter a valid number.")

        print()

        for product_no in range(1, number_of_products + 1):

            print(f"Product {product_no}")

            product_name = input("Product Name: ").strip().title()

            product_price = get_price()

            product_category = get_category()

            orders.append(
                (
                    customer_name,
                    product_name,
                    product_price,
                    product_category
                )
            )

            print()

    return customers, orders

# Display Raw Data
def display_entered_data(customers, orders):

    print("\n")
    print("=" * 60)
    print("ENTERED CUSTOMER DATA")
    print("=" * 60)

    print("\nCustomers")

    for customer in customers:
        print("-", customer)

    print("\nOrders")

    for customer, product, price, category in orders:

        print(
            f"{customer:15}"
            f"{product:20}"
            f"${price:<10}"
            f"{category}"
        )