import os
import discord
from discord.ext import commands
from webserver import keep_alive


client = commands.Bot(command_prefix='>')

@client.event
async def on_ready():
	await client.change_presence(activity=discord.Game('Genshin Impact'))
	print('We\'re online!')


@client.command()
async def ping(ctx):
	await ctx.send(f'Pong, ur mom. Latency: {round((client.latency) * 1000)}ms')


@client.command()
async def pong(ctx):
	await ctx.send(f'Wrong command dumbass')


@client.command()
async def say(ctx, *, arg):
	await ctx.send(arg)

############################# Troll Commands
@client.command()
async def inv(ctx):
	await ctx.send(f"INVITE!!! INVITE ME! LEMME JOINNNN!")

@client.command()
async def pro(ctx):
	await ctx.send(f"pro")

@client.command()
async def hug(ctx):
	await ctx.send(f"aww, come here :pleading_face:")

@client.command()
async def owo(ctx):
	await ctx.send(f"owo")

@client.command()
async def uwu(ctx):
	await ctx.send(f"uwu")
############################# Troll Commands

@client.command()
async def ban(ctx, *arg):
	out = ''
	for shit in arg:
		out += shit
		out += ' '
	await ctx.send(f'No, you do it. Ban ' + out + 'yourself!')


@client.command(pass_context=True)
@commands.has_permissions(manage_messages = True)
async def yeet(ctx, amount=99):
	channel = ctx.message.channel
	messages = []
	async for message in channel.history(limit = amount + 1):
		messages.append(message)
	await channel.delete_messages(messages)
	await ctx.send(
	    f'{amount} messages have been purged by {ctx.message.author.mention}')

@client.command()
async def tell(ctx, *, arg):
	channel = ctx.message.channel
	messages = []
	async for message in channel.history(limit = 1):
		messages.append(message)
	await channel.delete_messages(messages)
	await ctx.send(arg)

@client.event
async def on_ready():
	await client.change_presence(activity=discord.Game('Genshin Impact'))
	print('We\'re online!')

def add(numbers):
	return sum(numbers)

def sub(n: float, n2: float):
	return n - n2

def rando(n: int, n2: int):
	return random.randint(n, n2)

def div(n: float, n2: float):
	return n / n2

def sqrt(n: float):
	return math.sqrt(n)
  
def mult(n: float, n2: float):
	return n * n2

@client.command(aliases=['Add', 'addition', 'Addition', '+'])
async def mathadd(ctx, *numbers: float):
	try:
		result = add(numbers)
		await ctx.send(result)

	except:
		pass

@client.command(aliases=['Sub', 'subtract', 'Subtract', '-'])
async def mathsub(ctx, x: float, y: float):
	try:
		result = sub(x, y)
		await ctx.send(result)

	except:
		pass


@client.command(aliases=['Rand', 'random', 'Random'])
async def mathrando(ctx, x: int, y: int):
	try:
		result = rando(x, y)
		await ctx.send(result)

	except:
		pass


@client.command(aliases=['Div', 'divide', 'Divide', '/'])
async def mathdiv(ctx, x: float, y: float):
	try:
		result = div(x, y)
		await ctx.send(result)

	except:
		pass


@client.command(aliases=['multi', 'Multi', 'multiply', 'Multiply', '*'])
async def mathmult(ctx, x: float, y: float):
	try:
		result = mult(x, y)
		await ctx.send(result)

	except:
		pass


@client.command(aliases=['Sqrt', 'root', 'Root'])
async def mathsqrt(ctx, x: float):
	try:
		result = sqrt(x)
		await ctx.send(result)

	except:
		pass


