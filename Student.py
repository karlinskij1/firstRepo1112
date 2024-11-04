# ніби то шаблон
import datetime

class Student:
    def __init__(self,name:str, surname:str, birthdate, height=160):
        #  помилка, якщо name не є str
        if(type(name) != str):
            raise TypeError(f"Name must be str type. Not a '{type(name)}'")
        # помилка, якщо surname не є str
        if (type(surname) != str):
            raise TypeError(f"Surname must be str type. Not a '{type(surname)}'")
        # помилка, якщо birthdate не є str
        # помилка, якщо birthdate більший ніж поточний день
        # помилка, якщо height не є int/float
        # помилка, якщо height менший або дорівнює нулю
        self.name = name
        self.surname = surname
        # 25.10.2006
        self.birthdate = datetime.datetime.strptime(birthdate, '%d.%m.%Y')
        print(self.birthdate.date() < datetime.date.today())
        self.height = height
        print(f"I am {self.name}")

    def printStudent(self):
        print(f"Name: {self.name}")
        print(f"Surname: {self.surname}")
        print(f"Birthdate: {self.birthdate.strftime('%d.%m.%Y')}")
        print(f"Height: {self.height}")

    def __str__(self):
        return f"Name: {self.name}\nSurname: {self.surname}\nBirthdate: {self.birthdate.strftime('%d.%m.%Y')}\nHeight: {self.height}\n"

    def __int__(self):
        age = (datetime.datetime.now()-self.birthdate)
        return int(age.days / 365)




# створення об'єкта
first_student = Student("vlad", 'karlinskij', '04.11.2000',186)
second_student = Student('oleg', 'palkin', '25.5.2000',220)

first_student.printStudent()

print('------------------------------')
print(type(first_student.__str__()))
print(first_student)
print('------------------------------')
print(type(first_student.__int__()))
print(int(first_student))

