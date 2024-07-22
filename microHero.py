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
EnemyMolds = []
Monsters = []
Encounters = []
Monsters = []
Abilities = []
Items = []
UsableItems = []

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
        self.Inventory = []
        self.InventorySize = InventorySize
        self.InventoryMaxSize = InventoryMaxSize
        self.Exp = Exp
        self.ToLevel = ToLevel
        self.Gold = Gold
        self.Level = Level
        self.Abilities = Abilities
        self.NearDeath = False
        self.PotionEffects = []
        self.Abilities = []
        self.Allies = []
        self.ItemEffects = []

    def __repr__(self):
        return f"""{self.Name} / The {self.Vocation}
        HP: {self.HP} / {self.MaxHP}
        STR: {self.Str}
        INT: {self.Int}
        FAI: {self.Fai}
        
        DMG: {self.MinDmg}—{self.MaxDmg}
        Prot: {self.Prot}
                
        Inventory: {self.Inventory}
        Abilities: {self.Abilities}"""  

class Enemy:
    def __init__(self, Name, HP, Vocation, Str, Int, Fai, MinDmg, MaxDmg, Prot, Tier, Exp):
        self.Name = Name
        self.HP = HP
        self.MaxHP = HP
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
    
class Ally:
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
        return self.Name
    
class Item:
    def __init__(self, Prefix, Core):
        self.Prefix = Prefix
        self.Core = Core
        self.Name = self.Prefix.Name + self.Core.Name
        self.Price = self.Prefix.Price + self.Core.Price
        self.Location = self.Core.Location

    def __repr__(self):
        return f"{self.Name}"
    
class Prefix:
    def __init__(self, Name, Stat, Modifier, Tier, Description, Price):
        self.Name = Name
        self.Stat = Stat
        self.Modifier = Modifier
        self.Tier = Tier
        self.Description = Description
        self.Price = Price
    
    def __repr__(self):
        return f"{self.Name}"

class Core:
    def __init__(self, Name, Stat, Modifier, Location, Description, Price, Tier):
        self.Name = Name
        self.Stat = Stat
        self.Modifier = Modifier
        self.Location = Location
        self.Description = Description
        self.Price = Price
        self.Tier = Tier

    def __repr__(self):
        return f"{self.Name}"

    def __repr__(self):
        return f"{self.Name}"

class Ability:
    def __init__(self, Name, AbType, Description, Cooldown, AbCooldown, CooldownType, Vocation, Scope, EffectCooldownType):
        self.Name = Name
        self.Description = Description
        self.AbType = AbType
        self.EffectCooldown = Cooldown
        self.AbCooldown = AbCooldown
        self.CooldownType = CooldownType
        self.Vocation = Vocation
        self.Scope = Scope
        self.Amount = 0
        self.EffectCooldownType = EffectCooldownType

    def __repr__(self):
        return f"{self.Name}"
    
class UsableItem:
    def __init__(self, Name, Form, Modifier, Location, Description, Price, EffectCooldown, MaxCooldown, Stat, Scope):
        self.Name = Name
        self.Form = Form
        self.Modifier = Modifier
        self.Location = Location
        self.Description = Description
        self.Price = Price
        self.Cooldown = EffectCooldown
        self.MaxCooldown = MaxCooldown
        self.Stat = Stat
        self.Scope = Scope

    def __repr__(self):
        return self.Name
    
def unpack_lists():
    global Names
    global Nicknames
    global Prefixes
    global Cores
    global EnemyMolds
    global Encounters
    global Abilities
    
    with open("names.lst") as NamesLst:
        Text = NamesLst.read()
        Names = Text.split(",")

    with open("nicknames.lst") as NicknamesLst:
        Text = NicknamesLst.read()
        Nicknames = Text.split(",")

    with open("item_prefixes.lst") as PrefixesLst:
        Text = PrefixesLst.read()
        TempLst = Text.split("\n")
        for Element in TempLst:
            Stat = Element.split(",")
            TempPrefix = Prefix(Stat[0], Stat[1], int(Stat[2]), int(Stat[3]), Stat[4], int(Stat[5]))
            Prefixes.append(TempPrefix)
        print(Prefixes)

    with open("item_cores.lst") as CoresLst:
        Text = CoresLst.read()
        TempLst = Text.split("\n")
        for Element in TempLst:
            Stat = Element.split(",")
            TempCore = Core(Stat[0], Stat[1], int(Stat[2]), Stat[3], Stat[4], int(Stat[5]), int(Stat[6]))
            Cores.append(TempCore)
        print(Cores)

    # with open("item_postfixes.lst") as PostfixesLst:
    #     Text = PostfixesLst.read()
    #     TempLst = Text.split("\n")
    #     for Element in TempLst:
    #         Stat = Element.split(",")
    #         TempPostfix = Postfix(Stat[0], Stat[1], int(Stat[2]), int(Stat[3]), Stat[4], int(Stat[5]))
    #         Postfixes.append(TempPostfix)
    #     print(Postfixes)

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
    
    with open("abilities.lst") as AbilityLst:
        Text = AbilityLst.read()
        TempLst = Text.split("\n")
        for Element in TempLst:
            TempLst2 = Element.split(";")
            TempAbility = Ability(TempLst2[0], TempLst2[1], TempLst2[2], int(TempLst2[3]), int(TempLst2[4]), TempLst2[5], TempLst2[6], TempLst2[7], TempLst2[8])
            Abilities.append(TempAbility)

    with open("usable_items.lst") as UsableLst:
        Text = UsableLst.read()
        TempLst = Text.split("\n")
        for Element in TempLst:
            TempLst2 = Element.split(";")
            TempItem = UsableItem(TempLst2[0], TempLst2[1], int(TempLst2[2]), TempLst2[3], TempLst2[4], int(TempLst2[5]), int(TempLst2[6]), int(TempLst2[7]), TempLst2[8], TempLst2[9])
            UsableItems.append(TempItem)

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
    CharAbilities = []

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
            CharAbilities.append(Abilities[0])
            CharAbilities.append(Abilities[1])
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
            CharAbilities.append(Abilities[2])
            CharAbilities.append(Abilities[3])
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
            CharAbilities.append(Abilities[4])
            CharAbilities.append(Abilities[5])
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
            CharAbilities.append(Abilities[6])
            CharAbilities.append(Abilities[7])
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
            CharAbilities.append(Abilities[8])
            CharAbilities.append(Abilities[9])
    
    Char = Character(CharName, CharHP, CharMaxHP, CharVoc, CharStr, CharInt, CharFai, CharMinDMG, CharMaxDMG, CharProt)
    Char.Abilities = CharAbilities
    Char.Allies.append(Char)
    if Char.Vocation == "Necromancer":
        Char.Souls = 1
        Char.MaxSouls = 2
    Char.Inventory.append(UsableItems[0])
    Char.Inventory.append(UsableItems[4])
    Char.Inventory.append(UsableItems[5])
    Char.Inventory.append(UsableItems[6])
    Char.Inventory.append(UsableItems[7])
    Char.Inventory.append(UsableItems[8])
    Char.InventorySize += 6
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
    while True:
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
                Cast = choose_ability("all")
            case "5":
                print("\nVery well. Come back when you feel adventurous again... ")
                time.sleep(3)
                exit()

