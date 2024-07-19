import random

day = 0
PlayerCount = 0
Names = []
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

Player = None

class User:
    def __init__(self, Name):
        self.Name = Name
    
    def __repr__(self):
        return self.Name

class Character:
    def __init__(self, Name, HP, MaxHP, Vocation, Str, Int, Fai, MinDmg, MaxDmg, Prot):
        self.Name = Name
        self.HP = HP
        self.MaxHP = MaxHP
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
    def __init__(self, Name, HP, MaxHP, Vocation, Str, Int, Fai, MinDmg, MaxDmg, Prot):
        self.Name = Name
        self.HP = HP
        self.MaxHP = MaxHP
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
    global Names
    global Nicknames
    
    with open("names.lst") as NamesLst:
        Text = NamesLst.read()
        Names = Text.split(",")

    with open("nicknames.lst") as NicknamesLst:
        Text = NicknamesLst.read()
        Nicknames = Text.split(",")

def create_player(Name):
    global Player
    Player = User(Name)

def generate_name(List1, List2):
    A = random.randint(0,len(Names)-1)
    B = random.randint(0,len(Nicknames)-1)
    FullName = str(List1[A] + List2[B])
    return FullName

def create_character():
    CharName = generate_name(Names, Nicknames)
    VocNum = random.randint(1,5)
    match VocNum:
        case 1:
            CharVoc = "Barbarian"
            CharHP = random.randint(50,150)
            CharMaxHP = CharHP
            CharStr = random.randint(12,20)
            CharInt = random.randint(5,10)
            CharFai = random.randint(7,15)
            CharMinDMG = random.randint(15,20)
            CharMaxDMG = random.randint(30,40)
            CharProt = random.randint(8,10)
        case 2:
            CharVoc = "Wizard"
            CharHP = random.randint(30,60)
            CharMaxHP = CharHP
            CharStr = random.randint(5,8)
            CharInt = random.randint(12,20)
            CharFai = random.randint(5,8)
            CharMinDMG = random.randint(20,30)
            CharMaxDMG = random.randint(40,60)
            CharProt = random.randint(2,6)
        case 3:
            CharVoc = "Warrior"
            CharHP = random.randint(60,80)
            CharMaxHP = CharHP
            CharStr = random.randint(10,18)
            CharInt = random.randint(7,15)
            CharFai = random.randint(5,8)
            CharMinDMG = random.randint(12,18)
            CharMaxDMG = random.randint(25,30)
            CharProt = random.randint(15,20)
        case 4:
            CharVoc = "Cleric"
            CharHP = random.randint(35,50)
            CharMaxHP = CharHP
            CharStr = random.randint(7,12)
            CharInt = random.randint(8,13)
            CharFai = random.randint(12,20)
            CharMinDMG = random.randint(8,15)
            CharMaxDMG = random.randint(18,25)
            CharProt = random.randint(5,8)
        case 5:
            CharVoc = "Necromancer"
            CharHP = random.randint(25,55)
            CharMaxHP = CharHP
            CharStr = random.randint(5,8)
            CharInt = random.randint(9,17)
            CharFai = random.randint(2,4)
            CharMinDMG = random.randint(9,17)
            CharMaxDMG = random.randint(18,20)
            CharProt = random.randint(5,8)
    
    Char = Character(CharName, CharHP, CharMaxHP, CharVoc, CharStr, CharInt, CharFai, CharMinDMG, CharMaxDMG, CharProt)
    Player.Char = Char

PlayerName = input("\nWhat is your name? ")
unpack_lists()
create_player(PlayerName)
create_character()
print(f"""
        Hello, {Player.Name}! Welcome to MicroHero!
        Your champion for today is {Player.Char.Name}, the {Player.Char.Vocation}
        HP: {Player.Char.HP} / {Player.Char.MaxHP}
        STR: {Player.Char.Str}
        INT: {Player.Char.Int}
        FAI: {Player.Char.Fai}
        Min.DMG: {Player.Char.MinDmg}
        Max.DMG: {Player.Char.MaxDmg}
        Protection: {Player.Char.Prot}
        """)