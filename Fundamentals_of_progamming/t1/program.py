from functions import *
def menu():
    print("This is your menu")
    print("1. Add product")
    print("2. Remove product")
    print("3. View products in descending order of name")
    print("4.Total ")
    print("5. Exit")

def start():
    list=[]
    list=[create_product("honey",3,6),
          create_product("towel",10,5),
          create_product("chair",35,50)]
    while True:
        menu()
        command=input("Enter your choice: ")

        if command == "1":
            print("add <name> <price> <quantity>")
            text = input("Enter command:")
            x = text.split(' ')
            if x[0] == "add":
                if len(x) == 4:
                    try:
                        add_product(list, x[1], x[2], x[3])
                    except ValueError as e:
                        print(e)
                else:
                    print("Invalid input: The command requires exactly 3 parameters.")
            else:
                print("Invalid choice. Please try again.")
        elif command == "2":
            print("remove <name>")
            text = input("Enter the product:")
            x = text.split(' ')
            if x[0] == "remove":
                if len(x) == 2:
                    try:
                        remove_product(list, x[1])
                    except ValueError as e:
                        print(e)
                else:
                    print("Invalid input: The command requires exactly 1 parameter (name).")
            else:
                    print("Invalid choice. Please try again.")
        elif command == "3":
                sorted_products = list_sorted(list)
                print("Products sorted in descending order of name:")
                for product in sorted_products:
                    print(to_string(product))
        elif command == "4":
            total = total_price(list)
            print(total)
        elif command == "5":
            print("You chose to exit the menu")
            break
        else:
            print("Not a command. Please try again.")
        print(list)
