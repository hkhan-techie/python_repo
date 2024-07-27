class LandAnimals:
    def walk(self):
        print('Walk')


class WaterAnimals:
    def swim(self):
        print('Swim')


class Amphibians(LandAnimals, WaterAnimals):
    pass


amphibians = Amphibians()
amphibians.swim()
amphibians.walk()