def choose_encounter():
    global EncounterCounter
    global Battles
    global PositiveEncounters

    EncounterCounter += 1
    if (random.randint(1,100) - Player.Char.Fai) <= 25:
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
            Grab = CheckForSpace(FoundItem, "found")
        case "item", "mid":
            FoundItem = find_item("mid")
            Grab = CheckForSpace(FoundItem, "found")
        case "item", "large":
            FoundItem = find_item("large")
            Grab = CheckForSpace(FoundItem, "found")
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
        case "shop", "small":
            Stock = stock_the_shop("small")
            Shop = open_shop(Stock)
        case "shop", "mid":
            Stock = stock_the_shop("mid")
            Shop = open_shop(Stock)
        case "shop", "large":
            Stock = stock_the_shop("large")
            Shop = open_shop(Stock)

    GoOn = input("\nPress 'Enter' to continue... ")

def stock_the_shop(Size):
    Count = 0
    Shop = []
    if Size == "small":
        while Count < 3:
            NewItem = create_item()
            Shop.append(NewItem)
            Count +=1
        Count = 0
        while Count < 2:
            NewItem = random.randint(0, len(UsableItems)-1)
            Shop.append(UsableItems[NewItem])
            Count += 1
    if Size == "mid":
        while Count < 5:
            NewItem = create_item()
            Shop.append(NewItem)
            Count +=1
        Count = 0
        while Count < 3:
            NewItem = random.randint(0, len(UsableItems)-1)
            Shop.append(UsableItems[NewItem])
            Count += 1
    if Size == "large":
        while Count < 10:
            NewItem = create_item()
            Shop.append(NewItem)
            Count +=1
        Count = 0
        while Count < 5:
            NewItem = random.randint(0, len(UsableItems)-1)
            Shop.append(UsableItems[NewItem])
            Count += 1

    Trade = open_shop(Shop)        

def open_shop(Stock):
    global GoldAcquired
    Choice = input("Hi there! Are you [b]uying or [s]elling? Enter '0' to leave... ")
    while Choice not in ("b", "s", "0"):
        Choice = input("Please, choose either [b]uy, [s]ell or '0' to leave... ")
    if Choice == "0":
        return
    elif Choice == "b":
        Num = 1
        print("\nHere's today's stock.")
        for Element in Stock:
            print(f"\n{Num}. {Element.Name}")
            if hasattr(Element, "Prefix"):
                print(f"{Element.Prefix.Name}: {Element.Prefix.Description}")
                print(f"{Element.Core.Name}: {Element.Core.Description}")
                Element.Price = Element.Prefix.Price + Element.Core.Price
                print(f"Price: {Element.Price} gold")
            else:
                print(f"{Element.Description}")
                print(f"Price: {Element.Price}")
            Num += 1
        Choice = input(f"\nYou have {Player.Char.Gold} gold. What would you like to buy? Enter '0' to go back... ")
        while not Choice.isdigit() and int(Choice) not in range(0, len(Stock)+1):
            Choice = input("\nPlease, enter a valid number or '0' to go back... ")
        Choice = int(Choice)
        if Choice == 0:
            open_shop(Stock)
        else:
            if Stock[Choice-1].Price > Player.Char.Gold:
                print("You do not have enough money.")
                time.sleep(2)
                open_shop()
            Player.Char.Gold -= Stock[Choice-1].Price
            Space = CheckForSpace(Stock[Choice-1], "bought")
            Stock.remove(Stock[Choice-1])
            open_shop(Stock)
    elif Choice == "s":
        if Player.Char.InventorySize > 0:
            print("\nHere are your items.")
            Num = 1
            for Element in Player.Char.Inventory:
                print(f"\n{Num}. {Element.Name}")
                if hasattr(Element, "Prefix"):
                    print(f"{Element.Prefix.Name}: {Element.Prefix.Description}")
                    print(f"{Element.Core.Name}: {Element.Core.Description}")
                    print("Price: " + str(Element.Prefix.Price + Element.Core.Price))
                else:
                    print(f"{Element.Description}")
                    print(f"Price: {Element.Price}")
                Num += 1
            Choice = input("What would you like to sell? Enter '0' to go back... ")
            while not Choice.isdigit() and int(Choice) not in range(0,len(Player.Char.Inventory) + 1):
                Choice = input("Please, enter a valid number or '0' to go back... ")
            Choice = int(Choice)
            if Choice == 0:
                open_shop(Stock)
            else:
                if hasattr(Player.Char.Inventory[Choice-1], "Prefix"):
                    Price = Player.Char.Inventory[Choice-1].Prefix.Price + Player.Char.Inventory[Choice-1].Core.Price
                else:
                    Price = Player.Char.Inventory[Choice-1].Price
                ToSell = Player.Char.Inventory[Choice-1]
                Player.Char.Gold += Price
                GoldAcquired += Price
                print(f"[-{ToSell.Name}]")
                print(f"[+{Price}]")
                MinusBuff = remove_item_buff(ToSell)
                Player.Char.Inventory.remove(ToSell)                
                time.sleep(2)
                open_shop(Stock)

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
#    PostfixFound = False
    TempPrefix = None
    TempCore = None

    while not (PrefixFound and CoreFound):
        TempPrefixes = []
        TempCores = []
#        TempPostfixes = []

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
        # if not PostfixFound:
        #     print("\nPostfix stage...")
        #     for Element in Postfixes:
        #         if Element.Tier <= Tier:
        #             TempPostfixes.append(Element)
        #         PostfixNum = random.randint(0, len(TempPostfixes)-1)
        #         print("Looking for postfix.")
        #         TempPostfix = TempPostfixes[PostfixNum]
        #         PostfixFound = True
        #         break

    Reward = create_item(TempPrefix, TempCore)
    print(f"Item '{Reward}' created.")
    return Reward

