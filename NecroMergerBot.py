# This is a bunch of functions based around the game Necromerger

def gold_guide():
    goldguide = """
    Gold I've Spent:
    DE 5% All Skin 		2000 gold  2000 total
    TS +2 All Skin 		1250 gold  3250 total
    NM Darkness Skin 	1500 gold  4750 total
    NM Slime Skin 		1000 gold  5750 total
    NM Mana Skin 		0500 gold  6250 total
    TS Cauldron Skin 	1750 gold  8000 total
    TS Chicken Skin		0750 gold  8750 total
    Safe    			0500 gold  9250 total
    Safe +2 (6) 		1000 gold 10250 total
    Safe +2 (8) 		1500 gold 11750 total
    Safe +2 (10)		2000 gold 13750 total
    """
    print(goldguide)


def gems_guide():
    gemsguide = """
    Gems I've spent:
    Crate 	base 4  		0250 gems 0250 total
    Cage 	base 4  		0250 gems 0500 total
    Crate 	+2 (6)  		0500 gems 1000 total
    Crate   +2 (8)   		0750 gems 1750 total
    Diet    +1 (2)  		0250 gems 2000 total
    Diet	+1 (3)  		0500 gems 2500 total
    Cage    +2 (6)  		0500 gems 3000 total
    NM 	5% champ         	0750 gems 
    Cage 	+2 (8)  		0750 gems
    ThemeE  Cosmic/Blood	1500 gems
    Crate	+2 (10) 		1000 gems 
    Cage 	+2 (10) 		1000 gems
    ThemeA  Ice/Moon/Cosmic 2000 gems 
    ThemeP  Blood/Death 	1500 gems
    ThemeT	Poison/Moon 	1500 gems
    NM	10% dmg 	    	0250 gems 
    NM 	10% food        	0500 gems 
    DE	20% dmg     		1250 gems
    DE 	20% food           	1000 gems
    """
    print(gemsguide)


# Devourer level base * (100%+Feats bonus) * (100%+Legendaries bonus) * (100%+Other bonus)=Total Shards
def time_shard_calculator(DevourerLevel, FeatLevel, T1L, T2L, T3L, Robo, ShieldBot, SSLeg, BabyTrueFalse):
    DevourerShards = {
        "35": 150,
        "40": 275,
        "45": 500,
        "50": 750,
        "55": 1000,
        "60": 1500,
        "65": 2000,
        "70": 3250,
        "75": 4500,
        "80": 5750,
        "85": 7500,
        "90": 10000,
        "95": 12500,
        "100": 15000
    }
    if DevourerLevel % 5 != 0:
        DLremainder = DevourerLevel % 5
        DevourerLevel = str(DevourerLevel - DLremainder)
        DevourerLevel = DevourerShards.get(DevourerLevel)
    else:
        DevourerLevel = DevourerShards.get(str(DevourerLevel))
    # Max feat level is 25, first prestige is *supposed* to prestige after 16
    if FeatLevel > 25:
        FeatLevel = 25
    elif FeatLevel < 16:
        print("You shouldn't prestige until you finish all of your feats.")
    FeatShards = FeatLevel/10
    #   Legendary bonuses
    #   "T1": 20 all, 10 first, 5 subsequent
    #   "T2": 40 all, 20 first, 10 subsequent
    #   "T3": 60 all, 30 each, cap 1 each
    #   "T4": 80 all
    #   "Robo": 20, cap 3
    #   "ShieldBot": 30, cap 3
    #   "SoulStalker": 40
    LegendaryBonus = 0
    if T1L >= 3:
        LegendaryBonus += (T1L * .05) + .35
    elif 3 > T1L > 0:
        LegendaryBonus += T1L * .10
    if T2L >= 3:
        LegendaryBonus += (T2L * .10) + .7
    elif 3 > T2L > 0:
        LegendaryBonus += T2L * .20
    if T3L >= 3:
        LegendaryBonus += 1.5
    elif 3 > T3L > 0:
        LegendaryBonus += (T3L * .3)
    if Robo > 3:
        Robo = 3
    if ShieldBot > 3:
        ShieldBot = 3
    if Robo > 0 and ShieldBot > 0 and SSLeg > 0:
        LegendaryBonus += (Robo * .2) + (ShieldBot * .3) + (SSLeg * .4) + .8
    else:
        LegendaryBonus += (Robo * .2) + (ShieldBot * .3) + (SSLeg * .4)
    # Does player have Baby skin?
    if BabyTrueFalse != False:
        OtherBonus = .05
    else:
        OtherBonus = 0
    return DevourerLevel*(1 + FeatShards)*(1 + LegendaryBonus)*(1 + OtherBonus)


