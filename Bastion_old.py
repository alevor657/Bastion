import discord
from discord.ext import commands
import asyncio
import random
from datetime import datetime

client = discord.Client()
#bot = commands.Bot(command_prefix = '!', description = ' ')
answer = ('DO IT!', 'Nope', 'I don\'t think so :\\', 'It sucks.', 'Dunno :C',)
response = ('Doo-woo.', 'Boo boo doo de doo.', 'Dweet! Dweet! Dweet!',
            'Hee hoo hoo hoo-wee, hee hee hoo hoo hoo-wee.', 'Zwee?')

modes = {'hide' : True,
         'defense' : False,
         'log' : True} #hide - сканит сообщения только в black_forest, defence - посылает всех, кроме меня, log пишет лог, кек.

help_message = '''commands are:

**!help**
Show help (lel).

**Bastion!**
Bastion simply replies to you.

**Bastion <sample_text> ?**
Ask Bastion is it worth doing, or not.

**!channel**
Get channel name.

**!my_id**
Get your ID.

**!tts <sample_text>**
Send text-to-speech message.

**!set_game <sample_text>**
Set 'Playing...' status.

**!hide**
Hide Bastion in the black_forest.

**!defense**
Set Bastion to defense mode (he will reply only to his owner).

**!mode**
Get info on Bastion\'s modes (hide/defense).

**!bot_kill**
Kills Bastion (plz don't do this, he's the last one remaining :C).'''

def log(*message):
    '''Prints log record'''
    print(datetime.now().strftime('%d-%m-%Y %H:%M:%S'))
    for msg in message:
        print(msg, end=' ')
    print('\n------')

@client.event
async def on_ready():
    if modes['log']:
        #print(datetime.now().strftime('%d-%m-%Y %H:%M:%S'))
        #print('Logged in as')
        #print(client.user.name)
        #print(client.user.id)
        #print('------')
        log('Logged in as:\n', client.user.name, '\n', client.user.id)
    
    #await client.change_presence(game=discord.Game(name='game'))


@client.event
async def on_message(message):

#if hide
    if modes['hide'] and message.channel.name != 'black_forest':
        return

#if defense
    elif modes['defense'] and message.author.id != '214030651588870144' and message.author != client.user: #Добавь сюда and message.author.id != 'твой id'
        msg = 'INTRUDERS! \*LSHIFT, LEFT CLICK\* GET THE FUCK OUT, '                                       #Если хочешь чтобы он тебя не посылал в дефенс моде
        msg += '{0.author.mention}!'.format(message)                                                       #Id можно получить по !my_id
        await client.send_message(message.channel, msg)
        if modes['log']:
            #print(datetime.now().strftime('%d-%m-%Y %H:%M:%S'))
            #print('Intruder:', message.author.name)
            #print('------')
            log('Intruder:', message.author.name)

#!help
    elif message.content.startswith('!help'):
        msg = '{0.author.mention}, '.format(message)
        msg += help_message
        await client.send_message(message.channel, msg)
        if modes['log']:
            #print(datetime.now().strftime('%d-%m-%Y %H:%M:%S'))
            #print('Help requested from', message.author.name)
            #print('------')
            log('Help requested from', message.author.name)

#Bastion!
    elif message.content.startswith('Bastion!'):
        msg = '{0.author.mention}, '.format(message)
        msg += random.choice(response)
        await client.send_message(message.channel, msg)
        if modes['log']:
            #print(datetime.now().strftime('%d-%m-%Y %H:%M:%S'))
            #print('Responded to', message.author.name)
            #print('------')
            log('Responded to', message.author.name)

#Bastion .. ?
    elif message.content.startswith('Bastion') and message.content.endswith('?'):
        msg = '{0.author.mention}, '.format(message)
        msg += random.choice(answer)
        await client.send_message(message.channel, msg)
        if modes['log']:
            #print(datetime.now().strftime('%d-%m-%Y %H:%M:%S'))
            #print('Answered to', message.author.name)
            #print('------')
            log('Answered to', message.author.name)

#!bot_kill   
    elif message.content.startswith('!bot_kill'):
        await client.send_message(message.channel, 'BOOoooop.. :C')
        await client.close()
        if modes['log']:
            #print(datetime.now().strftime('%d-%m-%Y %H:%M:%S'))
            #print('Shutdown by', message.author.name)
            #print('------')
            log('Shutdown by', message.author.name)
        raise SystemExit

#!channel
    elif message.content.startswith('!channel'):
        msg = '{0.author.mention}, '.format(message)
        msg += message.channel.name
        await client.send_message(message.channel, msg)
        if modes['log']:
            #print(datetime.now().strftime('%d-%m-%Y %H:%M:%S'))
            #print('!channel', message.author.name)
            #print('------')
            log('!channel', message.author.name)

#!set_game
    elif message.content.startswith('!set_game'):
        await client.change_presence(game=discord.Game(name=message.content[10:]))
        if modes['log']:
            #print(datetime.now().strftime('%d-%m-%Y %H:%M:%S'))
            #print('!set_game', message.author.name)
            #print('------')
            log('!set_game', message.author.name)

#!hide
    elif message.content.startswith('!hide'):
        modes['hide'] = not modes['hide']
        msg = '{0.author.mention}, '.format(message)
        
        if modes['hide']:
            msg += 'Stealth mode ON'
        else:
            msg += 'Stealth mode OFF'

        await client.send_message(message.channel, msg)
        if modes['log']:
            #print(datetime.now().strftime('%d-%m-%Y %H:%M:%S'))
            #print(msg, 'by', message.author.name)
            #print('------')
            log(msg, 'by', message.author.name)

#!defense
    elif message.content.startswith('!defense'):
        modes['defense'] = not modes['defense']
        msg = '{0.author.mention}, '.format(message)

        if modes['defense']:
            msg += 'Defense mode ON'
        else:
            msg += 'Defense mode OFF'

        await client.send_message(message.channel, msg)
        if modes['log']:
            #print(datetime.now().strftime('%d-%m-%Y %H:%M:%S'))
            #print(msg, 'by', message.author.name)
            #print('------')
            log(msg, 'by', message.author.name)

#!mode
    elif message.content.startswith('!mode'):
        msg = '{0.author.mention}\n'.format(message)
        msg += 'Hide mode '
        if modes['hide']:
            msg += 'ON\n'
        else:
            msg += 'OFF\n'

        msg += 'Defense mode '
        if modes['defense']:
            msg += 'ON\n'
        else:
            msg += 'OFF\n'

        if modes['log']:
            log('!modes', message.author.name)

        await client.send_message(message.channel, msg)

#!my_id
    elif message.content.startswith('!my_id'):
        msg = '{0.author.mention}, '.format(message)
        msg += message.author.id
        await client.send_message(message.channel, msg)
        if modes['log']:
            #print(datetime.now().strftime('%d-%m-%Y %H:%M:%S'))
            #print('Id requested by', message.author.name)
            #print('------')
            log('Id requested by', message.author.name)

#!tts
    elif message.content.startswith('!tts'):
        await client.send_message(message.channel, message.content[5:], tts=True)
        if modes['log']:
            #print(datetime.now().strftime('%d-%m-%Y %H:%M:%S'))
            #print('TTS used by', message.author.name)
            #print('------')
            log('TTS used by', message.author.name, '\nMessage: \"', message.content[5:], '\"')

'''@bot.command()
async def test(msg : str):
    await bot.say(msg)'''
            
                                         
client.run('token')
