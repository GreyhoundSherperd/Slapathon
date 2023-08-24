

from random import shuffle
from random import randint

deck = []
for v in range(4):
    appenddeck = 1
    while appenddeck <= 10:
        deck.append(appenddeck)
        appenddeck += 1

shuffle(deck)

PlayerDeck = []
BotDeck = []

for v in range(len(deck)):
    if v <= 12:
        PlayerDeck.append(deck[v])
    else:
        BotDeck.append(deck[v])

BotHP, PlayerHP = 15, 15
lenB = len(BotDeck)
lenP = len(PlayerDeck)
PlayerOfficer = []
BotOfficer = []
PlayerSols = []
BotSols = []
warnings = 0

def ordering():
    dict = {}
    for v in PlayerDeck:
        if v not in dict:
            dict.update({v : 1})
        else:
            dict[v] += 1
    
    strng = ""
    for x in dict:
        strng += "Rank " + str(x) + " " + str(dict[x]) + ","

    return strng

print("*** Welcome to the official Slapathon executable! ***")
print("*** For the rules, please see the README.md file. ***")
print("***                   Good luck!                  ***")
print("")

while (lenB != 0) or (lenP != 0):
    PlayerDeck.sort()
    BotDeck.sort()
    print("Your cards: ", ordering())
    cmd = input("Make a command: ")
    if cmd == "Play Soldier":
        if len(PlayerSols) >= 2:
            print("Sorry, your soldier slots have already been filled!")
            print("Penalty: Lose a turn")
            warnings += 1
        else:
            cmd = int(input("Choose your desired soldier: "))
            if cmd in PlayerDeck:
                PlayerDeck.remove(cmd)
                PlayerSols.append(cmd)
                print("Soldier added! 💂")
            else:
                print("That soilder does not exist!")
                print("Penalty: Lose a turn")
                warnings += 1

    elif cmd == "Play Officer":
        if len(PlayerOfficer) >= 1:
            print("Sorry, your officer slot has already been filled!")
            print("Penalty: Lose a turn")
            warnings += 1
        else:
            cmd = int(input("Choose your desired officer (5 Strength or Above): "))
            if cmd in PlayerDeck:
                PlayerDeck.remove(cmd)
                PlayerOfficer.append(cmd)
                print("Officer added! 🥷")
            else:
                print("That officer does not exist!")
                print("Penalty: Lose a turn")
                warnings += 1

    elif cmd == "Soldier Attack":
        if len(PlayerSols) == 0:
            print("You do not have any soldiers!")
            print("Penalty: Lose a turn")
            warnings += 1
        else:
            if BotOfficer == [] and BotSols == []:
                print("There is nothing to attack!")
                print("Penalty: Lose a turn")
                warnings += 1
            else:
                cmd = int(input("Choose your desired soldier to attack: "))
                if cmd in PlayerSols:
                    currentAttacker = cmd
                    cmd = int(input("Choose your desired target 🎯: "))
                    currentDefender = cmd
                    if currentDefender in BotSols:
                        if currentAttacker >= currentDefender:
                            BotSols.remove(currentDefender)
                            print("The target has been slapped succesfully 😎👍")
                        elif currentAttacker < currentDefender:
                            PlayerSols.remove(currentAttacker)
                            BotSols[BotSols.index(currentDefender)] -= currentAttacker
                            print("You lost the fight, but your soldier has dealt damage on the enemy 💥😨 ")
                    else:
                        print("That soldier does not exist!")
                        print("Penalty: Lose a turn")
                        warnings += 1
                else:
                    print("That soldier does not exist!")
                    print("Penalty: Lose a turn")
                    warnings += 1
    
    elif cmd == "Officer Attack":
        if len(PlayerOfficer) == 0:
            print("You do not have any officers!")
            print("Penalty: Lose a turn")
            warnings += 1
        else:
            if BotOfficer == [] and BotSols == []:
                print("There is nothing to attack!")
                print("Penalty: Lose a turn")
                warnings += 1
            else:
                currentAttacker = BotOfficer[0]
                cmd = int(input("Choose your desired target 🎯: "))
                currentDefender = cmd
                if (currentDefender in BotSols) or (currentDefender in BotOfficer):
                    if currentAttacker >= currentDefender:
                        if currentDefender in BotSols:
                            BotSols.remove(currentDefender)
                            print("Your officer totally annihilated the target! 😵⚰️")
                        elif currentDefender in BotOfficer:
                            BotOfficer.remove(currentDefender)
                            print("Your officer totally had won the fight! 😄🙌")
                            injuries = randint(0, 2)
                            if injuries == 0:
                                print("Your officer is fine! 🥗👍")
                            elif injuries == 1:
                                print("Your officer is hurt! 🤕🚑")
                                print("He was damaged by ", str(currentDefender / 2), " damages! 🗡️🔫")
                                PlayerOfficer[0] -= currentDefender / 2
                                if PlayerOfficer[0] < 5:
                                    encounting = PlayerOfficer[0]
                                    PlayerOfficer.pop()
                                    if len(PlayerSols) >= 2:
                                        pass
                                    else:
                                        PlayerSols.append(encounting)
                                        print("Your officer is demoted to a ", str(encounting), " rank soldier! 💂")
                                else:
                                    pass
                            else:
                                print("Unfortunately, your officer is injured badly! 🤕🏥")
                                PlayerOfficer.pop()
                    else:
                        if currentDefender in BotSols:
                            experienceExtra = randint(0, 3)
                            if currentDefender - (currentAttacker + experienceExtra) <= 0:
                                BotSols.remove(currentDefender)
                                PlayerOfficer.pop()
                                if len(PlayerSols) >= 2:
                                    print("As people says, matter and anti-matter destroy both each other... ⚗️💥")
                                else:
                                    PlayerSols.append(1)
                                    print("Your officer had an exhausting fight! 🥱💤")
                                    print("Your officer is demoted to a 1 rank soldier! 💂")
                            else:
                                PlayerOfficer.pop()
                                print("Your officer had been defeated! 😵🪦")
                                print("Your officer has dealt damage on the enemy 💥😱")
                                BotSols[BotSols.index(currentDefender)] -= currentAttacker + experienceExtra
                        else:
                            injuries = randint(0, 1)
                            if injuries == 0:
                                PlayerOfficer.pop()
                                BotOfficer[0] -= currentAttacker
                                print("Your officer had been defeated! 😵🪦")
                                print("Your officer has dealt damage on the enemy 💥😱")
                            else:
                                PlayerOfficer.pop()
                                if len(PlayerSols) >= 2:
                                    print("Your officer had been defeated! 😵🪦")
                                    print("Your officer has dealt damage on the enemy 💥😱")
                                    BotOfficer[0] -= currentAttacker
                                else:
                                    PlayerSols.append(1)
                                    print("Your officer is demoted to a 1 rank soldier! 💂")
                else:
                    print("That soldier or officer does not exist!")
                    print("Penalty: Lose a turn")
                    warnings += 1
    
    elif cmd == "Swap Soldier":
        if len(PlayerSols) == 0:
            print("You don't have any soldiers!")
            print("Penalty: Lose a turn")
            warnings += 1
        else:
            cmd = int(input("Choose your desired soldier to swap ↩️: "))
            retiring = cmd
            if cmd in PlayerSols:
                cmd = int(input("Choose your desired soldier to swap with ↪️: "))
                advancing = cmd
                if cmd in PlayerDeck:
                    PlayerDeck.remove(advancing)
                    PlayerDeck.append(retiring)
                    PlayerSols.append(advancing)
                    PlayerSols.remove(retiring)
                    print("Soldier swapped! 🤸🏃")
                else:
                    print("That soldier does not exist!")
                    print("Penalty: Lose a turn")
                    warnings += 1
            else:
                print("That soldier does not exist!")
                print("Penalty: Lose a turn")
                warnings += 1
    
    lenP = len(PlayerDeck)
    lenB = len(BotDeck)

if lenP == 0:
    print("You lost the war, better luck next time. 😭💀")
else:
    print("You're the champion! 😄🏆")