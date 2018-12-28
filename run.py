# Work with Python 3.6
import discord, requests, random, json


with open('config.json') as f:
    TOKEN = json.load(f)['token']

client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.lower().startswith('!ip'):
        ipaddr = requests.get("https://ipinfo.io/ip").text
        flavor_text = random.choice(["Happy Crafting!",
                                    "Don't let any creepers get too close!",
                                    "There's gold in them hills!",
                                    "Untap, upkeep, draw...",
                                    "Me too thanks!",
                                    "H*ckin groovy!",
                                    "I can't believe I'm working for you jagaloons. :sob:",
                                    "5318008"])
        msg = '{0.author.mention}, the server IP is: `{1}`! {2}'.format(message, ipaddr, flavor_text)
        await client.send_message(message.channel, msg)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
