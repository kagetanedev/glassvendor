import discord

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, whalecum at Aldi!'
    )

@client.event
async def on_message(message):
    if client.user.mentioned_in(message) and message.mention_everyone is False:
        await message.channel.send('fuck off im busy greeting peeps')

client.run('###')


#whalecum at Aldi!
#what up, young blood!
#ahoi matey.
#