# isort: skip_file
# Python Imports
import os
from datetime import datetime as dt

# Thrid Parties Imports
import discord
from discord import app_commands
from dotenv import load_dotenv

# Local Imports
from app.crud.notification import notification_crud
from app.crud.numbers import numbers_crud
from app.schemas.register import RegisterSchema

load_dotenv()

TOKEN = os.environ.get("DISCORD_TOKEN")
GUILD_ID = os.environ.get("DISCORD_GUILD_ID")
LOGS_CHANNEL = os.environ.get("DISCORD_LOGS_CHANNEL_ID")


class DiscordClient(discord.Client):
    guild_id: int

    def __init__(self, guild_id: int):
        super().__init__(intents=discord.Intents.default())
        self.guild_id = guild_id
        self.synced = False

    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced:
            await tree.sync(guild=discord.Object(id=self.guild_id))
            self.synced = True
        print(f"We have logged in as {self.user}.")


client = DiscordClient(guild_id=GUILD_ID)


async def send_logs(
    command: str, user: str, message: str, logs_channel: str = LOGS_CHANNEL
):
    channel = client.get_channel(int(logs_channel))
    embed = discord.Embed(
        title="Logs",
        description=f"Logged at : {dt.utcnow().strftime('%Y-%m-%d %H:%M:%S')} UTC",
        color=discord.Colour.green(),
    )
    embed.add_field(name="Command", value=f"`{command}`", inline=True)
    embed.add_field(name="User", value=f"`{user}`", inline=True)
    embed.add_field(name="Result", value=f"`{message}`", inline=False)
    await channel.send(embed=embed)


tree = app_commands.CommandTree(client)


@tree.command(
    guild=discord.Object(id=GUILD_ID),
    name="register",
    description="Register a new number",
)
async def register(interaction: discord.Interaction, number: str):

    await interaction.response.defer(ephemeral=True)
    try:
        new_number = RegisterSchema(
            number=number, created_by=interaction.user.name
        )
    except Exception as err:
        msg_error = f"❌ERROR❌\n{err}"
        await interaction.followup.send(msg_error)
        await send_logs(
            interaction.command.name, interaction.user.name, msg_error
        )
        return

    result = numbers_crud.register_number(new_number=new_number)
    await interaction.followup.send(content=f"{result}")
    await send_logs(interaction.command.name, interaction.user.name, result)
    return


@tree.command(
    guild=discord.Object(id=GUILD_ID),
    name="unregister",
    description="Unregister an existing number",
)
async def unregister(interaction: discord.Interaction, number: str):
    await interaction.response.defer(ephemeral=True)
    try:
        existing_number = RegisterSchema(
            number=number, created_by=interaction.user.name
        )
    except Exception as err:
        msg_error = f"❌ERROR❌\n{err}"
        await interaction.followup.send(msg_error)
        await send_logs(
            interaction.command.name, interaction.user.name, msg_error
        )

    result = numbers_crud.unregister_number(existing_number=existing_number)
    await interaction.followup.send(content=f"{result}")
    await send_logs(interaction.command.name, interaction.user.name, result)
    return


@tree.command(
    guild=discord.Object(id=GUILD_ID),
    name="send_sms",
    description="Send sms message to all active numbers",
)
async def send_sms(interaction: discord.Interaction, message: str):
    await interaction.response.defer(ephemeral=True)
    result = notification_crud.send_sms(
        body=message, user=interaction.user.name
    )
    await interaction.followup.send(f"{result}")
    await send_logs(interaction.command.name, interaction.user.name, result)
    return


@tree.command(
    guild=discord.Object(id=GUILD_ID),
    name="clean_channel",
    description="clean all chats",
)
async def clean_channel(interaction: discord.Interaction):
    await interaction.response.defer(ephemeral=True)
    await interaction.channel.purge(limit=50)
    await interaction.followup.send(
        f"Channel cleaned by: `{interaction.user.name}`"
    )
    await send_logs(
        interaction.command.name,
        interaction.user.name,
        (
            f"User:`{interaction.user.name}` have cleaned the"
            f"messages from channel {interaction.channel.name}"
        ),
    )
    return


client.run(TOKEN)
