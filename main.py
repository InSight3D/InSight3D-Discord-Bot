
# Save New Duplicate & Edit Just Text Twitter
# ye try it
# Twitter?
 #Imports
import discord
import os
import random
from keep_alive import keep_alive
import pyjokes
from discord.ext import commands
from lists import idea_printing
from lists import idea_coding
# from discord_slash import SlashCommand, SlashContext
intents = discord.Intents().all()
bot = commands.Bot(command_prefix="!", intents=intents)
# slash = SlashCommand(bot, sync_commands=True)
bot.remove_command('help')
# Start Discord Client

# hey i was working on a music bot if u wanna see 

#Varuables
live = print('We Have Logged In As {0.user}'.format(bot))


# Discord Bot If Online Chck, See #Varuabe For More Info
@bot.event
async def on_ready():
  await bot.change_presence(activity=discord.Game(name='!support'))
  live

#Start Client Check


@bot.event
async def on_message(message):
  await bot.process_commands(message)
  if message.author == bot.user:
    return

#   with open('users.json', 'r') as f:
#     users = json.load(f)

#   await update_data(users, message.author)
#   await add_experience(users, message.author, 5)
#   await level_up(users, message.author, message.channel)


#   with open('users.json', 'w') as f:
#     json.dump(users, f)

# async def update_data(users, user):
#   if not user.id in users:
#     users[user.id] = {}
#     users[user.id]['experience'] = 0
#     users[user.id]['level'] = 1

# async def add_experience(users, user, exp):
#   users[user.id]['experience'] += exp

# async def level_up(users, user, channel):
#   experience = users[user.id]['experience']
#   lvl_start = users[user.id]['level']
#   lvl_end = int(experience ** (1/4))

#   if lvl_start < lvl_end:
#     await channel.send_message(channel,'{} has leveled up to level {}'. format(user.mention, lvl_end))
#     users[user.id]['level'] = lvl_end

# @bot.command()
# async def invite(ctx):
#    invite = await ctx.create_invite(reason='Testing', max_age = 0, temporary = False)
#    await ctx.send(f'Invite link: {invite.url}')

# Slash Commands



# @slash.slash(name="test")                   
# async def _test(ctx: SlashContext): 
#   embedVar = discord.Embed(title='Hey! These Are My Commands:')
#   embedVar.add_field(name="`!roll`", value="Pick Any Value From 1-6", inline=False)
#   embedVar.add_field(name="`!roll <number>`", value="Pick Any Value From 0 And The Number You Picked", inline=False)
#   await ctx.send(embed=embedVar)


@bot.command()
async def say(ctx, arg):
  await ctx.send(arg)


@bot.command()
async def insight3d(ctx):
  embedVar = discord.Embed(title="https://insight3d.tech/", color=0xFF0000)
  await ctx.send(embed=embedVar)

@bot.command()
async def joke(ctx):
  embedVar = discord.Embed(description = pyjokes.get_joke())
  await ctx.send(embed=embedVar)



@bot.command()
async def blog(ctx):
     masked_link_embed = discord.Embed(
         title = 'Use The Link Below To Got To The Blog',
         description= '[InSight3D Blog Posts](https://insight3d.tech/blog-2/)',
           color = discord.Colour.red()
      )
     await ctx.send(embed=masked_link_embed)

@bot.command()
async def creators(ctx):
     masked_creator_emebed = discord.Embed(
       title = 'Here Are The Coders That Contributed To My Code:',
       description= '@neil Shah #6469 & MehoB #1483',
       color = discord.Colour.red()
     )
     await ctx.send(embed=masked_creator_emebed)

@bot.command()
async def repo(ctx):
     masked_repo_emebed = discord.Embed(
       title = 'Ok, Here is The Link To My GitHub Repo:',
       description= '[GitHub InSight3D Bot](https://github.com/InSight3D/InSight3D-Discord-Bot)',
       color = discord.Colour.red()
     )
     await ctx.send(embed=masked_repo_emebed)

