food = 0
Travel = 0
Groceries = 0
personal_expenses = 0
others = 0
total = 0
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
        # switch cases for category choosing
            while x != 6:
                print("1.Food")
                print("2.Travel")
                print("3.Groceries")
                print("4.personal expenses")
                print("5.other")
                print("6.exit")
                x = int(input("enter your choice(1,2,3,4,5):"))

                match x:
                    case 1:
                        food = Toprintval()
                        print("food : ", food)

                    case 2:
                        Travel = Toprintval()
                        print("Travel : ", Travel)
                    case 3:
                        Groceries = Toprintval()
                        print("Groceries : ", Groceries)
                    case 4:
                        personal_expenses = Toprintval()
                        print("personal expenses : ", personal_expenses)
                    case 5:
                        others = Toprintval()
                        print("others : ", others)
                    case 6:
                        print("expenses added")
                        break
        # to view expenses
                with open("expenses.txt", "w") as f:
                    for category, amount in expenses.items():
                        f.write(f"{category}:{amount}\n")
        case 2:

                    print("\n------ Expenses ------")
                    print("food : ", food)
                    print("Travel : ", Travel)
                    print("Groceries : ", Groceries)
                    print("personal expenses : ", personal_expenses)
                    print("others : ", others)
        case 3:
                    print("show total")
                    total = food + Travel + Groceries + personal_expenses + others
                    print("total : ",total)
        case 4:
                    print("thank you")
                    break










