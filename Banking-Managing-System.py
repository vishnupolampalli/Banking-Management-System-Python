import os
class BankAccount:
    def __init__(self, acc_no, name, pin, balance=0):
        self.acc_no = acc_no
        self.name = name
        self.pin = pin
        self.balance = balance
        self.history = []

    def authenticate(self):
        try:
            entered_pin = int(input("Enter PIN: "))
            return entered_pin == self.pin
        except ValueError:
            print("Invalid PIN format")
            return False

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.history.append(f"Deposited ₹{amount}")
            print(f"₹{amount} deposited successfully")
        else:
            print("Invalid amount")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            self.history.append(f"Withdrawn ₹{amount}")
            print(f"₹{amount} withdrawn successfully")
        else:
            print("Insufficient balance")

    def check_balance(self):
        print(f"Current Balance: ₹{self.balance}")

    def show_history(self):
        print("\n--- Transaction History ---")
        if not self.history:
            print("No transactions yet")
        else:
            for h in self.history:
                print(h)

    def save_to_file(self):
        with open("account.txt", "w") as f:
            f.write(f"{self.acc_no},{self.name},{self.pin},{self.balance}\n")
            for h in self.history:
                f.write(h + "\n")

    def load_from_file(self):
        if not os.path.exists("account.txt"):
            return False

        with open("account.txt", "r") as f:
            lines = f.readlines()
            acc_data = lines[0].strip().split(",")
            self.acc_no = int(acc_data[0])
            self.name = acc_data[1]
            self.pin = int(acc_data[2])
            self.balance = float(acc_data[3])
            self.history = [line.strip() for line in lines[1:]]

        return True
# -------- MAIN PROGRAM --------
print("🏦 Welcome to Banking System")

account = BankAccount(0, "", 0)

if account.load_from_file():
    print("Account loaded successfully")
else:
    try:
        acc_no = int(input("Create Account Number: "))
        name = input("Enter Name: ")
        pin = int(input("Set 4-digit PIN: "))
        balance = float(input("Enter Initial Balance: "))
        account = BankAccount(acc_no, name, pin, balance)
        account.save_to_file()
        print("Account created successfully")
    except ValueError:
        print("Invalid input! Restart program.")
        exit()

while True:
    print("\n----- MENU -----")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Transaction History")
    print("5. Exit")

    try:
        choice = int(input("Enter choice: "))
    except ValueError:
        print("Enter valid number")
        continue

    if choice == 1:
        if account.authenticate():
            amt = float(input("Enter amount: "))
            account.deposit(amt)
            account.save_to_file()
        else:
            print("Authentication failed")

    elif choice == 2:
        if account.authenticate():
            amt = float(input("Enter amount: "))
            account.withdraw(amt)
            account.save_to_file()
        else:
            print("Authentication failed")

    elif choice == 3:
        if account.authenticate():
            account.check_balance()
        else:
            print("Authentication failed")

    elif choice == 4:
        if account.authenticate():
            account.show_history()
        else:
            print("Authentication failed")

    elif choice == 5:
        account.save_to_file()
        print("Thank you for using Banking System 🙏")
        break

    else:
        print("Invalid choice")
