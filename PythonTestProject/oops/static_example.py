class Player:
    count = 0

    def __init__(self, name):
        self.name = name
        Player.count += 1

    @staticmethod
    def get_count():
        return Player.count


messi = Player('messi')
ronaldo = Player('Ronaldo')

print("first count details")
print(Player.get_count())
print(messi.get_count())
print(ronaldo.get_count())

print("second count details")
print(Player.count)
print(messi.count)
print(ronaldo.count)

print("third count details")
messi.count = 100
print(Player.count)
print(messi.count)
print(ronaldo.count)

print("fourth count details")
Player.count = 50
print(Player.count)
print(messi.count)
print(ronaldo.count)
