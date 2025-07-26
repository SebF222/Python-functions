
def calculate_budget():
    income = float(input("Enter your monthly income: $"))
    rent_expense = float(input("How much is your rent: $"))
    food_expense = float(input("How much do you spend on food: $"))
    entertainment_expense = float(input("How much do you spend on entertainment and fun: $"))

    total_expenses = rent_expense + food_expense + entertainment_expense

    remaining_money = income - rent_expense - food_expense - entertainment_expense

    if remaining_money < 0:
        advice = "You're overspending bud! calm your horses"
    elif remaining_money < 100:
        advice = "whats how your spending! your almost at broke"
    else:
        advice = "Yessir your ratio is great you have more then enough!"

    print("=== BUDGET SUMMARY ===")
    print(f"Monthly Income: ${income:.2f}")
    print(f"Total Expenses: ${total_expenses:.2f}")
    print(f"Remaining Money: ${remaining_money:.2f}")
    print(f"Budget Advice: {advice}")
calculate_budget()

