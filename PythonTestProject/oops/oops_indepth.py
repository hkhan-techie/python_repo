class Planet:
    def __init__(self, name, distance_from_sun):
        self.name = name
        self.distance_from_sun = distance_from_sun


planet = Planet('Earth', 5000)
planet.speed = 1000

print(f'{planet.name}, {planet.distance_from_sun}, {planet.speed}')