def rune_farming():
    print("REMEMBER TO PLACE YOUR RELEVANT RELIC ON THE PEDESTAL AND ACTIVATE!")
    print("Optimal champion farming stations per 1 million mana | 750k slime | 500k darkness:")
    peasants = """
        Peasants:
        T4 Grave:           22.24
        T5 Grave:           21.28
        T2 Grave:           19.74
        T5 Supply Cupboard: 18.35
        Note: the supply cupboard is worse than any grave except t1
    """
    knights = """
        Knights:
        T2 Supply Cupboard: 13.60
        T2 Alter:           11.67
        T1 Supply Cupboard: 11.66
        T1 Alter:           10.00
        T1 Fridge:          8.16
    """
    clerics = """
        Clerics:
        T5 Alter:           7.07
        T4 Alter:           5.78
        T2 Lectern:         5.60
        T1 Lectern:         4.20
        T3 Alter:           3.09
    """
    paladins = """
        Paladins:
        T1 Saucer (Dark):   3.33
        T1 Saucer (Slime):  2.34
        T5 Lectern:         2.33
        T3 Fridge:          2.09
        T3 Portal:          1.78
        T4 Lectern:         1.75
    """

    rivals = """
        Rivals:
        T5 Fridge:          1.73
        T5 Portal:          1.50
        T4 Fridge:          0.74
        T4 Portal:          0.64
    """
    print(peasants)
    print(knights)
    print(clerics)
    print(paladins)
    print(rivals)


def damage_percent_calc(wearwolfdamage):
    wearwolfdamage /= 1000
    print("Your current damage multiplier is:", wearwolfdamage, " or ", (wearwolfdamage*100), "%")


def food_percent_calc(mummyfood):
    mummyfood /= 2000
    print("Your current food multiplier is:", mummyfood, " or ", (mummyfood*100), "%")


def complete_creature_cost():
    complete_creatures = """
        Resource Needed Per Minion:
        Skeleton: 	    55K T2 Grave
        Zombie: 	    75k	T5 Grave
        Eye Monster:	27K	T2 Supply Cupboard
        Mummy:		    37K	T5 Supply Cupboard
        Werewolf:	    14k	T2 Alter
        Bat:		    19K	T5 Alter
        Shade:		    20K	T2 Lectern // 80k T5 Lectern
        Banshee:	    60k	T5 Lectern
        Ghoul:		    32K T3 Fridge // 29K T1 Crashed Saucer (Slime)
        Abomination:	34K	T5 Fridge
        Imp:		    32K	T3 Portal // 17K T1 Crashed Saucer (Darkness)
        Demon:		    34K	T5 Portal
        Alien Mana:	    88K	T3 Crashed Saucer
        Alien Slime:	72K	T3 Crashed Saucer
        Alien Darkness:	56K	T3 Crashed Saucer
        Guzzler Mana:	46k	T3 Crashed Saucer
        Guzzler Slime:	40k	T3 Crashed Saucer
        Guzzler Dark:	34k	T3 Crashed Saucer
    """
    print(complete_creatures)


def food_farming():
    food_farm = """
        Food Optimization:
        Mana: T5 Lectern > T5 Grave > T2 Grave > T2 Lectern
        Slime: T5 Fridge > T5 Supply Cupboard > T1 Fridge > T3 Fridge> T2 Supply Cupboard
        Darkness: T5 Portal > T3 Portal > T5 Alter > T2 Alter
    """
    print(food_farm)


