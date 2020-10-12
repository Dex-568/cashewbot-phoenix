from discord.ext import commands
import json


class StatH(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        with open('db/stats.json', 'r+') as f:
            data = json.load(f)
            data['messages'] += 1
            f.seek(0)
            json.dump(data, f)

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        with open('db/stats.json', 'r+') as f:
            data = json.load(f)
            data['guilds'] += 1
            f.seek(0)
            json.dump(data, f)

    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        with open('db/stats.json', 'r+')as f:
            data = json.load(f)
            data['guilds'] -= 1
            f.seek(0)
            json.dump(data, f)


def setup(bot):
    bot.add_cog(StatH(bot))
