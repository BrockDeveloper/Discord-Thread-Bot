import discord
import requests

BOT_TOKEN = ""
BOT_CMD = "!new"


# create a thread: see https://discord.com/developers/docs/topics/threads
async def create_thread(self,name,minutes,message):
    token = 'Bot ' + self._state.http.token
    url = f"https://discord.com/api/v9/channels/{self.id}/messages/{message.id}/threads"

    headers = {
        "authorization" : token,
        "content-type" : "application/json"
    }
    data = {
        "name" : name,
        "type" : 11,
        "auto_archive_duration" : minutes
    }
 
    return requests.post(url,headers=headers,json=data).json()
 

# event on new discord message
@Bot.event
async def on_message(ctx):
    if "!ask" in ctx.content:
        name = ctx.content.replace("!ask ", "")
        name = name[:32]

        f = await ctx.channel.create_thread(name=name, minutes=1440, message=ctx)


discord.TextChannel.create_thread = create_thread
Bot = discord.Client()
Bot.run(BOT_TOKEN)