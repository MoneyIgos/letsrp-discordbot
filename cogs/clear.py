import discord

from discord.ext import commands


class Clear(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def clear(self, ctx, amount=0):
        await ctx.message.delete()

        if amount == 0:
            await ctx.channel.send("Musisz podać liczbę wiadomości do usunięcia", delete_after = 5)
        else:
            await ctx.channel.purge(limit = amount)
            await ctx.channel.send(f'Usunięto {amount} wiadomości', delete_after = 5)


def setup(client):
    client.add_cog(Clear(client))
