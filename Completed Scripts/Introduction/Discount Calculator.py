original_price = float(input("Enter the original price: "))

discount_required = float(input("What is the discount?: "))

discount_calc = discount_required / 100

discount = original_price * discount_calc

discounted_price = original_price - discount

print("The discount price is", discounted_price)
print(discount)
