# Aryan Gidwani
# ICS3UO - A
# December 29, 2021
# This program simulates an online version of the card game known as President. Each player will get a set amount of cards, and 
# will begin to play the game. In president, a player can play either singles, doubles, triples, or quadruples. The user can only play
# more than 1 card if all the cards that the user decides to play has the same number. For example, if the user has four 3's in their
# deck, the user can choose to play a single(one card), double(two cards), triple(three cards), or a quadruple(four cards) with the 
# number 3, barring the suit of the card. If the user decides to play 2 cards with the same number, the rest of the players must play
# 2 cards that have a higher number or value then the value of the previous cards that were played. If the user cannot play anything, 
# they may pass. Any card that has the number 2 can burn the pile of cards that the players have played. 
# Below is a list of essential rules regarding 2's, or burn cards.
# - One 2 can burn singles or doubles
# - You will require two 2's to burn the pile if the previous player(s) played a triple
# - You will require three 2's to burn the pile if the previous player(s) played a quadruple
import random
# imports the random module 
import sys
# imports a module that helps with the overall system of the program

def stopProgram(userInput):
    if userInput.lower() == "quit":
        print("Thank you for using this program!")
        # concluding message
        sys.exit()
        # terminates the program

    else :
        pass
        # passes and does nothing in this else statement

def removingCards(players, chosenCard, numberOfCards, cardDecks):
    counter = 0
    # sets a counter variable to zero
    counterTwo = 0
    # sets a counterTwo variable to zero
    removedCards = players[cardDecks].copy()
    # copy of list
    cardCheck = False
    # creates a cardCheck variable that holds the boolean value of False
    while counterTwo < len(players[cardDecks]):
        if cardCheck:
            counterTwo -= 1
            # decreases the counter if the flag variable is True

        if counter >= numberOfCards:
            break
            # stops the loop from running so that the appropriate number of cards can be removed

        if str(chosenCard) in str(players[cardDecks][counterTwo]): 
            pileOfCards.append(players[cardDecks][counterTwo])
            # appends the cards that the user wants to remove to the pileOfCards list
            del removedCards[counterTwo]
            # deletes the element 
            counter += 1
            # increments the counter variable by 1 
            cardCheck = True
            # sets the Flag variable to True

        counterTwo += 1
        # increments the counterTwo variable at the end of the loop

    players[cardDecks] = removedCards
    # assigns the changed list of removedCards to the original list
    print("Player " + str(cardDecks + 1) + "'s hand: " + str(players[cardDecks]) + "\n" + "\n" + "The pile: " + "\n")
    # prints the updated version of the hand with the removed cards
    for index in range(0, len(pileOfCards)):
        print(pileOfCards[index], end= " ")
        # prints out the cards that are meant to be in the pile
        
    print("\n")
    # prints out a space between the lines
def checkPile(chosenCard, chosenCards, cardDecks, players, numberOfCards):
    flag = True
    # flag variable set to True
    if cardDecks >= 1:
        looperVariable = 1
        # creates a variable and sets it to one
        while looperVariable < len(chosenCards):
            if numbersDict[chosenCards[looperVariable]] > numbersDict[chosenCards[looperVariable-1]]:
                pass
                # does nothing

            elif numbersDict[chosenCards[looperVariable]] == numbersDict[chosenCards[looperVariable-1]]:
                pileOfCards.clear()
                # gets rid of all the elemenents in the pileOfCards list
                return True
                # returns the boolean value of True

            else:
                print("The person that recently played has not played a card that has a value higher than the last one!")
                # invalid input message
                flag = False
                # changes the boolean value of the Flag to False 
                break
                # breaks the loop 
            
            looperVariable += numberOfCards
            # increments the counter variable looperVariable by the number of cards specified by the user
    if flag:
        removingCards(players, chosenCard, numberOfCards, cardDecks)
        # calls the removingCards function with the following parameters

def checkWin(cardDecks, players):
    if len(players[cardDecks]) == 0:
        print("Player " + str(cardDecks + 1) + " has won the game,so they are the president! Hope all of the players had fun!")
        # winning message
        return True
        # returns True
    
    else:
        return False
        # returns False
                
