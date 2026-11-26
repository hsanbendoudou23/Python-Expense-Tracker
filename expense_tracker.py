
expenses = []

def add_expense():
    description = input("Description : ")
    amount = float(input("Montant : "))

    expenses.append({
        "description": description,
        "amount": amount
    })

    print("Depense ajoutee !")


def show_expenses():
feature-delete
    pass
def show_total():  
    pass
def delete_expense():
    if not expenses:
        print("No expenses to delete.")
        return
    if not expenses:
        print("Aucune depense enregistree.")
        return

    for number, expense in enumerate(expenses, start=1):
        print(f"{number}. {expense['description']} - "
              f"{expense['amount']:.2f}")
main

    for i, expense in enumerate(expenses, start=1):
        print(f"{i}. {expense['description']} - {expense['amount']}")

feature-delete
    choice = input("Enter expense number to delete: ")

    if not choice.isdigit():
        print("Invalid number.")
        return

    index = int(choice) - 1

    if 0 <= index < len(expenses):
        removed = expenses.pop(index)
        print(f"Deleted: {removed['description']}")
    else:
        print("Invalid number.")
def show_total():
    total = sum(item["amount"] for item in expenses)
    print(f"Total : {total:.2f}")
    main


def show_average():
    if not expenses:
        print("No expenses recorded.")
        return

    total = sum(item["amount"] for item in expenses)
    average = total / len(expenses)
    print(f"Average expense: {average:.2f}")


def main():
    while True:
        print("\n===== SUIVI DES DEPENSES =====")
        print("1. Ajouter une depense")
        print("2. Afficher les depenses")
        print("3. Afficher le total")
        print("4. Quitter")
        print("5. Delete an expense")
        print("6. Show average")
        choice = input("Votre choix : ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            show_expenses()
        elif choice == "3":
            show_total()
        elif choice =="5":
            delete_expense() 
        elif choice == "4":
            print("Au revoir !")
            break
        elif choice == "5":
            show_average()
        else:
            print("Choix invalide.")


if __name__ == "__main__":
    main()
