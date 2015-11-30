def pagination_text(page_number, page_size, total_products):
    first_product = (page_size * (page_number-1)) + 1
    last_product = (page_size * (page_number))
    if last_product < total_products:
        print("Showing " + str(first_product) + " to " + str(last_product) + "of " + str(total_products) + " Products.")
    else:)
        print("Showing " + str(first_product) + "to " + str(total_products) + "of " + str(total_products) + " Products.")


pagination_text(1,10,30)
