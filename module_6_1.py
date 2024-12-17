class Animal:
    def __init__(self, name):
        self.name = name
        self.alive = True
        self.fed = False

class Plant:
    def __init__(self, name):
        self.edible = False
        self.name = name

class Mammal(Animal):
    def eat(self, food):
        if food.edible:
            print(f"{self.name} съел {food.name}")
            self.fed = True
        else:
            print(f"{self.name} не стал есть {food.name}")
            self.alive = False

class Predator(Mammal):
    pass

class Herbivore(Mammal):
    pass

class Flower(Plant):
    pass

class Fruit(Plant):
    def __init__(self, name):
        super().__init__(name)
        self.edible = True


lion = Predator("Лев")
rabbit = Herbivore("Кролик")
rose = Flower("Роза")
apple = Fruit("Яблоко")


lion.eat(rose)
print(f"Жив ли {lion.name}? {'Да' if lion.alive else 'Нет'}")


rabbit.eat(apple)
print(f"Насыщен ли {rabbit.name}? {'Да' if rabbit.fed else 'Нет'}")
print(f"Жив ли {rabbit.name}? {'Да' if rabbit.alive else 'Нет'}")