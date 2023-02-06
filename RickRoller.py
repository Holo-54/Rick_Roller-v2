# import libraries
import discord
import random
import asyncio
from discord import app_commands

# bot configuration
intents = discord.Intents.all()
client = discord.Client(command_prefix='/', intents=intents)
tree = app_commands.CommandTree(client)

# -------------------------------------------------
# FUNCTIONS, FILES, AND IMPORTANT VARIABLES
# -------------------------------------------------

# fetch help message
f = open('./help.txt', 'r')
help_txt = f.read()
f.close()

# API Token
a = open('./API_Token.txt', 'r')
api_token = a.read()
a.close()

# roll function
def roll_dice(num_dice):
    roll = random.randint(1, num_dice)
    return roll

# multi roll function
def multi_roll(sides, num_dice):
    global total_roll # allows reference in multi_roll command code
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

# -------------------------------------------------
# EVENTS
# -------------------------------------------------

# basic roll
@tree.command(name="roll", description="A basic dice roll")
@app_commands.describe(die="Type of dice")
async def roll(interaction: discord.Interaction, die: int):
    if die in die_sides:
        simple_roll = roll_dice(die)
        await interaction.response.send_message(f'You rolled a {simple_roll}!')
    else:
        await interaction.response.send_message(f'"{die}" is not a valid dice!')

# multi roll
@tree.command(name="multi_roll",description="Roll multiple dice")
@app_commands.describe(die="Type of dice",number_of_dice="Number of dice")
async def m_roll(interaction: discord.Interaction, die: int, number_of_dice: int):
    mroll=multi_roll(die,number_of_dice)
    await interaction.response.send_message(f'Here are your rolls:\n{mroll}\nGrand total: {total_roll}')

@client.event
async def on_message(message):
    print('{0.channel.id} Message from {0.author}: {0.content}'.format(message))

@client.event
async def on_ready():
    await tree.sync()
    print('Ready to roll!')


# -------------------------------------------------
# INITIALIZATION
# -------------------------------------------------
client.run(api_token)