def station_cost_calculator(stationNumber=-1, levelNeeded=-1, levelHave=-1):
    completestationcosts = """
        Here are the T1 stations:
        |     |  Grave  | Supply Cupboard  |   Alter   |
        | T1: |  20 Ice |     20 Poison    |  20 Blood |
        | T2: |  40 Ice |     40 Poison    |  40 Blood |
        | T3: |  80 Ice |     80 Poison    |  80 Blood | 
        | T4: | 160 Ice |    160 Poison    | 160 Blood |
        | T5: | 320 Ice |    320 Poison    | 320 Blood |
        
        Here are resource storage:
        |     |      Mana Pool      |       Slime Vat       |     Dark Stores     |
        | T1: |   5 Poison  10 Ice  |   5 Blood  10 Poison  | 160 Moon 320 Blood  |
        | T2: |  10 Poison  20 Ice  |  10 Blood  20 Poison  | 160 Moon 320 Blood  |
        | T3: |  20 Poison  40 Ice  |  20 Blood  40 Poison  | 160 Moon 320 Blood  |
        | T4: |  40 Poison  80 Ice  |  40 Blood  80 Poison  | 160 Moon 320 Blood  |
        | T5: |  80 Poison 160 Ice  |  80 Blood 160 Poison  | 160 Moon 320 Blood  |
        | T6: | 160 Poison 320 Ice  | 160 Blood 320 Poison  | 160 Moon 320 Blood  |
        
        |     |  Foul Chicken:     |
        | T1: |  15 Poison  30 Ice |
        | T2: |  30 Poison  60 Ice |
        | T3: |  60 Poison 120 Ice |
        | T4: | 120 Poison 240 Ice |
        | T5: | 240 Poison 480 Ice |
        
        Here are the T2 stations:
        |     |      Lectern       |       Fridge        |        Portal       | Crashed Saucer |
        | T1: |  20 Moon  50 Ice   |  20 Moon 50 Poison  |  30 Blood  30 Death |    20 Cosmic   |
        | T2: |  40 Moon 100 Ice   |  40 Moon 100 Poison |  60 Blood  60 Death |    40 Cosmic   |
        | T3: |  80 Moon 200 Ice   |  80 Moon 200 Poison | 120 Blood 120 Death |    80 Cosmic   |
        | T4: | 160 Moon 400 Ice   | 160 Moon 400 Poison | 240 Blood 240 Death |   160 Cosmic   |
        | T5: | 320 Moon 800 Ice   | 320 Moon 800 Poison | 480 Blood 480 Death |   320 Cosmic   |
        
        Other stations:
        |     |      Telepad     |     Soul Grinder     |         Prism         |
        | T1: | 30 Blood 30 Moon | 200 Cosmic 200 Death | 300 Moon   600 Ice    |
        | T2: |         X        | 400 Cosmic 400 Death | 250 Death  500 Poison |
        | T3: |         X        |          X           | 200 Cosmic 400 Blood  |
        Notes: Telepad is per spawn, Prism rotates between 1 2 and 3
    """
    if stationNumber == -1 and levelHave == -1 and levelNeeded == -1:
        print(completestationcosts)
    elif stationNumber < 1 or levelHave < 0 or levelNeeded < 0:
        print("Either missing arguments or incorrect arugments detected.")
        command_help_print = """
        Here's how to use this command:
        (Station Type | Level Needed | Level Obtained)
        
        Station Numbers:
        1: Grave            2: Supply Cupboard      3: Alter
        4: Mana Well        5: Slime Vat            6: Dark Store
        7: Lectern          8: Fridge               9: Portal
        10: Chicken
        11: Crashed Saucer
        12: Telepad
        13: Soul Grinder

        
        Level Needed:
        This is the level of station you want to have.
        
        Level Obtained:
        This is the level of station you currently have.  Enter 0 if you want to make a station from scratch.
        
        For example if I had a level 3 fridge and I wanted to know the cost to get to level 5 I would use
        (4,5,3)
        """
        print(command_help_print)
    # Grave | Supply Cupboard | Alter | Crashed Saucer
    if stationNumber == 1 or stationNumber == 2 or stationNumber == 3 or stationNumber == 11:
        runes_needed = (2 ** levelNeeded - 2 ** levelHave) * 20
        if stationNumber == 1:
            print("You need: ", runes_needed, " Ice Runes to get your station level ", levelNeeded)
        if stationNumber == 2:
            print("You need: ", runes_needed, " Poison Runes to get your station level ", levelNeeded)
        if stationNumber == 3:
            print("You need: ", runes_needed, " Blood Runes to get your station level ", levelNeeded)
        if stationNumber == 11:
            print("You need: ", runes_needed, " Cosmic Runes to get your station level ", levelNeeded)
    # Mana Well | Slime Vat | Dark Stores
    elif stationNumber == 4 or stationNumber == 5 or stationNumber == 6:
        runes_needed = (2 ** levelNeeded - 2 ** levelHave) * 10
        if stationNumber == 4:
            print("You need: ", runes_needed, " Ice Runes and ", (runes_needed/2),
                  " Poison runes to get your station level ", levelNeeded)
        if stationNumber == 5:
            print("You need: ", runes_needed, " Poison Runes and ", (runes_needed/2),
                  " Blood runes to get your station level ", levelNeeded)
        if stationNumber == 6:
            print("You need: ", runes_needed, " Blood Runes and ", (runes_needed/2),
                  " Moon runes to get your station level ", levelNeeded)
    # Chicken
    elif stationNumber == 10:
        runes_needed = (2 ** levelNeeded - 2 ** levelHave) * 30
        print("You need: ", runes_needed, " Ice Runes and ", (runes_needed / 2),
              " Poison runes to get your station level ", levelNeeded)
    # Lectern | Fridge
    elif stationNumber == 7 or stationNumber == 8:
        runes_needed = (2 ** levelNeeded - 2 ** levelHave) * 50
        if stationNumber == 7:
            print("You need: ", runes_needed, " Ice Runes and ", (runes_needed * (2/5)),
                  " Moon runes to get your station level ", levelNeeded)
        if stationNumber == 8:
            print("You need: ", runes_needed, " Poison Runes and ", (runes_needed * (2/5)),
                  " Moon runes to get your station level ", levelNeeded)
    # Portal
    elif stationNumber == 9:
        runes_needed = (2 ** levelNeeded - 2 ** levelHave) * 30
        print("You need: ", runes_needed, " Blood Runes and ", (runes_needed / 2),
              " Moon runes to get your station level ", levelNeeded)
    # Telepad
    elif stationNumber == 12:
        print("You need 30 blood and 30 moon runes per telepad spawn.")
    # Soul Grinder
    elif stationNumber == 13:
        runes_needed = (2 ** levelNeeded - 2 ** levelHave) * 200
        print("You need: ", runes_needed, " Death Runes and ", runes_needed,
              " Cosmic runes to get your station level ", levelNeeded)


def MonsterCalc():
    # todo create a clac to determine cost of a certain tier of monster given a station
    return 0


def Nectarguide():
    # todo
    return 0


def SRguide():
    # todo
    return 0


def DinoGuide():
    # todo
    return 0