########################################################### Genshin Commands Below here ###########################################################
@client.command(aliases=['dilluc', 'Dilluc', 'diluc', 'dil', 'Dil'])
async def Diluc(ctx):
	embed = discord.Embed(
	    title='Diluc Farming List',
	    description=
	    'This is for Diluc specific talent and character materials only. Refer to corresponding commands for the specific weapons that this character uses.',
	    colour=discord.Colour.red())

	embed.set_footer(text='Banner by: discord.gg/Keqing')  #Bottom Text
	embed.set_image(
	    url=
	    'https://media.discordapp.net/attachments/831885537811234886/833689508330602546/Diluc.png?width=1039&height=702'
	)  #Banner
	embed.set_thumbnail(
	    url='https://rerollcdn.com/GENSHIN/Characters/Diluc.png'
	)  #Small Icon top right
	embed.set_author(
	    name='Jukelyn',
	    icon_url=
	    'https://cdn.discordapp.com/avatars/347216701055565827/5f29ea98f32f2db110e52780c2f657dc.png?size=256'
	)
	embed.add_field(
	    name='Everyday',
	    value=
	    'Small Lamp Grass \n Pyro Regisvines \n Skirmishers \n Agents \n Electro Cicin Mages',
	    inline=False)
	embed.add_field(name='Mondays', value='None', inline=False)
	embed.add_field(name='Tuesdays',
	                value='Teachings of Resistance',
	                inline=False)
	embed.add_field(name='Wednesdays', value='None', inline=False)
	embed.add_field(name='Thursdays', value='None', inline=False)
	embed.add_field(name='Fridays',
	                value='Teachings of Resistance',
	                inline=False)
	embed.add_field(name='Saturdays', value='None', inline=False)
	embed.add_field(name='Sundays',
	                value='Teachings of Resistance',
	                inline=False)
	await ctx.send(embed=embed)


@client.command(aliases=['benett', 'bennett', 'ben', 'benny', 'Ben', 'Benny'])
async def Bennett(ctx):
	embed = discord.Embed(
	    title='Bennett Farming List',
	    description=
	    'This is for Bennett specific talent and character materials only. Refer to corresponding commands for the specific weapons that this character uses.',
	    colour=discord.Colour.red())

	embed.set_footer(text='Banner by: discord.gg/Keqing')  #Bottom Text
	embed.set_image(url='https://i.imgur.com/nhBVUWn.png')  #Banner
	embed.set_thumbnail(
	    url='https://rerollcdn.com/GENSHIN/Characters/Bennett.png'
	)  #Small Icon top right
	embed.set_author(
	    name='Jukelyn',
	    icon_url=
	    'https://cdn.discordapp.com/avatars/347216701055565827/5f29ea98f32f2db110e52780c2f657dc.png?size=256'
	)
	embed.add_field(
	    name='Everyday',
	    value='Windwheel Asters \n Pyro Regisvines \n Treasure Hoarders',
	    inline=False)
	embed.add_field(name='Mondays', value='None', inline=False)
	embed.add_field(name='Tuesdays',
	                value='Teachings of Resistance',
	                inline=False)
	embed.add_field(name='Wednesdays', value='None', inline=False)
	embed.add_field(name='Thursdays', value='None', inline=False)
	embed.add_field(name='Fridays',
	                value='Teachings of Resistance',
	                inline=False)
	embed.add_field(name='Saturdays', value='None', inline=False)
	embed.add_field(name='Sundays',
	                value='Teachings of Resistance',
	                inline=False)
	await ctx.send(embed=embed)


@client.command(aliases=['sucrose', 'suc', 'sucroce', 'Suc'])
async def Sucrose(ctx):
	embed = discord.Embed(
	    title='Sucrose Farming List',
	    description=
	    'This is for Sucrose specific talent and character materials only. Refer to corresponding commands for the specific weapons that this character uses.',
	    colour=discord.Colour.red())

	embed.set_footer(text='Banner by: discord.gg/Keqing')  #Bottom Text
	embed.set_image(url='')  #Banner
	embed.set_thumbnail(
	    url='https://rerollcdn.com/GENSHIN/Characters/Sucrose.png'
	)  #Small Icon top right
	embed.set_author(
	    name='Jukelyn',
	    icon_url=
	    'https://cdn.discordapp.com/avatars/347216701055565827/5f29ea98f32f2db110e52780c2f657dc.png?size=256'
	)
	embed.add_field(
	    name='Everyday',
	    value='Windwheel Asters \n Anemo Hypostatis \n Whopperflowers',
	    inline=False)
	embed.add_field(name='Mondays', value='Teachings of Freedom', inline=False)
	embed.add_field(name='Tuesdays', value='None', inline=False)
	embed.add_field(name='Wednesdays', value='None', inline=False)
	embed.add_field(name='Thursdays',
	                value='Teachings of Freedom',
	                inline=False)
	embed.add_field(name='Fridays', value='None', inline=False)
	embed.add_field(name='Saturdays', value='None', inline=False)
	embed.add_field(name='Sundays', value='Teachings of Freedom', inline=False)
	await ctx.send(embed=embed)


