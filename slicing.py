planet1 = "closest to sun"
print(planet1)

print(planet1[0])
print(planet1[1])

print(planet1[-1])
print(planet1[-2])

#slicing a string, get a substring from a string

print(planet1[1:4])
print(planet1[:])
print(planet1[:7])

#Sluicing tupple

devops = ("linux", "vagrent", "bash scripting", "AWS", "jenkins", "python", "ancible")

print(devops[0])
print(devops[2:4])
print(devops[2:4][0])
print(devops[2:4][0][5:11])
print(devops[2:4][0][5:11][-1])


#Sluicing list
print("sluicing list")

devops = ["linux", "vagrent", "bash scripting", "AWS", "jenkins", "python", "ancible"]

print(devops[0])
print(devops[2:4])
print(devops[2:4][0])
print(devops[2:4][0][5:11])
print(devops[2:4][0][5:11][-1])

#dictionary example

print("dectionary example")

skills = {"devops":("AWS", "jenkins", "python", "ancible") , "development":["java" , "node JS" , ".net"]}
print(skills["development"])
print(skills["devops"][-1])
print(skills["devops"][1][:3])