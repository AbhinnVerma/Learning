#   Mad libs
import random


def intro():
    print('\n\t_______________  MAD-LIBS  _______________')
    ask = str((input('Up for a round of MAB-LIBS ? (yes/no) : '))).lower()
    if ask in ['y', 'yes']:
        gamemode()
    elif ask in ['n', 'no']:
        print('Bye then.')
    else:
        print('I did\'t understand!')
        intro()


def gamemode():
    mode = str(input('Would you like to a play a Randomized madlib or an dev\'s Choice madlib (dev/random) : ')).lower()
    if mode in ['random', 'r']:
        randomized()
    elif mode in ['dev', 'd']:
        developer()
    else:
        print('I did\'t understand!')
        gamemode()


def randomized():
    print('\n\t_____ RANDOMIZED MODE _____')
    with open('randomized.txt', 'r') as f:
        madlib_text = f.readlines()
        madlib = random.choice(madlib_text)

        noun = str(input('Enter a noun : '))
        madlib = madlib.replace("var_noun", noun)

        adj = str(input('Enter an adjective : '))
        madlib = madlib.replace("var_adj", adj)

        name = str(input('Enter your name : '))
        madlib = madlib.replace("var_name", name)

        print('\n',madlib)
        intro()

        
def developer():
    print('\n\t_____ DEV\'S CHOICE _____')
    print(
        'This game mode includes MAD-LIBS that are a bit longer and more fun. \n Now Choose a storyline -  ')
    storyline = str(input(
        '\t Storyline 1 - A day at the zoo (12 inputs) \n\t Storyline 2 - My trip to Disney Land (15 inputs) \n Your Choice (1/2) : '))
    if storyline == "1":
        story1()
    elif storyline == '2':
        story2()
    else:
        print('I did\'t understand!')
        developer()


def story1():
    # INPUTS
    print()
    adj_1 = str(input('Enter an adjective : '))
    noun_1 = str(input('Enter a noun : '))
    verb_1_past = str(input('Enter a verb (past tense) : '))
    adverb_1 = str(input('Enter a adverb : '))
    adj_2 = str(input('Enter an adjective : '))
    noun_2 = str(input('Enter a noun : '))
    noun_3 = str(input('Enter a noun : '))
    adj_3 = str(input('Enter an adjective : '))
    verb_2 = str(input('Enter a verb : '))
    adverb_2 = str(input('Enter a adverb : '))
    verb_3_past = str(input('Enter a verb (past tense) : '))
    adj_4 = str(input('Enter an adjective : '))

    # OUTPUT
    print('\n\n\n\t\t---------- A DAY AT THE ZOO! ----------')
    print(
        f' Today I went to the zoo. I saw a(n) {adj_1} {noun_1} jumping up and down in its tree. \n He {verb_1_past} {adverb_1} through the large tunnel that led to its {adj_2} {noun_2}. \nI got some peanuts and passed them through the cage to a gigantic gray {noun_3}  \n towering above my head. Feeding that animal made me hungry. \n I went to get a {adj_3} scoop of ice cream. \n It filled my stomach. Afterwards I had to {verb_2} {adverb_2} to catch our bus. \n When I got home I {verb_3_past} my mom for a {adj_4} day at the zoo.')
    print('\t \t -------------\t  x  \t-------------')
    intro()


def story2():
    # INPUTS
    print()
    friend_name = str(input('Enter a friend\'s name : '))
    hours = str(input('Enter number of hours : '))
    vehicle = str(input('Enter a type of vehicle : '))
    adj_1 = str(input('Enter an adjective : '))
    adj_2 = str(input('Enter an adjective : '))
    verb_ing = str(input('Enter a verb ending with \'ing\' : '))
    animal = str(input('Enter name of an animal : '))
    adj_3 = str(input('Enter an adjective : '))
    verb_1_past = str(input('Enter a verb (past tense) : '))
    adj_4 = str(input('Enter an adjective : '))
    noun_1 = str(input('Enter a noun : '))
    verb_2_past = str(input('Enter a verb (past tense) : '))
    verb_3_past = str(input('Enter a verb (past tense) : '))
    place = str(input('Enter name of a place : '))
    verb_5 = str(input('Enter a verb : '))

    # OUTPUT
    print('\n\n\n\t__________ MY TRIP TO DISNEY LAND! __________')
    print(f"""
    Last month, I went to Disney World with {friend_name}. We
    traveled for {hours} hours by {vehicle}. Finally, we
    arrived and it was very {adj_1}. There were
    {adj_2} people {verb_ing} everywhere. There
    were also people dressed up in {animal} costumes.

    I wish it had been more {adj_3}, but we {verb_1_past} anyway.
    We also went on a(n) {adj_4} ride called Magic {noun_1}.
    {friend_name} nearly fell off a ride and had to be
    {verb_2_past}. Later, we went to the hotel and {verb_3_past}.
    Next year, I want to go to {place}, where we can {verb_5}.
    """)
    intro()


intro()
