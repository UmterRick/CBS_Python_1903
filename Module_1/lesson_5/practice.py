"""
# Sort numbers from user input

input_numbers = input("Type numbers ").split(' ')  # Type numbers with space between
# print(input_numbers)
for i in range(0, len(input_numbers)):
    input_numbers[i] = int(input_numbers[i])  # Make all elements in list integers

# print(input_numbers)
print(tuple(sorted(input_numbers))) # Sort elements and convert result to tuple
"""

comment = """
Всім привіт, я з курорту "Морська зірка". Чудове меню, відстуній спортзал, 
хотілось спортзал, але приємне обслуговування! Дякую 
"""

# triggers = "меню", "спортзал", "обслуговування"
# discount = 0
# if len(comment) > 60:
#     discount += 15
#
# for word in triggers:
#     discount += comment.lower().count(word) * 5
# print(discount)

triggers = ("меню", "спортзал", "обслуговування")
'''
Скількі разів повторювались слова тригери в тексті
за кожне повторення +5%
Якщо текст >60 символів: + 15%
'''
# discount = 0
# for trigger_word in triggers:
#     discount_per_word = comment.lower().count(trigger_word) * 5
#     discount += discount_per_word
#
# if len(comment) > 60:
#     discount += 15

rgb_colour = tuple(input("Set Red, Green, Blue: ").split(","))
# print(rgb_colour, type(rgb_colour))

possible_range = range(0, 256)

for colour in rgb_colour:
    if not colour.isdigit() or int(colour) not in possible_range:
        print("Invalid colour value")
        exit()
print(rgb_colour, type(rgb_colour))
