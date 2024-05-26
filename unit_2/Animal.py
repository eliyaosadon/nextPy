class Animal:
    zoo_name = "Hayaton"

    def __init__(self, name, hunger=0):
        self.name_ = name
        self.hunger_ = hunger

    def get_name(self):
        return self.name_

    def is_hungry(self):
        return self.hunger_ > 0

    def feed(self):
        if self.is_hungry():
            self.hunger_ -= 1

    def __str__(self):
        return 'Animal'

    def talk(self):
        pass


class Dog(Animal):
    def __str__(self):
        return 'Dog'

    def talk(self):
        print('woof woof')

    def fetch_stick(self):
        print('There you go, sir!')


class Cat(Animal):
    def __str__(self):
        return 'Cat'

    def talk(self):
        print('meow')

    def chase_laser(self):
        print('Meeeeow')


class Skunk(Animal):
    def __init__(self, name, hunger=0):
        self._stink_count = 6
        super().__init__(name, hunger)

    def __str__(self):
        return 'Skunk'

    def talk(self):
        print('tsssss')

    def stink(self):
        print('Dear lord!')


class Unicorn(Animal):

    def __str__(self):
        return 'Unicorn'

    def talk(self):
        print('Good day, darling')

    def sing(self):
        print('I’m not your toy...')


class Dragon(Animal):

    def __init__(self, name, hunger=0):
        self._color = 'Green'
        super().__init__(name, hunger)

    def __str__(self):
        return 'Dragon'

    def talk(self):
        print('Raaaawr')

    def breath_fire(self):
        print('$@#$#@$')


def main():
    zoo_lst = [
        Dog("Brownie", 10),
        Cat("Zelda", 3),
        Skunk("Stinky"),
        Unicorn("Keith", 7),
        Dragon("Lizzy", 1450),
        Dog("Doggo", 80),
        Cat("Kitty", 80),
        Skunk("Stinky Jr.", 80),
        Unicorn("Clair", 80),
        Dragon("McFly", 80)
    ]

    for animal in zoo_lst:
        print(f'{animal} {animal.get_name()}')
        while animal.is_hungry():
            animal.feed()
        animal.talk()
        if isinstance(animal, Dog):
            animal.fetch_stick()
        elif isinstance(animal, Cat):
            animal.chase_laser()
        elif isinstance(animal, Skunk):
            animal.stink()
        elif isinstance(animal, Unicorn):
            animal.sing()
        elif isinstance(animal, Dragon):
            animal.breath_fire()

    print(Animal.zoo_name)


if __name__ == "__main__":
    main()
