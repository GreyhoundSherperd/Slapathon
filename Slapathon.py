from random import shuffle
from random import randint

deck = []
for v in range(2):
    appenddeck = 1
    while appenddeck <= 10:
        deck.append(appenddeck)
        appenddeck += 1

for v in range(4):
    deck.append("+2")
    deck.append("+4")
    deck.append("WILDCARD")

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
Warnings = 0

def ordering():
    """
    Calculates the order of cards in a player's deck.

    This function takes no parameters.

    Returns:
        str: A string representing the order of cards in the player's deck. Each card is followed by a space and the number of occurrences of that card in the deck.
    """
    dict = {}
    for v in PlayerDeck:
        if v not in dict:
            dict.update({v : 1})
        else:
            dict[v] += 1
    
    strng = ""
    for x in dict:
        strng += str(x) + " " + str(dict[x]) + " "

    return strng

print("*** Welcome to the official Slapathon executable! ***")
print("*** For the rules, please see the README.md file. ***")
print("***                   Good luck!                  ***")
print("")

while (BotHP != 0 or PlayerHP != 0) and (lenB != 0 or lenP != 0):
    PlayerDeck.sort()
    BotDeck.sort()
    print("Your cards: ", PlayerDeck)
    cmd = input("Make a command: ")
    if cmd == "Play Soldier":
        if len(PlayerSols) >= 2:
            print("Sorry, your soldier slots have already been filled!")
            print("Penalty: Lose a turn")
            Warnings += 1
        else:
            cmd = int(input("Choose your desired soldier: "))
            if cmd in PlayerDeck:
                PlayerDeck.remove(cmd)
                PlayerSols.append(cmd)
                print("Soldier added! 💂")
            else:
                print("That soilder does not exist!")
                print("Penalty: Lose a turn")
                Warnings += 1

    elif cmd == "Play Officer":
        if len(PlayerOfficer) >= 1:
            print("Sorry, your officer slot has already been filled!")
            print("Penalty: Lose a turn")
            Warnings += 1
        else:
            cmd = int(input("Choose your desired officer (5 Strength or Above): "))
            if cmd in PlayerDeck:
                PlayerDeck.remove(cmd)
                PlayerOfficer.append(cmd)
                print("Officer added! 🥷")
            else:
                print("That officer does not exist!")
                print("Penalty: Lose a turn")
                Warnings += 1

    elif cmd == "Soldier Attack":
        if len(PlayerSols) == 0:
            print("You do not have any soldiers!")
            print("Penalty: Lose a turn")
            Warnings += 1
        else:
            if BotOfficer == [] and BotSols == []:
                print("There is nothing to attack!")
                print("Penalty: Lose a turn")
                Warnings += 1
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
                            print("Your soldier has dealt damage on the enemy 💥😨 ")
                    else:
                        print("That soldier does not exist!")
                        print("Penalty: Lose a turn")
                        Warnings += 1
                else:
                    print("That soldier does not exist!")
                    print("Penalty: Lose a turn")
                    Warnings += 1
    
    elif cmd == "Officer Attack":
        if len(PlayerOfficer) == 0:
            print("You do not have any officers!")
            print("Penalty: Lose a turn")
            Warnings += 1
        else:
            if BotOfficer == [] and BotSols == []:
                print("There is nothing to attack!")
                print("Penalty: Lose a turn")
                Warnings += 1
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
                                print("Unfortunately, your officer is injured! 🤕🏥")
                                print("But, with your help, he healed and decided to retire. 🧓🏼📺")