import random
import time

EncounterCounter = 0
PositiveEncounters = 0
Battles = 0
ItemsFound = 0
ItemsKept = 0
GoldAcquired = 0

Names = []
Nicknames = []
FullNames = []

Vocations = ["Barbarian", "Wizard", "Warrior", "Cleric", "Necromancer"]

Prefixes = []
Cores = []
Postfixes = []
EnemyMolds = []
Monsters = []
Encounters = []

Player = None

class User:
    def __init__(self, Name):
        self.Name = Name
    
    def __repr__(self):
        return self.Name

class Character:
    def __init__(self, Name, HP, MaxHP, Vocation, Str, Int, Fai, MinDmg, MaxDmg, Prot, InventorySize=0, InventoryMaxSize=10, Exp=0, ToLevel=100, Gold=50, Level=1):
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
        self.Inventory = None
        self.InventorySize = InventorySize
        self.InventoryMaxSize = InventoryMaxSize
        self.Exp = Exp
        self.ToLevel = ToLevel
        self.Gold = Gold
        self.Level = Level

    def __repr__(self):
        return f"""
                {self.Name} / The {self.Vocation}
                HP: {self.HP} / {self.MaxHP}
                STR: {self.Str}
                INT: {self.Int}
                FAI: {self.Fai}

                DMG: {self.MinDmg}—{self.MaxDmg}
                Prot: {self.Prot}
                
                Inventory: {self.Inventory}"""  

class Enemy:
    def __init__(self, Name, MinHP, MaxHP, Vocation, MinStr, MaxStr, MinInt, MaxInt, MinFai, MaxFai, MinDmgMin, MinDmgMax, MaxDmgMin, MaxDmgMax,
                 ProtMin, ProtMax, Tier, Exp):
        self.Name = Name
        self.MinHp = MinHP
        self.MaxHP = MaxHP
        self.Vocation = Vocation
        self.MinStr = MinStr
        self.MaxStr = MaxStr
        self.MinInt = MinInt
        self.MaxInt = MaxInt
        self.MinFai = MinFai
        self.MaxFai = MaxFai
        self.MinDmgMin = MinDmgMin
        self.MinDmgMax = MinDmgMax
        self.MaxDmgMin = MaxDmgMin
        self.MaxDmgMax = MaxDmgMax
        self.ProtMin = ProtMin
        self.ProtMax = ProtMax
        self.Tier = Tier
        self.Exp = Exp

    def __repr__(self):
        return self.Name
    
class Item:
    def __init__(self, Prefix, Core, Postfix):
        self.Prefix = Prefix
        self.Core = Core
        self.Postfix = Postfix
        self.Name = self.Prefix.Name + self.Core.Name + self.Postfix.Name
        self.Price = self.Prefix.Price + self.Core.Price + self.Postfix.Price
        self.Location = self.Core.Location

    def __repr__(self):
        return f"{self.Name}"
    
class Prefix:
    def __init__(self, Name, Effect, Modifier, Tier, PosNeg, Description, Price):
        self.Name = Name
        self.Effect = Effect
        self.Modifier = Modifier
        self.Tier = Tier
        self.PosNeg = PosNeg
        self.Description = Description
        self.Price = Price
    
    def __repr__(self):
        return f"{self.Name}"

class Core:
    def __init__(self, Name, Effect, Modifier, Location, Element, Description, Price, Tier):
        self.Name = Name
        self.Effect = Effect
        self.Modifier = Modifier
        self.Location = Location
        self.Element = Element
        self.Description = Description
        self.Price = Price
        self.Tier = Tier

    def __repr__(self):
        return f"{self.Name}"

class Postfix:
    def __init__(self, Name, Effect, Modifier, Tier, Description, Price):
        self.Name = Name
        self.Effect = Effect
        self.Modifier = Modifier
        self.Tier = Tier
        self.Description = Description
        self.Price = Price

    def __repr__(self):
        return f"{self.Name}"
    
