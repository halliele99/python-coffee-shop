print("""Welcome to Python Coffee!

      Menu
      1. Latte       $5.50
      2. Americano   $4.00
      3. Mocha       $6.00
      4. Cold Brew   $5.00
      5. Matcha      $6.50
      """)

menu_cost = {
    "Latte": 5.50,
    "Americano": 4.00,
    "Mocha": 6.00,
    "Cold Brew": 5.00,
    "Matcha": 6.50
}
subtotal = 0
another_drink = "yes"
drink_order = {}
while another_drink == "yes":
    drink = input("Choose your drink: ").title()
    if drink not in menu_cost:
        print("Sorry, that drink isn't on the menu. Try Again.")
    else:
        while True:
            try:
                num_drink = int(input("Quantity: "))
                if num_drink > 0:
                    break
            except ValueError:
                print("Please enter a valid number.")
        if drink in drink_order:
            drink_order[drink] += num_drink
        else:
            drink_order[drink] = num_drink
        another_drink = input("Would you like another drink? ").lower()
        cost_per_drink_order = menu_cost[drink] * num_drink
        subtotal += cost_per_drink_order

l = ""
for d, count in drink_order.items():
    l += f"""{d} x{count}          ${menu_cost[d] * count:.2f}\n"""

## 10% discount if their order exceeds $25


if subtotal > 25:
    discount = round(subtotal * 0.1, 2)
else:
    discount = 0
total = subtotal - discount

print(f"""----- RECEIPT ----- 
{l}
Subtotal: $ {subtotal:.2f}
Discount: $ {discount:.2f}
Total: $ {total:.2f}
-------------------
""")