@bot.command()  
async def idea(ctx):
     masked_idea_emebed = discord.Embed(
       title = 'Here Is The Link To The Idea Sheet:',
       description= '[Share Your Ideas Here](https://docs.google.com/spreadsheets/d/1HHQMCAI5Cg4ul-GSQYx6t9xvcXBz8LBN0wKKHqi4h3E/edit?usp=sharing)',
       color = discord.Colour.red()
     )
     await ctx.send(embed=masked_idea_emebed)

@bot.command() 
async def ping(ctx):
     embedVar = discord.Embed(title="Latency", description=f'Pong! In {round(bot.latency * 1000)} Milliseconds')
     await ctx.send(embed=embedVar)

@bot.command()  
async def jam(ctx):
     masked_jam_emebed = discord.Embed(
       title = 'Here Is The Link To InSight3D Code Jam 1:',
       description= '[InSight3D Itch Code Jam](https://itch.io/jam/insight3d-code-jam-1)',
       color = discord.Colour.red()
     )
     await ctx.send(embed=masked_jam_emebed)

@bot.command()
async def topic1(ctx):
  embedVar = discord.Embed(description=random.choice(idea_printing), color=0xFF0000)
  await ctx.send(embed=embedVar)

@bot.command()
async def topic2(ctx):
  embedVar = discord.Embed(description=random.choice(idea_coding), color=0xFF0000)
  await ctx.send(embed=embedVar)



@bot.command()
async def support(ctx):
     embedVar = discord.Embed(title="Please Use One Of The Following Commands:", color=0xFF0000)
     embedVar.add_field(name="`!web`", value="Gives You All Web Based Commands", inline=False)
     embedVar.add_field(name="`!server`", value="Gives You All Server Based Commands", inline=False)
     embedVar.add_field(name="`!mod`", value="Get Mod Commands, (Only Accsesable By Mods)", inline=False)
     embedVar.add_field(name="`!other`", value="Get All Non-Relatable Commands", inline=False)
     await ctx.send(embed=embedVar)
    
@bot.command()
async def web(ctx):
     embedVar = discord.Embed(title="Here Are The Web Based Commands:", color=0xFF0000)
     embedVar.add_field(name="`!insight3d`", value="Gives You A Link To Our Site", inline=False)
     embedVar.add_field(name="`!blog`", value="Gives You A Link To Our Blog", inline=False)
     embedVar.add_field(name="`!repo`", value="Gives You The Link To My Repo", inline=False)
     embedVar.add_field(name="`!idea`", value="Gives You A Link To The Ideq Sheet", inline=False)
     embedVar.add_field(name="`!jam`", value="Gives You A Link To The Current Code Jam", inline=False)
     await ctx.send(embed=embedVar)
    
@bot.command()
async def server(ctx):
     embedVar = discord.Embed(title="Here Are The Server Based Commands:", color=0xFF0000)
     embedVar.add_field(name="`!invite`", value="Created A Server Invite Link", inline=False)
     embedVar.add_field(name="`!ping`", value="Find The Latency Between You And The Bot", inline=False)
     embedVar.add_field(name="`!callmod`", value="Ping A Moderator To Report A Situation", inline=False)
     embedVar.add_field(name="`!members`", value="Find Out How Many Members Are In The Server", inline=False)
     await ctx.send(embed=embedVar)

@bot.command()
async def text(ctx):
  embedVar = discord.Embed(title="Here Are The Text Based Commands:", color=0xFF0000)
  embedVar.add_field(name="`!joke`", value="Picks A Random Coding Joke", inline=False)
  embedVar.add_field(name="`!topic1`", value="Picks A Random Topic Starter About 3D Printing", inline=False)
  embedVar.add_field(name="`!topic2`", value="Picks A Random Topic Starter About Coding", inline=False)
  embedVar.add_field(name="`!embed <text with quotes>`", value="Make A Simple Title Embed", inline=False)
  embedVar.add_field(name="`!game <number>`", value="A Simple Number Guessing Game", inline=False)  
  await ctx.send(embed=embedVar)

