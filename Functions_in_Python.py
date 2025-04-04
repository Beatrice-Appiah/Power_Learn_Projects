# QUESTION 1:
def calculate_discount(price, discount_percent):
  """Calculates the final price after applying a discount, if applicable.

  Args:
    price: The original price of the item (numeric).
    discount_percent: The discount percentage (numeric).

  Returns:
    The final price after applying the discount if the discount_percent
    is 20% or higher. Otherwise, returns the original price.
  """
  # Checks if the discount percentage meets the threshold (20% or higher)
  if discount_percent >= 20:
    # Calculates the discount amount
    # discount_amount = price * (discount_percent / 100)
    # Calculates the final price by subtracting the discount amount
    # final_price = price - discount_amount

    # Alternative calculation: Calculates the remaining percentage to pay
    final_price = price * (1 - discount_percent / 100)
    return final_price
  else:
    # If the discount is less than 20%, return the original price
    return price

# --- Example Usage ---

# Scenario 1: Discount is 25% (>= 20%), so it should be applied
original_price1 = 100
discount_percentage1 = 25
final_price1 = calculate_discount(original_price1, discount_percentage1)
print(f"Original Price: ${original_price1}, Discount: {discount_percentage1}%, Final Price: ${final_price1}")
# Expected Output: Original Price: $100, Discount: 25%, Final Price: $75.0

# Scenario 2: Discount is 10% (< 20%), so the original price should be returned
original_price2 = 150
discount_percentage2 = 10
final_price2 = calculate_discount(original_price2, discount_percentage2)
print(f"Original Price: ${original_price2}, Discount: {discount_percentage2}%, Final Price: ${final_price2}")
# Expected Output: Original Price: $150, Discount: 10%, Final Price: $150

# Scenario 3: Discount is exactly 20%, so it should be applied
original_price3 = 80
discount_percentage3 = 20
final_price3 = calculate_discount(original_price3, discount_percentage3)
print(f"Original Price: ${original_price3}, Discount: {discount_percentage3}%, Final Price: ${final_price3}")
# Expected Output: Original Price: $80, Discount: 20%, Final Price: $64.0








# QUESTION 2:
def calculate_discount(price, discount_percent):
  """Calculates the final price after applying a discount, if applicable.

  Args:
    price: The original price of the item (numeric).
    discount_percent: The discount percentage (numeric).

  Returns:
    The final price after applying the discount if the discount_percent
    is 20% or higher. Otherwise, returns the original price.
  """
  if discount_percent >= 20:
    # Calculate the remaining percentage to pay
    final_price = price * (1 - discount_percent / 100)
    return final_price
  else:
    # If the discount is less than 20%, return the original price
    return price

# --- Main part of the script ---

# Use a try-except block to handle potential errors if the user enters non-numeric input
try:
  # Prompt the user for the original price and convert it to a float
  original_price_str = input("Please enter the original price of the item: ")
  original_price = float(original_price_str)

  # Prompt the user for the discount percentage and convert it to a float
  discount_percent_str = input("Please enter the discount percentage (e.g., 25 for 25%): ")
  discount_percent = float(discount_percent_str)

  # Basic validation: Ensure price and discount are not negative
  if original_price < 0 or discount_percent < 0:
      print("Error: Price and discount percentage cannot be negative.")
  else:
      # Call the function to calculate the final price
      final_price = calculate_discount(original_price, discount_percent)

      # Check if a discount was actually applied by comparing final price to original
      if final_price < original_price:
          print(f"\nA discount of {discount_percent}% was applied.")
          print(f"The final price after the discount is: ${final_price:.2f}")
      else:
          print(f"\nThe discount of {discount_percent}% is less than 20%, so no discount was applied.")
          print(f"The price remains the original price: ${final_price:.2f}")

except ValueError:
  # This block runs if float() fails (e.g., user entered text instead of numbers)
  print("\nError: Invalid input. Please enter numeric values for price and discount percentage.")
  
