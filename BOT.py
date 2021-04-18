import discord
import asyncio

client = discord.Client()

token = "ODE2Njc1MTA1MTgyMDU2NTQ4.YD-Z9g.REwDmLgQYsgUO17OCaX-qm4CHsw"

@client.event
async def on_ready():

    print(client.user.name)
    print('봇이 시작되었습니다')
    game = discord.Game('York Terror Server')
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
    if message.content == "s!help":
        await message.channel.send("""```명령어 목록입니다.
1.s!디스코드
2.s!ping```""")

    if message.content == "s!디스코드":
        await message.channel.send("https://discord.gg/Q3vxAFBbTG")

    if message.content == "s!ping":
        await message.channel.send("pong!")

client.run(token)