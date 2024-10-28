import random



class Human:
    def __init__(self, name="Human", job=None, home=None, car=None):
        self.name = name
        self.money = 100
        self.gladness = 50
        self.satiety = 50
        self.job = job
        self.home = home
        self.car = car

    def get_job(self):
       if self.car.drive():
           pass
       else:
           self.to_repair()
           return
       self.job = Job(job_list)

    def get_home(self):
        pass
    def get_car(self):
        pass

    def eat(self):
        if self.home.food <= 0:
            self.shopping("food")
    def work(self):
        pass
    def shopping(self, manage):
        pass
    def chill(self):
        pass
    def clean_home(self):
        pass
    def to_repair(self):
        pass


    def days_indexes(self, day):
        pass

    def is_alive(self):
        if(self.gladness < 0):
            print(f"{self.name} has depression ...")
            return False
        if(self.satiety < 0):
            print(f"{self.name} is dead...")
            return False
        if (self.money < -500):
            print(f"{self.name} is bankrupt ...")
            return False
        return True

    def live(self,day):
        if self.is_alive() == False:
            return False


class Auto:
    def __init__(self, brand_list):
        self.brand = random.choice(list(brand_list))
        self.fuel = brand_list[self.brand]["fuel"]
        self.strength = brand_list[self.brand]["strength"]
        self.consumption = brand_list[self.brand]["consumption"]

    def drive(self):
        if self.strength > 0 and self.fuel >= self.consumption:
            self.fuel -= self.consumption
            return True
        else:
            print("Car cannot move")
            return False

class House:
    def __init__(self):
        self.food = 0
        self.mess = 0


class Job:
    def __init__(self, job_list):
        self.job = random.choice(list(job_list))
        self.salary = job_list[self.job]['salary']
        self.gladness = job_list[self.job]['gladness']


job_list = {
    'Java Developer' :
        {'salary': 50, 'gladness': 10, },
    'Python Developer' :
        {'salary': 100, 'gladness': 10, },
    'C++ Developer' :
        {'salary': 100, 'gladness': 5, },
    'Rust Developer' :
        {'salary': 50, 'gladness': 3, },
}

brands_of_cars = {
    'BMW' : {'fuel': 100, 'strength': 100, 'consumption': 6 },
    'Volvo' : {'fuel': 200, 'strength': 120, 'consumption': 20 },
    'Ferrari' : {'fuel': 80, 'strength': 120, 'consumption': 8 },
}

first_car = Auto(brands_of_cars)