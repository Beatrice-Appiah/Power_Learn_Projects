def calculate_discount(price, discount_percent):
  """Calculates the final price after applying a discount, if applicable.

  Args:
    price: The original price of the item (numeric).
    discount_percent: The discount percentage (numeric).

  Returns:
    The final price after applying the discount if the discount_percent
    is 20% or higher. Otherwise, returns the original price.
  """
  # Check if the discount percentage meets the threshold (20% or higher)
  if discount_percent >= 20:
    # Calculate the discount amount
    # discount_amount = price * (discount_percent / 100)
    # Calculate the final price by subtracting the discount amount
    # final_price = price - discount_amount

    # Alternative calculation: Calculate the remaining percentage to pay
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

# Scenario 4: Discount is 50% (>= 20%), so it should be applied
original_price4 = 200
discount_percentage4 = 50
final_price4 = calculate_discount(original_price4, discount_percentage4)
print(f"Original Price: ${original_price4}, Discount: {discount_percentage4}%, Final Price: ${final_price4}")
# Expected Output: Original Price: $200, Discount: 50%, Final Price: $100.0
