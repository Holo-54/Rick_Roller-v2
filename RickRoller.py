# import libraries
import discord
import random
import asyncio

#help message
f = open('./help.txt', 'r')
help_txt = f.read()
f.close()

# API Token
a = open('./API_Token.txt', 'r')
token = a.read()
a.close()

# roll function
def roll_dice(num_dice):
    roll = random.randint(1, num_dice)
    return roll

# multi roll function
def multi_roll(sides, num_dice):
    global total_roll
    rolls = []
    total_roll = 0
    for i in range(num_dice):
        roll = random.randint(1,sides)
        rolls.append(roll)
        total_roll = total_roll + roll
    return rolls

# response list
b = open('./Bot_Responses.txt','r')
responses = b.readlines()
bot_response = []
for response in responses:
    bot_response.append(response.strip('\n'))

# types of dice
die_sides = [4, 6, 8, 10, 12, 20, 100]