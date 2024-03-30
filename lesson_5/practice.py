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

triggers = "меню", "спортзал", "обслуговування"
discount = 0
if len(comment) > 60:
    discount += 15

for word in triggers:
    discount += comment.lower().count(word) * 5
print(discount)