@client.command(
    aliases=['XQ', 'xq', 'Xq', 'xQ', 'xingqiu', 'xqc', 'xQc', 'XQC', 'xQcL'])
async def Xingqiu(ctx):
	embed = discord.Embed(
	    title='Xingqiu Farming List',
	    description=
	    'This is for Xingqiu specific talent and character materials only. Refer to corresponding commands for the specific weapons that this character uses.',
	    colour=discord.Colour.red())

	embed.set_footer(text='Banner by: discord.gg/Keqing')  #Bottom Text
	embed.set_image(
	    url=
	    'https://media.discordapp.net/attachments/824481856862158849/830641405667835904/Xingqiu.png?width=1039&height=702'
	)  #Banner
	embed.set_thumbnail(
	    url='https://rerollcdn.com/GENSHIN/Characters/Xingqiu.png'
	)  #Small Icon top right
	embed.set_author(
	    name='Jukelyn',
	    icon_url=
	    'https://cdn.discordapp.com/avatars/347216701055565827/5f29ea98f32f2db110e52780c2f657dc.png?size=256'
	)
	embed.add_field(
	    name='Everyday',
	    value='Silk Flowers \n Oceanids \n Hilichurls and Samachurls (Masks)',
	    inline=False)
	embed.add_field(name='Mondays', value='None', inline=False)
	embed.add_field(name='Tuesdays', value='None', inline=False)
	embed.add_field(name='Wednesdays', value='Teachings of Gold', inline=False)
	embed.add_field(name='Thursdays', value='None', inline=False)
	embed.add_field(name='Fridays', value='None', inline=False)
	embed.add_field(name='Saturdays', value='Teachings of Gold', inline=False)
	embed.add_field(name='Sundays', value='Teachings of Gold', inline=False)
	await ctx.send(embed=embed)


@client.command(
    aliases=['PR', 'pr', 'proran', 'ProRan', 'proRan', 'prototyperancour'])
async def protoRan(ctx):
	embed = discord.Embed(
	    title='Prototype Rancour Farming List',
	    description=
	    'This is for Prototype Rancour specific weapon ascension materials only. Refer to corresponding commands for the specific characters that this weapon is used on.',
	    colour=discord.Colour.red())

	embed.set_footer(text='Made by: Jukelyn#9848')  #Bottom Text
	embed.set_thumbnail(
	    url='https://rerollcdn.com/GENSHIN/Weapon/NEW/Prototype_Rancour.png'
	)  #Small Icon top right
	embed.set_author(
	    name='Jukelyn',
	    icon_url=
	    'https://cdn.discordapp.com/avatars/347216701055565827/5f29ea98f32f2db110e52780c2f657dc.png?size=256'
	)
	embed.add_field(
	    name='Everyday',
	    value=
	    'Fatui Cicin Mages \n Skirmishers \n Agents \n Electo Cicin Mages',
	    inline=False)
	embed.add_field(name='Mondays', value='None', inline=False)
	embed.add_field(name='Tuesdays', value='Mist Veiled Elixir', inline=False)
	embed.add_field(name='Wednesdays', value='None', inline=False)
	embed.add_field(name='Thursdays', value='None', inline=False)
	embed.add_field(name='Fridays', value='Mist Veiled Elixir', inline=False)
	embed.add_field(name='Saturdays', value='None', inline=False)
	embed.add_field(name='Sundays', value='Mist Veiled Elixir', inline=False)
	await ctx.send(embed=embed)


