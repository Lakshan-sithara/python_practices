"""# Break Statment
for i in "DevOps":
    print(i)
    if i == "O":
        print("found my data.")
        break
print("out of the loop")"""

# Continue Statment
for i in "DevOps":

    if i == "O":
        print("found my data.")
        continue
    print(i)
print("out of the loop")