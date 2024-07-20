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
Monsters = []

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
    def __init__(self, Name, HP, Vocation, Str, Int, Fai, MinDmg, MaxDmg, Prot, Tier, Exp):
        self.Name = Name
        self.HP = HP
        self.FullHP = HP
        self.Vocation = Vocation
        self.Str = Str
        self.Int = Int
        self.Fai = Fai
        self.MinDmg = MinDmg
        self.MaxDmg = MaxDmg
        self.Prot = Prot
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

    start = input("\n         Onwards! Press 'Enter' to continue... ")

    main_menu()

def main_menu():
    if EncounterCounter == 0:
        print(f"\nYou, a young {Player.Char.Vocation}, have left your past behind.")
        print("Friends, family, the easy country life — not for you.")
        print("You've heard the call of the open road for as long as you can remember.")
        print("Now, it is finally before you — broad and endless.")
        print("What adventure awaits ahead? Only one way to find out...")
    
    print("\n1. Onwards!")
    print("2. Check your character sheet")
    print("3. Look at your inventory")
    print("4. Use an ability")
    print("5. Quit the adventure")

    choice = input("\nWhat would you like to do? ")
    while int(choice) not in range(1,7):
        choice = input("\nPlease, pick a valid number... ")
    match choice:
        case "1":
            choose_encounter()
        case "2":
            open_character()
        case "3":
            open_inventory()
        case "4":
            choose_ability()
        case "5":
            print("\nVery well. Come back when you feel adventurous again... ")
            time.sleep(3)
            exit()

def choose_encounter():
    global EncounterCounter
    global Battles
    global PositiveEncounters

    EncounterCounter += 1
    if (random.randint(1,100) - Player.Char.Fai) <= 30:
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
            CheckExp = level_up()
        case "exp", "mid":
            ExpGain = int(100 + Player.Char.ToLevel * 0.5)
            Player.Char.Exp += ExpGain
            print(f"[+ {ExpGain}] exp")
            CheckExp = level_up()
        case "exp", "large":
            ExpGain = int(500 + Player.Char.ToLevel * 0.7)
            Player.Char.Exp += ExpGain
            print(f"[+ {ExpGain}] exp")
            CheckExp = level_up()

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
    while Player.Char.Exp >= Player.Char.ToLevel:
        Char = Player.Char
        Char.Level += 1
        Char.ToLevel += Char.ToLevel * 0.5
        match Char.Vocation:
            case "Barbarian":
                print(f"\n{Char.Name} is now Level {Char.Level}!")
                NewHP = random.randint(1, 8)
                NewStr = random.randint(1,3)
                NewFai = random.randint(1,2)
                NewMinDmg = random.randint(2,7)
                NewMaxDmg = random.randint(2,7)
                Char.FullHP += NewHP
                Char.HP = Char.FullHP
                Char.Str += NewStr
                Char.Fai += NewFai
                Char.MinDmg += NewMinDmg
                Char.MaxDmg += NewMaxDmg
                print(f"\n[HP: +{NewHP}]")
                print(f"[STR: +{NewStr}]")
                print(f"[FAI: +{NewFai}]")
                print(f"[Min.DMG: +{NewMinDmg}]")
                print(f"[Max.DMG: +{NewMaxDmg}]")
            case "Wizard":
                print(f"\n{Char.Name} is now Level {Char.Level}!")
                NewHP = random.randint(1,4)
                NewInt = random.randint(2,5)
                NewMinDmg = random.randint(4,7)
                NewMaxDmg = random.randint(5,10)
                Char.FullHP += NewHP
                Char.HP = Char.FullHP
                Char.Int += NewInt
                Char.MinDmg += NewMinDmg
                Char.MaxDmg += NewMaxDmg
                print(f"\n[HP: +{NewHP}]")
                print(f"[INT: +{NewInt}]")
                print(f"[Min.DMG: +{NewMinDmg}]")
                print(f"[Max.DMG: +{NewMaxDmg}]")
            case "Warrior":
                print(f"\n{Char.Name} is now Level {Char.Level}!")
                NewHP = random.randint(2,12)
                NewStr = random.randint(1,2)
                NewFai = random.randint(0,1)
                NewProt = random.randint(3,7)
                Char.FullHP += NewHP
                Char.HP = Char.FullHP
                Char.Str += 2
                Char.Fai += 1
                Char.Prot += 5
                print(f"\n[HP: +{NewHP}]")
                print(f"[STR: +{NewStr}]")                
                if NewFai > 0:
                    print(f"[FAI: +{NewFai}]")
                print(f"[Prot.: +{NewProt}]")
            case "Cleric":
                print(f"\n{Char.Name} is now Level {Char.Level}!")
                NewHP = random.randint(2,8)
                NewFai = random.randint(2,3)
                NewMinDmg = random.randint(2,4)
                NewMaxDmg = random.randint(2,4)
                Char.FullHP += NewHP
                Char.HP = Char.FullHP
                Char.Fai += 3
                Char.MinDmg += 2
                Char.MaxDmg += 2
                print(f"\n[HP: +{NewHP}]")
                print(f"[FAI: +{NewFai}]")
                print(f"Min.DMG: +{NewMinDmg}")
                print(f"Max.DMG: +{NewMaxDmg}")
            case "Necromancer":
                print(f"\n{Char.Name} is now Level {Char.Level}!")
                NewHP = random.randint(1,4)
                NewInt = random.randint(1,4)
                NewMinDmg = random.randint(2,5)
                NewMaxDmg = random.randint(3,8)
                NewMaxSouls = random.randint(0,1)
                Char.FullHP += NewHP
                Char.HP = Char.FullHP
                Char.Int += 2
                Char.MinDmg += 2
                Char.MaxDmg += 4
                Char.MaxSouls += 1
                print(f"\n[HP: +{NewHP}]")
                print(f"[INT: +{NewInt}]")
                print(f"[Min.DMG: +{NewMinDmg}]")
                print(f"[Max.DMG: +{NewMaxDmg}]")
                if NewMaxSouls > 0:
                    print(f"[Max Souls: +{NewMaxSouls}]")

        GoOn = input("Press 'Enter' to continue... ")
        return

