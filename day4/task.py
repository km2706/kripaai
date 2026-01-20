products = ["1. tea",
             "2. coffee", 
             "3. burger", 
             "4. pizza",
             "5. sandwich",
             "6. Exit"
]
tea_types = ["1.ginger",
            "2.normal"
]
coffee_types = [
    "1. Hot Coffee",
    "2. Cold Coffee",
    "3. Black Coffee",
    "4. Cappuccino"
]
burger_types = [
    "1. Veg Burger",
    "2. Cheese Burger",
    "3. Aloo Tikki Burger",
    "4. Double Cheese Burger"
]
pizza_types = [
    "1. Margherita Pizza",
    "2. Veg Pizza",
    "3. Paneer Pizza",
    "4. Cheese Burst Pizza"
]
sandwich_types = [
    "1. Veg Sandwich",
    "2. Cheese Sandwich",
    "3. Grilled Sandwich",
    "4. Paneer Sandwich"
]

while True:
    print("=======CAFE MENU=======")
    for product in products:
        print(product)

    selected_product = int(input("Select product: "))

    if selected_product == 1:
        print("\nTea")
        for tea in tea_types:
            print(tea)

        selected_tea = int(input("Select tea: "))
        if selected_tea == 1:
            print("ginger chai selected")
        elif selected_tea == 2:
            print("normal chai selected")
        else:
            print("biji chai nathi")

    elif selected_product == 2:
        print("\nCoffee")
        for coffee in coffee_types:
            print(coffee)

        selected_coffee = int(input("Select coffee: "))
        if selected_coffee == 1:
            print("Hot Coffee selected")
        elif selected_coffee == 2:
            print("Cold coffee selected")
        elif selected_coffee == 3:
            print("Black Coffee selected")
        elif selected_coffee == 4:
            print("Cappuccino selected")
        else:
            print("biji coffee nathi")

    elif selected_product == 3:
        print("\nBurger")
        for Burger in burger_types:
            print(Burger)

        selected_burger = int(input("Select Burger: "))
        if selected_burger == 1:
            print("Veg Burger selected")
        elif selected_burger == 2:
            print("Cheese Burger selected")
        elif selected_burger == 3:
            print("Aloo Tikki Burger selected")
        elif selected_burger == 4:
            print("Double Cheese Burger selected")
        else:
            print("biji coffee nathi")

    elif selected_product == 4:
        print("\n")
        for pizza in pizza_types:
            print(pizza)

        selected_pizza = int(input("Select pizza: "))
        if selected_pizza == 1:
            print("Margherita Pizza selected")
        elif selected_pizza == 2:
            print("Veg Pizza selected")
        elif selected_pizza == 3:
            print("Paneer Pizza selected")
        elif selected_pizza == 4:
            print("Cheese Burst Pizza selected")
        else:
            print("biji coffee nathi")

    
    elif selected_product == 5:
        print("\n")
        for sandwich in sandwich_types:
            print(sandwich)

        selected_sandwich = int(input("Select pizza: "))
        if selected_sandwich == 1:
            print("Veg Sandwich selected")
        elif selected_sandwich == 2:
            print("Cheese Sandwich selected")
        elif selected_sandwich == 3:
            print("Grilled Sandwich selected")
        elif selected_sandwich == 4:
            print("Paneer Sandwich selected")
        else:
            print("biji coffee nathi")

    elif selected_product == 6:
        print("Thank you for visiting our Cafe ")

else:
    print("biju bija cafe ma malse")
