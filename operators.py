#membership operator

tupple = ("IOT", "devops", 23,10,3.14)
ans = "devops" in tupple
print(ans)

ans = "game" not in tupple
print(ans)

#identity operator

a = 12
b = 12

result = a is b
print(result)

result = a is not b
print(result)