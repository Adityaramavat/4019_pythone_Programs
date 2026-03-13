#. Write a program to create a list and perform various operations on list using menu.
my_list = []

while True:
    print("\n--- LIST OPERATIONS MENU ---")
    print("1. Add element")
    print("2. Remove element")
    print("3. Display list")
    print("4. Search element")
    print("5. Sort list")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        element = int(input("Enter element to add: "))
        my_list.append(element)
        print("Element added.")

    elif choice == 2:
        element = int(input("Enter element to remove: "))
        if element in my_list:
            my_list.remove(element)
            print("Element removed.")
        else:
            print("Element not found.")

    elif choice == 3:
        print("List elements:", my_list)

    elif choice == 4:
        element = int(input("Enter element to search: "))
        if element in my_list:
            print("Element found at index", my_list.index(element))
        else:
            print("Element not found.")

    elif choice == 5:
        my_list.sort()
        print("List sorted:", my_list)

    elif choice == 6:
        print("Exiting program.")
        break

    else:
        print("Invalid choice. Please try again.")