def unpack_lists():
    global Names
    global Nicknames
    global Prefixes
    global Cores
    global Postfixes
    global EnemyMolds
    global Encounters
    
    with open("names.lst") as NamesLst:
        Text = NamesLst.read()
        Names = Text.split(",")

    with open("nicknames.lst") as NicknamesLst:
        Text = NicknamesLst.read()
        Nicknames = Text.split(",")

    with open("item_prefixes.lst") as PrefixesLst:
        Text = PrefixesLst.read()
        TempLst = Text.split(";")
        for Element in TempLst:
            Stat = Element.split(",")
            TempPrefix = Prefix(Stat[0], Stat[1], int(Stat[2]), int(Stat[3]), Stat[4], Stat[5], int(Stat[6]))
            Prefixes.append(TempPrefix)
        print(Prefixes)

    with open("item_cores.lst") as CoresLst:
        Text = CoresLst.read()
        TempLst = Text.split("\n")
        for Element in TempLst:
            Stat = Element.split(",")
            TempCore = Core(Stat[0], Stat[1], Stat[2], Stat[3], Stat[4], Stat[5], int(Stat[6]), int(Stat[7]))
            Cores.append(TempCore)
        print(Cores)

    with open("item_postfixes.lst") as PostfixesLst:
        Text = PostfixesLst.read()
        TempLst = Text.split(";")
        for Element in TempLst:
            Stat = Element.split(",")
            TempPostfix = Postfix(Stat[0], Stat[1], int(Stat[2]), int(Stat[3]), Stat[4], int(Stat[5]))
            Postfixes.append(TempPostfix)
        print(Postfixes)

    with open("enemies.lst") as EnemyMoldsLst:
        Text = EnemyMoldsLst.read()
        TempLst = Text.split("\n")
        for Element in TempLst:
            TempEnemy = Element.split(",")
            EnemyMolds.append(TempEnemy)
        print(EnemyMolds)

    with open("encounters.lst") as EncountersLst:
        Text = EncountersLst.read()
        TempLst = Text.split("\n")
        for Element in TempLst:
            TempEncounter = Element.split(";")
            Encounters.append(TempEncounter)
        print(Encounters)

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
            CharHP = random.randint(15,30)
            CharMaxHP = CharHP
            CharStr = random.randint(15,18)
            CharInt = random.randint(5,7)
            CharFai = random.randint(7,15)
            CharMinDMG = random.randint(4,9)
            CharMaxDMG = random.randint(10,12)
            CharProt = random.randint(2,4)
        case 2:
            CharVoc = "Wizard"
            CharHP = random.randint(8,12)
            CharMaxHP = CharHP
            CharStr = random.randint(2,7)
            CharInt = random.randint(15,18)
            CharFai = random.randint(5,8)
            CharMinDMG = random.randint(2,6)
            CharMaxDMG = random.randint(12,17)
            CharProt = random.randint(2,3)
        case 3:
            CharVoc = "Warrior"
            CharHP = random.randint(10,20)
            CharMaxHP = CharHP
            CharStr = random.randint(13,16)
            CharInt = random.randint(7,12)
            CharFai = random.randint(5,8)
            CharMinDMG = random.randint(3,7)
            CharMaxDMG = random.randint(8,10)
            CharProt = random.randint(3,6)
        case 4:
            CharVoc = "Cleric"
            CharHP = random.randint(9,15)
            CharMaxHP = CharHP
            CharStr = random.randint(7,12)
            CharInt = random.randint(8,13)
            CharFai = random.randint(12,20)
            CharMinDMG = random.randint(4,6)
            CharMaxDMG = random.randint(7,9)
            CharProt = random.randint(1,3)
        case 5:
            CharVoc = "Necromancer"
            CharHP = random.randint(9,13)
            CharMaxHP = CharHP
            CharStr = random.randint(5,8)
            CharInt = random.randint(12,17)
            CharFai = random.randint(1,2)
            CharMinDMG = random.randint(2,5)
            CharMaxDMG = random.randint(6,8)
            CharProt = random.randint(1,2)
    
    Char = Character(CharName, CharHP, CharMaxHP, CharVoc, CharStr, CharInt, CharFai, CharMinDMG, CharMaxDMG, CharProt)
    if Char.Vocation == "Necromancer":
        Char.Souls = 1
        Char.MaxSouls = 2
    Char.Inventory = []
    Player.Char = Char