def battle():
    check = Player.Char.Level
    if check < 5:
        Tier = 1
        Amount = 1
    elif check >=5 and check <10:
        Tier = 1
        Amount = 2
    elif check >= 10 and check < 15:
        Tier = 1
        Amount = 3
    elif check >= 15 and check < 25:
        Tier = 2
        Amount = 1
    elif check >= 25 and check < 30:
        Tier = 2
        Amount = 2
    elif check >= 30 and check < 40:
        Tier = 2
        Amount = 3
    elif check >= 40:
        Tier = 3
        Amount = 1

    create_monster(Tier, Amount)
    
    player_turn()

def player_turn():
    print("\nYou stumbled upon some monsters. It's time for battle!")
    print("Your adversaries:")
    count = 1
    for Element in Monsters:
        print(f"""\n{count}. {Element.Name}
              HP: {Element.HP} / {Element.FullHP}""")
    Choice = input("\nWould you like to [a]ttack, [u]se an item, use an a[b]ility or [r]etreat? ")
    while Choice != "a" and Choice != "u" and Choice != "b" and Choice != "r":
        Choice = input("\n[a]ttack, [u]se an item, use an a[b]ility or [r]etreat? ")

    match Choice:
        case "a":
            if len(Monsters) > 1:
                Choice = input("\nWhich enemy would you like to attack? ")
                while int(Choice) not in range(1, len(Monsters)):
                    Choice = input("\nPlease, enter a valid number... ")
                Dmg = calculate_dmg(Player.Char, Monsters[int(Choice-1)])
                Monsters[int(Choice-1)].HP -= Dmg
                print(f"\n{Player.Char.Name} attacks {Monsters[int(Choice-1)]} for {Dmg} dmg")
                if Monsters[int(Choice-1)].HP <= 0:
                    Player.Char.Exp += Monsters[int(Choice-1)].Exp
                    print(f"{Monsters[int(Choice-1)]} has perished. [+{[Monsters.Choice-1].Exp} exp]")
                    CheckExp = level_up()
                    Monsters.remove(Monsters[int(Choice-1)])
                    if len(Monsters) == 0:
                        victory()
                    else:
                        monster_turn()
                else:
                    print(f"\n{Monsters[int(Choice-1)]} is now at {Monsters[int(Choice-1)].HP} HP")
                    time.sleep(3)
                    monster_turn()
            else:
                Dmg = calculate_dmg(Player.Char, Monsters[0])
                Monsters[0].HP -= Dmg
                print(f"\n{Player.Char.Name} attacks {Monsters[0]} for {Dmg} dmg")
                if Monsters[0].HP <= 0:
                    Player.Char.Exp += Monsters[0].Exp
                    print(f"{Monsters[0]} has perished. [+{Monsters[0].Exp} exp]")
                    CheckExp = level_up()
                    victory()
                else:
                    print(f"\n{Monsters[0]} is now at {Monsters[0].HP} HP")
                    time.sleep(3)
                    monster_turn()
        case "u":
            if Player.Char.InventorySize == 0:
                print("\nYou don't have anything.")
                time.sleep(3)
                player_turn()
            
            print(f"\nINVENTORY")
            Num = 1
            for Item in Player.Char.Inventory:
                print(f"""\n{Num}. {Item.Name}
{Item.Prefix.Name}: {Item.Prefix.Description}
{Item.Core.Name}: {Item.Core.Description}
{Item.Postfix.Name}: {Item.Postfix.Description}""")     

            Choice = input("Which item would you like to use? Enter '0' to go back... ") 
            while Choice not in range (0, len(Player.Char.Inventory)):
                Choice = input("Please, pick a valid number or enter '0; to go back... ")
            if Choice == "0":
                player_turn()
            else:
                if Player.Char.Inventory[int(Choice)-1].Location != "heal" or Player.Char.Inventory[int(Choice)-1].Location != "buff":
                    back = input(f"{Player.Char.Inventory[int(Choice)-1]} is not usable. Press 'Enter' to go back... ")
                    player_turn()
                elif Player.Char.Inventory[int(Choice)-1].Location == "heal":
                    use_heal(Player.Char.Inventory[int(Choice)-1], "battle")
                elif Player.Char.Inventory[int(Choice)-1].Location == "buff":
                    use_buff(Player.Char.Inventory[int(Choice)-1], "battle")
        case "b":
            use_ability("peace")
        case "r":
            retreat()

