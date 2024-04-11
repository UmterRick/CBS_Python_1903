"""
while True:
    print("Hello User")
    x = input("You question: ")
    if x.lower() == "stop":
        print("You got break the loop")
        break
    print("Thanks for your question")
"""

"""
x = 0
while True:
    print(f"{x=}")
    # x += 1
    if x > 10:
        break
    x += 1
"""


"""
x = 0
while x <= 100:
    if x % 2 == 0:
        print(f"Skip {x}")
        x += 1
        continue
    print(f"{x**2}")
    x += 1
"""

"""
# Break in for loop
for i in range(0, 11):
    if i == 5:
        break
    print(i)
print("Loop 1 finished")
"""

"""
# Continue in for loop
for i in range(0, 11):
    if i == 5:
        continue
    print(i)
print("Loop 2 finished")
"""