def CheckForSpace(FoundItem, Status):
    global ItemsKept
    if Status == "found":
        if Player.Char.InventorySize < Player.Char.InventoryMaxSize:
            print(f"\n[{FoundItem} found!]")
            if hasattr(FoundItem, "Prefix"):
                print(f"{FoundItem.Prefix.Name}: {FoundItem.Prefix.Description}")
                print(f"{FoundItem.Core.Name}: {FoundItem.Core.Description}")
            else:
                print(f"{FoundItem.Description}")
            keep = input("\nWould you like to keep it? [y/n]")
            while keep != "y" and keep != "n":
                keep = input("Please, answer either 'y' or 'n'... ")
            if keep == "y":
                ItemsKept += 1
                Player.Char.Inventory.append(FoundItem)
                Player.Char.ItemEffects.append(FoundItem)
                Buff = apply_item_buff(FoundItem)
                Player.Char.InventorySize += 1
                print(f"\n[+ {FoundItem}]")
                input("Press 'Enter' to continue... ")
            if keep == "n":
                print(f"\nYou decide to leave the {FoundItem} alone, and continue on your way.")
                del FoundItem
                input("\nPress 'Enter' to continue... ")
        else:
            print("\nThere is no room in your inventory. Would you like to discard something?")
            count = 1
            for Item in Player.Char.Inventory:
                print(f"\n{count}. {Item.Name}")
                print(f"{Item.Prefix.Name}: {Item.Prefix.Description}")
                print(f"{Item.Core.Name} {Item.Core.Description}")
            Discard = input(f"\nChoose a number or enter '0' to leave the {FoundItem.Name} where it is and move on... ")
            while not Discard.isdigit() and Discard not in range(0, len(Player.Char.Inventory)+1):
                Discard = input(f"\nPlease, choose a valid number or enter '0' to leave the {FoundItem.Name} where it is and move on... ")
            if Discard == "0":
                print(f"\nYou decide that you don't need the {FoundItem.Name}, and continue your journey.")
                GoOn = input("Press 'Enter' to continue... ")
            else:
                Discard = int(Discard)
                MinusBuff = remove_item_buff(Player.Char.Inventory[Discard-1])
                Player.Char.Inventory.remove(Player.Char.Inventory[Discard-1])
                ItemsKept += 1
                Player.Char.Inventory.append(FoundItem)
                PlusBuff = apply_item_buff(FoundItem)
                print(f"\n[+ {FoundItem.Name}]")
                time.sleep(2)
    elif Status == "bought":
        if Player.Char.InventorySize < Player.Char.InventoryMaxSize:
            ItemsKept += 1
            Player.Char.Inventory.append(FoundItem)
            Player.Char.ItemEffects.append(FoundItem)
            Buff = apply_item_buff(FoundItem)
            Player.Char.InventorySize += 1
            print(f"\n[+ {FoundItem}]")
        else:
            print("\nThere is no room in your inventory. Would you like to discard something?")
            count = 1
            for Item in Player.Char.Inventory:
                print(f"\n{count}. {Item.Name}")
                if hasattr(Item, "Prefix"):
                    print(f"{Item.Prefix.Name}: {Item.Prefix.Description}")
                    print(f"{Item.Core.Name} {Item.Core.Description}")
                else:
                    print(f"{Item.Description}")
            Discard = input(f"\nChoose a number or enter '0' to leave the {FoundItem.Name} where it is and move on... ")
            while not Discard.isdigit() and Discard not in range(0, len(Player.Char.Inventory)+1):
                Discard = input(f"\nPlease, choose a valid number or enter '0' to leave the {FoundItem.Name} where it is and move on... ")
            if Discard == "0":
                print(f"\nYou decide that you don't need the {FoundItem.Name}, and continue your journey.")
                GoOn = input("Press 'Enter' to continue... ")
            else:
                Discard = int(Discard)
                MinusBuff = remove_item_buff(Player.Char.Inventory[Discard-1])
                print(f"[-{Player.Char.Inventory[Discard-1]}]")
                Player.Char.Inventory.remove(Player.Char.Inventory[Discard-1])
                ItemsKept += 1
                Player.Char.Inventory.append(FoundItem)
                PlusBuff = apply_item_buff(FoundItem)
                print(f"\n[+{FoundItem.Name}]")
                time.sleep(2)

def apply_item_buff(Item):
    if hasattr(Item, "Prefix"):
        Player.Char.ItemEffects.append(Item)
        match Item.Prefix.Stat:
            case "str":
                Player.Char.Str += Item.Prefix.Modifier
                print(f"Applying buff for {Item.Name}: {Item.Prefix.Description}")
            case "int":
                Player.Char.Int += Item.Prefix.Modifier
                print(f"Applying buff for {Item.Name}: {Item.Prefix.Description}")
            case "fai":
                Player.Char.Fai += Item.Prefix.Modifier
                print(f"Applying buff for {Item.Name}: {Item.Prefix.Description}")
        match Item.Core.Stat:
            case "prot":
                Player.Char.Prot += Item.Core.Modifier
                print(f"Applying buff for {Item.Name}: {Item.Core.Description}")
            case "dmg":
                Player.Char.MinDmg += Item.Core.Modifier
                Player.Char.MaxDmg += Item.Core.Modifier
                print(f"Applying buff for {Item.Name}: {Item.Core.Description}")
                print(f"Applying buff for {Item.Name}: {Item.Core.Description}")

def remove_item_buff(Item):
    if hasattr(Item, "Prefix"):
        match Item.Prefix.Stat:
            case "str":
                Player.Char.Str -= Item.Prefix.Modifier
                print(f"Removing buff for {Item.Name}: {Item.Prefix.Description}")
            case "int":
                Player.Char.Int -= Item.Prefix.Modifier
                print(f"Removing buff for {Item.Name}: {Item.Prefix.Description}")
            case "fai":
                Player.Char.Fai -= Item.Prefix.Modifier
                print(f"Removing buff for {Item.Name}: {Item.Prefix.Description}")
        match Item.Core.Stat:
            case "prot":
                Player.Char.Prot -= Item.Core.Modifier
                print(f"Removing buff for {Item.Name}: {Item.Core.Description}")
            case "dmg":
                Player.Char.MinDmg -= Item.Core.Modifier
                Player.Char.MaxDmg -= Item.Core.Modifier
                print(f"Removing buff for {Item.Name}: {Item.Core.Description}")
                print(f"Removing buff for {Item.Name}: {Item.Core.Description}")
        Player.Char.ItemEffects.remove(Item)

def level_up():
    while Player.Char.Exp >= Player.Char.ToLevel:
        Char = Player.Char
        Char.Level += 1
        Char.ToLevel += int(Char.ToLevel * 0.5)
        match Char.Vocation:
            case "Barbarian":
                print(f"\n{Char.Name} is now Level {Char.Level}!")
                NewHP = random.randint(1, 8)
                NewStr = random.randint(1,3)
                NewFai = random.randint(1,2)
                NewMinDmg = random.randint(2,7)
                NewMaxDmg = random.randint(2,7)
                Char.MaxHP += NewHP
                Char.HP = Char.MaxHP
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
                Char.MaxHP += NewHP
                Char.HP = Char.MaxHP
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
                Char.MaxHP += NewHP
                Char.HP = Char.MaxHP
                Char.Str += NewStr
                Char.Fai += NewFai
                Char.Prot += NewProt
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
                Char.MaxHP += NewHP
                Char.HP = Char.MaxHP
                if Char.NearDeath:
                    Char.NearDeath == False
                    Player.Char.Fai -= Player.Char.Abilities[1].Amount
                    print("In My Hour of Need has expired.")
                    time.sleep(2)
                Char.Fai += NewFai
                Char.MinDmg += NewMinDmg
                Char.MaxDmg += NewMaxDmg        
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
                Char.MaxHP += NewHP
                Char.HP = Char.MaxHP
                Char.Int += NewInt
                Char.MinDmg += NewMinDmg
                Char.MaxDmg += NewMaxDmg
                Char.MaxSouls += NewMaxSouls
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