@client.command(aliases=[
    'PA', 'pa', 'proarc', 'ProArc', 'proArc', 'prototypearchaic',
    'prototypeanimus'
])
async def protoArch(ctx):
	embed = discord.Embed(
	    title='Prototype Archaic/Aminus Farming List',
	    description=
	    'This is for Prototype Archaic/Aminus specific weapon ascension materials only. Refer to corresponding commands for the specific characters that this weapon is used on.',
	    colour=discord.Colour.red())

	embed.set_footer(text='Made by: Jukelyn#9848')  #Bottom Text
	embed.set_thumbnail(
	    url='https://rerollcdn.com/GENSHIN/Weapon/NEW/Prototype_Aminus.png'
	)  #Small Icon top right
	embed.set_author(
	    name='Jukelyn',
	    icon_url=
	    'https://cdn.discordapp.com/avatars/347216701055565827/5f29ea98f32f2db110e52780c2f657dc.png?size=256'
	)
	embed.add_field(name='Everyday',
	                value='Geovishaps \n Hilichurls and Samachurls (Masks)',
	                inline=False)
	embed.add_field(name='Mondays', value='None', inline=False)
	embed.add_field(name='Tuesdays', value='None', inline=False)
	embed.add_field(name='Wednesdays', value='Aerosiderite', inline=False)
	embed.add_field(name='Thursdays', value='None', inline=False)
	embed.add_field(name='Fridays', value='None', inline=False)
	embed.add_field(name='Saturdays', value='Aerosiderite', inline=False)
	embed.add_field(name='Sundays', value='Aerosiderite', inline=False)
	await ctx.send(embed=embed)


@client.command(
    aliases=['sr', 'SR', 'skyrider', 'Skyrider', 'SkyRider', 'skyridersword'])
async def skyRider(ctx):
	embed = discord.Embed(
	    title='Skyrider Farming List',
	    description=
	    'This is for Skyrider specific weapon ascension materials only. Refer to corresponding commands for the specific characters that this weapon is used on.',
	    colour=discord.Colour.red())

	embed.set_footer(text='Made by: Jukelyn#9848')  #Bottom Text
	embed.set_thumbnail(
	    url='https://rerollcdn.com/GENSHIN/Weapon/NEW/Skyrider_Sword.png'
	)  #Small Icon top right
	embed.set_author(
	    name='Jukelyn',
	    icon_url=
	    'https://cdn.discordapp.com/avatars/347216701055565827/5f29ea98f32f2db110e52780c2f657dc.png?size=256'
	)
	embed.add_field(name='Everyday', value='None', inline=False)
	embed.add_field(name='Mondays', value='None', inline=False)
	embed.add_field(name='Tuesdays', value='None', inline=False)
	embed.add_field(name='Wednesdays', value='None', inline=False)
	embed.add_field(name='Thursdays', value='None', inline=False)
	embed.add_field(name='Fridays', value='None', inline=False)
	embed.add_field(name='Saturdays', value='None', inline=False)
	embed.add_field(name='Sundays', value='None', inline=False)
	await ctx.send(embed=embed)


@client.command(aliases=[
    'TTDS', 'TToDS', 'talesofdragon', 'talesOfdragon', 'dragonbook',
    'thrillingTales'
])
async def ttds(ctx):
	embed = discord.Embed(
	    title='Thrilling Tales of Dragon Slayers Farming List',
	    description=
	    'This is for Thrilling Tales of Dragon Slayers specific weapon ascension materials only. Refer to corresponding commands for the specific characters that this weapon is used on.',
	    colour=discord.Colour.red())

	embed.set_footer(text='Made by: Jukelyn#9848')  #Bottom Text
	embed.set_thumbnail(
	    url=
	    'https://rerollcdn.com/GENSHIN/Weapon/NEW/Thrilling_Tales_of_Dragon_Slayers.png'
	)  #Small Icon top right
	embed.set_author(
	    name='Jukelyn',
	    icon_url=
	    'https://cdn.discordapp.com/avatars/347216701055565827/5f29ea98f32f2db110e52780c2f657dc.png?size=256'
	)
	embed.add_field(name='Everyday',
	                value='Abyss Mages \n Samachurls (Scrolls)',
	                inline=False)
	embed.add_field(name='Mondays', value='None', inline=False)
	embed.add_field(name='Tuesdays',
	                value='Boreal Wolf\'s Tooth',
	                inline=False)
	embed.add_field(name='Wednesdays', value='None', inline=False)
	embed.add_field(name='Thursdays', value='None', inline=False)
	embed.add_field(name='Fridays', value='Boreal Wolf\'s Tooth', inline=False)
	embed.add_field(name='Saturdays', value='None', inline=False)
	embed.add_field(name='Sundays', value='Boreal Wolf\'s Tooth', inline=False)
	await ctx.send(embed=embed)