@bot.command()
async def other(ctx):
  embedVar = discord.Embed(title="Here Are Other Commands Options:", color=0xFF0000)
  embedVar.add_field(name="`!text`", value="Gets All Text Based Commands (Games, Topics, Joke)", inline=False)
  embedVar.add_field(name="`!math`", value="Gets All Math Based Commands", inline=False)
  await ctx.send(embed=embedVar)

@bot.command()
async def math(ctx):
  embedVar = discord.Embed(title="Here Are Math Based Commands:", color=0xFF0000)
  embedVar.add_field(name="`!add`", value="Add Numbers: `!add (Num1) (Num2)`", inline=False)
  embedVar.add_field(name="`!sub`", value="Subtract Numbers: `!sub (Num1) (Num2)`", inline=False)
  embedVar.add_field(name="`!mul`", value="Multiply Numbers: `!mul (Num1) (Num2)`", inline=False)
  embedVar.add_field(name="`!div`", value="Divide Numbers: `!div (Num1) (Num2)`", inline=False)
  embedVar.add_field(name="`!sqr`", value="Square A Number: `!sqr (Num1)`", inline=False)
  await ctx.send(embed=embedVar)


@bot.command()
@commands.has_permissions(ban_members=True)
async def mod(ctx):
    embedVar = discord.Embed(title="Here Are The Moderator Commands:", color=0xFF0000)
    embedVar.add_field(name="`!ban <@user> <reason>`", value="Ban A User", inline=False)
    embedVar.add_field(name="`!kick <@user> <reason>`", value="Kick A User", inline=False)
    embedVar.add_field(name="`!warn <@user> <reason>`", value="Warn A User", inline=False)
    embedVar.add_field(name="`!mute <@user>`", value="Mute A User", inline=False)
    embedVar.add_field(name="`!unmute <@user>`", value="Unmute A User", inline=False)
    embedVar.add_field(name="`!purge <Number Of Messages>`", value="Delete A Number Of Messages", inline=False)
    await ctx.send(embed=embedVar)
  



@bot.command()
@commands.cooldown(1, 30.0, commands.BucketType.user)
async def callmod(ctx):
     embedVar = discord.Embed(description = f"<@&799666759908065355>", color=0xFF0000)
     embedVar.add_field(name='I Have Pinged A Mod', value="Thank You For Using InSight3D", inline=False)
     await ctx.send(embed=embedVar)
       
#Mod Commands
@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
  await member.kick(reason=reason)
  embedVar = discord.Embed(description=f'{member.mention} Has Been Kicked Successfully For {reason}', color=0xFF0000)
  await ctx.send(embed=embedVar)

@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):
  await member.ban(reason=reason)
  embedVar = discord.Embed(description=f'{member.mention} Has Been Banned Successfully For {reason}', color=0xFF0000)
  await ctx.send(embed=embedVar)

@bot.command()
@commands.has_permissions(kick_members=True)
async def mute(ctx, member: discord.Member, *, reason=None):
  guild = ctx.guild
  mutedRole = discord.utils.get(guild.roles, name="Muted")

  await member.add_roles(mutedRole, reason=reason)
  embedVar = discord.Embed(description=f'Muted {member.mention}, Reason: {reason}', color=0xFF0000)
  await ctx.send(embed=embedVar)
  await member.send(f'You Were Muted In The Server {guild.name} For {reason}')

@bot.command()
@commands.has_permissions(kick_members=True)
async def unmute(ctx, member: discord.Member, reason=None):
  mutedRole = discord.utils.get(ctx.guild.roles, name="Muted")

  await member.remove_roles(mutedRole, reason=reason)
  embedVar = discord.Embed(description=f'{member.mention} Was Unmuted, Reason: {reason}', color=0xFF0000)
  await ctx.send(embed=embedVar)

@bot.command()
@commands.has_permissions(ban_members=True)
async def unban(ctx, *, member):
  banned_users = await ctx.guild.bans()
  member_name, member_discriminator = member.split('#')

  for ban_entry in banned_users:
    user = ban_entry.user

    if (user.name, user.discriminator) == (member_name, member_discriminator):
      await ctx.guild.unban(user)
      embedVar = discord.Embed(description=f'{user.mention} Has Been Unbanned', color=0xFF0000)
      await ctx.send(embed=embedVar)
      return

