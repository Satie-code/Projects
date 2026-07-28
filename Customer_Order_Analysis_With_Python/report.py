# Responsible for displaying all reports

# Customer -> Products Dictionary
def display_customer_products(customer_products):

    print("\n" + "=" * 70)
    print("CUSTOMER ORDERS")
    print("=" * 70)

    for customer, products in customer_products.items():
        print(f"{customer:<15} : {', '.join(products)}")

# Product -> Category Dictionary
def display_product_categories(product_category):

    print("\n" + "=" * 70)
    print("PRODUCT CATEGORY MAPPING")
    print("=" * 70)

    for product, category in product_category.items():
        print(f"{product:<25} : {category}")

# Available Categories
def display_categories(categories):

    print("\n" + "=" * 70)
    print("AVAILABLE PRODUCT CATEGORIES")
    print("=" * 70)

    for category in sorted(categories):
        print(f"• {category}")

# Customer Spending Summary
def display_customer_summary(customer_spending,
                             customer_classification):

    print("\n" + "=" * 70)
    print("CUSTOMER SPENDING SUMMARY")
    print("=" * 70)

    print(f"{'Customer':<15}{'Total Spending':<20}{'Classification'}")
    print("-" * 70)

    for customer in customer_spending:

        print(
            f"{customer:<15}"
            f"${customer_spending[customer]:<19.2f}"
            f"{customer_classification[customer]}"
        )

# Revenue by Category
def display_category_revenue(category_revenue):

    print("\n" + "=" * 70)
    print("REVENUE BY PRODUCT CATEGORY")
    print("=" * 70)

    for category, revenue in category_revenue.items():

        print(f"{category:<25} : ${revenue:.2f}")

# Unique Products
def display_unique_products(unique_products):

    print("\n" + "=" * 70)
    print("UNIQUE PRODUCTS")
    print("=" * 70)

    for product in sorted(unique_products):
        print(f"• {product}")

# Electronics Customers
def display_electronics_customers(electronics_customers):

    print("\n" + "=" * 70)
    print("CUSTOMERS WHO PURCHASED ELECTRONICS")
    print("=" * 70)

    if len(electronics_customers) == 0:
        print("No customer purchased Electronics.")

    else:

        for customer in sorted(electronics_customers):
            print(customer)

# Top Three Customers
def display_top_three_customers(top_three):

    print("\n" + "=" * 70)
    print("TOP 3 HIGHEST-SPENDING CUSTOMERS")
    print("=" * 70)

    rank = 1

    for customer, amount in top_three:

        print(f"{rank}. {customer:<15} ${amount:.2f}")

        rank += 1

# Customers with Multiple Categories
def display_multiple_category_customers(multiple_customers):

    print("\n" + "=" * 70)
    print("CUSTOMERS WHO PURCHASED FROM MULTIPLE CATEGORIES")
    print("=" * 70)

    if len(multiple_customers) == 0:

        print("No customers purchased from multiple categories.")

    else:

        for customer, categories in multiple_customers.items():

            print(f"{customer:<15} : {', '.join(sorted(categories))}")

# Electronics & Clothing Customers
def display_common_customers(common_customers):

    print("\n" + "=" * 70)
    print("CUSTOMERS WHO BOUGHT BOTH ELECTRONICS AND CLOTHING")
    print("=" * 70)

    if len(common_customers) == 0:

        print("No customer purchased both categories.")

    else:

        for customer in sorted(common_customers):
            print(customer)

# Most Purchased Products
def display_most_purchased_products(products):

    print("\n" + "=" * 70)
    print("MOST FREQUENTLY PURCHASED PRODUCTS")
    print("=" * 70)

    for product, frequency in products.items():

        print(f"{product:<25} Purchased {frequency} time(s)")

# Final Business Insights
def display_business_insights(highest_customer,
                              customer_spending,
                              highest_category,
                              category_revenue):

    print("\n" + "=" * 70)
    print("KEY BUSINESS INSIGHTS")
    print("=" * 70)

    print(f"Highest Spending Customer : {highest_customer}")

    print(
        f"Total Spending            : "
        f"${customer_spending[highest_customer]:.2f}"
    )

    print()

    print(f"Highest Revenue Category  : {highest_category}")

    print(
        f"Category Revenue          : "
        f"${category_revenue[highest_category]:.2f}"
    )

# Final Report
def display_final_report(customers,
                         orders,
                         unique_products,
                         categories):

    print("\n" + "=" * 70)
    print("PROJECT SUMMARY")
    print("=" * 70)

    print(f"Total Customers        : {len(customers)}")
    print(f"Total Orders           : {len(orders)}")
    print(f"Unique Products        : {len(unique_products)}")
    print(f"Product Categories     : {len(categories)}")

    print("\nAnalysis Completed Successfully!")
    print("=" * 70)