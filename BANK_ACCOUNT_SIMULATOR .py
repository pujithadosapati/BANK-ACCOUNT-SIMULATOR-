# ==========================================
# MENU-DRIVEN BANK ACCOUNT SIMULATOR
# ==========================================
# Account details
account_holder = input("Enter account holder name: ")
balance = 0.0
transactions = []
# Function to check balance
def check_balance():
    print("\n========== ACCOUNT BALANCE ==========")
    print(f"Account Holder: {account_holder}")
    print(f"Available Balance: Rs.{balance:.2f}")
# Function to deposit money
def deposit():
    global balance
    print("\n========== DEPOSIT MONEY ==========")
    try:
        amount = float(input("Enter deposit amount: "))
        if amount <= 0:
            print("Error: Deposit amount must be greater than zero.")
        else:
            balance += amount
            transactions.append(
                f"Deposited Rs.{amount:.2f}"
            )
            print("Money deposited successfully!")
            print(f"Updated Balance: Rs.{balance:.2f}")

    except ValueError:
        print("Invalid input! Please enter a valid number.")
# Function to withdraw money
def withdraw():
    global balance
    print("\n========== WITHDRAW MONEY ==========")
    try:
        amount = float(input("Enter withdrawal amount: "))
        if amount <= 0:
            print("Error: Withdrawal amount must be greater than zero.")
        elif amount > balance:
            print("Insufficient balance!")
            print(f"Available Balance: Rs.{balance:.2f}")
        else:
            balance -= amount
            transactions.append(
                f"Withdrawn Rs.{amount:.2f}"
            )
            print("Withdrawal successful!")
            print(f"Remaining Balance: Rs.{balance:.2f}")
    except ValueError:
        print("Invalid input! Please enter a valid number.")
# Function to display transaction history
def transaction_history():
    print("\n========== TRANSACTION HISTORY ==========")
    if len(transactions) == 0:
        print("No transactions found.")
    else:
        for index, transaction in enumerate(transactions, start=1):
            print(f"{index}. {transaction}")
        print("-----------------------------------------")
        print(f"Current Balance: Rs.{balance:.2f}")
# Main menu function
def main():
    while True:
        print("\n")
        print("========================================")
        print("       BANK ACCOUNT SIMULATOR")
        print("========================================")
        print("1. Check Account Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Transaction History")
        print("5. Exit")
        print("========================================")
        choice = input("Enter your choice (1-5): ")
        if choice == "1":
            check_balance()
        elif choice == "2":
            deposit()
        elif choice == "3":
            withdraw()
        elif choice == "4":
            transaction_history()
        elif choice == "5":
            print("\nThank you for using our bank!")
            print(f"Goodbye, {account_holder}!")
            break
        else:
            print("Invalid choice! Please select between 1 and 5.")
# Start the application
if __name__ == "__main__":
    main()
