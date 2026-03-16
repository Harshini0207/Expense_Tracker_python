import json

try:
    with open("expenses.json", "r") as f:
        expenses = json.load(f)
except FileNotFoundError:
    expenses = {"food": 0, "Travel": 0, "Groceries": 0, "Personal": 0, "Others": 0}
while True:
    print("Expense Tracker")
    print("1.Add expenses")
    print("2.view expenses")
    print("3.show total")
    print("4.exit")
    y = int(input("choice: "))

    match y:
        case 1:
            def Toprintval():
                          vals = int(input("enter value : "))
                          if(vals < 0):
                              print("expense cannot be negative")
                          return vals
            x = 0
            while x != 6:
                print("1.Food\n2.Travel\n3.Groceries\n4.personal expenses\n5.Others\n6.Exit")
                x = int(input("Enter your choice (1-6): "))
        # switch cases for category choosing
                categories = {
                    1: "food",
                    2: "Travel",
                    3: "Groceries",
                    4 :"personal_expenses",
                    5: "others"
                }
                if x in [1,2,3,4,5]:
                        expenses[categories[x]] += Toprintval()
                        with open("expenses.json", "w") as f:
                            json.dump(expenses, f)

                else:
                    print("expenses added")

                    #to view expenses
        case 2:

                    print("\n------ Expenses ------")
                    for category, amount in expenses.items():
                        print(category, ":", amount)
        case 3:
                    total = 0
                    print("show total")
                    total = sum(expenses.values())
                    print("total : ",total)
        case 4:
                    print("thank you")
                    break










