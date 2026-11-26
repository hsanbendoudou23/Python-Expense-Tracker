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
    pass
def show_total():  
    pass
def delete_expense():
    if not expenses:
        print("No expenses to delete.")
        return

    for i, expense in enumerate(expenses, start=1):
        print(f"{i}. {expense['description']} - {expense['amount']}")

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


def main():
    while True:
        print("\n===== SUIVI DES DEPENSES =====")
        print("1. Ajouter une depense")
        print("2. Afficher les depenses")
        print("3. Afficher le total")
        print("4. Quitter")
        print("5. Delete an expense")

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
        else:
            print("Choix invalide.")


if __name__ == "__main__":
    main()
