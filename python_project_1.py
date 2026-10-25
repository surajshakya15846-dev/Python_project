
correct_pin = "1234"
balance = 10000
transactions = []


attempts = 3

while attempts > 0:
    pin = input("Enter your PIN: ")

    if pin == correct_pin:
        print("PIN verified successfully!")
        break
    else:
        attempts -= 1

        if attempts > 0:
            print("Wrong PIN. Attempts left:", attempts)
        else:
            print("Card blocked.")

if attempts > 0:

  
    while True:
        print("----- ATM MENU -----")
        print("1. Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Enter your choice: ")

      
        if choice == "1":
            print("Current balance:", balance)

        elif choice == "2":
            amount = float(input("Enter deposit amount: "))

            if amount > 0:
                balance += amount
                transactions.append(("Deposit", amount))
                print("New balance:", balance)
            else:
                print("Amount must be above 0.")

        elif choice == "3":
            amount = float(input("Enter withdrawal amount: "))

            if amount <= 0:
                print("Amount must be above 0.")
            elif amount > balance:
                print("Insufficient balance")
            else:
                balance -= amount
                transactions.append(("Withdraw", amount))
                print("New balance:", balance)

        elif choice == "4":
            print("Thank you!")

            
            print("----- TRANSACTION HISTORY -----")

            if len(transactions) == 0:
                print("No transactions made.")
            else:
                for transaction, amount in transactions:
                    print(transaction, amount)

            break

        else:
            print("Invalid choice. Please try again.")
