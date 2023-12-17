"""
this script will implement our knowledge of on
conditional and different datatype
"""
print("this it organization has various skills sets.")
print("find out your match.")
print("enter the capitalised value: ")

devops = ["linux", "vagrant", "bash scripting", "AWS", "jenkins", "python", "puppet", "anciable"]
development = ["java", "node JS", ".net"]
cntr_emp1 = {"name":"santa" , "skills":"blockchin" , "code":"1024"}
cntr_emp2 = {"name":"john" , "skills":"AI" , "code":"1218"}

user_skills = input("enter your skills: ")
#print(user_skills)

#checking the database if we have this skills
if user_skills in devops:
    print(f"we have {user_skills} in development team.")
elif (user_skills in development):
    print(f"we have {user_skills} in development team.")
elif (user_skills in cntr_emp1.values()) or (user_skills in cntr_emp2.values()):
    print(f"we have contract employees in with {user_skills} skills.")
else :
    print("skill not found")
    print("please check if you  check the spelling of the skills.")