@client.command(aliases=['monday', 'Monday', 'jukeMon', 'mon'])
async def JukeMonday(ctx):
	embed = discord.Embed(
	    title='__Juke\'s Monday Farming List__',
	    description=
	    'This is for Jukelyn\'s team only. Refer to corresponding commands for the specific characters or weapon info.',
	    colour=discord.Colour.red())

	embed.set_footer(text='Made by: Jukelyn#9848')  #Bottom Text
	embed.set_thumbnail(
	    url=
	    'https://cdn.discordapp.com/avatars/347216701055565827/5f29ea98f32f2db110e52780c2f657dc.png?size=256'
	)  #Small Icon top right
	embed.set_author(
	    name='Jukelyn',
	    icon_url=
	    'https://cdn.discordapp.com/avatars/347216701055565827/5f29ea98f32f2db110e52780c2f657dc.png?size=256'
	)
	embed.add_field(
	    name='__Diluc__',
	    value=
	    '**Character:** Small Lamp Grass, Pyro Regisvines, Skirmishers, Agents, and Electro Cicin Mages. \n \n **Prototype Aminus:** Geovishaps, Hilichurls (Masks), and Samachurls (Masks). \n \n **Talents:** None',
	    inline=False)
	embed.add_field(
	    name='Xingqiu',
	    value='Silk Flowers \n Oceanids \n Hilichurls and Samachurls (Masks)',
	    inline=False)
	embed.add_field(
	    name='Skyrider Sword',
	    value='Windwheel Asters \n Anemo Hypostatis \n Whopperflowers',
	    inline=False)
	embed.add_field(
	    name='Bennett',
	    value='Windwheel Asters \n Pyro Regisvines \n Treasure Hoarders',
	    inline=False)
	embed.add_field(
	    name='Prototype Rancour',
	    value='Windwheel Asters \n Anemo Hypostatis \n Whopperflowers',
	    inline=False)
	embed.add_field(
	    name='Sucrose',
	    value='Windwheel Asters \n Anemo Hypostatis \n Whopperflowers',
	    inline=False)
	embed.add_field(
	    name='Thrilling Tales of Dragon Slayers',
	    value='Windwheel Asters \n Anemo Hypostatis \n Whopperflowers',
	    inline=False)

	await ctx.send(embed=embed)


@client.command(aliases=['tuesday', 'Tuesday', 'jukeTues', 'tues'])
async def JukeTuesday(ctx):
	embed = discord.Embed(
	    title='__Juke\'s Tuesday Farming List__',
	    description=
	    'This is for Jukelyn\'s team only. Refer to corresponding commands for the specific characters or weapon info.',
	    colour=discord.Colour.red())

	embed.set_footer(text='Made by: Jukelyn#9848')  #Bottom Text
	embed.set_thumbnail(
	    url=
	    'https://cdn.discordapp.com/avatars/347216701055565827/5f29ea98f32f2db110e52780c2f657dc.png?size=256'
	)  #Small Icon top right
	embed.set_author(
	    name='Jukelyn',
	    icon_url=
	    'https://cdn.discordapp.com/avatars/347216701055565827/5f29ea98f32f2db110e52780c2f657dc.png?size=256'
	)
	embed.add_field(
	    name='__Diluc__',
	    value=
	    '**Character:** Small Lamp Grass, Pyro Regisvines, Skirmishers, Agents, and Electro Cicin Mages. \n \n **Prototype Aminus:** Geovishaps, Hilichurls (Masks), and Samachurls (Masks). \n \n **Talents:** None',
	    inline=False)
	embed.add_field(
	    name='Xingqiu',
	    value=
	    '**Character:** Silk Flowers, Oceanids, Hilichurls (Masks), and Samachurls (Masks) \n \n **Skyrider Sword:** \n \n **Talents:**',
	    inline=False)
	embed.add_field(
	    name='Bennett',
	    value=
	    '**Character:** Windwheel Asters, Pyro Regisvines, Treasure Hoarders. \n \n **Prototype Rancour:** \n \n **Talents:**',
	    inline=False)
	embed.add_field(
	    name='Sucrose',
	    value=
	    '**Character:** Windwheel Asters, Anemo Hypostatis, Whopperflowers. \n \n **TTDS:** \n \n **Talents:** ',
	    inline=False)

	await ctx.send(embed=embed)