def cardGame(players, totalPlayers):
    print("Cards: " + "\n")
    # introductory statement showing the user what cards they have
    while True:
        cardDecks = 0
        # initializes cardDecks to 0
        while cardDecks < len(players):
            for counter in range(0, len(players[cardDecks])):
                print(players[cardDecks][counter], end=" ")
                # prints out all the cards of the player

            print("\n")
            # provides a space between the lines to make the output look more organized
            validInput = True
            # creates a variable that holds the boolean value of True
            userPass = input("Player " + str(cardDecks + 1) + ", looking at your cards, do you want to pass? Type in either yes or no! ")
            # asks the user if they want to pass
            stopProgram(userPass)
            # checks to see if the user wanted to quit
            if userPass.lower() == "yes":
                cardDecks += 1
                # increments the variable by 1
                print("Since this player has decided to pass on their turn, it will go to the next player!")
                # informs the users/players that a player has decided to pass and skip on their turn
                passList.append("yes")
                # appends yes to the list if the user/player wanted to pass
                if len(passList) == totalPlayers - 1:
                    print("All the players have passed, which now means it will go back to the only player recently that has not passed! You will be given the choice to pass if you want, but that would just be giving the other player a chance to play their card!")
                    # tells the user that all the three players have passed
                    pileOfCards.clear()
                    # clears all the cards when all the players have decided to pass
                    cardAppearances.clear()
                    # clears the cardAppearances list
                    chosenCards.clear()
                    # clears the chosenCards list

                continue
                # continues and goes to the next iteration

            elif userPass.lower() == "no":
                passList.clear()
                # clears all the elements in the list
                
            else:
                print("Please input either yes or no!")
                # invalid input message
                continue
                # continues without incrementing the cardDecks value so that it asks player 1 again

            while validInput:
                cardTracker = 0
                # assigns 0 to a cardTracker variable
                chosenCard = input("Player " + str(cardDecks + 1) + ", type in the number or value of card that you want to play. For instance, if you want to play a 4, type in 4, or if you want to play a " + "\n" + " Queen, type in the word Queen. Make sure that you have that card in your hand!!" + "\n" + "Enter the card you want to play here: ").lower().strip()
                # asks the player what card they want to play
                stopProgram(chosenCard)
                # checks to see if the user wanted to quit
                chosenCards.append(str(chosenCard))
                # appends whatever chosen card that the user wants to the chosenCards list
                numberOfCards = input("How many cards do you want to play of that have said number? Please input a valid number, otherwise you will be asked again!")
                # asks the user how many cards they want to play
                stopProgram(numberOfCards)
                # checks to see if the user wanted to quit
                numberOfCards = int(numberOfCards)
                # casts to an integer
                cardAppearances.append(numberOfCards)
                # appends the number of cards that the users want to remove to a list named cardAppearances

                if cardAppearances.count(cardAppearances[0]) == len(cardAppearances):
                    pass
                    # passes; nothing is done in the if statement

                else:
                    print("Invalid input! You must play the same amount of cards that the previous player played! Try again!")
                    # invalid input message
                    del cardAppearances[len(cardAppearances)-1]
                    # delete the last element in cardAppearances
                    del chosenCards[len(chosenCards) - 1]
                    # deletes the last element in chosenCards
                    continue
                    # continues the process of the iteration

                for number in range(0, len(players[cardDecks])):
                    if str(chosenCard) not in str(players[cardDecks]):
                        print("You do not have that card in your hand!")
                        # invalid input message
                        break
                        # momentarily stops the loop from running if this condition is satisfied, printing the error message only once

                    elif str(chosenCard) in str(players[cardDecks]):    
                        if chosenCard in players[cardDecks][number]:
                            cardTracker = cardTracker + 1
                            # increments the variable if the conditions are satisfied
                            if cardTracker == numberOfCards:
                                playerChecker = checkPile(chosenCard, chosenCards, cardDecks, players, numberOfCards)
                                # stores the result of the function in a variable playerChecker
                                validInput = False
                                # changes the boolean value of validInput to false
                                if playerChecker:
                                    print("The pile is burned!" + "\n")
                                    # tells the user that the pile is burned
                                    del players[cardDecks][number]
                                    cardDecks -= 1
                                    # decrements the cardDecks value by 1, making it so that the player who burned the card 
                                    cardAppearances.clear()
                                    # clears and empties the cardAppearances list
                                    chosenCards.clear()
                                    # clears the chosenCards list
                                    playerChecker = False

                                break
                                # breaks the loop

                            else:
                                pass
                                # purpose here: find out what to do if it is not the same; make sure that it reasks the player(continue)

                winner = checkWin(cardDecks, players)
                # calls the function and stores it in a variable
                if winner:
                    break
                    # stops the loop

                cardDecks += 1
                # increments the cardDecks variable
                print("=========================================" + "\n")
                # space between the player's turns

