# ніби то шаблон
class Student:
    print("Hi")

    def __init__(self, height=160):
        self.height = height
        print("I am alive")



# створення об'єкта
first_student = Student(186)
second_student = Student(220)

#вивети інормацію про їого зріст
print(first_student.height)
print(second_student.height)

print('test')