class Dog:
    def __init__(self, name, age, coat_color):
        self.name = name
        self.age = age
        self.coat_color = coat_color

    def description(self):
        print(f"Name: {self.name}, Age: {self.age} years")

    def get_info(self):
        print(f"Coat color: {self.coat_color}")


class JackRussellTerrier(Dog):
    def __init__(self, name, age, coat_color, weight):
        super().__init__(name, age, coat_color)
        self.weight = weight

    def description(self):
        print(f"Name: {self.name}, Age: {self.age} years, Weight: {self.weight} lbs")

    def bark(self):
        print("Barking: Woof! Woof!")


class Bulldog(Dog):
    def __init__(self, name, age, coat_color, size):
        super().__init__(name, age, coat_color)
        self.size = size

    def description(self):
        print(f"Name: {self.name}, Age: {self.age} years, Size: {self.size}")

    def snore(self):
        print("Snoring: Zzzzzz...")


# Create objects of Dog, JackRussellTerrier, and Bulldog classes
dog1 = Dog("Buddy", 5, "Brown")
dog2 = JackRussellTerrier("Max", 3, "White and Tan", 10)
dog3 = Bulldog("Rocky", 4, "Fawn", "Medium")

# Call methods on the objects
dog1.description()
dog1.get_info()

dog2.description()
dog2.get_info()
dog2.bark()

dog3.description()
dog3.get_info()
dog3.snore()
