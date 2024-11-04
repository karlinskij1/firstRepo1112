print("Prev code")
try:
    input()
    print(10 / 2)
    print(value)
except KeyboardInterrupt:
    print("Помилка роботи з клавіатурою")
except ZeroDivisionError:
    print("Не можна ділити на нуль")
except (NameError, KeyError) as error:
    print(error)


print("Next code")



