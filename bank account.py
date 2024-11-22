class SavingAccount:

    def __init__(self, name):
        self.name = name
        self.balance = 0.0
        self.transactions = []  # Corrected attribute name

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be greater than zero")
            return
        self.balance += amount
        self.transactions.append(f"Deposited: Rs{amount:.2f}")
        print(f"Successfully deposited Rs{amount:.2f}. Current balance: Rs{self.balance:.2f}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be greater than zero")
            return
        if amount > self.balance:
            print("Insufficient funds")
            return
        self.balance -= amount
        self.transactions.append(f"Withdrew: Rs{amount:.2f}")
        print(f"Successfully withdrew Rs{amount:.2f}. Current balance: Rs{self.balance:.2f}")

    def view_balance(self):
        print(f"Current balance: Rs{self.balance:.2f}")

    def view_transactions(self):
        if not self.transactions:
            print("No transactions made!")
        else:
            print("Transaction History:")
            for i, transaction in enumerate(self.transactions, 1):
                print(f"{i}. {transaction}")


def main():
    print("Welcome to the Saving Account Manager")
    name = input("Enter your name: ")
    account = SavingAccount(name)

    while True:
        print("\nMenu:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. View Balance")
        print("4. View Transactions")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            try:
                amount = float(input("Enter the amount to deposit: Rs"))
                account.deposit(amount)
            except ValueError:
                print("Invalid amount. Please enter a number.")
        elif choice == "2":
            try:
                amount = float(input("Enter the amount to withdraw: Rs"))
                account.withdraw(amount)
            except ValueError:
                print("Invalid amount. Please enter a number.")
        elif choice == "3":
            account.view_balance()
        elif choice == "4":
            account.view_transactions()
        elif choice == "5":
            print("Thank you for using the Saving Account Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

        