AngryShout = False
StrBuffAmount = 0
IntBuffAmount = 0
FaiBuffAmount = 0
DmgBuffAmount = 0
ProtBuffAmount = 0

def player_turn():
    global AngryShout
    global StrBuffAmount
    global IntBuffAmount
    global FaiBuffAmount
    global DmgBuffAmount
    global ProtBuffAmount

    print("\nYou stumbled upon some monsters. It's time for battle!")
    print("Your adversaries:")
    count = 1
    for Element in Monsters:
        print(f"""\n{count}. {Element.Name}
              HP: {Element.HP} / {Element.MaxHP}""")
    Choice = input("\nWould you like to [a]ttack, [u]se an item, use an a[b]ility or [r]etreat? ")
    while Choice not in ("a", "u", "b", "r"):
        Choice = input("\n[a]ttack, [u]se an item, use an a[b]ility or [r]etreat? ")

    match Choice:
        case "a":
            if len(Monsters) > 1:
                Choice = input("\nWhich enemy would you like to attack? ")
                Choice = int(Choice)
                while int(Choice) not in range(1, len(Monsters)):
                    Choice = input("\nPlease, enter a valid number... ")
                Dmg = calculate_dmg(Player.Char, Monsters[int(Choice)-1])
                if AngryShout:
                    Dmg = Dmg * 2
                    AngryShout = False
                Monsters[int(Choice)-1].HP -= Dmg
                if Monsters[int(Choice)-1].HP <= 0:
                    Player.Char.Exp += Monsters[Choice-1].Exp
                    print(f"{Monsters[int(Choice)-1]} perished. [+{Monsters[int(Choice)-1].Exp} exp")
                    CheckExp = level_up()
                    Monsters.remove(Monsters[int(Choice)-1])
                    if Player.Char.Vocation == "Necromancer" and Player.Char.Souls < Player.Char.MaxSouls:
                        Player.Char.Souls += 1
                        print("\nWorking your dark magics, you make your enemy's soul serve you.")
                        print(f"[Souls: {Player.Char.Souls}/{Player.Char.MaxSouls}]")
                    if Player.Char.Vocation == "Wizard":
                        if len(Monsters) > 0:
                            NewAmount = int(Player.Char.Int * 0.1)
                            Player.Char.Int += NewAmount
                            Player.Char.Abilities[1].Amount +=NewAmount
                            if len(Monsters) > 0:
                                Player.Char.Abilities[1].AbCooldown = 3
                            else:
                                Player.Char.Abilities[1].AbCooldown = 2
                            print(f"\nOutwitting your opponent, you get a boost of confidence. Your INT is temporarily raised by {NewAmount}. It is now at {Player.Char.Int}")
                    if Player.Char.Vocation == "BarBarian":
                        NewAmount = int(Player.Char.Str * 0.3)
                        Player.Char.MinDmg += NewAmount
                        Player.Char.MaxDmg += NewAmount
                        Player.Char.Abilities[1].Amount += NewAmount
                        if len(Monsters) > 0:
                            Player.Char.Abilities[1].AbCooldown = 3
                        else:
                            Player.Char.Abilities[1].AbCooldown = 2
                        print(f"\nYour opponent falls. You feel blood rushing to your head. Everyone shall know your fury now! Your damage is temporarily raised by {NewAmount}. It is now {Player.Char.MinDmg}—{Player.Char.MaxDmg}")
                    time.sleep(2)
                    if len(Monsters) == 0:
                        cooldown = cooldowns("encounter")
                        cooldown = cooldowns("turn")
                        victory()
                    else:
                        monster_turn()
                print(f"\n{Player.Char.Name} attacks {Monsters[int(Choice)-1]} for {Dmg} dmg")
                if len(Player.Char.Allies) > 0:
                    for Element in Player.Char.Allies:
                        if Element.Name == Player.Char.Name:
                            continue
                        else:
                            Choice = random.randint(0,len(Monsters))
                            Dmg = calculate_dmg(Element, Monsters[Choice-1])
                            Monsters[Choice-1].HP -= Dmg
                            print(f"{Element.Name} attacks {Monsters[Choice-1]} for {Dmg} dmg")
                            if Monsters[Choice-1].HP <= 0:
                                Player.Char.Exp += Monsters[int(Choice-1)].Exp
                                print(f"{Monsters[int(Choice-1)]} perished. [+{[Monsters.Choice-1].Exp} exp]")
                                CheckExp = level_up()
                                Monsters.remove(Monsters[int(Choice-1)])
                                if Player.Char.Vocation == "Necromancer" and Player.Char.Souls < Player.Char.MaxSouls:
                                    Player.Char.Souls += 1
                                    print("\nWorking your dark magics, you make your enemy's souls serve you.")
                                    print(f"[Souls: {Player.Char.Souls}/{Player.Char.MaxSouls}]")
                                if Player.Char.Vocation == "Wizard":
                                    NewAmount = int(Player.Char.Int * 0.1)
                                    Player.Char.Int += NewAmount
                                    Player.Char.Abilities[1].Amount += NewAmount
                                    if len(Monsters) > 0:
                                        Player.Char.Abilities[1].AbCooldown = 3
                                    else:
                                        Player.Char.Abilities[1].AbCooldown = 2
                                    print(f"\nOutwitting your opponent, you get a boost of confidence. Your INT is temporarily raised by {NewAmount}. It is now at {Player.Char.Int}")
                                if Player.Char.Vocation == "BarBarian":
                                    NewAmount = int(Player.Char.Str * 0.3)
                                    Player.Char.MinDmg += NewAmount
                                    Player.Char.MaxDmg += NewAmount                                    
                                    Player.Char.Abilities[1].Amount += NewAmount
                                    if len(Monsters) > 0:
                                        Player.Char.Abilities[1].AbCooldown = 3
                                    else:
                                        Player.Char.Abilities[1].AbCooldown = 2
                                    print(f"\nYour opponent falls. You feel blood rushing to your head. Everyone shall know your fury now! Your damage is temporarily raised by {NewAmount}. It is now {Player.Char.MinDmg}—{Player.Char.MaxDmg}")
                                time.sleep(2)
                                if len(Monsters) == 0:
                                    cooldown = cooldowns("encounter")
                                    cooldown = cooldowns("turn")
                                    victory()
                                else:
                                    monster_turn()
                if Monsters[int(Choice-1)].HP <= 0:
                    Player.Char.Exp += Monsters[int(Choice-1)].Exp
                    print(f"{Monsters[int(Choice-1)]} perished. [+{[Monsters.Choice-1].Exp} exp]")
                    CheckExp = level_up()
                    Monsters.remove(Monsters[int(Choice-1)])
                    if Player.Char.Vocation == "Necromancer" and Player.Char.Souls < Player.Char.MaxSouls:
                        Player.Char.Souls += 1
                        print("\nWorking your dark magics, you make your enemy's souls serve you.")
                        print(f"[]Souls: {Player.Char.Souls}/{Player.Char.MaxSouls}]")
                    if Player.Char.Vocation == "Wizard":
                        NewAmount = int(Player.Char.Int * 0.1)
                        Player.Char.Int += NewAmount                        
                        Player.Char.Abilities[1].Amount += NewAmount
                        if len(Monsters) > 0:
                            Player.Char.Abilities[1].AbCooldown = 3
                        else:
                            Player.Char.Abilities[1].AbCooldown = 2
                        print(f"\nOutwitting your opponent, you get a boost of confidence. Your INT is temporarily raised by {NewAmount}. It is now at {Player.Char.Int}")
                    if Player.Char.Vocation == "BarBarian":
                        NewAmount = int(Player.Char.Str * 0.3)
                        Player.Char.MinDmg += NewAmount
                        Player.Char.MaxDmg += NewAmount
                        Player.Char.Abilities[1].Amount += NewAmount
                        if len(Monsters) > 0:
                            Player.Char.Abilities[1].AbCooldown = 3
                        else:
                            Player.Char.Abilities[1].AbCooldown = 2
                        print(f"\nYour opponent falls. You feel blood rushing to your head. Everyone shall know your fury now! Your damage is temporarily raised by {NewAmount}. It is now {Player.Char.MinDmg}—{Player.Char.MaxDmg}")
                    time.sleep(2)
                    if len(Monsters) == 0:
                        cooldown = cooldowns("encounter")
                        cooldown = cooldowns("turn")
                        victory()
                    else:
                        monster_turn()
                else:
                    print(f"\n{Monsters[int(Choice-1)]} is now at {Monsters[int(Choice-1)].HP} HP")
                    time.sleep(3)
                    monster_turn()
            else:
                Dmg = calculate_dmg(Player.Char, Monsters[0])
                if AngryShout:
                    Dmg = Dmg * 2
                    AngryShout = False
                Monsters[0].HP -= Dmg
                print(f"\n{Player.Char.Name} attacks {Monsters[0]} for {Dmg} dmg")
                if Monsters[0].HP <= 0:
                    Player.Char.Exp += Monsters[0].Exp
                    print(f"{Monsters[0]} has perished. [+{Monsters[0].Exp} exp]")
                    Monsters.remove(Monsters[0])
                    CheckExp = level_up()
                    if Player.Char.Vocation == "Necromancer" and Player.Char.Souls < Player.Char.MaxSouls:
                        Player.Char.Souls += 1
                        print("\nWorking your dark magics, you make your enemy's souls serve you.")
                        print(f"[]Souls: {Player.Char.Souls}/{Player.Char.MaxSouls}]")
                    if Player.Char.Vocation == "Wizard":
                        NewAmount = int(Player.Char.Int * 0.1)
                        Player.Char.Int += NewAmount                        
                        Player.Char.Abilities[1].Amount += NewAmount
                        Player.Char.Abilities[1].AbCooldown = 2
                        print(f"\nOutwitting your opponent, you get a boost of confidence. Your INT is temporarily raised by {NewAmount}. It is now at {Player.Char.Int}")
                    if Player.Char.Vocation == "BarBarian":
                        NewAmount = int(Player.Char.Str * 0.3)
                        Player.Char.MinDmg += NewAmount
                        Player.Char.MaxDmg += NewAmount
                        Player.Char.Abilities[1].Amount += NewAmount
                        Player.Char.Abilities[1].AbCooldown = 2
                        print(f"\nYour opponent falls. You feel blood rushing to your head. Everyone shall know your fury now! Your damage is temporarily raised by {NewAmount}. It is now {Player.Char.MinDmg}—{Player.Char.MaxDmg}")
                    time.sleep(2)
                    cooldown = cooldowns("encounter")
                    cooldown = cooldowns("turn")
                    victory()
                else:
                    print(f"\n{Monsters[0]} is now at {Monsters[0].HP} HP")
                    time.sleep(3)
                    for Element in Player.Char.Allies:
                        if Element.Name == Player.Char.Name:
                            continue
                        else:
                            Dmg = calculate_dmg(Element, Monsters[0])
                            Monsters[0].HP -= Dmg
                            print(f"{Element.Name} attacks {Monsters[0]} for {Dmg} dmg")
                            if Monsters[0].HP <= 0:
                                Player.Char.Exp += Monsters[0].Exp
                                print(f"{Monsters[0]} perished. [+{Monsters[0].Exp} exp]")
                                CheckExp = level_up()
                                Monsters.remove(Monsters[0])
                                if Player.Char.Vocation == "Wizard":
                                    NewAmount = int(Player.Char.Int * 0.1)
                                    Player.Char.Int += NewAmount                                    
                                    Player.Char.Abilities[1].Amount += NewAmount
                                    Player.Char.Abilities[1].AbCooldown = 2
                                    print(f"\nOutwitting your opponent, you get a boost of confidence. Your INT is temporarily raised by {NewAmount}. It is now at {Player.Char.Int}")
                                if Player.Char.Vocation == "Necromancer" and Player.Char.Souls < Player.Char.MaxSouls:
                                    Player.Char.Souls += 1
                                    print("\nWorking your dark magics, you make your enemy's souls serve you.")
                                    print(f"[Souls: {Player.Char.Souls}/{Player.Char.MaxSouls}]")
                                if Player.Char.Vocation == "BarBarian":
                                    NewAmount = int(Player.Char.Str * 0.3)
                                    Player.Char.MinDmg += NewAmount
                                    Player.Char.MaxDmg += NewAmount
                                    Player.Char.Abilities[1].Amount += NewAmount
                                    Player.Char.Abilities[1].AbCooldown = 2
                                    print(f"\nYour opponent falls. You feel blood rushing to your head. Everyone shall know your fury now! Your damage is temporarily raised by {NewAmount}. It is now {Player.Char.MinDmg}—{Player.Char.MaxDmg}")
                                time.sleep(2)
                                cooldown = cooldowns("encounter")
                                cooldown = cooldowns("turn")
                                victory()
                    monster_turn()
        case "u":
            if Player.Char.InventorySize == 0:
                print("\nYou don't have anything.")
                time.sleep(3)
                player_turn()

            Usable = []

            for Item in Player.Char.Inventory:
                if Item.Location == "heal" or Item.Location == "buff":
                    Usable.append(Item)
            
            if len(Usable) == 0:
                Back = input("You don't have any usable items in your inventory. Press 'Enter' to go back... ")
                player_turn()

            print(f"\nINVENTORY")
            Num = 1
            for Item in Usable:
                print(f"\n{Num}. {Item.Name}: {Item.Description}")     

            Choice = input("Which item would you like to use? Enter '0' to go back... ") 
            while int(Choice) not in range (0, len(Usable)+1):
                Choice = input("Please, pick a valid number or enter '0; to go back... ")
            if Choice == "0":
                player_turn()
            
            if Usable[int(Choice)-1].Location == "heal":
                Heal = use_heal(Usable[int(Choice)-1])
                monster_turn()
            elif Usable[int(Choice)-1].Location == "buff":
                buff = use_buff(Usable[int(Choice)-1])
                monster_turn()

        case "b":
            Usable = []
            for Element in Player.Char.Abilities:
                if Element.AbType == "active":
                    Usable.append(Element)
            print("\nHere are the abilities you can use:")
            num = 1
            for Element in Usable:
                print(f"\n{num}. {Element.Name}: {Element.Description}")
                if Element.AbCooldown > 1:
                    print(f"ON COOLDOWN: {Element.AbCooldown} {Element.CooldownType}s")
                elif Element.AbCooldown == 1:
                    print(f"ON COOLDOWN: 1 {Element.CooldownType}")
            Choice = input("\nWhich ability would you like to use? Enter '0' to go back... ")
            while int(Choice) not in range(0,len(Usable)+1):
                Choice = input("\nPlease, pick a valid number or enter '0' to go back... ")
            if Choice == "0":
                player_turn()
            if Usable[int(Choice)-1].AbCooldown != 0:
                print(f"\n{Usable[int(Choice)-1].Name} is on cooldown.")
                time.sleep(2)
                player_turn()
            Cast = use_ability(Usable[int(Choice)-1])
            if Usable[int(Choice)-1].Name == "Deadly Spark":
                Which = input("\nWhich enemy would you like to burn? Enter '0' to cancel... ")
                while int(Which) not in range (0, len(Monsters)+1):
                    Which = int(input("\nPlease, enter a valid number or '0' to cancel... "))
                if Which == "0":
                    Usable[int(Choice)-1].AbCooldown = 0
                    player_turn()
                else:
                    Monsters[int(Which)-1].HP -= Cast
                    print(f"\nYou hurl magic flame at your adversary, hitting them for {Cast} dmg. They shriek in pain.")
                    if Monsters[0].HP <= 0:
                        Player.Char.Exp += Monsters[int(Which)-1].Exp
                        print(f"{Monsters[int(Which)-1]} perished. [+{Monsters[int(Which)-1].Exp} exp]")
                        CheckExp = level_up()
                        Monsters.remove(Monsters[int(Which)-1])
                        NewAmount = int(Player.Char.Int * 0.25)
                        Player.Char.Int += NewAmount
                        Player.Char.Abilities[1].Amount += NewAmount
                        if len(Monsters) > 0:
                            Player.Char.Abilities[1].AbCooldown = 3
                        else:
                            Player.Char.Abilities[1].AbCooldown = 2
                        print(f"\nOutwitting your opponent, you get a boost of confidence. Your INT is temporarily raised by {NewAmount}. It is now at {Player.Char.Int}")
                        cooldown = cooldowns("encounter")
                        cooldown = cooldowns("turn")
                        time.sleep(2)
                        victory()
                    else:
                        monster_turn()
            monster_turn()
        case "r":
            FleeRoll = random.randint(1,100) - int(Player.Char.Fai * 0.5)
            if FleeRoll <= 35:
                print("\nYou flee the battlefield.")
                if Player.Char.InventorySize > 0:
                    LoseRoll = random.randint(1,100) + int(Player.Char.Fai * 0.5)
                    if LoseRoll <= 30:
                        LoseItem = random.random(0, len(Player.Char.Inventory))
                        print(f"In all the confusion you somehow lose the {LoseItem}")
                        remove_item_buff(LoseItem)
                        Player.Char.Inventory.remove(LoseItem)
                        Player.Char.InventorySize -= 1
                        GoOn = input("Press 'Enter' to continue... ")
            else:
                print("\nYou try to get away but fail to do so. ")
                GoOn = input("Press 'Enter' to continue... ")
                monster_turn()