def welcome():
    print(f"""
            Hello, {Player.Name}! Welcome to MicroHero!
            Your champion for today is:
            {Player.Char}""")

    print("""
          There is no real goal in MicroHero — just the path
          on which your champion will become stronger and stronger.
          Help them overcome untold dangers, share in their loot,
          equip them and guide them to riches and glory!""")
    
    time.sleep(4)

    start = input("\n         Onwards! Press 'Enter' to continue... ")

    choose_encounter()

def choose_encounter():
    global EncounterCounter
    global Battles
    global PositiveEncounters

    EncounterCounter += 1
    if (random.randint(1,100) - Player.Char.Fai) <= 99:
        PositiveEncounters += 1
        encounter()
    else:
        Battles += 1
        battle()

def encounter():
    global GoldAcquired
    global ItemsFound
    EncounterNum = random.randint(0, len(Encounters)-1)
    print(f"\n{Encounters[EncounterNum][0]}")
    
    Reward = Encounters[EncounterNum][1]
    Amount = Encounters[EncounterNum][2]

    match Reward, Amount:
        case "gold", "small":
            Gold = int(10 + GoldAcquired * 0.05)
            Player.Char.Gold += Gold
            GoldAcquired += Gold
            print(f"\n[+{Gold} gold]")
        case "gold", "mid":
            Gold = int(50 + GoldAcquired * 0.1)
            Player.Char.Gold += Gold
            GoldAcquired += Gold
            print(f"\n[+{Gold} gold]")
        case "gold", "large":
            Gold = int(100 + GoldAcquired * 0.25)
            Player.Char.Gold += Gold
            GoldAcquired += Gold
            print(f"\n[+{Gold} gold]")
        case "item", "small":
            FoundItem = find_item("small")
            CheckForSpace(FoundItem)
        case "item", "mid":
            FoundItem = find_item("mid")
            CheckForSpace(FoundItem)
        case "item", "large":
            FoundItem = find_item("large")
            CheckForSpace(FoundItem)
        case "exp", "small":
            ExpGain = int(25 + Player.Char.ToLevel * 0.2)
            Player.Char.Exp += ExpGain
            print(f"[+ {ExpGain}] exp")
            level_up()
        case "exp", "mid":
            ExpGain = int(100 + Player.Char.ToLevel * 0.5)
            Player.Char.Exp += ExpGain
            print(f"[+ {ExpGain}] exp")
            level_up()
        case "exp", "large":
            ExpGain = int(500 + Player.Char.ToLevel * 0.7)
            Player.Char.Exp += ExpGain
            print(f"[+ {ExpGain}] exp")
            level_up()

    GoOn = input("\nPress 'Enter' to continue... ")
    choose_encounter()

