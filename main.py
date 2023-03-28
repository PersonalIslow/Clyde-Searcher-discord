import discord
import asyncio

TOKEN = 'your_bot_token'

client = discord.Client()

async def check_clyde():
    while True:
        try:
            guilds = client.guilds
            for guild in guilds:
                if guild.name == 'server_name':
                    bot_found = False
                    for member in guild.members:
                        if member.bot and member.name == 'Clyde':
                            bot_found = True
                            break
                    if not bot_found:
                        await guild.delete()
                        print("Deleted server " + guild.name)
                    break
            else:
                await client.create_guild(name='server_name', region='us-west')
                print("Created server server_name")
        except Exception as e:
            print(e)
        await asyncio.sleep(60)

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    asyncio.create_task(check_clyde())

client.run(TOKEN)