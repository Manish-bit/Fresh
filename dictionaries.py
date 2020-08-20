number = input("input:")
number_index = {
    "1":"one",
    "2":"two",
    "3":"three",
    "4":"four"
}
output = ""
for x in number:
    output += number_index.get(x,"!") + " "
print(output)