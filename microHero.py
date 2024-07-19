import random

day = 0
PlayerCount = 0
CharacterNames = []
Nicknames = []
FullNames = []

Vocations = ["Barbarian", "Wizard", "Warrior", "Cleric", "Necromancer"]

TempPrefixes = []
Prefixes = []
TempItems = []
Items = []
TempPostfixes = []
Postfixes = []
ItemList = []

store_visited = False

class Player:
    def __init__(self, Name):
        self.Name = Name
    
    def __repr__(self):
        return self.Name

class Character:
    def __init__(self, Name, Vocation, Str, Int, Fai, MinDmg, MaxDmg, Prot):
        self.Name = Name
        self.Vocation = Vocation
        self.Str = Str
        self.Int = Int
        self.Fai = Fai
        self.MinDmg = MinDmg
        self.MaxDmg = MaxDmg
        self.Prot = Prot


    def __repr__(self):
        return f"""
                {self.Name}, the {self.Vocation}
                STR: {self.Str}
                INT: {self.Int}
                FAI: {self.Fai}

                DMG: {self.MinDmg}—{self.MaxDmg}
                Prot: {self.Prot
        }"""
    
class Enemy:
    def __init__(self, Name, Vocation, Str, Int, Fai, MinDmg, MaxDmg, Prot):
        self.Name = Name
        self.Vocation = Vocation
        self.Str = Str
        self.Int = Int
        self.Fai = Fai
        self.MinDmg = MinDmg
        self.MaxDmg = MaxDmg
        self.Prot = Prot


    def __repr__(self):
        return f"""
                {self.Name}, the {self.Vocation}
                STR: {self.Str}
                INT: {self.Int}
                FAI: {self.Fai}

                DMG: {self.MinDmg}—{self.MaxDmg}
                Prot: {self.Prot
        }"""
    
class Item:
    def __init__(self, Name):
        self.Name = Name

    def __repr__(self):
        return f"{self.Name}"

class Prefix:
    def __init__(self, Name, Effect, Modifier, Tier, PosNeg, Description, Price):
        self.Name = Name
        self.Effect = Effect
        self.Modifier = Modifier
        self.tier = Tier
        self.posneg = PosNeg
        self.description = Description
        self.price = Price
    
    def __repr__(self):
        return f"{self.Name}"

class Core:
    def __init__(self, Name, Effect, Modifier, Location, Element, Description, Price):
        self.Name = Name
        self.Effect = Effect
        self.Modifier = Modifier
        self.location = Location
        self.element = Element
        self.description = Description
        self.price = Price

    def __repr__(self):
        return f"{self.Name}"

class Postfix:
    def __init__(self, Name, Effect, Modifier, Tier, Description, Price):
        self.Name = Name
        self.Effect = Effect
        self.Modifier = Modifier
        self.tier = Tier
        self.description = Description
        self.price = Price

    def __repr__(self):
        return f"{self.Name}"
    
def unpack_lists():
    with open("micro_arena_names.lst") as NamesLst:
        CharacterNames = NamesLst.read().split(",")

    with open("micro_arena_nicknames.lst") as NicknamesLst:
        Nicknames = NicknamesLst.read().split(",") 

def generate_name(List1, List2):
    A = random.randint(0,len(CharacterNames)-1)
    B = random.randint(0,len(Nicknames)-1)
    FullName = str(List1[A] + List2[B])

def generate_hp(VNum):
    match VNum:
        case 1:
            return random.randint(50, 150)
        case 2:
            return random.randint(40, 60)
        case 3:
            return random.randint(45, 100)
        case 4:
            return random.randint(45,80)
        case 5:
            return random.randint(40, 60)

def create_character():
    CharVoc = random.randint(1,5)
    CharHP = generate_hp(CharVoc)

