
def display_menu():
    print("Shopping List Manager")
    print(f"1. Add Item")
    print(f"2. Remove Item")
    print(f"3. View list")
    print(f"4. Exit")

def main():
    shopping_list = []

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            item = int(input("Enter the item to add:"))
            shopping_list.append(item)
            print(f"'{item}', has been added to the shopping list")

        elif choice == '2' :
             item = input("Enter the item to remove: ")
             if item in shopping_list:
                shopping_list.remove(item)
                print(f"'{item}' removed from your shopping list.")
             else:
                print(f"'{item}' not found in your shopping list.")

        elif choice == '3':
            if shopping_list:
                print("Your Shopping List:")
                for i, item in enumerate(shopping_list, 1):
                    print(f"{i}. {item}")
            else:
                print("Your shopping list is empty.")
        
        elif choice == '4':
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()



    