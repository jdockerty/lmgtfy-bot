import discord
import os

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):

    # Stops the bot replying to itself.
    if message.author == client.user:
        return

    # Send message to user if true.
    if check_message(message.content):
        initial_string = "https://lmgtfy.com/?q="
        user_message = message.content.replace(" ", "+")
        await message.channel.send(f"{message.author.mention} \nHere you go: {initial_string}{user_message}")

def check_message(message):
    sent_msg = message.lower()
    if sent_msg.startswith("how do i"):
        return True
    else:
        return False

client.run(os.getenv("API_KEY"))