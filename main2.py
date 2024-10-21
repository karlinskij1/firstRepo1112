import datetime

#output

def testFunc(show: bool):
    value = [1, "2", 3, 4]
    if show:
        print(value)
        print(type(value))
    return value

result = testFunc(False)
# name = input("Ім'я: ")
#
#
#
# print(f'Ваше ім\'я {name}')
print(datetime.datetime.now())

file = open("text.txt", "a")
file.write("Hello")
file.close()