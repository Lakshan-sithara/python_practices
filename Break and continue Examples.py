"""import random
VACCINES = ["moderna","pfizer","synophrme", "covaxin", "sputnic v"]

random.shuffle(VACCINES)
print(VACCINES)

LUCKY = random.choice(VACCINES)
print(LUCKY)

for vac in VACCINES:
    print(f"**********TESTING VACCINES {LUCKY}")
    if vac == LUCKY:
        print("###############################")
        print(f"{LUCKY} vaccine, Test successfully completed")
        print("###############################")
        break
    print("XXXXXXXXXXXX")
    print("Test failed")
    print("XXXXXXXXXXXX")
"""
import random
VACCINES = ["moderna","pfizer","synophrme", "covaxin", "sputnic v"]

random.shuffle(VACCINES)
print(VACCINES)

LUCKY = random.choice(VACCINES)
print(LUCKY)

for vac in VACCINES:
    print(f"**********TESTING VACCINES {vac}")
    if vac == LUCKY:
        print("###############################")
        print(f"{LUCKY} vaccine, Test successfully completed")
        print("###############################")
        continue
    print("XXXXXXXXXXXX")
    print("Test failed")
    print("XXXXXXXXXXXX")


