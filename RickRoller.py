# import libraries
import discord
import random
import asyncio
from discord import app_commands
from discord.app_commands import Choice

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

# wrangler protocol users
w = open('./Wrangler_Protocol_Users.txt','r')
unique_ids = w.readlines()
wranglers = []
for wrangler in unique_ids:
    wranglers.append(int(wrangler.strip('\n')))
w.close()

# response list
b = open('./Bot_Responses.txt','r')
responses = b.readlines()
bot_response = []
for response in responses:
    bot_response.append(response.strip('\n'))
b.close()

# types of dice
die_sides = [4, 6, 8, 10, 12, 20, 100]

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

# -------------------------------------------------
# EVENTS AND COMMANDS
# -------------------------------------------------

# basic roll
@tree.command(name="roll", description="A basic dice roll")
@app_commands.describe(die="Type of dice", modifier="Modifier")
@app_commands.choices(die=[
    Choice(name=4, value=1),
    Choice(name=6, value=2),
    Choice(name=8, value=3),
    Choice(name=10, value=4),
    Choice(name=12, value=5),
    Choice(name=20, value=6),
    Choice(name=100, value=7)
])
async def roll(interaction: discord.Interaction, die: Choice[int], modifier: int=0):
    simple_roll = roll_dice(die.name)
    total_roll = simple_roll + modifier
    await interaction.response.send_message(f'D{die.name} + {modifier}: You rolled ({simple_roll} + {modifier}) = **{total_roll}**!')

# multi roll
@tree.command(name="multi_roll",description="Roll multiple dice")
@app_commands.describe(die="Type of dice",number_of_dice="Number of dice", modifier="Modifier")
@app_commands.choices(die=[
    Choice(name=4, value=1),
    Choice(name=6, value=2),
    Choice(name=8, value=3),
    Choice(name=10, value=4),
    Choice(name=12, value=5),
    Choice(name=20, value=6),
    Choice(name=100, value=7)
])
async def m_roll(interaction: discord.Interaction, die: Choice[int], number_of_dice: int, modifier: int=0):
    mroll=multi_roll(die.name,number_of_dice)
    grand_total = total_roll + modifier
    await interaction.response.send_message(f'You rolled: {number_of_dice} D{die.name}\nHere are your rolls:\n{mroll}\nTotal: {total_roll}\n**Grand Total: {total_roll} + {modifier} = {grand_total}**')

# custom roll
@tree.command(name="custom_roll",description="Multiple multi rolls at once")
@app_commands.describe(die1="First type of dice",first_num="Number of first dice",
                       die2="Second type of dice",second_num="Number of second dice",
                       die3="Third type of dice",third_num="Number of third dice",)
@app_commands.choices(
die1=[
    Choice(name=4, value=1),
    Choice(name=6, value=2),
    Choice(name=8, value=3),
    Choice(name=10, value=4),
    Choice(name=12, value=5),
    Choice(name=20, value=6),
    Choice(name=100, value=7)
],
die2=[
    Choice(name=4, value=1),
    Choice(name=6, value=2),
    Choice(name=8, value=3),
    Choice(name=10, value=4),
    Choice(name=12, value=5),
    Choice(name=20, value=6),
    Choice(name=100, value=7)
],
die3=[
    Choice(name=4, value=1),
    Choice(name=6, value=2),
    Choice(name=8, value=3),
    Choice(name=10, value=4),
    Choice(name=12, value=5),
    Choice(name=20, value=6),
    Choice(name=100, value=7)
])
async def custom_roll(interaction: discord.Interaction,
                      die1: Choice[int], first_num: int,
                      die2: Choice[int], second_num: int,
                      die3: Choice[int]=0, third_num: int=0):
    mroll1=multi_roll(die1.name,first_num)
    mroll2=multi_roll(die2.name,second_num)
    sum1=sum(mroll1)
    sum2=sum(mroll2)
    embed_message=discord.Embed(title="**Custom Roll**",colour=discord.Colour.blue())
    embed_message.add_field(name=f"__{first_num} D{die1.name}__", value=f"{mroll1} = {sum1}", inline=False)
    embed_message.add_field(name=f"__{second_num} D{die2.name}__", value=f"{mroll2} = {sum2}", inline=False)
    if die3!=0:
        mroll3=multi_roll(die3.name,third_num)
        sum3=sum(mroll3)
        custom_total=sum1+sum2+sum3
        embed_message.add_field(name=f"{third_num} D{die3.name}", value=f"{mroll3} = {sum3}", inline=False)
    else:
        custom_total=sum1+sum2
    embed_message.add_field(name="__Grand Total__", value=custom_total)
    await interaction.response.send_message(embed=embed_message)

# wrangler protocol
@tree.command(name="wrangler_protocol",description="Annoy the living hell out of someone until they respond")
@app_commands.describe(poor_soul="@ of poor soul to be wrangled")
async def wrangler_protocol(interaction: discord.Interaction, poor_soul: discord.Member):
    if interaction.user.id in wranglers:
        await interaction.response.send_message('Commencing Protocol: Wrangle')
        while True:
            for i in range(4):
                await interaction.channel.send(f'{poor_soul.mention} This won\'t stop until someone says stop')
            def check(m):
                return m.content.lower() == 'stop' and m.channel == interaction.channel
            try:
                await client.wait_for('message', check=check, timeout=45)
                await interaction.channel.send('oke')
                break
            except asyncio.TimeoutError:
                await interaction.channel.send('Still nothing...')
    else:
        await interaction.response.send_message(f'You aren\'t my superior!')

# help page
@tree.command(name="rick_help", description="Get some help with Rick Roller")
async def rick_help(interaction: discord.Interaction):
    await interaction.response.send_message(help_txt)

@client.event
async def on_message(message):
    print('{0.channel.id} Message from {0.author}: {0.content}'.format(message))
    if client.user.mention in message.content.split(): # pinging the Lord consequence
        reply = random.choice(bot_response)
        await message.reply(reply)

@client.event
async def on_ready():
    await tree.sync()
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='for /rick_help'))
    print('Ready to roll!')


# -------------------------------------------------
# INITIALIZATION
# -------------------------------------------------
client.run(api_token)