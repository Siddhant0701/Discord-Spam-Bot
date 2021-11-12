import discord
import os
from dotenv import load_dotenv


load_dotenv()

TOKEN = os.getenv('TOKEN')
client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
	
    if message.content.startswith('$spam '):
        user_msg = message.content.split()
        spam_user = user_msg[1]

        spam_count = int(user_msg[2])
        maximum_spam = 20
        num = min(maximum_spam, spam_count)
        
        for i in range(num):
            await message.channel.send(spam_user)
             
client.run(TOKEN)
