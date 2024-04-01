print("Welcome To Riddle It Roulette")

Char = str(input("Enter Your Name "))
print()
print(f"Lets Begin {Char} You Will Be Given a Phrase To Guess The Word I Have In Mind!")
print("Get It Right You Move on, Get It Wrong You Lose a Life!")
print("Lose 3 Times It's Game Over")
print()

import random

words = {
        'banana': 'A Yellow Crescent',
        'nothing': 'The Poor Have It, The Rich Need It, Eat It You Die, What is It?',
        'bank': 'It Has Branches But No Fruit, Trunk or Leaves.',
        'alphabet': 'It Contains All 26 Letters',
        'swims': 'It Can Be Read The Same Upside-Down and Right Side Up',
        'orange' : 'Its a Colour You Can Eat',
        'what': 'W-H-A-T Spells what?',
        'coin': 'What Has a Head And a Tail, But No Arms or Legs?',
        'book': 'Has Many Words But Never Speaks',
        'n': 'Throw me out the window, You will have a Grieving Wife, But Drop Me In The Middle Of a Door, And You Might Just Save a Life. What Am I?',
        'stars': 'They come at night without being called and are lost in the day without being stolen. What are they?',
        'lightining': 'I touch the earth and I touch the sky, but if I touch you, you’ll likely die. What am I?',
        'three': 'If there are five apples and you take away three, how many apples do you have?',
        'bubble': ' I am lighter than air, but a hundred people cannot lift me—I’m too fragile. What am I?',
        'corn': 'You throw away the outside and cook the inside. Then you eat the outside and throw away the inside. What did you eat?',
        'eye': 'Pronounced as one letter and written with three, two letters there are and two only in me. I’m double. I’m single. I’m black, blue, and gray. I’m read from both ends, but the same either way. What am I?',
        'crows': 'You’ll often find us on a line. When we’re together, it’s a crime. What are we?',
        }

def choose_word():
    return random.choice(list(words.items()))

def display_word(word_to_guess, guessed_word):
    displayed_word = ''
    for letter in word_to_guess:
        if letter.lower() in guessed_word:
            displayed_word += letter
        else:
            displayed_word += '_'
    return displayed_word

game_running = True
score = 0
games = 0


while game_running:
    word_to_guess, hint = choose_word()
    guessed_word = ''
    attempts = 0
    life = 3

    while True:
        word_display = display_word(word_to_guess, guessed_word)
        print("\n" + word_display)
        print("Hint: ", hint)
            
        if word_display.lower() == word_to_guess:
            print()
            print(f" Thats Correct! {word_to_guess} Was The Word")
            score += 1
            print("congrats")
            print()
            break
                
        if attempts >= life:
            print()
            print(f" You Ran Out of Lives!, The Word Was {word_to_guess}")
            print()
            break
                
        guess = input("Enter The Correct Word To Proceed: ").lower()
        
        if guess == word_to_guess:
            print()
            print(f" Thats Correct! {word_to_guess} Was The Word")
            score += 1
            print("congrats")
            print()
            break
        else:
            attempts += 1
            print("That's Not Correct", life - attempts, "lives left.")
            print()
            
    games += 1
    replay = input("Do you want to play again? (yes/no): ").lower()
    if replay != "yes":
        game_running = False
        print(f" Score: {score}")
        print(f" Games Played: {games}")
        print(f" Average Score: {score / games}")
        print()
        
    