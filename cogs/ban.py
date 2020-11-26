import discord

from discord.ext import commands


class Ban(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(ban_members = True)
    async def ban(self, ctx, user: discord.Member = None, *, reason = None):

        if user is None:
            await ctx.message.delete()
            await ctx.channel.send(f"Sorry, You've to specify user to ban", delete_after = 5)
        else:
            if reason is not None:
                await ctx.message.delete()
                await ctx.channel.send(f'Banned {user.mention}, for: {reason}', delete_after = 5)
                await user.kick(reason = reason)
            else:
                await ctx.message.delete()
                await ctx.channel.send(f'Banned {user.mention}, for: No reason', delete_after = 5)
                await user.ban(reason = 'No reason given')




def setup(client):
    client.add_cog(Ban(client))