@client.command(aliases=['wednesday', 'Wednesday', 'jukeWed', 'wed'])
async def JukeWednesday(ctx):
	embed = discord.Embed(
	    title='__Juke\'s Wednesday Farming List__',
	    description=
	    'This is for Jukelyn\'s team only. Refer to corresponding commands for the specific characters or weapon info.',
	    colour=discord.Colour.red())

	embed.set_footer(text='Made by: Jukelyn#9848')  #Bottom Text
	embed.set_thumbnail(
	    url=
	    'https://cdn.discordapp.com/avatars/347216701055565827/5f29ea98f32f2db110e52780c2f657dc.png?size=256'
	)  #Small Icon top right
	embed.set_author(
	    name='Jukelyn',
	    icon_url=
	    'https://cdn.discordapp.com/avatars/347216701055565827/5f29ea98f32f2db110e52780c2f657dc.png?size=256'
	)
	embed.add_field(
	    name='__Diluc__',
	    value=
	    '**Character:** Small Lamp Grass, Pyro Regisvines, Skirmishers, Agents, and Electro Cicin Mages. \n \n **Prototype Aminus:** Geovishaps, Hilichurls (Masks), and Samachurls (Masks). \n \n **Talents:** None',
	    inline=False)
	embed.add_field(
	    name='Xingqiu',
	    value=
	    '**Character:** Silk Flowers, Oceanids, Hilichurls (Masks), and Samachurls (Masks) \n \n **Skyrider Sword:** \n \n **Talents:**',
	    inline=False)
	embed.add_field(
	    name='Bennett',
	    value=
	    '**Character:** Windwheel Asters, Pyro Regisvines, Treasure Hoarders. \n \n **Prototype Rancour:** \n \n **Talents:**',
	    inline=False)
	embed.add_field(
	    name='Sucrose',
	    value=
	    '**Character:** Windwheel Asters, Anemo Hypostatis, Whopperflowers. \n \n **TTDS:** \n \n **Talents:** ',
	    inline=False)

	await ctx.send(embed=embed)


@client.command(aliases=['thursday', 'Thursday', 'jukeThurs', 'thurs'])
async def JukeThursday(ctx):
	embed = discord.Embed(
	    title='__Juke\'s Thursday Farming List__',
	    description=
	    'This is for Jukelyn\'s team only. Refer to corresponding commands for the specific characters or weapon info.',
	    colour=discord.Colour.red())

	embed.set_footer(text='Made by: Jukelyn#9848')  #Bottom Text
	embed.set_thumbnail(
	    url=
	    'https://cdn.discordapp.com/avatars/347216701055565827/5f29ea98f32f2db110e52780c2f657dc.png?size=256'
	)  #Small Icon top right
	embed.set_author(
	    name='Jukelyn',
	    icon_url=
	    'https://cdn.discordapp.com/avatars/347216701055565827/5f29ea98f32f2db110e52780c2f657dc.png?size=256'
	)
	embed.add_field(
	    name='__Diluc__',
	    value=
	    '**Character:** Small Lamp Grass, Pyro Regisvines, Skirmishers, Agents, and Electro Cicin Mages. \n \n **Prototype Aminus:** Geovishaps, Hilichurls (Masks), and Samachurls (Masks). \n \n **Talents:** None',
	    inline=False)
	embed.add_field(
	    name='Xingqiu',
	    value=
	    '**Character:** Silk Flowers, Oceanids, Hilichurls (Masks), and Samachurls (Masks) \n \n **Skyrider Sword:** \n \n **Talents:**',
	    inline=False)
	embed.add_field(
	    name='Bennett',
	    value=
	    '**Character:** Windwheel Asters, Pyro Regisvines, Treasure Hoarders. \n \n **Prototype Rancour:** \n \n **Talents:**',
	    inline=False)
	embed.add_field(
	    name='Sucrose',
	    value=
	    '**Character:** Windwheel Asters, Anemo Hypostatis, Whopperflowers. \n \n **TTDS:** \n \n **Talents:** ',
	    inline=False)

	await ctx.send(embed=embed)


