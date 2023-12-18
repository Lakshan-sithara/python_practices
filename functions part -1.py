# Defining function

"""def add(arg1, arg2):
    total = arg1 + arg2
    return total

out = add(2,4)
print(out)
print(add(10,20))

def adder (num1, num2):
    total = num1 + num2
    print(total)
adder(10,50)
print(adder(30,40))



def sum(arg):
    x = 0
    for i in arg:
        x = x + i
    return x


out = sum([1, 2, 3])
print(out)
"""

# Defult Argument

def greetings(MSG = "morning"):
    print(f"Good {MSG}.")
    print("Welcome to Functions.")

greetings("Afternoon")

# keyword Argument
def vac_feedback(vac , efficacy):
    print(f"{vac} vaccine is have {efficacy}% efficacy.")
    if (efficacy > 50) and (efficacy <= 75):
        print("Seems not so effectively vaccinated.")
    elif (efficacy>75) and (efficacy <=90):
        print("Can consider this vaccine.")
    elif efficacy>=90:
        print("Can consider this vaccine.")
    else:
        print("Can't consider this vaccine.")
vac_feedback("pfizer" , 40)

vac_feedback(efficacy=80,vac="unknown")