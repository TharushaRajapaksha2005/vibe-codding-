def main():
    print("--- Monthly Budget Tracker ---")
    
    try:
        # 1. Ask the user for total monthly budget
        total_budget = float(input("Enter your total monthly budget: "))
        
        expenses = []
        # 2. Ask for multiple expenses until "done"
        while True:
            name = input("Enter the name of the expense (or type 'done' to finish): ").strip().lower()
            if name == 'done':
                break
            try:
                amount = float(input(f"Enter the amount for {name}: "))
                expenses.append(amount)
            except ValueError:
                print("Invalid amount. Please enter a number.")
        
        # 4. Subtract expenses from total budget
        total_expenses = sum(expenses)
        remaining_balance = total_budget - total_expenses
        
        # 5. Displays remaining balance
        print("\n--- Summary ---")
        print(f"Total Budget:    LKR {total_budget:,.2f}")
        print(f"Total Expenses:  LKR {total_expenses:,.2f}")
        print(f"Remaining Balance: LKR {remaining_balance:,.2f}")

        if remaining_balance < 0:
            print("Warning: You are over budget!")
        elif 0 <= remaining_balance < 500:
            print("Warning: Low Funds")
        elif remaining_balance == 500:
             print("You are on the limit.")
        else:
            print("You are within your budget.")

    except ValueError:
        print("Error: Please enter valid numeric values for budget and expenses.")

if __name__ == "__main__":
    main()
