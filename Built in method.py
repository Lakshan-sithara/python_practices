# String Built in methods/ functions

massage = "corona vaccine is ready to use, most of them are more than 90% effective."

print(massage)
print(massage.capitalize())

Message = massage.capitalize()
print(Message)

"""# dir() function
print(dir(""))
print(dir([]))
print(dir(()))
print(dir({}))"""

print(massage.upper())
print(massage.islower())
print(massage.isupper())
print(massage.find("ready"))
print(massage[18:24])
print(massage.find("not"))

seq1 = ("192" , "168" , "40" , "90")
print(".".join(seq1))
print("/".join(seq1))
print("-".join(seq1))

mountains = ["Everest" , "Himalaya" , "Ritigala" , "Hanthana"]
print(mountains)
mountains.append("piduruthalagala")
print(mountains)

mountains.extend(["Haputhale" , "Kinihiri"])
print(mountains)

mountains.insert(2,"Mt Abu")
print(mountains)

mountains.pop()
print(mountains)

mountains.pop(3)
print(mountains)

cntr_emp1 = {"name":"santa" , "skills":"blockchin" , "code":"1024"}
print(cntr_emp1.keys())
print(cntr_emp1.values())
cntr_emp1.clear()
print(cntr_emp1)