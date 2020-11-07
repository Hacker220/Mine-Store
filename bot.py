# -*- coding: utf8 -*-
import discord
import asyncio
from discord.ext import commands
from config import settings
bot = commands.Bot(command_prefix = "!!")
bot.remove_command('help')
#=====================================================================================Commands=====================================================================================
@bot.command(aliases=['si', 'серверинфо'])
async def serverinfo(ctx):
    lg = bot.get_guild(739951510892314654)
    lc = lg.get_channel(739952498797838366)
    guild = ctx.message.guild
    region = guild.region
    author = ctx.message.author
    avatar = author.avatar_url
    name = guild.name
    owner = guild.owner
    icon = guild.icon_url
    gicon = guild.icon
    texchannel = guild.text_channels
    voichannel = guild.voice_channels
    channels = len(texchannel) + len(voichannel)
    users = guild.member_count
    role = guild.roles
    roles = len(role)
    if gicon == None:
        vicon = 'Отсутствует'
    else:
        vicon = '⠀'
    if vicon == '⠀':
        embed = discord.Embed(title='Инфо о сервере',colour=discord.Colour.gold())
        embed.add_field(name = 'Название сервера:', value = name)
        embed.add_field(name = 'Владелец сервера:', value = owner)
        embed.add_field(name = 'Иконка сервера:', value  = vicon)
        embed.add_field(name = 'Регион:', value  = region)
        embed.add_field(name = 'Каналов:', value = channels)
        embed.add_field(name = 'Участников:', value = users)
        embed.add_field(name = 'Ролей:', value = roles)
        embed.set_thumbnail(url = icon)
        embed.set_footer(text = author, icon_url = avatar)
    else:
        embed = discord.Embed(title='Инфо о сервере',colour=discord.Colour.gold())
        embed.add_field(name = 'Название сервера:', value = name)
        embed.add_field(name = 'Владелец сервера:', value = owner)
        embed.add_field(name = 'Иконка сервера:', value  = vicon)
        embed.add_field(name = 'Регион:', value  = region)
        embed.add_field(name = 'Каналов:', value = channels)
        embed.add_field(name = 'Участников:', value = users)
        embed.add_field(name = 'Ролей:', value = roles)
        embed.set_footer(text = author, icon_url = avatar)
    await ctx.send(embed = embed)
    print(f'{guild} -> Участник {author} использовал команду serverinfo')
    await lc.send(f'{guild} -> Участник {author} использовал команду serverinfo')
@bot.command(aliases=['юсеринфо', 'ui'])
async def userinfo(ctx, member: discord.Member = None):
    lg = bot.get_guild(739951510892314654)
    lc = lg.get_channel(739952498797838366)
    guild = ctx.message.guild
    author = ctx.message.author
    author_url = ctx.message.author.avatar_url
    if not member:
        name = ctx.message.author.name
        avatar = ctx.message.author.avatar
        id = ctx.message.author.id
        time = ctx.message.author.created_at
        status = ctx.message.author.status
        if avatar == None:
            vicon = 'Отсутствует'
        else:
            vicon = '⠀'
        if vicon == '⠀':
            embed = discord.Embed(title='Инфо о пользователе',colour=discord.Colour.gold())
            embed.add_field(name = 'Никнейм:', value = name)
            embed.add_field(name = 'Аватар:', value = vicon)
            embed.add_field(name = 'Id:', value  = id, inline = False)
            embed.add_field(name = 'Статус', value  = status)
            embed.add_field(name = 'Время создания аккаунта:', value = time)
            embed.set_thumbnail(url = author_url)
            embed.set_footer(text = author, icon_url = author_url)
        else:
            embed = discord.Embed(title='Инфо о пользователе',colour=discord.Colour.gold())
            embed.add_field(name = 'Никнейм:', value = name)
            embed.add_field(name = 'Аватар:', value = vicon)
            embed.add_field(name = 'Id:', value  = id, inline = False)
            embed.add_field(name = 'Статус', value  = status)
            embed.add_field(name = 'Время создания аккаунта:', value = time)
            embed.set_footer(text = author, icon_url = author_url)
        await ctx.send(embed = embed)
        print(f'{guild} -> Участник {author} использовал команду userinfo')
        await lc.send(f'{guild} -> Участник {author} использовал команду userinfo')
    else:
        name = member.name
        avatar = member.avatar
        avatar_url = member.avatar_url
        id = member.id
        time = member.created_at
        status = member.status
        if avatar == None:
            vicon = 'Отсутствует'
        else:
            vicon = '⠀'
        if vicon == '⠀':
            embed = discord.Embed(title='Инфо о пользователе',colour=discord.Colour.gold())
            embed.add_field(name = 'Никнейм:', value = name)
            embed.add_field(name = 'Аватар:', value = vicon)
            embed.add_field(name = 'Id:', value  = id, inline = False)
            embed.add_field(name = 'Статус', value  = status)
            embed.add_field(name = 'Время создания аккаунта:', value = time)
            embed.set_thumbnail(url = avatar_url)
            embed.set_footer(text = author, icon_url = author_url)
        else:
            embed = discord.Embed(title='Инфо о пользователе',colour=discord.Colour.gold())
            embed.add_field(name = 'Никнейм:', value = name)
            embed.add_field(name = 'Аватар:', value = vicon)
            embed.add_field(name = 'Id:', value  = id, inline = False)
            embed.add_field(name = 'Статус', value  = status)
            embed.add_field(name = 'Время создания аккаунта:', value = time)
            embed.set_footer(text = author, icon_url = author_url)
        await ctx.send(embed = embed)
        print(f'{guild} -> Участник {author} использовал команду userinfo')
        await lc.send(f'{guild} -> Участник {author} использовал команду userinfo')
