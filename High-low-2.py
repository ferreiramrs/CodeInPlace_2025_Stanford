# High-Low Game
# We want you to gain more experience working with control flow and Booleans in Python. To do this, we are going to have you develop a game! The game is called High-Low and the way it's played goes as follows:
# Two numbers are generated from 1 to 100 (inclusive on both ends): one for you and one for a computer, who will be your opponent. You get to see your number, but not the computer's!
# You make a guess, saying your number is either higher than or lower than the computer's number
# If your guess matches the truth (ex. you guess your number is higher, and then your number is actually higher than the computer's), you get a point!
# These steps make up one round of the game. The game is over after all rounds have been played.
# Here's a sample run of the game where we play three rounds (user input is in blue for visual clarity):

# Welcome to the High-Low Game!
# --------------------------------
# Round 1
# Your number is 8
# Do you think your number is higher or lower than the computer's?: lower
# You were right! The computer's number was 35
# Your score is now 1

# Round 2
# Your number is 88
# Do you think your number is higher or lower than the computer's?: higher
# Aww, that's incorrect. The computer's number was 100
# Your score is now 1

# Round 3
# Your number is 63
# Do you think your number is higher or lower than the computer's?: higher
# You were right! The computer's number was 5
# Your score is now 2

# Thanks for playing!

# To help out, we've made some milestones to guide you. 

# Milestone #1: Generate the random numbers
# Generate the random numbers for you and the computer. For now, print both of them out to help you test the logic in later milestones. Your output should look like this (with different random numbers):

# Welcome to the High-Low Game!
# --------------------------------
# The computer's number is 23
# Your number is 82

# Milestone #2: Get user choice
# Get user input for their choice of whether they think their number is higher or lower than the computer's number.

# Welcome to the High-Low Game!
# --------------------------------
# The computer's number is 7
# Your number is 17
# Do you think your number is higher or lower than the computer's?: higher

# Milestone #3: Write the game logic

# Write code that maps out all the ways to win the round and prints out the results. When does the user win? How might we check for this? (Note: If you and the computer share the same number, the computer should win since your number wouldn't be higher nor lower.)

# Welcome to the High-Low Game!
# --------------------------------
# The computer's number is 79
# Your number is 3
# Do you think your number is higher or lower than the computer's?: lower
# You were right! The computer's number was 79

# (Example case for when you and the computer have the same number)

# Welcome to the High-Low Game!
# --------------------------------
# The computer's number is 57
# Your number is 57
# Do you think your number is higher or lower than the computer's?: lower
# Aww, that's incorrect. The computer's number was 57

# Milestone #4: Play multiple rounds
# Milestones 1-3 make up a single round of the game. Now that your game logic is sound, you can remove the line printing out the computer's number. Next, write code to play multiple rounds of the game! How many rounds should they play you ask? We've provided you with the NUM_ROUNDS constant. NUM_ROUNDS is the number of rounds you should have the user play. For reference, in the first example, we had NUM_ROUNDS = 3. After each round, add a blank line to separate the rounds visually. Make sure to print out the round number as well!

# Welcome to the High-Low Game!
# --------------------------------
# Round 1
# Your number is 22
# Do you think your number is higher or lower than the computer's?: lower
# You were right! The computer's number was 23

# Round 2
# Your number is 76
# Do you think your number is higher or lower than the computer's?: higher
# Aww, that's incorrect. The computer's number was 81

# ... (more rounds are played)

# Milestone #5: Adding a points system and a thank you!

# Keep track of the player's score! You should print out the player's score after each round. After they finish all the rounds, say thank you! After this step, you will have coded up the entire game! 

# Welcome to the High-Low Game!
# --------------------------------
# Round 1
# Your number is 22
# Do you think your number is higher or lower than the computer's?: lower
# You were right! The computer's number was 23
# Your score is now 1

# Round 2
# Your number is 76
# Do you think your number is higher or lower than the computer's?: higher
# Aww, that's incorrect. The computer's number was 81
# Your score is now 1

# ... (more rounds are played)

# Round 5
# Your number is 88
# Do you think your number is higher or lower than the computer's?: higher
# You were right! The computer's number was 35
# Your score is now 3

# Thanks for playing!

# Extension #1: Safeguard user input

# Add safety precautions that make sure the player can only input 'higher' or 'lower' as an answer. If they enter anything else, prompt them again and let them know there's only two options!

# Welcome to the High-Low Game!
# --------------------------------
# Round 1
# Your number is 1
# Do you think your number is higher or lower than the computer's?: even
# Please enter either higher or lower: lower
# You were right! The computer's number was 6
# Your score is now 1


# Extension #2: Conditional ending messages

# Add conditional messages at the end which gauge players on how they performed! For ours, we evaluated the player and gave them separate messages if:

# they had a perfect game

# they won at least half the rounds (rounded down)

# they won less than half the rounds

# For example, if the user played five rounds, here's the messages we chose:

# (Won 5 rounds)

# ...
# Your score is now 5

# Wow! You played perfectly!

# (Won at least half the rounds, rounded down)

# ...
# Your score is now 2

# Good job, you played really well!

# (Won less than half the rounds)

# ...
# Your score is now 1

# Better luck next time!

import random

NUM_ROUNDS = 5

def main():
    print("Welcome to the High-Low Game!")
    print('--------------------------------')
    user_score = 0
    for i in range (1, NUM_ROUNDS + 1):
         print("Round", i)
     # 1. Define varianles for the number on the computer and the number of the user
         user_num = random.randint(1,100)
         comput_num = random.randint(1,100)

     # 2. Print the number of the user
         print ("Your number is", user_num)

     # 3. Let the user guess if higher or lower
         user_input = input ("Do you think your number is higher or lower than the computer's?: ")
         if (user_input != "higher" and user_input != "lower"):
            print ("That's not a valid answer! Please type higher or lower")
     
     # 4. Check the number to see which one is here
         win_higher = user_num > comput_num and user_input == "higher"
         win_lower = user_num < comput_num and user_input == "lower"
         if (win_higher or win_lower):
             print ("You were right! The computer's number was",comput_num)
             user_score +=1

         else: 
             print ("Aww, that's incorrect. The computer's number was",comput_num)
     
     # 5. Print the result
         print ("Your score is now", user_score)
         print()
    print("Thanks for playing!")
if __name__ == "__main__":
    main()