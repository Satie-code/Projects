import data
import functions
import report


def main():

    customers, orders = data.collect_customer_orders()

    customer_products = functions.create_customer_product_dict(orders)

    product_category = functions.create_product_category_dict(orders)

    categories = functions.get_unique_categories(product_category)

    customer_spending = functions.calculate_customer_spending(orders)

    customer_classification = functions.classify_customers(customer_spending)

    category_revenue = functions.calculate_category_revenue(orders)

    unique_products = functions.get_unique_products(orders)

    electronics_customers = functions.get_electronics_customers(orders)

    top_three = functions.get_top_three_customers(customer_spending)

    customer_categories = functions.get_customer_categories(orders)

    multiple_customers = functions.get_multiple_category_customers(customer_categories)

    common_customers = functions.get_common_customers(orders)

    product_frequency = functions.get_product_frequency(orders)

    most_purchased_products = functions.get_most_purchased_products(product_frequency)

    highest_category = functions.get_highest_revenue_category(category_revenue)

    highest_customer = functions.get_highest_spending_customer(customer_spending)

    report.display_customer_products(customer_products)

    report.display_product_categories(product_category)

    report.display_categories(categories)

    report.display_customer_summary(
        customer_spending,
        customer_classification
    )

    report.display_category_revenue(category_revenue)

    report.display_unique_products(unique_products)

    report.display_electronics_customers(electronics_customers)

    report.display_top_three_customers(top_three)

    report.display_multiple_category_customers(multiple_customers)

    report.display_common_customers(common_customers)

    report.display_most_purchased_products(most_purchased_products)

    report.display_business_insights(
        highest_customer,
        customer_spending,
        highest_category,
        category_revenue
    )

    report.display_final_report(
        customers,
        orders,
        unique_products,
        categories
    )


if __name__ == "__main__":
    main()