@client.command(aliases=['friday', 'Friday', 'jukeFri', 'fri'])
async def JukeFriday(ctx):
	embed = discord.Embed(
	    title='__Juke\'s Friday Farming List__',
	    description=
	    'This is for Jukelyn\'s team only. Refer to corresponding commands for the specific characters or weapon info.',
	    colour=discord.Colour.red())

	embed.set_footer(text='Made by: Jukelyn#9848')  #Bottom Text
	embed.set_thumbnail(
	    url=
	    'https://cdn.discordapp.com/avatars/347216701055565827/5f29ea98f32f2db110e52780c2f657dc.png?size=256'
	)  #Small Icon top right
	embed.set_author(
	    name='Jukelyn',
	    icon_url=
	    'https://cdn.discordapp.com/avatars/347216701055565827/5f29ea98f32f2db110e52780c2f657dc.png?size=256'
	)
	embed.add_field(
	    name='__Diluc__',
	    value=
	    '**Character:** Small Lamp Grass, Pyro Regisvines, Skirmishers, Agents, and Electro Cicin Mages. \n \n **Prototype Aminus:** Geovishaps, Hilichurls (Masks), and Samachurls (Masks). \n \n **Talents:** None',
	    inline=False)
	embed.add_field(
	    name='Xingqiu',
	    value=
	    '**Character:** Silk Flowers, Oceanids, Hilichurls (Masks), and Samachurls (Masks) \n \n **Skyrider Sword:** \n \n **Talents:**',
	    inline=False)
	embed.add_field(
	    name='Bennett',
	    value=
	    '**Character:** Windwheel Asters, Pyro Regisvines, Treasure Hoarders. \n \n **Prototype Rancour:** \n \n **Talents:**',
	    inline=False)
	embed.add_field(
	    name='Sucrose',
	    value=
	    '**Character:** Windwheel Asters, Anemo Hypostatis, Whopperflowers. \n \n **TTDS:** \n \n **Talents:** ',
	    inline=False)

	await ctx.send(embed=embed)


@client.command(aliases=['saturday', 'Saturday', 'jukeSat', 'sat'])
async def JukeSaturday(ctx):
	embed = discord.Embed(
	    title='__Juke\'s Saturday Farming List__',
	    description=
	    'This is for Jukelyn\'s team only. Refer to corresponding commands for the specific characters or weapon info.',
	    colour=discord.Colour.red())

	embed.set_footer(text='Made by: Jukelyn#9848')  #Bottom Text
	embed.set_thumbnail(
	    url=
	    'https://cdn.discordapp.com/avatars/347216701055565827/5f29ea98f32f2db110e52780c2f657dc.png?size=256'
	)  #Small Icon top right
	embed.set_author(
	    name='Jukelyn',
	    icon_url=
	    'https://cdn.discordapp.com/avatars/347216701055565827/5f29ea98f32f2db110e52780c2f657dc.png?size=256'
	)
	embed.add_field(
	    name='__Diluc__',
	    value=
	    '**Character:** Small Lamp Grass, Pyro Regisvines, Skirmishers, Agents, and Electro Cicin Mages. \n \n **Prototype Aminus:** Geovishaps, Hilichurls (Masks), and Samachurls (Masks). \n \n **Talents:** None',
	    inline=False)
	embed.add_field(
	    name='Xingqiu',
	    value=
	    '**Character:** Silk Flowers, Oceanids, Hilichurls (Masks), and Samachurls (Masks) \n \n **Skyrider Sword:** \n \n **Talents:**',
	    inline=False)
	embed.add_field(
	    name='Bennett',
	    value=
	    '**Character:** Windwheel Asters, Pyro Regisvines, Treasure Hoarders. \n \n **Prototype Rancour:** \n \n **Talents:**',
	    inline=False)
	embed.add_field(
	    name='Sucrose',
	    value=
	    '**Character:** Windwheel Asters, Anemo Hypostatis, Whopperflowers. \n \n **TTDS:** \n \n **Talents:** ',
	    inline=False)

	await ctx.send(embed=embed)


