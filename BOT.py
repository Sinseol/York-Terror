import discord
import asyncio

client = discord.Client()

token = "봇토큰"

@client.event
async def on_ready():

    print(client.user.name)
    print('봇이 시작되었습니다')
    game = discord.Game('봇상메')
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
    if message.content == "감지할 말":
        await message.channel.send("출력할말")

    if message.content == "감지할 말":
        await message.channel.send("출력할말")

    if message.content == "감지할 말":
        await message.channel.send("출력할말")

client.run(token)