def monster_turn():
    cooldowns("turn")
    AllyList = Player.Char.Allies
    for Element in Monsters:
        Target = random.randint(0,len(AllyList))
        Evade = False
        if AllyList[Target-1].Vocation == "Warrior":
            EvadeRoll = random.randint(1,100) - AllyList[Target-1].Str / 2
            if EvadeRoll < 10:
                Evade = True
        if Evade == True:
            print(f"{Element.Name} tries to hit {AllyList[Target-1].Name}, but they narrowly evade the oncoming strike.")
            Evade = False
            time.sleep(2)
            continue
        Dmg = calculate_dmg(Element, AllyList[Target-1])
        Player.Char.HP -= Dmg
        print(f"\n{Element.Name} attacks {AllyList[Target-1].Name} for {Dmg} dmg")
        if AllyList[Target-1].HP <= 0 and AllyList[Target-1].Name == Player.Char.Name:
            defeat()
        elif AllyList[Target-1].HP <= 0 and AllyList[Target-1].Name != Player.Char.Name:
            print(f"\nYour {AllyList[Target-1].Name} perished.")
            AllyList.remove(AllyList[Target-1])
            time.sleep(2)
        if Player.Char.HP < int(Player.Char.MaxHP * 0.2) and Player.Char.Vocation == "Cleric" and Player.Char.NearDeath == False:
            Player.Char.NearDeath == True
            Player.Char.Abilities[1].Amount += Player.Char.Fai
            Player.Char.Fai += Player.Char.Fai
            print(f"Sensing that death is near, you hold fast in your convictions. Your FAI has doubled. It is now at {Player.Char.Fai}")
        if AllyList[Target-1].Name == Player.Char.Name:
            print(f"{Player.Char.Name} is now at {Player.Char.HP} HP")
            time.sleep(2)
    player_turn()

