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

# variable lists
bot_DM = ['Fuck you', 'fuck u', 'feck u', 'bitch', 'https://www.youtube.com/watch?v=dQw4w9WgXcQ']
bot_response = ['the fuck you want?','sup bitch','you wot m8','i will gut you alive','i will kill your family','enjoy your last breath','your blood isn\'t worth my time','i\'m in your walls','**heavy breathing**','just turn around and talk to me']
die_sides = [4, 6, 8, 10, 12, 20, 100]