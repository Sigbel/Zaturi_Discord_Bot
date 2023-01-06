import discord

from discord.ext import commands

class CustomHelpCommand(commands.HelpCommand):
    def __init__(self, **kwargs):
        super().__init__()
        self.cmd_prefix = kwargs['command_prefix']

    async def send_bot_help(self, mapping):
        embed = discord.Embed(title="Commands List")
        c = 0
        for cog in mapping:
            if c != 0 and cog != None:
                embed.add_field(name=f"{cog.qualified_name.upper()}:", value=",".join([f"`{command.aliases[0]}`" for command in mapping[cog]]))
            c+=1
        
        embed.set_footer(text=f'To get more info on a command, type {self.cmd_prefix}help <command name>')

        await self.get_destination().send(embed=embed)

    # async def send_cog_help(self, cog):
    #     await self.get_destination().send(f'{cog.qualified_name}: {[command.name for command in cog.get_commands()]}')

    # async def send_group_help(self, group):
    #     await self.get_destination().send(f'{group.name}: {[command.name for index, command in enumerate(group.commands)]}')

    async def send_command_help(self, command):
        embed=discord.Embed(
            description=f'''**{command.aliases[0]}**: {command.short_doc}
            
            Usage:
            `{self.cmd_prefix}{command.aliases[0]} {command.description}`
            
            Aliases:
            `{', '.join(command.aliases)}`
            '''
        )
        embed.set_author(name=f'Help')

        await self.get_destination().send(embed=embed)

class HelpCog(commands.Cog, name="Help"):
    def __init__(self, client):
        self.client = client
        self._original_help_command = client.help_command

        client.help_command = CustomHelpCommand(
            command_prefix = client.command_prefix
        )
        client.help_command.cog = self

    async def cog_unload(self):
        self.client.help_command = self._original_help_command

async def setup(client):
    await client.add_cog(HelpCog(client))