@bot.command(aliases=['m', 'м', 'мьют'])
@commands.has_permissions(administrator = True)
async def mute(ctx, member:discord.Member = None, time: int = None, *, reason = None):
    url = 'https://s7.gifyu.com/images/mute-2.gif'
    lg = bot.get_guild(739951510892314654)
    lc = lg.get_channel(739952498797838366)
    guild = ctx.message.guild
    role = guild.get_role(774647553219231745)
    author = ctx.message.author
    moder = ctx.message.author.mention
    channel = ctx.channel
    if not member:
        await ctx.send(f'{ctx.author.mention} Использование - [Игрок] [Время] [Причина]')
    else:
        if not time:
            await ctx.send('Вы не указали срок действия мута')
        else:
            if not reason:
                reason = 'Не указана'
                muted = member.mention
                embed = discord.Embed(title = 'Мут', colour = discord.Colour.red())
                embed.add_field(name = 'Модератор:', value = moder, inline = False)
                embed.add_field(name = 'Нарушитель:', value = muted, inline = False)
                embed.add_field(name = 'Время:', value = f'{time} минут', inline = False)
                embed.add_field(name = 'Причина:', value = reason, inline = False)
                embed.set_thumbnail(url = url)
                await member.add_roles(role)
                await channel.send(embed = embed)
                print(f'{guild} -> Модератор {author} выдал мут {member} на {time} минут по причине: {reason}')
                await lc.send(f'{guild} -> Модератор {author} выдал мут {member} на {time} минут по причине: {reason}')
                await asyncio.sleep(time * 60)
                await member.remove_roles(role)
            else:
                muted = member.mention
                embed = discord.Embed(title = 'Мут', colour = discord.Colour.red())
                embed.add_field(name = 'Модератор:', value = moder, inline = False)
                embed.add_field(name = 'Нарушитель:', value = muted, inline = False)
                embed.add_field(name = 'Время:', value = f'{time} минут', inline = False)
                embed.add_field(name = 'Причина:', value = reason, inline = False)
                embed.set_thumbnail(url = url)
                await member.add_roles(role)
                await channel.send(embed = embed)
                print(f'{guild} -> Модератор {author} выдал мут {member} на {time} минут по причине: {reason}')
                await lc.send(f'{guild} -> Модератор {author} выдал мут {member} на {time} минут по причине: {reason}')
                await asyncio.sleep(time * 60)
                await member.remove_roles(role)
@bot.command(aliases=['um', 'р', 'размут'])
@commands.has_permissions(administrator = True)
async def unmute(ctx, member:discord.Member = None):
    url = 'https://s7.gifyu.com/images/unmute.gif'
    lg = bot.get_guild(739951510892314654)
    lc = lg.get_channel(739952498797838366)
    guild = ctx.message.guild
    role = guild.get_role(737056764050145360)
    moder = ctx.message.author.mention
    muted = member.mention
    author = ctx.message.author
    channel = ctx.channel
    if not member:
        await ctx.send(f'{ctx.author.mention} Использование - [Игрок]')
    else:
        embed = discord.Embed(title = 'Размут', colour = discord.Colour.green())
        embed.add_field(name = 'Модератор:', value = moder, inline = False)
        embed.add_field(name = 'Нарушитель:', value = muted, inline = False)
        embed.set_thumbnail(url = url)
        await member.remove_roles(role)
        print(f'{guild} -> Модератор {author} снял мут {member}')
        await lc.send(f'{guild} -> Модератор {author} снял мут {member}')
        await channel.send(embed = embed)
