# -*- coding: utf-8 -*-
import asyncio
import json
import discord
import random

with open('monika.json', 'r') as f:
    monikablah = json.load(f)

monikasick = ['{0.author.mention}...','You completely, truly make me sick.']

class Blah:
    def __init__(self, bot):
        self.bot = bot
        self.blah_tasks = {}

    def get_blah_task(self, message):
        task = self.blah_tasks.get(message.channel.id)
        return task

    async def create_blah(self, message):
        task = self.get_blah_task(message)
        if task is None:
            task = self.bot.loop.create_task(self.blahblah(message,random.choice(monikablah)))
            self.blah_tasks[message.channel.id] = task

    async def stop_blah(self, message):
        task = self.get_blah_task(message)
        try:
            task.cancel()
            del self.blah_tasks[message.channel.id]
        except:
            pass
        task = self.bot.loop.create_task(self.blahblah(message,monikasick))
        self.blah_tasks[message.channel.id] = task

    async def blahblah(self, message, monikachat):
        for monikasay in monikachat:
            await self.bot.send_typing(message.channel)
            await asyncio.sleep(5)
            await self.bot.send_message(message.channel, monikasay.format(message))
        del self.blah_tasks[message.channel.id]

bot = discord.Client()
blah = Blah(bot)





@bot.event
async def on_ready():
    print('Logged in as:\n{0} (ID: {0.id})'.format(bot.user))
    await bot.change_presence(game=discord.Game(name='Doki Doki Literature Club',type=0))
    
@bot.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == bot.user:
        return

    if message.content.startswith(bot.user.mention):
        if 'shut up' in message.content:
            await blah.stop_blah(message)
            return
        await blah.create_blah(message)

bot.run(BOT_TOKEN)
