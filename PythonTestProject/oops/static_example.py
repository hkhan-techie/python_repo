class Player:
    count = 0

    def __init__(self, name):
        self.name = name
        Player.count+=1

    @staticmethod
    def get_count():
        return Player.count

messi = Player('messi')
ronaldo = Player('Ronaldo')

print(Player.get_count())
print(messi.get_count())
print(ronaldo.get_count())



print(Player.count)
print(messi.count)
print(ronaldo.count)

messi.count=100
print(Player.count)
print(messi.count)
print(ronaldo.count)

Player.count=50
print(Player.count)
print(messi.count)
print(ronaldo.count)


