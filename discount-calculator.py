def calculate_discount(price, discount_percent):
    """
    This function calculates the final price of a product after applying the discount.
    It checks if the discount percentage is 20% or more. If the discount meets this condition,
    the discount is applied to the original price. Otherwise, the original price remains unchanged.
    """
    if discount_percent >= 20:
        # Calculate the discount amount based on the given percentage
        discount_amount = (discount_percent / 100) * price
        # Subtract the discount from the original price to get the discounted price
        final_price = price - discount_amount
        return final_price
    else:
        # If the discount is too low, the price remains unchanged
        return price


def main():
    print("Welcome to the Discount Calculator.")
    
    try:
        # Ask the user to input the price of the item
        original_price = float(input("What is the original price of the product (in KES)? "))
        # Prompt the user for the discount percentage they want to apply
        discount = float(input("Enter the discount percentage you wish to offer"))

        if original_price < 0 or discount < 0:
            # Ensure that the input values are positive numbers
            print("❌ Price and discount cannot be negative. Please enter valid values.")
            return

        # Call the function to calculate the final price after applying the discount
        final_price = calculate_discount(original_price, discount)

        # If the discount is 20% or more, display the final price after the discount is applied
        if discount >= 20:
            print(f"✅ Great deal! The price after a {discount}% discount is: KES {final_price:.2f}")
        else:
            # If the discount is too low, show the original price
            print(f"⚠️ The discount is too low. The original price remains: KES {original_price:.2f}")

    except ValueError:
        # Handle cases where the user enters non-numeric values
        print("❌ Please enter valid numbers for the price and discount.")

# Run the program2
if __name__ == "__main__":
    main()