@bot.command(aliases=['k', 'кик', 'к'])
@commands.has_permissions(administrator = True)
async def kick(ctx, member:discord.Member = None, *, reason = None):
    url = 'https://s7.gifyu.com/images/kick93a68b4b8d883629.gif'
    lg = bot.get_guild(739951510892314654)
    lc = lg.get_channel(739952498797838366)
    guild = ctx.message.guild
    moder = ctx.message.author.mention
    author = ctx.message.author
    channel = ctx.channel
    if not member:
        await ctx.send(f'{ctx.author.mention} Использование - [Игрок] [Причина]')
    else:
        if not reason:
            reason = 'Не указана'
            kicked = member.mention
            embed = discord.Embed(title = 'Кик', colour = discord.Colour.red())
            embed.add_field(name = 'Модератор:', value = moder, inline = False)
            embed.add_field(name = 'Нарушитель:', value = kicked, inline = False)
            embed.add_field(name = 'Причина:', value = reason, inline = False)
            embed.set_thumbnail(url = url)
            embed1 = discord.Embed(titel = 'Кик', colour = discord.Colour.red())
            embed1.description = f'Вас кикнули с сервера {guild}'
            embed1.add_field(name = 'Модератор:', value = moder, inline = False)
            embed1.add_field(name = 'Причина:', value = reason, inline = False)
            embed1.set_thumbnail(url = url)
            await member.kick()
            await member.send(embed = embed1)
            await channel.send(embed = embed)
            print(f'{guild} -> Модератор {author} кикнул {member} по причине: {reason}')
            await lc.send(f'{guild} -> Модератор {author} кикнул {member} по причине: {reason}')
        else:
            kicked = member.mention
            embed = discord.Embed(title = 'Кик', colour = discord.Colour.red())
            embed.add_field(name = 'Модератор:', value = moder, inline = False)
            embed.add_field(name = 'Нарушитель:', value = kicked, inline = False)
            embed.add_field(name = 'Причина:', value = reason, inline = False)
            embed.set_thumbnail(url = url)
            embed1 = discord.Embed(titel = 'Кик', colour = discord.Colour.red())
            embed1.description = f'Вас кикнули с сервера {guild}'
            embed1.add_field(name = 'Модератор:', value = moder, inline = False)
            embed1.add_field(name = 'Причина:', value = reason, inline = False)
            embed1.set_thumbnail(url = url)
            await member.kick()
            await member.send(embed = embed1)
            await channel.send(embed = embed)
            print(f'{guild} -> Модератор {author} кикнул {member} по причине: {reason}')
            await lc.send(f'{guild} -> Модератор {author} кикнул {member} по причине: {reason}')
@bot.command(aliases=['b', 'бан', 'б'])
@commands.has_permissions(administrator = True)
async def ban(ctx, member:discord.Member = None, *, reason = None):
    url = 'https://s7.gifyu.com/images/ban.gif'
    lg = bot.get_guild(739951510892314654)
    lc = lg.get_channel(739952498797838366)
    guild = ctx.message.guild
    moder = ctx.message.author.mention
    author = ctx.message.author
    channel = ctx.channel
    if not member:
        await ctx.send(f'{ctx.author.mention} Использование - [Игрок] [Причина]')
    else:
        if not reason:
            reason = 'Не указана'
            banned = member.mention
            embed = discord.Embed(title = 'Бан', colour = discord.Colour.red())
            embed.add_field(name = 'Модератор:', value = moder, inline = False)
            embed.add_field(name = 'Нарушитель:', value = banned, inline = False)
            embed.add_field(name = 'Причина:', value = reason, inline = False)
            embed.set_thumbnail(url = url)
            embed1 = discord.Embed(titel = 'Бан', colour = discord.Colour.red())
            embed1.description = f'Вас забанили на сервере {guild}'
            embed1.add_field(name = 'Модератор:', value = moder, inline = False)
            embed1.add_field(name = 'Причина:', value = reason, inline = False)
            embed1.set_thumbnail(url = url)
            await member.ban()
            await member.send(embed = embed1)
            await channel.send(embed = embed)
            print(f'{guild} -> Модератор {author} забанил {member} по причине: {reason}')
            await lc.send(f'{guild} -> Модератор {author} забанил {member} по причине: {reason}')
        else:
            banned = member.mention
            embed = discord.Embed(title = 'Бан', colour = discord.Colour.red())
            embed.add_field(name = 'Модератор:', value = moder, inline = False)
            embed.add_field(name = 'Нарушитель:', value = banned, inline = False)
            embed.add_field(name = 'Причина:', value = reason, inline = False)
            embed.set_thumbnail(url = url)
            embed1 = discord.Embed(titel = 'Бан', colour = discord.Colour.red())
            embed1.description = f'Вас забанили на сервере {guild}'
            embed1.add_field(name = 'Модератор:', value = moder, inline = False)
            embed1.add_field(name = 'Причина:', value = reason, inline = False)
            embed1.set_thumbnail(url = url)
            await member.ban()
            await member.send(embed = embed1)
            await channel.send(embed = embed)
            print(f'{guild} -> Модератор {author} забанил {member} по причине: {reason}')
            await lc.send(f'{guild} -> Модератор {author} забанил {member} по причине: {reason}')