def find_item(amount):
    global ItemsFound

    ItemsFound += 1    

    if amount == "small":
        Tier = 1
    elif amount == "mid":
        Tier = 2
    elif amount == "large":
        Tier = 3

    PrefixFound = False
    CoreFound = False
    PostfixFound = False
    TempPrefix = None
    TempCore = None
    TempPostfix = None

    while not (PrefixFound and CoreFound and PostfixFound):
        TempPrefixes = []
        TempCores = []
        TempPostfixes = []

        if not PrefixFound:
            print("\nPrefix stage...")
            for Element in Prefixes:
                if Element.Tier <= Tier:
                    TempPrefixes.append(Element)
                PrefixNum = random.randint(0, len(TempPrefixes)-1)
                print("Looking for prefix.")
                TempPrefix = TempPrefixes[PrefixNum]
                PrefixFound = True
                print(f"Prefix '{TempPrefix}' found.")
                break
        if not CoreFound:
            print("\nCore stage...")
            for Element in Cores:
                if Element.Tier <= Tier:
                    TempCores.append(Element)
                CoreNum = random.randint(0, len(TempCores)-1)
                print("Looking for core.")
                TempPrefix = TempPrefixes[CoreNum]
                CoreFound = True
                print(f"Core {TempCore} found.")
                break
        if not PostfixFound:
            print("\nPostfix stage...")
            for Element in Postfixes:
                if Element.Tier <= Tier:
                    TempPostfixes.append(Element)
                PostfixNum = random.randint(0, len(TempPostfixes)-1)
                print("Looking for postfix.")
                TempPostfix = TempPostfixes[PostfixNum]
                PostfixFound = True
                break

    Reward = create_item(TempPrefix, TempCore, TempPostfix)
    print(f"Item '{Reward}' created.")
    return Reward

def CheckForSpace(FoundItem):
    global ItemsKept

    if Player.Char.InventorySize < Player.Char.InventoryMaxSize:
        print(f"\n[{FoundItem} found!]")
        print(f"{FoundItem.Prefix.Name}: {FoundItem.Prefix.Description}")
        print(f"{FoundItem.Core.Name}: {FoundItem.Core.Description}")
        print(f"{FoundItem.Postfix.Name}: {FoundItem.Postfix.Description}")
        keep = input("\nWould you like to keep it? [y/n]")
        while keep != "y" and keep != "n":
            keep = input("Please, answer either 'y' or 'n'... ")
        if keep == "y":
            ItemsKept += 1
            Player.Char.Inventory.append(FoundItem)
            print(f"\n[+ {FoundItem}]")
            input("Press 'Enter' to continue... ")
            choose_encounter()
        if keep == "n":
            print(f"\nYou decide to leave the {FoundItem} alone, and continue on your way.")
            del FoundItem
            input("\nPress 'Enter' to continue... ")
            choose_encounter()
    else:
        print("\nThere is no room in your inventory. Would you like to discard something?")
        count = 1
        for Item in Player.Char.Inventory:
            print(f"\n{count}. {Item.Name}")
            print(f"{Item.Prefix.Name}: {Item.Prefix.Description}")
            print(f"{Item.Core.Name} {Item.Core.Description}")
            print(f"{Item.Postfix.Name} {Item.Postfix.Description}")
            Discard = input(f"\nChoose a number or enter '0' to leave the {FoundItem.Name} where it is and move on... ")
            while Discard not in range(1, Player.Char.InventorySize+1):
                Discard = input(f"\nPlease, choose a valid number or enter '0' to leave the {FoundItem.Name} where it is and move on... ")
            if Discard == "0":
                print(f"\nYou decide that you don't need the {FoundItem.Name}, and continue your journey.")
                GoOn = input("Press 'Enter' to continue... ")
                choose_encounter()
            else:
                ItemsKept += 1
                Player.Char.Inventory.append(FoundItem)
                print(f"\n[+ {FoundItem.Name}]")
                GoOn = input("Press 'Enter' to continue... ")
                choose_encounter()

