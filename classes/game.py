import random


class bcolors:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    B0LD = "\033[1m"
    UNDERLINE = "\033[4m"


class person:
    def __init__(self, hp, mp, atk, df, magic):
        self.maxHp = hp
        self.hp = hp
        self.maxMp = mp
        self.atkh = atk - 10
        self.atkl = atk + 10
        self.df = df
        self.magic = magic = ["Attack", "Magic"]

    def generate_damage(self):
        return random.randrange(self.atkh, self.atkl)
