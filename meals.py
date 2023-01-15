menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
total = 0
while True:
    try:
        item = input("Item: ").title()
        if item in menu:
            total = total + menu[item]
            quantity = round(int(input("How many: ")))
    except EOFError:
        break
print(f"Total ${float(total)*float(quantity)}")