def level_up():
    if Player.Char.Exp >= Player.Char.ToLevel:
        Char = Player.Char
        Char.Level += 1
        match Char.Vocation:
            case "Barbarian":
                print(f"\n{Char.Name} is now Level {Char.Level}!")
                NewStr = random.randint(1,3)
                NewFai = random.randint(1,2)
                NewMinDmg = random.randint(2,7)
                NewMaxDmg = random.randint(2,7)
                Char.Str += NewStr
                Char.Fai += NewFai
                Char.MinDmg += NewMinDmg
                Char.MaxDmg += NewMaxDmg
                print(f"\n[STR: +{NewStr}]")
                print(f"[FAI: +{NewFai}]")
                print(f"[Min.DMG: +{NewMinDmg}]")
                print(f"[Max.DMG: +{NewMaxDmg}]")
            case "Wizard":
                print(f"\n{Char.Name} is now Level {Char.Level}!")
                NewInt = random.randint(2,5)
                NewMinDmg = random.randint(4,7)
                NewMaxDmg = random.randint(5,10)
                Char.Int += NewInt
                Char.MinDmg += NewMinDmg
                Char.MaxDmg += NewMaxDmg
                print(f"\n[INT: +{NewInt}]")
                print(f"[Min.DMG: +{NewMinDmg}]")
                print(f"[Max.DMG: +{NewMaxDmg}]")
            case "Warrior":
                print(f"\n{Char.Name} is now Level {Char.Level}!")
                NewStr = random.randint(1,2)
                NewFai = random.randint(0,1)
                NewProt = random.randint(3,7)
                Char.Str += 2
                Char.Fai += 1
                Char.Prot += 5
                print(f"\n[STR: +{NewStr}]")                
                if NewFai > 0:
                    print(f"[FAI: +{NewFai}]")
                print(f"[Prot.: +{NewProt}]")
            case "Cleric":
                print(f"\n{Char.Name} is now Level {Char.Level}!")
                NewFai = random.randint(2,3)
                NewMinDmg = random.randint(2,4)
                NewMaxDmg = random.randint(2,4)
                Char.Fai += 3
                Char.MinDmg += 2
                Char.MaxDmg += 2
                print(f"\n[FAI: +{NewFai}]")
                print(f"Min.DMG: +{NewMinDmg}")
                print(f"Max.DMG: +{NewMaxDmg}")
            case "Necromancer":
                print(f"\n{Char.Name} is now Level {Char.Level}!")
                NewInt = random.randint(1,4)
                NewMinDmg = random.randint(2,5)
                NewMaxDmg = random.randint(3,8)
                NewMaxSouls = random.randint(0,1)
                Char.Int += 2
                Char.MinDmg += 2
                Char.MaxDmg += 4
                Char.MaxSouls += 1
                print(f"\n[INT: +{NewInt}]")
                print(f"[Min.DMG: +{NewMinDmg}]")
                print(f"[Max.DMG: +{NewMaxDmg}]")
                if NewMaxSouls > 0:
                    print(f"[Max Souls: +{NewMaxSouls}]")
                
        GoOn = input("Press 'Enter' to continue... ")

    choose_encounter()

def battle():
    pass

def create_monster():
    Num = random.randint(0,len(EnemyMolds)-1)
    Stats = EnemyMolds[Num]
    Monster = Enemy(Stats[0], Stats[1], Stats[2], Stats[3], Stats[4], Stats[5],
                    Stats[6], Stats[7], Stats[8], Stats[9], Stats[10], Stats[11],
                    Stats[12], Stats[13], Stats[14], Stats[15], Stats[16], Stats[17])
    print(f"{Monster} joins the fray!") 
    return Monster

def create_item(PrefixNum=None, CoreNum=None, PostfixNum=None):
    if PrefixNum == None or CoreNum == None or PostfixNum == None:
        PrefixNum = random.randint(0, len(Prefixes)-1)
        CoreNum = random.randint(0, len(Cores)-1)
        PostfixNum = random.randint(0, len(Postfixes)-1)

    NewItem = Item(Prefixes[PrefixNum], Cores[CoreNum], Postfixes[PostfixNum])
    print(f"{NewItem} was created!")
    return NewItem

PlayerName = input("\nWhat is your name? ")
unpack_lists()
create_player(PlayerName)
create_character()

welcome()