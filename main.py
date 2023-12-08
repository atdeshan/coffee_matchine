materials = {"milk":200,"water":500,"coffee":50.0,"money":0.0}
next_one = True
# type of coffee
espresso = {"milk":0,"water":50,"coffee":18.0,"money":1.5}
latte = {"milk":150,"water":200,"coffee":24.0,"money":2.5}
cappuchino = {"milk":100,"water":250,"coffee":24.0,"money":3.0}

# available materials 
def get_report():
    print(f"milk : {materials["milk"]}\nwater : {materials["water"]}\
          \ncoffee : {materials["coffee"]}\nmoney : {materials["money"]}")
get_report()

# coffee making process
def make_a_coffee(choice):
    if (choice == "espresso" or choice == "ESPRESSO") \
        and (materials["milk"]>espresso["milk"]\
              and materials["water"]>espresso["water"]\
                and materials["coffee"]>espresso["coffee"] ):
        materials["money"]+=espresso["money"]
        materials["milk"]-=espresso["milk"]
        materials["water"]-=espresso["water"]
        materials["coffee"]-=espresso["coffee"]
        print("this is yours espresso")
    elif (choice == "latte" or choice == "LATTE") \
        and (materials["milk"]>=latte["milk"]\
              and materials["water"]>=latte["water"]\
                and materials["coffee"]>=latte["coffee"]):
        materials["money"]+=latte["money"]
        materials["milk"]-=latte["milk"]
        materials["water"]-=latte["water"]
        materials["coffee"]-=latte["coffee"]
        print("this is your latte")
    elif (choice == "cappuchino" or choice == "CUPPUCHINO") \
        and (materials["milk"]>=cappuchino["milk"]\
              and materials["water"]>=cappuchino["water"]\
                and materials["coffee"]>=cappuchino["coffee"]):
        materials["money"]+=cappuchino["money"]
        materials["milk"]-=cappuchino["milk"]
        materials["water"]-=cappuchino["water"]
        materials["coffee"]-=cappuchino["coffee"]
        print("this is your cappuchino")
    elif choice == "report":
        get_report()
    else:
        print("NO AWAILABLE RESOURCES FOR MAKING A COFFEE")
        global next_one
        next_one = False

while (next_one):
    make_a_coffee(input("""\nThere are three types of coffees
        *latte
        *espresso
        *capuchino\n"""))
    exit = input("exit/continue : ")
    if exit == "exit":
        next_one = False
