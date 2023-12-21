import random

"""# Variable Lengh Argument *args(non keyword Argument) -> this give tupple

def oder_food(min_order , *args):
    print("You have ordered: ",min_order)
    #print(args)
    for item in args:
        print("You have ordered: ", item)
    print("Your food will be delivered in 30 mins: ")
    print("Enjoy the party")

oder_food("Salad" , "Pizza" , "Biriyani" , "Soup")
"""


# Variable Lengh Argument **kwargs(non keyword Argument) -> this give dictionary

def time_activity(*args, **kwargs):
#    print(args)
#    print(kwargs)
    min = sum(args) + random.randint(0, 60)
#    print(min)
    choice = random.choice(list(kwargs.keys()))
#    print(choice)
    print(f"You have to spend {min} for {kwargs[choice]}")

time_activity(10, 20, 30, hobby="Dance", sport="Basketball", fun="Driving", Work="Devops") 
