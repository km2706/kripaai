# nested if

products = ["1.chai", "2.coffee", "3.pani", "4.exit"]

chai_types = ["ginger", "normal"]

for product in products:
    print(product)

selected_product = int(input("Select product:"))

if selected_product == 1:
    print("chai")
    for chai in chai_types:
        print(chai)
    selected_chai = int(input("Select chai:"))
    if selected_chai == 1:
        print("ginger")
    elif selected_chai == 2:
        print("normal")
    else:
        print("biji cha nathi")
elif selected_product == 2:
    print("coffee")
elif selected_product == 3:
    print("pani")
else:
    print("biju kasu nathi")
