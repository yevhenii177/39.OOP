class Player:
    def __init__(self, name):
        self.name = name
        self.__health = 100
        self.__level = 1

    def take_damage(self, amount):
        self.__health -= amount

        if self.__health < 0:
            self.__health = 0

    def heal(self, amount):
        self.__health += amount

        if self.__health > 100:
            self.__health = 100

    def level_up(self):
        self.__level += 1

    def get_info(self):
        return f"Player: {self.name}, Health: {self.__health}, Level: {self.__level}"


player = Player("Hero")

# Отримання урону
player.take_damage(30)

# Лікування
player.heal(20)

# Підвищення рівня
player.level_up()

# Вивід інформації
print(player.get_info())