@bot.command(aliases=['c', 'очистить'])
@commands.has_permissions(administrator = True)
async def clear(ctx, count = 10):
    deleted = await ctx.message.channel.purge(limit = count + 1)
    print(f'{ctx.message.guild} -> Модератор {ctx.message.author} удалил {count} сообщений в канале {ctx.message.channel}')
    await bot.get_channel(739952498797838366).send(f'{ctx.message.guild} -> Модератор {ctx.message.author} удалил {count} сообщений в канале {ctx.message.channel}')
@bot.command(aliases=['h', 'хелп', 'помощь'])
async def help(ctx):
    lg = bot.get_guild(739951510892314654)
    lc = lg.get_channel(739952498797838366)
    guild = ctx.message.guild
    author = ctx.message.author
    avatar = author.avatar_url
    embed = discord.Embed(title = 'Помощь с командами', colour = discord.Colour.gold())
    embed.add_field(name = 'Пользовательские команды:', value = '___help | userinfo | serverinfo___', inline = False)
    embed.add_field(name = 'Команды для администраторов', value = '___mute | unmute | kick | ban | clear___', inline = False)
    embed.set_footer(text = author, icon_url = avatar)
    await ctx.send(embed = embed)
    print(f'{guild} -> Участник {author} использовал команду help')
    await lc.send(f'{guild}  -> Участник {author} использовал команду help')
#=====================================================================================Events=====================================================================================
@bot.event
async def on_ready():
    activity = discord.Activity(name="🔥24/7🔥", type = discord.ActivityType.watching)
    await bot.get_channel(739952498797838366).send(f'Бот авторизовался как {bot.user}')
    print(f'Бот авторизовался как {bot.user}')
    await bot.change_presence(status=discord.Status.dnd, activity = activity)
@bot.event
async def on_member_join(member):
    lg = bot.get_guild(739951510892314654)
    lc = lg.get_channel(739952498797838366)
    guild = member.guild
    name = guild.name
    user = member.name
    role = guild.get_role(774301869412450304)
    channel = guild.get_channel(773935697701896272)
    embed = discord.Embed(title=name,colour=discord.Colour.green())
    embed.description = f'```yaml\n{user}  присоединился к нам```'
    embed1 = discord.Embed(title="Welcome",colour=discord.Colour.green())
    embed1.description = '```yaml\n Привет!\n Добро пожаловать на наш сервер!\n Надеюсь тебе тут понравится.\n Если заблудишься пиши !!help\n Удачи тебе🙂```'
    await channel.send(embed = embed)
    await member.send(embed = embed1)
    await member.add_roles(role)
    print(f'{name} -> {user} вступил на сервер')
    print(f'{name} -> Участнику {user} успешно выдана роль {role}')
    await lc.send(f'{name} -> {user} вступил на сервер')
    await lc.send(f'{name} -> Участнику {user} успешно выдана роль {role}')
@bot.event
async def on_member_remove(member):
    lg = bot.get_guild(739951510892314654)
    lc = lg.get_channel(739952498797838366)
    user = member.name
    guild = member.guild
    name = guild.name
    channel = guild.get_channel(773935697701896272)
    embed = discord.Embed(title=name,colour=discord.Colour.red())
    embed.description = f'```yaml\n{user} покинул нас```'
    await channel.send(embed = embed)
    print(f'{name} -> {user} покинул сервер')
    await lc.send(f'{name} -> {user} покинул сервер')

bot.run('TOKEN')