def sortCards(allPlayers, totalPlayers):
    for cards in range(0, len(allPlayers)):
        allPlayers[cards].sort()
        # sorts all the hands that each player has, which is useful for the game   
    print("The cards have been sorted! The game will begin just about now!")
    # tells the user that all the cards have been sorted
    cardGame(allPlayers, totalPlayers)
    # calls the cardGame function which will start the card game

def cardDealer(cardDeck, totalPlayers):
    totalCards = len(cardDeck)
    # creates a variable totalCards that holds the number 52, the length of the list cardDeck 
    random.shuffle(cardDeck)
    # shuffles the deck and arranges the order of the cards to a random order
    if totalCards % totalPlayers != 0:
        remainingCards = totalCards % totalPlayers
        # stores the remaining cards that are treated as "extras"
        del cardDeck[0:remainingCards]
        # removes the extra cards from the list
        totalCards = len(cardDeck)
        # reassigns the length of the list cardDeck to the totalCards variable

    counter = 0
    # creates a variable that will help with the looping process
    while counter < totalPlayers:
        allPlayers.append(cardDeck[counter::totalPlayers])
        # adds the cards to the allPlayers list
        counter = counter + 1
        # increments counter

    print("The cards for all the players have been generated!")
    # informs the user that the cards have been generated for all users
    sortCards(allPlayers, totalPlayers)
    # calls the sortCards function
        
def totalPlayers(cardDeck):
    while True:
        try:
            totalPlayers = input("How many players are there that are willing to play? Only 2-6 players can play this game. Enter in an integer please: ")
            # asks the user how many people are going to play
            stopProgram(totalPlayers)
            # checks to see if the user wanted to quit
            totalPlayers = int(totalPlayers)
            # casts it to an integer
            if (totalPlayers >= 2) and (totalPlayers <= 6):
                cardDealer(cardDeck, totalPlayers)
                # calls the cardDealer function which is responsible for dealing out the cards to all the players
                
            else: 
                print("Please input a number greater than or equal to 2 and less than or equal to 6!")
                # invalid input message

        except:
            print("Please input a valid value! You have inputted a word or string when the program asks for a number!")
            # invalid input message

def deckOfCards():
    for counter in range(0, len(cardValues)):
        for counterTwo in range(0, len(suits)):
            cardDeck.append(cardValues[counter] + " " + suits[counterTwo])
            # loops through both lists of values and suits, and makes a deck of cards
            
    totalPlayers(cardDeck)
    # calls the totalPlayers function

name = input("Hello! What is your name? ")
# asks the user for their name
stopProgram(name)
# checks to see if the user wanted to quit
print("Hello " + name + "! What are the rules of the game?" + "\n" +  " The game that you are about to play is a card game known as President! In president, a player can play either singles, doubles, triples, or " + "\n" + "quadruples. The user can only play more than 1 card if all the cards that the user decides to play has the same number. For example, if the user has four 3's in their deck, the user can choose to play a single(one card), double(two cards), triple(three cards), or a quadruple(four cards) with the number 3, " + "\n" + "barring the suit of the card. If the user decides to play 2 cards with the same number, the rest of the players must play 2 cards that have a higher " + "\n" + "number or value  then the value of the previous cards that were played. When the user wants to play cards of their choice, these cards are added to the " + "\n" + "pile. However, the pile can be burned if two players place the same number of cards along with the same value. For instance, if a player puts down one 6, the pile can be burned if another player places another 6 on the pile, causing it to be burned. Similarly, if a player places down two 9's, the two 9's " + "\n" + "can be burned if another player also has two 9's. The first one to lose and get rid of all their cards wins!" + "\n" +  "If the user cannot play anything, they may pass." + "\n" + "===================================================")
# introductory message

suits = ["♠", "♡", "♣", "♢"]
# creates a list of all the possible suits of the cards
cardValues = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "jack", "queen", "king", "ace"]
# creates a list containing all the possible values that a card may have
cardDeck = []
# creates an empty list named cardDeck
allPlayers = []
# stores all the cards for all the players
pileOfCards = []
# creates an empty list named pileOfCards
chosenCards = []
# creates an empty list named chosenCards
cardAppearances = []
# creates an empty listn named cardAppearances
passList = []
# creates an empty list named passList
numbersDict = {"2": 1, "3": 2, "4": 3, "5": 4, "6": 5, "7": 6, "8": 7, "9": 8, "10": 9, "jack": 10, "queen": 11, "king": 12, "ace": 13}
# cards dictionary, with card values being associated with a number from 1-13
deckOfCards()
# calls the deckOfCards function


