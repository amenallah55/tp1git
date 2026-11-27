
expenses = []


# 1. Add an expense
def add_expense():
    description = input("Description: ")

    try:
        amount = float(input("Amount: "))
        expenses.append({
            "description": description,
            "amount": amount
        })
        print("Expense added successfully!")

    except ValueError:
        print("Invalid amount!")


# 2. Show all expenses
def show_expenses():
    if len(expenses) == 0:
        print("No expenses found.")
        return

    print("\n===== EXPENSES =====")

    for i, expense in enumerate(expenses, start=1):
        print(f"{i}. {expense['description']} : {expense['amount']:.2f}")


# 3. Show total
def show_total():
    total = 0

    for expense in expenses:
        total += expense["amount"]

    print(f"Total: {total:.2f}")


# 4. Delete an expense (Student A)
def delete_expense():
    if len(expenses) == 0:
        print("No expenses to delete.")
        return

    show_expenses()

    try:
        number = int(input("Enter expense number to delete: "))

        if number < 1 or number > len(expenses):
            print("Invalid expense number!")
            return

        deleted = expenses.pop(number - 1)
        print(f"{deleted['description']} deleted successfully!")

    except ValueError:
        print("Please enter a valid number!")





# Main menu
def main():
    while True:
        print("\n===== EXPENSE TRACKER =====")
        print("1. Add an expense")
        print("2. View expenses")
        print("3. Show total")
        print("4. Exit")
        print("5. Delete an expense")

        choice = input("Choose an option: ")

        if choice == "1":
            add_expense()

        elif choice == "2":
            show_expenses()

        elif choice == "3":
            show_total()

        elif choice == "4":
            print("Goodbye!")
            break

        elif choice == "5":
            delete_expense()

        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()
