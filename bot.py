import discord
import os
from dotenv import load_dotenv


load_dotenv()

TOKEN = os.getenv('TOKEN')
client = discord.Client()
MAXIMUM_SPAM = 20

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
	
    if message.content.startswith('$spam '):
        user_msg = message.content.split()
        sentence_array = user_msg[1:len(user_msg)-1]

        spam_count = int(user_msg[len(user_msg)-1])
        num = min(MAXIMUM_SPAM, spam_count)

        sentence = ""
        for word in sentence_array:
            sentence += word + " "
        sentence = sentence[:len(sentence)-1]

        for i in range(num):
            await message.channel.send(sentence)

    elif (message.content.startswith('$spam')):
        await message.channel.send('Incorrect Usage')
        await message.channel.send('$spam [text message] [number of times to spam]')
        await message.channel.send(f'Currently, the maximum number is {MAXIMUM_SPAM}')
             
client.run(TOKEN)
