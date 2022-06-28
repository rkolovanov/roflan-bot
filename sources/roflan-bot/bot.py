import discord


class BotClient(discord.Client):
    async def on_ready(self):
        print(f"Logged on as '{self.user}'.")

    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content == 'roflan':
            await message.channel.send('<:roflanYliba:701217539044278302>')