def cooldowns(Scope):

    for Element in Player.Char.Abilities:
        if Element.CooldownType == Scope and Element.AbCooldown > 0:
            Element.AbCooldown -= 1
            if Element.AbCooldown == 0:
                if Element.Name == "Dangerous Cunning":
                        Player.Char.Int -= Element.Amount
                        Element.Amount = 0
                        print("Dangerous Cunning has expired.")
                        time.sleep(2)
                if Element.Name == "Angry Shout":
                        print("Angry Shout is not on cooldown anymore.")
                        time.sleep(2)
                if Element.Name == "Bloodlust":
                        Player.Char.MinDmg -= Element.Amount
                        Player.Char.MaxDmg -= Element.Amount
                        Element.Amount = 0
                        print("Bloodlust has expired.")
                        time.sleep(2)
                if Element.Name == "Brace for Impact":
                        print("Brace for Impact is not on cooldown anymore.")
                        time.sleep(2)
                if Element.Name == "Mending":
                        print("Mending is not on cooldown anymore.")
                if Element.Name == "Deadly Spark":
                        print("Deadly Spark is not on cooldown anymore.")
                        time.sleep(2)
        if Element.EffectCooldownType == Scope:
            Element.EffectCooldown -= 1
            if Element.EffectCooldown == 0:
                if Element.Name == "Brace for Impact":
                    Player.Char.Prot -= Element.Amount
                    Element.Amount = 0
                    print("Brace For Impact has expired.")
    ElementsToRemove = []
    for Element in Player.Char.PotionEffects:
        if Element.Scope == Scope and Element.Cooldown > 0:
            Element.Cooldown -= 1
            print(f"Processing {Element.Name}: cooldown reduced to {Element.Cooldown}")
            if Element.Cooldown == 0:
                if Element.Stat == "dmg":
                    Player.Char.MinDmg -= Element.Modifier
                    Player.Char.MaxDmg -= Element.Modifier
                    print(f"\n{Element.Name} has worn off.")
                    time.sleep(2)
                if Element.Stat == "str":
                    Player.Char.Str -= Element.Modifier
                    print(f"\n{Element.Name} has worn off.")
                    time.sleep(2)
                if Element.Stat == "int":
                    Player.Char.Int -= Element.Modifier
                    print(f"\n{Element.Name} has worn off.")
                    time.sleep(2)
                if Element.Stat == "fai":
                    Player.Char.Fai -= Element.Modifier
                    print(f"\n{Element.Name} has worn off.")
                    time.sleep(2)
                if Element.Stat == "prot":
                    Player.Char.Prot -= Element.Modifier
                    print(f"\n{Element.Name} has worn off.")
                    time.sleep(2)
                ElementsToRemove.append(Element)
    for Element in ElementsToRemove:
        if Element in Player.Char.PotionEffects:
            Player.Char.PotionEffects.remove(Element)

