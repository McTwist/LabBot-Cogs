"""discord red-bot jail"""
from redbot.core import commands, Config, checks
import discord
import random
import string


def randomword(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))


class JailCog(commands.Cog):
    """Jail Cog"""

    def __init__(self, bot):
        self.bot = bot
        self.settings = Config.get_conf(self, identifier=1249812384)

        default_guild_settings = {
            "jail": None,
            "count": 0,
            "history": []
        }

        self.settings.register_guild(**default_guild_settings)

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        if not isinstance(message.guild, discord.Guild):
            # The user has DM'd us. Ignore.
            return

        # TODO Check if message is in jail channel
        # TODO If yes, add to settings[history]
        pass

    @commands.Cog.listener()
    async def on_message_edit(
        self,
        before: discord.Message,
        after: discord.Message
    ):
        if not isinstance(before.guild, discord.Guild):
            # The user has DM'd us. Ignore.
            return

        # TODO Check if message is in jail channel
        # TODO If yes, add change to settings[history]
        pass

    @commands.command(name="jail")
    @commands.guild_only()
    @checks.mod()
    async def jail(
        self,
        ctx: commands.Context,
        user: discord.Member,
        *,
        time: int = None
    ):
        """Jail a user until they are bailed or for a set time

        Example:
        - `[p]jail <user>`
        - `[p]jail <user> <time in minutes>`
        """
        # TODO Generate a 4 character string for uniqueness
        uuid = randomword(4)

        # TODO Get category channel object
        jail_area_id = await self.settings.guild(ctx.guild).jail()
        if jail_area_id is None:
            ctx.send("Jail is not configured.")
            return

        jail_area = ctx.guild.get_channel(jail_area_id)
        if jail_area is None:
            ctx.send("Configured jail could not be found.")
            return

        # TODO Create a channel inside the category channel

        # TODO Create a role with the 4 char string
        # TODO Add special config to role
        # TODO Apply role to user
        # TODO Create record in settings[history] with the 4 chars
        pass

    @commands.group("jails")
    @checks.mod()
    @commands.guild_only()
    async def _jails(
        self,
        ctx: commands.Context
    ):
        pass

    @_jails.command(name="enable")
    async def jails_enable(
        self,
        ctx: commands.Context,
        channel: discord.CategoryChannel
    ):
        """Enable usage of jails and set their parent category

        Example:
        - `[p]jails enable <category channel>`
        """
        await self.settings.guild(ctx.guild).jail.set(channel.id)
        await ctx.send(f"Set jail category to {channel.name}")

    @_jails.command(name="status")
    async def jails_status(
        self,
        ctx: commands.Context,
        channel: discord.CategoryChannel
    ):
        """Show status of the jails

        Example:
        - `[p]jails status`
        """
        # Get values for embed
        count = await self.settings.guild(ctx.guild).count()

        # Create embed
        data = discord.Embed(colour=(await ctx.embed_colour()))
        data.add_field(name="Jailed", value=f"{count} users")

        # Send embed
        try:
            await ctx.send(embed=data)
        except discord.Forbidden:
            await ctx.send("I need the `Embed links` permission to " +
                           "send a purge status.")

    @commands.command(name="bail")
    @commands.guild_only()
    @checks.mod()
    async def bail(
        self,
        ctx: commands.Context,
        user: discord.Member
    ):
        """Bail a user out of jail.
        The bot will remove a user's jailed role but leave the
        jail channel in tact.

        Example:
        - `[p]bail <user>`
        """
        # TODO Get the unique code from user's role
        # TODO Remove role from user
        # TODO Delete generated role
        # TODO Delete generated channel for user
        # TODO Log in settings[history] of deletion
        pass