def monster_turn():
    for Element in Monsters:
        Dmg = calculate_dmg(Element, Player.Char)
        Player.Char.HP -= Dmg
        print(f"\n{Element.Name} attacks {Player.Char.Name} for {Dmg} dmg")
        if Player.Char.HP <= 0:
            defeat()
        else:
            print(f"{Player.Char.Name} is now at {Player.Char.HP} HP")
            time.sleep(3)
            player_turn()

def use_ability(status):
    pass

def retreat():
    pass

def calculate_dmg(Attacker, Defender):
    if Attacker.Vocation == "Barbarian" or Attacker.Vocation == "Warrior":
        InitialDmg = random.randint(Attacker.MinDmg, Attacker.MaxDmg) + int(Attacker.Str * 0.2)
    elif Attacker.Vocation == "Wizard":
        InitialDmg = random.randint(Attacker.MinDmg, Attacker.MaxDmg) + int(Attacker.Int * 0.2)
    elif Attacker.Vocation == "Cleric":
        InitialDmg = random.randint(Attacker.MinDmg, Attacker.MaxDmg) + int(Attacker.Fai * 0.2)
    elif Attacker.Vocation == "Necromancer":
        InitialDmg = random.randint(Attacker.MinDmg, Attacker.MaxDmg) + int(Attacker.Int * 0.1)

    Dmg = InitialDmg - int(Defender.Prot * 0.3)
    if Dmg <= 0:
        Dmg = 1
    
    return Dmg

def victory():
    pass

def defeat():
    pass

def open_character():
    print(f"""\n{Player.Char.Name}, the {Player.Char.Vocation}
Level: {Player.Char.Level}
Exp: {Player.Char.Exp} / {Player.Char.ToLevel}

HP: {Player.Char.HP} / {Player.Char.MaxHP}

STR: {Player.Char.Str}
INT: {Player.Char.Int}
FAI: {Player.Char.Fai}

Dmg: {Player.Char.MinDmg}—{Player.Char.MaxDmg}
Prot: {Player.Char.Prot}""")
    
    GoOn = input("Press 'Enter' to go back... ")
    main_menu()