@bot.command()
@commands.has_permissions(kick_members=True)
async def purge(ctx, ammount=5):
  await ctx.channel.purge(limit=ammount + 1)
  embedVar = discord.Embed(description=f'{ammount} Messages Were Successfully Purged', color=0xFF0000)
  await ctx.send(embed=embedVar)

@bot.command()
@commands.has_permissions(kick_members=True)
async def warn(ctx, member: discord.Member, *, reason=None):
  embedVar = discord.Embed(description=f'{member} Has Been Warned', color=0xFF0000)
  await ctx.send(embed=embedVar)
  await member.send(f'You Have Been Warned For {reason}')

#Join And Leave

@bot.event
async def on_member_join(member):
  channel = discord.utils.get(member.guild.channels, name='welcome')
  embedVar = discord.Embed(description=f'Welcome, {member.mention} To InSight3D. We Hope You Enjoy Your Stay', color=0xFF0000)
  await channel.send(embed=embedVar)
  default_role = discord.utils.get(member.guild.roles, id=814559374659551282)
  await member.add_roles(default_role)

  embedVar = discord.Embed(title="Welcome To InSight3D! I Just Wanted To Welcome You Myself, And Show You Around", color=0xFF0000)
  embedVar.add_field(name="Rules:", value="Before Using The Server, Please Check Over The Roles In The Role Channel", inline=False)
  embedVar.add_field(name="Roles:", value="To Pick Roles, Visit The Role Channel In The InSight3D Server", inline=False)
  embedVar.add_field(name="InSight3D Bot:", value="To Use, Or Contribute To Me, You Can Use The `!support` Command In Any Channel", inline=False)
  embedVar.add_field(name="Help Ticket:", value="To Create A Help Channel, Please Use The `?ticket <reason>`, And Someone Will Come To Help You", inline=False)
  embedVar.add_field(name="Talk To Staff:", value="To Talk To A Staff, Please Use Mod Mail To Make A Ticket", inline=False)
  await member.send(embed=embedVar)

@bot.command()
async def welcome(ctx):
  embedVar = discord.Embed(title="Welcome To InSight3D! I Just Wanted To Welcome You Myself, And Show You Around", color=0xFF0000)
  embedVar.add_field(name="Rules:", value="Before Using The Server, Please Check Over The Roles In The Role Channel", inline=False)
  embedVar.add_field(name="Roles:", value="To Pick Roles, Visit The Role Channel In The InSight3D Server", inline=False)
  embedVar.add_field(name="InSight3D Bot:", value="To Use, Or Contribute To Me, You Can Use The `!support` Command In Any Channel", inline=False)
  embedVar.add_field(name="Help Ticket:", value="To Create A Help Channel, Please Use The `?ticket <reason>`, And Someone Will Come To Help You", inline=False)
  embedVar.add_field(name="Talk To Staff:", value="To Talk To A Staff, Please Use Mod Mail To Make A Ticket", inline=False)
  await ctx.send(embed=embedVar)



# Games 

@bot.command()
async def game(ctx, *, number=0):
  correct_number = random.randint(0, 10)

  if number == correct_number:
    embedVar = discord.Embed(title=f'Your Number Is {number}', color=0xFF0000)
    embedVar.add_field(name='You Picked The Correct Number! You Won', value="Thanks For Playing!")
    await ctx.send(embed=embedVar)
  
  else:
    embedVar = discord.Embed(title=f'Your Number Is {number}', color=0xFF0000)
    embedVar.add_field(name="Sorry, You Picked The Wrong Number", value=f'The Correct Number Was {correct_number}')
    await ctx.send(embed=embedVar)
  


# Math Commands
@bot.command()
async def add(ctx, number1:int=0, *, number2:int=0):
  sum = number1 + number2
  embedVar = discord.Embed(description = f'The Answer To Your Equation Is {sum}', color=0xFF0000)
  await ctx.send(embed=embedVar)

