def calculate_discount(price, discount_percent):
    # Check if the discount percent is 20% or higher
    if discount_percent >= 20:
        # Calculate the discount amount
        discount_amount = price * (discount_percent / 100)
        # Calculate the final price after applying the discount
        final_price = price - discount_amount
        return final_price
    else:
        # If the discount is less than 20%, return the original price
        return price

# Prompt the user to enter the original price and discount percentage
original_price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the discount percentage: "))

# Calculate the final price using the calculate_discount function
final_price = calculate_discount(original_price, discount_percent)

# Print the final price after applying the discount, or the original price if no discount was applied
if final_price != original_price:
    print("Final price after discount: ${:.2f}".format(final_price))
else:
    print("No discount applied. Final price: ${:.2f}".format(final_price))