def open_inventory():
    print(f"\nINVENTORY")
    Num = 1
    for Item in Player.Char.Inventory:
        print(f"""\n{Num}. {Item.Name}
{Item.Prefix.Name}: {Item.Prefix.Description}
{Item.Core.Name}: {Item.Core.Description}
{Item.Postfix.Name}: {Item.Postfix.Description}""")
    
    choice = input("Would you like to [d]iscard an item, [u]se one or go [b]ack? ")
    while choice != "d" and choice != "u" and choice != "b":
        choice = input("\nChoose: [d]iscard, [u]se or go [b]ack? ")
    match choice:
        case "b":
            main_menu()
        case "u":
            if Player.Char.InventorySize == 0:
                choice = input("\nYou don't have anything. Press 'Enter' to go back... ")
                main_menu()
            else:
                choice = input("\nWhat would you like to use? Enter '0' to go back. ")
                while int(choice) not in range(0, Player.Char.InventorySize+1):
                    choice = input("\nPlease, enter a valid number or '0' to go back... ")
                if choice == "0":
                    open_inventory()
                else:
                    x = int(choice)
                    if Player.Char.Inventory[x-1].Location != "heal" or Player.Char.Inventory[x-1].Location != "buff":
                        choice = input(f"\nThe {Player.Char.Inventory[x-1].Location} is not usable in this way. Press 'Enter' to go back... ")
                        open_inventory()
                    elif Player.Char.Inventory[x-1].Location == "heal":
                        use_heal(Player.Char.Inventory[x-1], "peace")
                    elif Player.Char.Inventory[x-1].Location == "buff":
                        use_buff(Player.Char.Inventory[x-1], "peace")
        case "d":
            if Player.Char.InventorySize == 0:
                choice = input("\nYou don't have anything. Press 'Enter' to go back... ")
                main_menu()
            else:
                choice = input("\nWhat would you like to discard? Enter '0' to go back. ")
                while choice not in range(0, Player.Char.InventorySize+1):
                    choice = input("\nPlease, enter a valid number or '0' to go back... ")
                if choice == "0":
                    open_inventory()
                else:
                    x = int(choice)
                    sure = input(f"\nAre you sure? The {Player.Char.Inventory[x-1]} will be lost forever. [y/n]")
                    while sure != "y" and sure != "n":
                        sure = input("\fPlease, say either 'y' or 'n'... ")
                    if sure == "y":
                        print(f"\n{Player.Char.Inventory[x-1]} has been discarded.")
                        ToDelete = Player.Char.Inventory[x-1]
                        Player.Char.Inventory.remove(Player.Char.Inventory[x-1])
                        del ToDelete
                        open_inventory()

def choose_ability():
    pass

def use_heal(item, status):
    pass

def use_buff(item, status):
    pass

def create_monster(Tier=1, Amount=1):
    Count = 1
    TempMonsters = []
    while Count <= Amount:
        for Candidate in EnemyMolds:
            if int(Candidate[16]) <= Tier:
                TempMonsters.append(Candidate)            
        Num = random.randint(0,len(TempMonsters)-1)
        Stats = TempMonsters[Num]
        MonsterName = Stats[0]
        MonsterHP = random.randint(int(Stats[1]), int(Stats[2]))
        MonsterVocation = Stats[3]
        MonsterStr = random.randint(int(Stats[4]), int(Stats[5]))
        MonsterInt = random.randint(int(Stats[6]), int(Stats[7]))
        MonsterFai = random.randint(int(Stats[8]), int(Stats[9]))
        MonsterMinDmg = random.randint(int(Stats[10]), int(Stats[11]))
        MonsterMaxDmg = random.randint(int(Stats[12]), int(Stats[13]))
        MonsterProt = random.randint(int(Stats[14]), int(Stats[15]))
        MonsterTier = int(Stats[16])
        MonsterExp = int(Stats[17])
        Monster = Enemy(MonsterName, MonsterHP, MonsterVocation, MonsterStr, MonsterInt, MonsterFai, MonsterMinDmg, MonsterMaxDmg, MonsterProt, MonsterTier, MonsterExp)
        print(f"{Monster} joins the fray!") 
        Monsters.append(Monster)
        Count += 1

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