@bot.command()
async def sub(ctx, number1:int=0, *, number2:int=0):
  sum = number1 - number2
  embedVar = discord.Embed(description = f'The Answer To Your Equation Is {sum}', color=0xFF0000)
  await ctx.send(embed=embedVar)

@bot.command()
async def mul(ctx, number1:int=0, *, number2:int=0):
  sum = number1 * number2
  embedVar = discord.Embed(description = f'The Answer To Your Equation Is {sum}', color=0xFF0000)
  await ctx.send(embed=embedVar)

@bot.command()
async def div(ctx, number1:int=0, *, number2:int=0):
  sum = number1 / number2
  embedVar = discord.Embed(description = f'The Answer To Your Equation Is {sum}', color=0xFF0000)
  await ctx.send(embed=embedVar)

@bot.command()
async def sqr(ctx, number1:int=0):
  sum = number1 * number1
  embedVar = discord.Embed(description = f'The Answer To Your Equation Is {sum}', color=0xFF0000)
  await ctx.send(embed=embedVar)

# User Commands

@bot.command()
async def embed(ctx, text=None):
  embedVar = discord.Embed(title=f'{text}', color=0xFF0000)
  await ctx.send(embed=embedVar)

# Bump Commands
@bot.command()
async def topbump(ctx):
  masked_idea_emebed = discord.Embed(
       title = 'Vote Our Server On Top.GG:',
       description= '[This Link Will Direct You To The Page](https://top.gg/servers/799339557250269244/vote)',
       color = discord.Colour.red()
     )
  await ctx.send(embed=masked_idea_emebed)
  
# Rules
@bot.command()
@commands.has_permissions(kick_members=True)
async def serverrule(ctx):
  embedVar = discord.Embed(title="Server Rules", description="Any Infracions Will Restult In A Mute, Kick Or Ban", color=0xFF0000)
  embedVar.add_field(name="Rule 1:", value="No Spam or flooding the chat with messages. Do not type in ALL CAPS.", inline=False)
  embedVar.add_field(name="Rule 2:", value="No bashing or heated arguments to other people in the chat.", inline=False)
  embedVar.add_field(name="Rule 3:", value="No adult (18+), explicit, or controversial messages.", inline=False)
  embedVar.add_field(name="Rule 4:", value="No racism or degrading content.", inline=False)
  embedVar.add_field(name="Rule 5:", value="Do not perform or promote the intentional use of glitches, hacks, bugs, and other exploits that will cause an incident within the community and other players.", inline=False)
  embedVar.add_field(name="Rule 6:", value="Do not use the @everyone / @here ping without permission.", inline=False)
  embedVar.add_field(name="Rule 7:", value="Do not argue with staff. Decisions are final.", inline=False)
  await ctx.send(embed=embedVar)

@bot.command()
async def userinfo(ctx, *, user: discord.Member = None):
    if user is None:
        user = ctx.author      
    date_format = "%a, %d %b %Y %I:%M %p"
    embed = discord.Embed(color=0xFF0000, description=user.mention)
    embed.set_author(name=str(user), icon_url=user.avatar_url)
    embed.set_thumbnail(url=user.avatar_url)
    embed.add_field(name="Joined Server", value=user.joined_at.strftime(date_format))
    members = sorted(ctx.guild.members, key=lambda m: m.joined_at)
    embed.add_field(name="Join Position", value=str(members.index(user)+1))
    embed.add_field(name="Joined Discord", value=user.created_at.strftime(date_format))
    if len(user.roles) > 1:
        role_string = ' '.join([r.mention for r in user.roles][1:])
        embed.add_field(name="Roles [{}]".format(len(user.roles)-1), value=role_string, inline=False)
    embed.set_footer(text='ID: ' + str(user.id))
    return await ctx.send(embed=embed)
  

# @bot.command()
# async def april(ctx):
#   title = random.choice(title)
#   embedVar = discord.Embed(description=f'{title}', color=0xFF0000)
#   await ctx.send(embed=embedVar)

keep_alive()

bot.run(os.getenv('TOKEN'))