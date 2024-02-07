import discord
from discord.ext import commands
from config import BOT_TOKEN, NOTIFY_CHANNEL_ID, TARGET_BOT_ID, NOTIFY_USER_ID, BOT_GUILD

intents = discord.Intents.default()
intents.presences = True
intents.members = True
client = commands.Bot(command_prefix='!', intents=intents)


@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

    bot_status = client.get_guild(BOT_GUILD).get_member(TARGET_BOT_ID)
    channel = client.get_channel(NOTIFY_CHANNEL_ID)
    status_message = ""

    if bot_status.status == discord.Status.online:
        status_message = "# <:positive:1203089362833768468> Bot up and running!"
        await client.change_presence(activity=discord.Game(name="Online"), status=discord.Status.online)

    if bot_status.status == discord.Status.offline:
        status_message = f"# <:negative:1203089360644476938> <@{NOTIFY_USER_ID}> Bot is offline."
        await client.change_presence(activity=discord.Game(name="Offline"), status=discord.Status.dnd)

    if bot_status.status != discord.Status.online and bot_status.status != discord.Status.offline:
        await client.change_presence(activity=discord.Game(name="Startup"), status=discord.Status.idle)


    if status_message != "":
        channel = client.get_channel(NOTIFY_CHANNEL_ID)
        # Update the bot's activity
        # Send a message to the channel
        message = await channel.send(status_message)
  
        if channel.type == discord.ChannelType.news:
            await message.publish()
            print("Message published in announcement channel.")
        else:
            print("Message sent to channel.")

    

@client.event
async def on_presence_update(before, after):
    if after.id == TARGET_BOT_ID:
        channel = client.get_channel(NOTIFY_CHANNEL_ID)
        if not channel:
            print(f"Channel with ID {NOTIFY_CHANNEL_ID} not found.")
            return
        
        if before.status == after.status: 
            # print("Status did not change.")
            return

        if after.status == discord.Status.online:
            status_message = "# <:positive:1203089362833768468> Bot up and running!"
            await client.change_presence(activity=discord.Game(name="Online"), status=discord.Status.online)

        if after.status == discord.Status.offline:
            status_message = f"# <:negative:1203089360644476938> <@{NOTIFY_USER_ID}> Bot is offline."
            await client.change_presence(activity=discord.Game(name="Offline"), status=discord.Status.dnd)

        # Send a message to the channel
        message = await channel.send(status_message)
        
        if channel.type == discord.ChannelType.news:
            await message.publish()
            print("Message published in announcement channel.")
        else:
            print("Message sent to channel.")


client.run(BOT_TOKEN)
