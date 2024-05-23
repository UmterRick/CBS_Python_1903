import re

test_string = "Test1 Test2 Test3 Test4"

pattern = r"Test"
result = re.match("daskd", test_string)
print("Match:", result)
# print(dir(result))

# print(result.start())
# print(result.end())
#
# print(result.string)

result = re.search("skdnas", test_string)
print("Search:", result)

result = re.findall(pattern, test_string)
print("Findall:", result)
for i in result:
    print(type(i), i)


result = re.finditer(pattern, test_string)
print("Finditer:", result)

# result_list = [i for i in result]
# print(result_list)
for i in result:
    print(type(i), i)


new_test_string = re.sub("T", "Qu", test_string)
print(test_string)
print(new_test_string)

splited_string = re.split("st", new_test_string, maxsplit=2)
print(splited_string)


compiled_pattern = re.compile(pattern="T")
print(compiled_pattern)
print(type(compiled_pattern))
print(dir(compiled_pattern))


compiled_pattern.match(test_string)

import re

pattern1 = '^L{0,3}(CM|CD|D?C{0,3})(XC|XL|M?X{0,3})(IX|IV|V?I{0,3})$'

pattern_compile = re.compile(pattern1)
print(re.search(pattern1, 'LDMV'))
pattern_compile.search("MDLV")