def use_ability(Ability):
    global AngryShout

    match Ability.Name:
        case "Mending":
            Player.Char.HP += Player.Char.Fai * 2
            if Player.Char.HP > Player.Char.MaxHP:
                Player.Char.HP = Player.Char.MaxHP
                Ability.AbCooldown = 2
            if Player.Char.NearDeath:
                Player.Char.NearDeath == False
                Player.Char.Fai -= Player.Char.Abilities[1].Amount
                print("In My Hour of Need has expired.")
                time.sleep(2)
            return
        case "Rise and Fight":
            NewAlly = create_ally("Skeleton", "EnemyMolds")
            Player.Char.Souls -= 1
            return
        case "Angry Shout":
            AngryShout = True
            Ability.AbCooldown = 2
        case "Deadly Spark":
            Dmg = Player.Char.Int * 2
            Ability.AbCooldown = 2
            return Dmg
        case "Brace for Impact":
            Ability.Amount += Player.Char.Str * 0.8
            Player.Char.Prot += Player.Char.Str * 0.8            
            Ability.AbCooldown = 2
            Ability.EffectCooldown = 3

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
    print("\nYou have prevailed! Your reward is:")
    Money = int(random.randint(int(Player.Char.ToLevel / 8), int(Player.Char.ToLevel / 4)))
    Player.Char.Gold += Money
    print(f"[{Money} gold]")
    ItemRoll = random.randint(1, 100)
    check = Player.Char.Level
    if check < 15:
        Tier = 1
    elif check >= 15 and check < 40:
        Tier = 2
    elif check >= 40:
        Tier = 3

    if ItemRoll <= 20:
        match Tier:
            case 1:
                Reward = find_item("small")
            case 2:
                Reward = find_item("mid")
            case 3:
                Reward = find_item("large")

        Grab = CheckForSpace(Reward)

    GoOn = input("Press 'Enter' to continue... ")
    main_menu()

def defeat():
    global EncounterCounter
    global PositiveEncounters
    global Battles
    global ItemsFound
    global ItemsKept
    global GoldAcquired
    global Monsters

    if Player.Char.Vocation == "Necromancer" and Player.Char.Souls > 0:
        Player.Char.Souls -= 1
        print("""\nYou feel the cold embrace of death, but you are not scared,
              for you know this is not the end. The souls in your possession
              tremble and wail. You reach for one of them and present it
              to the void. It will be an offering that shall take your intended
              place in the dark. Because you are a necromancer, a master of undeath.
              And you are not dying today. Not yet...""")
        GoOn = input("\nPress 'Enter' to continue")

    print("\nYOU HAVE BEEN DEFEATED!")
    print("\nYour champion was...")
    print(f"{Player.Char}")
    print(f"""\nDuring your travels you had {EncounterCounter} encounters.
    {PositiveEncounters} of them were peaceful.
    {Battles} of them were battles.
    You found {ItemsFound} items and kept {ItemsKept} of them.
    You also acquired {GoldAcquired} gold.""")

    EncounterCounter = 0
    PositiveEncounters = 0
    Battles = 0
    ItemsFound = 0
    ItemsKept = 0
    GoldAcquired = 0
    Monsters = []

    Again = input("\nWould you like to play again? [y/n]")
    while Again not in ("y", "n"):
        Again = input("Please, say either 'y' or 'n'... ")
    if Again == "y":
        create_character()
        welcome()
    else:
        print("Thank you for playing! Hope to see you again soon.")
        time.sleep(2)
        exit()

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

