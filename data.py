# gatech = open("./data/gatech.txt", "r", encoding='utf-8')
# print(gatech.read())
# print(type(gatech))

with open('./data/gatech.txt', 'r', encoding='utf-8') as file:
    content = file.read()
    print(content)
    print(content[2])
    print(type(content))