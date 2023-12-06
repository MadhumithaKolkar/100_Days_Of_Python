# print("Welcome to the band name generator")
# city = input("What's the name of the city you grew up in?\n")
# pet_name = input("What's your pet's name?\n")
# print("Your band name could be",city+" "+pet_name)
# for i in range(10):
#     print(i)

x = "Hello"
x = list(x)
x.remove("H")
x.pop(2)
for i,n in enumerate(x):
    if n in "eo":
        x.remove(x[i])
print(x)