def open_inventory():
    print(f"\nINVENTORY")
    Num = 1
    for Item in Player.Char.Inventory:          
        print(f"\n{Num}. {Item.Name}")
        if not hasattr(Item, "Prefix"):
            print(f"{Item.Description} ")
        else:
            print(f"{Item.Prefix.Name}: {Item.Prefix.Description}")
            print(f"{Item.Core.Name}: {Item.Core.Description}")
        Num += 1
    
    choice = input("Would you like to [d]iscard an item, [u]se one or go [b]ack? ")
    while choice != "d" and choice != "u" and choice != "b":
        choice = input("\nChoose: [d]iscard, [u]se or go [b]ack? ")
    match choice:
        case "b":
            pass
        case "u":
            if Player.Char.InventorySize == 0:
                choice = input("\nYou don't have anything. Press 'Enter' to go back... ")
            else:
                choice = input("\nWhat would you like to use? Enter '0' to go back. ")
                while int(choice) not in range(0, Player.Char.InventorySize+1):
                    choice = input("\nPlease, enter a valid number or '0' to go back... ")
                if choice == "0":
                    open_inventory()
                else:
                    x = int(choice)
                    if Player.Char.Inventory[x-1].Location != "heal" and Player.Char.Inventory[x-1].Location != "buff":
                        choice = input(f"\nThe {Player.Char.Inventory[x-1].Name} is not usable in this way. Press 'Enter' to go back... ")
                        open_inventory()
                    elif Player.Char.Inventory[x-1].Location == "heal":
                        Heal = use_heal(Player.Char.Inventory[x-1])
                    elif Player.Char.Inventory[x-1].Location == "buff":
                        Buff = use_buff(Player.Char.Inventory[x-1])
                    open_inventory()
        case "d":
            if Player.Char.InventorySize == 0:
                choice = input("\nYou don't have anything. Press 'Enter' to go back... ")
            else:
                choice = input("\nWhat would you like to discard? Enter '0' to go back. ")
                choice = int(choice)
                while choice not in range(0, len(Player.Char.Inventory)+1):
                    choice = input("\nPlease, enter a valid number or '0' to go back... ")
                if choice == "0":
                    open_inventory()
                else:
                    x = int(choice)
                    sure = input(f"\nAre you sure? The {Player.Char.Inventory[x-1]} will be lost forever. [y/n]")
                    while sure != "y" and sure != "n":
                        sure = input("\fPlease, say either 'y' or 'n'... ")
                    if sure == "y":
                        MinusBuff = remove_item_buff(Player.Char.Inventory[x-1])
                        print(f"\n{Player.Char.Inventory[x-1]} has been discarded.")
                        ToDelete = Player.Char.Inventory[x-1]
                        MinusBuff = remove_item_buff(ToDelete)
                        Player.Char.Inventory.remove(ToDelete)
                        open_inventory()

def choose_ability(Status):
    Usable = []
    for Ability in Player.Char.Abilities:
        if (Ability.Scope == Status or Ability.Scope == "all") and Ability.AbType == "active":
            Usable.append(Ability)
    if len(Usable) == 0:
        Nothing = input("\nYou don't have any abilities that you can use now. Press 'Enter' to continue. ")
    else:
        print("\nHere are the abilities you can use now:")
        print("")
        num = 1
        for Ability in Usable:
            print(f"{num}. {Ability.Name}: {Ability.Description}")
            if Ability.AbCooldown > 1:
                    print(f"ON COOLDOWN: {Ability.AbCooldown} {Ability.CooldownType}s")
            elif Ability.AbCooldown == 1:
                print(f"ON COOLDOWN: 1 {Ability.CooldownType}")
        Choice = input("\nWhich ability would you like to use? Enter '0' to go back...")
        while int(Choice) not in range(0, len(Usable)+1):
            Choice = input("\nPlease, enter a valid number or '0' to go back... ")
        if Choice != "0":
            if Usable[int(Choice)-1].AbCooldown != 0:
                print(f"\n{Usable[int(Choice)-1].Name} is on cooldown.")
                time.sleep(2)
                choose_ability("all")
            use_ability(Usable[int(Choice)-1])
        else:
            return

def use_heal(Item):
    Player.Char.HP += Item.Modifier
    if Player.Char.HP > Player.Char.MaxHP:
        Player.Char.HP = Player.Char.MaxHP
    if Player.Char.Vocation == "Cleric" and Player.Char.NearDeath:
        Player.Char.NearDeath = False
        Player.Char.Fai -= Player.Char.Abilities[1].Amount
    Player.Char.Inventory.remove(Item)
    Player.Char.InventorySize -= 1
    Healed = input(f"{Player.Char.Name} healed for {Item.Modifier} HP. They are now at {Player.Char.HP} HP. Press 'Enter' to go back... ")
    return

def use_buff(Item):
    match Item.Stat:
        case "dmg":
            Player.Char.MinDmg += Item.Modifier
            Player.Char.MaxDmg += Item.Modifier
            Item.Cooldown = Item.MaxCooldown
            Player.Char.PotionEffects.append(Item)
            Player.Char.Inventory.remove(Item)
            Player.Char.InventorySize -= 1
            print(f"{Player.Char.Name} consumes the {Item.Name}")
            return
        case "str":
            Player.Char.Str += Item.Modifier
            Item.Cooldown = Item.MaxCooldown
            Player.Char.PotionEffects.append(Item)
            Player.Char.Inventory.remove(Item)
            Player.Char.InventorySize -= 1
            print(f"{Player.Char.Name} consumes the {Item.Name}")
            return
        case "int":
            Player.Char.Int += Item.Modifier
            Item.Cooldown = Item.MaxCooldown
            Player.Char.PotionEffects.append(Item)
            Player.Char.Inventory.remove(Item)
            Player.Char.InventorySize -= 1
            print(f"{Player.Char.Name} consumes the {Item.Name}")
            return
        case "fai":
            Player.Char.Fai += Item.Modifier
            Item.Cooldown = Item.MaxCooldown
            Player.Char.PotionEffects.append(Item)
            Player.Char.Inventory.remove(Item)
            Player.Char.InventorySize -= 1
            print(f"{Player.Char.Name} consumes the {Item.Name}")
            return
        case "prot":
            Player.Char.Prot += Item.Modifier
            Item.Cooldown = Item.MaxCooldown
            Player.Char.PotionEffects.append(Item)
            Player.Char.Inventory.remove(Item)
            Player.Char.InventorySize -= 1
            print(f"{Player.Char.Name} consumes the {Item.Name}")
            return

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

def create_ally(Name, List):
    if List == "EnemyMolds":
        for Candidate in EnemyMolds:                      
            if Candidate[0] == Name:
                MonsterName = Candidate[0]
                MonsterHP = random.randint(int(Candidate[1]), int(Candidate[2]))
                MonsterVocation = Candidate[3]
                MonsterStr = random.randint(int(Candidate[4]), int(Candidate[5]))
                MonsterInt = random.randint(int(Candidate[6]), int(Candidate[7]))
                MonsterFai = random.randint(int(Candidate[8]), int(Candidate[9]))
                MonsterMinDmg = random.randint(int(Candidate[10]), int(Candidate[11]))
                MonsterMaxDmg = random.randint(int(Candidate[12]), int(Candidate[13]))
                MonsterProt = random.randint(int(Candidate[14]), int(Candidate[15]))
                MonsterTier = int(Candidate[16])
                MonsterExp = int(Candidate[17])
                Monster = Enemy(MonsterName, MonsterHP, MonsterVocation, MonsterStr, MonsterInt, MonsterFai, MonsterMinDmg, MonsterMaxDmg, MonsterProt, MonsterTier, MonsterExp)
                print(f"{Monster} joins the fray!") 
                Player.Char.Allies.append(Monster)
                return

def create_item(PrefixNum=None, CoreNum=None):
    if PrefixNum == None or CoreNum == None:
        PrefixNum = random.randint(0, len(Prefixes)-1)
        CoreNum = random.randint(0, len(Cores)-1)

    NewItem = Item(Prefixes[PrefixNum], Cores[CoreNum])
    print(f"{NewItem} was created!")
    return NewItem

PlayerName = input("\nWhat is your name? ")
unpack_lists()
create_player(PlayerName)
create_character()

welcome()