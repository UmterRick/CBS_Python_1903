username = "Vlad"
age = 99

# %s - style
# greetings = "Hello, my dear, %s (%s). How are you?" % (username, age)

# .format() style
# greetings = "Hello, my dear, {} ({}). How are you?".format(username, age)

# f"{}, {}" style
greetings = f"Hello, my dear, {username} ({age}). How are you?"
print(greetings)

print("-----" * 20)
greetings = f"\tHello, my dear, \"{username}\" ({age}).\nHow are you? \\"
# greetings = f'\tHello, my dear, "{username}" ({age}).\nHow are you?'
print(greetings)

print("First symbol:", greetings[11])