@client.command(aliases=['sunday', 'Sunday', 'jukeSun', 'sun'])
async def JukeSunday(ctx):
	embed = discord.Embed(
	    title='__Juke\'s Sunday Farming List__',
	    description=
	    'This is for Jukelyn\'s team only. Refer to corresponding commands for the specific characters or weapon info.',
	    colour=discord.Colour.red())

	embed.set_footer(text='Made by: Jukelyn#9848')  #Bottom Text
	embed.set_thumbnail(
	    url=
	    'https://cdn.discordapp.com/avatars/347216701055565827/5f29ea98f32f2db110e52780c2f657dc.png?size=256'
	)  #Small Icon top right
	embed.set_author(
	    name='Jukelyn',
	    icon_url=
	    'https://cdn.discordapp.com/avatars/347216701055565827/5f29ea98f32f2db110e52780c2f657dc.png?size=256'
	)
	embed.add_field(
	    name='__Diluc__',
	    value=
	    '**Character:** Small Lamp Grass, Pyro Regisvines, Skirmishers, Agents, and Electro Cicin Mages. \n \n **Prototype Aminus:** Geovishaps, Hilichurls (Masks), and Samachurls (Masks). \n \n **Talents:** None',
	    inline=False)
	embed.add_field(
	    name='Xingqiu',
	    value=
	    '**Character:** Silk Flowers, Oceanids, Hilichurls (Masks), and Samachurls (Masks) \n \n **Skyrider Sword:** \n \n **Talents:**',
	    inline=False)
	embed.add_field(
	    name='Bennett',
	    value=
	    '**Character:** Windwheel Asters, Pyro Regisvines, Treasure Hoarders. \n \n **Prototype Rancour:** \n \n **Talents:**',
	    inline=False)
	embed.add_field(
	    name='Sucrose',
	    value=
	    '**Character:** Windwheel Asters, Anemo Hypostatis, Whopperflowers. \n \n **TTDS:** \n \n **Talents:** ',
	    inline=False)

	await ctx.send(embed=embed)


@client.command(aliases=[
    'sch', 'sc', 'sd', 'give', 'wut', 'what', 'Sch', 'Schedule', 'shcedule',
    'Shcedule', 'Scedule', 'scedule'
])
async def schedule(ctx):
	embed = discord.Embed(
	    title='Daily Farming List',
	    description=
	    'Just farming for Ayaka, Mistsplitter, and Wolf\'s Gravestone.',
	    colour=discord.Colour.red())

	embed.set_footer(text='Poggers.')  #Bottom Text
	embed.set_thumbnail(
	    url='https://rerollcdn.com/GENSHIN/Weapon/NEW/Mistsplitter_Reforged.png'
	)  #Small Icon top right
	embed.set_author(
	    name='Jukelyn',
	    icon_url=
	    'https://cdn.discordapp.com/avatars/347216701055565827/a_04ad9809d2091e8e8c901ef93fe02f74.png?size=256'
	)
	embed.add_field(name='Everyday',
	                value='Samurais and Sakura Blooms',
	                inline=False)
	embed.add_field(name='Mondays', value='Mistsplitter', inline=False)
	embed.add_field(name='Tuesdays',
	                value='Ayaka Talent Scrolls',
	                inline=False)
	embed.add_field(name='Wednesdays', value='WGS or Ayaka Boss', inline=False)
	embed.add_field(name='Thursdays', value='Mistsplitter', inline=False)
	embed.add_field(name='Fridays', value='Ayaka Talent Scrolls', inline=False)
	embed.add_field(name='Saturdays', value='WGS or Ayaka Boss', inline=False)
	embed.add_field(name='Sundays',
	                value='Mistsplitter > WGS > Ayaka Talents',
	                inline=False)
	await ctx.send(embed=embed)


########################################################### Genshin Commands Above here ###########################################################

keep_alive()
botToken = os.environ['TOKEN']
client.run(botToken)