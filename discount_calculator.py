# Function to calculate the discounted price
def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount = price * (discount_percent / 100)
        final_price = price - discount
        return final_price
    else:
        return price

# Prompt the user for input
price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the discount percentage: "))

# Calculate the final price after discount
final_price = calculate_discount(price, discount_percent)

# Output the result
print(f"The final price after applying the discount is: ${final_price:.2f}" if discount_percent >= 20 else f"The price remains the same: ${final_price:.2f}")
#done and dusted 