import discord
import pycoingecko
import Paginator

from utils.coin_graph import coin_plot, coin_history, coin_range
from discord.ext import commands
from math import ceil

class Market(commands.Cog):
    def __init__(self, client):
        super().__init__()
        self.client=client
        self.cmd_pfx=client.command_prefix
        self.cg=pycoingecko.CoinGeckoAPI()

    @commands.command(aliases=['price','p'], description='<coin id> <vs_coin>')
    async def get_coin_price(self, ctx, *args):
        """get the current price of a coin"""
        if len(args) != 0:
            temp=' '.join(args[0:-1])

            try:
                _price=self.cg.get_price(ids=temp, vs_currencies=args[-1])
                embed=discord.Embed()
                embed.set_author(name=" ".join(args[0:-1]).upper(), icon_url=self.client.user.avatar)
                embed.add_field(name="Simple Price", value=f"{str(args[-1]).upper()}: {_price[temp][args[-1]]}")

                await ctx.send(embed=embed)

            except:
                embed=discord.Embed(
                    description=f"Invalid search. Try again."
                )
                embed.set_author(name="Error", icon_url=self.client.user.avatar)

                await ctx.send(embed=embed)
        else:
            embed=discord.Embed(
                description=f'''**Usage**: {self.cmd_pfx}price | p <coin id> <vs_coin>
                **Example**: {self.cmd_pfx}price | p bitcoin usd'''
            )
            embed.set_author(name="Help", icon_url=self.client.user.avatar)

            await ctx.send(embed=embed)

    @commands.command(aliases=['market', 'mkt'], description='<coin id> <vs_coin>')
    async def get_coin_market(self, ctx, *args): # Revise chart
        """get the current market info for a coin"""
        if len(args) != 0:
            
            try:
                _coin_info = self.cg.get_coins_markets(vs_currency=str(args[-1]), ids=' '.join(args[0:-1]))
                embed=discord.Embed(title=_coin_info[0]['name'])
                
                embed.set_author(name=self.client.user.name, icon_url=self.client.user.avatar)
                embed.set_thumbnail(url=_coin_info[0]['image'])
                embed.add_field(name="Current Price", value=_coin_info[0]['current_price'], inline=True)
                embed.add_field(name="Circulating Supply", value=_coin_info[0]['circulating_supply'], inline=True)
                embed.add_field(name="Market Cap", value=_coin_info[0]['market_cap'], inline=True)

                embed.add_field(name="24h-High", value=_coin_info[0]['high_24h'], inline=True)
                embed.add_field(name="24h-Low", value=_coin_info[0]['low_24h'], inline=True)
                embed.add_field(name="Price Change 24h", value=_coin_info[0]['price_change_24h'], inline=True)

                embed.add_field(name="All Time High", value=_coin_info[0]['ath'], inline=True)
                embed.add_field(name="ATH Percent Change", value=_coin_info[0]['ath_change_percentage'], inline=True)
                embed.add_field(name="All Time Low", value=_coin_info[0]['atl'], inline=True)

                # Plot
                coin_plot(''.join(args[0:-1]), vs_currency=args[-1])
                file = discord.File("images/fig1.png", filename='image.png')
                embed.set_image(url="attachment://image.png")

                embed.set_footer(text="Powered by Zaturi Discord Bot")

                await ctx.send(embed=embed, file=file)

            except:
                embed=discord.Embed(
                    description=f"Invalid search. Try again."
                )
                embed.set_author(name="Error", icon_url=self.client.user.avatar)

                await ctx.send(embed=embed)

        else: 
            embed=discord.Embed(
                description=f'''**Usage**: {self.cmd_pfx}market | mkt <coin id> <vs_coin>
                **Example**: {self.cmd_pfx}market | mkt bitcoin usd'''
            )
            embed.set_author(name="Help", icon_url=self.client.user.avatar)

            await ctx.send(embed=embed)

        
    @commands.command(aliases=['history'], description='<coin id> <date>') 
    async def get_coin_history(self, ctx, *args):
        """get the price of a especific date for the coin"""
        if  len(args) != 0:

            try:
                _coin_info = self.cg.get_coin_history_by_id(id=" ".join(args[0:-1]), date=args[-1])

                embed=discord.Embed(title=f"{_coin_info['name']} - Historical Prices")
                embed.set_thumbnail(url=_coin_info['image']['small'])

                embed.add_field(name='USD', value=f"{_coin_info['market_data']['current_price']['usd']:.4f}", inline=True)
                embed.add_field(name='Market Cap', value=f"{_coin_info['market_data']['market_cap']['usd']:.4f}", inline=True)
                embed.add_field(name='Total Vol', value=f"{_coin_info['market_data']['total_volume']['usd']:.4f}", inline=True)

                # Other coins treatment
                _coin_dict = _coin_info['market_data']['current_price']
                values=[f'{coin.upper()} : {_coin_dict[coin]:.4f}' for coin in _coin_dict]

                embed.add_field(name='Other Vs Currencies', value='\n'.join(values))

                await ctx.send(embed=embed)

            except:
                embed=discord.Embed(
                    description=f"Invalid search. Try again."
                )
                embed.set_author(name="Error", icon_url=self.client.user.avatar)

                await ctx.send(embed=embed)

        else: 
            embed=discord.Embed(
                description=f'''**Usage**: {self.cmd_pfx}history <coin id> <date>
                **Example**: {self.cmd_pfx}history bitcoin 16-10-2015'''
            )
            embed.set_author(name="Help", icon_url=self.client.user.avatar)

            await ctx.send(embed=embed)

    @commands.command(aliases=['mchart'], description='<coin id> <vs_coin> <days>') 
    async def get_coin_market_chart(self, ctx, *args):
        """get the historical market data"""
        if len(args) != 0:
            
            try:
                coin_history(' '.join(args[0:-2]), args=args[1:])
                embed=discord.Embed(title="Coin History")
        
                file = discord.File("images/fig10.png", filename='image10.png')
                embed.set_image(url="attachment://image10.png")

                await ctx.send(embed=embed, file=file)

            except:
                embed=discord.Embed(
                    description=f"Invalid search. Try again."
                )
                embed.set_author(name="Error", icon_url=self.client.user.avatar)

                await ctx.send(embed=embed)
        else:
            embed=discord.Embed(
                description=f'''**Usage**: {self.cmd_pfx}mchart <coin id> <vs_coin> <days>
                **Example**: {self.cmd_pfx}mchart bitcoin usd 14'''
            )
            embed.set_author(name="Help", icon_url=self.client.user.avatar)

            await ctx.send(embed=embed)

    @commands.command(aliases=['mrange'], description='<coin id> <vs_coin> <start_day> <end_day>')
    async def get_coin_market_chart_range(self, ctx, *args):
        """get the historical market data for an especific date range"""
        if len(args) != 0:
            
            try:
                coin_range(id=" ".join(args[0:-3]), vs_currency=args[-3], s_day=args[-2], e_day=args[-1])
                embed=discord.Embed(title="Coin History in Range")
        
                file = discord.File("images/fig20.png", filename='image20.png')
                embed.set_image(url="attachment://image20.png")

                await ctx.send(embed=embed, file=file)

            except:
                embed=discord.Embed(
                    description=f"Invalid search. Try again."
                )
                embed.set_author(name="Error", icon_url=self.client.user.avatar)

                await ctx.send(embed=embed)
        else:             
            embed=discord.Embed(
                description=f'''**Usage**: {self.cmd_pfx}mrange <coin id> <vs_coin> <start_day> <end_day>
                **Example**: {self.cmd_pfx}mrange bitcoin usd 14-10-2020 15-11-2020'''
            )
            embed.set_author(name="Help", icon_url=self.client.user.avatar)

            await ctx.send(embed=embed)

    @commands.command(aliases=['search', 's'], description='<coin id>')
    async def search_coin(self, ctx, *args):
        """search for coins from the given query"""
        if len(args) != 0:
            try:
                _coin_info = self.cg.search(query=" ".join(args))
                temp_l = [] 
                embeds = []

                for i in _coin_info['coins']:
                    temp_l.append(f"""```ID: {i['id']}\nNAME: {i['name']}\nSYMBOL: {i['symbol']}\nRANK (Market Cap): {i['market_cap_rank']}```""")

                y = 5
                for i in range(ceil(len(_coin_info['coins'])/5)):
                    embed=discord.Embed(title=f"Page {i+1}/{ceil(len(_coin_info['coins'])/5)}")
                    
                    embed.add_field(name=f'Your search for "{" ".join(args)}"', value=' '.join(temp_l[i*5:y]))
                    embed.set_footer(text="Thanks for using Zaturi!")

                    embeds.append(embed)

                    y += 5

                await Paginator.Simple().start(ctx, pages=embeds)

            except:        
                embed=discord.Embed(
                    description=f"Invalid search. Try again."
                )
                embed.set_author(name="Error", icon_url=self.client.user.avatar)

                await ctx.send(embed=embed) 
        else:
            embed=discord.Embed(
                description=f'''**Usage**: {self.cmd_pfx}search | s <coin id> 
                **Example**: {self.cmd_pfx}search | s bitcoin'''
            )
            embed.set_author(name="Help", icon_url=self.client.user.avatar)

            await ctx.send(embed=embed)      


    @commands.command(aliases=['tickers', 't'], description='<coin id>')
    async def get_coin_ticker(self, ctx, *args):
        """get the coin exchanges"""
        if len(args) != 0:
            try:
                _coin_info = self.cg.get_coin_ticker_by_id(id=args[0])
                temp_l = []
                embeds = []

                for num, i in enumerate(_coin_info['tickers']):
                    if i['market']['name'] not in temp_l:
                        temp_l.append(f"```Exchange: {i['market']['name']}\nPair: {i['base']} | {i['target']}\nLink: {i['trade_url']}```")

                y = 10
                for i in range(ceil(len(temp_l)/10)):
                    embed=discord.Embed(title=f"Page {i+1}/{ceil(len(temp_l)/10)}")
                    sorted_temp_l = sorted(temp_l)


                    embed.set_author(name='Coin Exchanges', icon_url=self.client.user.avatar)
                    embed.add_field(name=f'Your search for "{" ".join(args)}"', value=''.join(sorted_temp_l[i*10:y]))
                    embed.set_footer(text="Thanks for using Zaturi!")

                    embeds.append(embed)

                    y += 10

                await Paginator.Simple().start(ctx, pages=embeds)

            except:       
                embed=discord.Embed(
                    description=f"Invalid search. Try again."
                )
                embed.set_author(name="Error", icon_url=self.client.user.avatar)

                await ctx.send(embed=embed) 
        else:
            embed=discord.Embed(
                description=f'''**Usage**: {self.cmd_pfx}tickers | t <coin id>
                **Example**: {self.cmd_pfx}tickers | t bitcoin'''
            )
            embed.set_author(name="Help", icon_url=self.client.user.avatar)

            await ctx.send(embed=embed)

    @commands.command(aliases=['trending'])
    async def get_search_treding(self, ctx):
        """get the top 7 coins (ordered by most popular)"""  
        try:
            _coin_info = self.cg.get_search_trending()
            embed=discord.Embed(title="Top 7 - Most Popular Coins")
            temp_l = []
            
            # Other coins treatment
            for i in _coin_info['coins']:
                for chave, valor in i.items():
                    temp_l.append(f"{valor['score']+1}º: {valor['name']}")

            embed.add_field(name='Ranking', value='\n'.join(temp_l))

            await ctx.send(embed=embed)

        except:
            embed=discord.Embed(
                description=f"Invalid search. Try again."
            )
            embed.set_author(name="Error", icon_url=self.client.user.avatar)

            await ctx.send(embed=embed)    
    
    @commands.command(aliases=['vsc']) 
    async def get_supported_vs_currencies(self, ctx):
        """get the supported vs currencies"""
        try:
            _coin_info = self.cg.get_supported_vs_currencies()
            embed = discord.Embed(title="Supported Vs Currencies", description="(Ordered Alphabetically)")

            _coin_info_s = sorted(_coin_info)
            lenght = len(_coin_info)

            embed.add_field(name=".", value="\n".join(_coin_info_s[0:(lenght//3)+1]))
            embed.add_field(name=".", value="\n".join(_coin_info_s[(lenght//3)+1:((lenght//3)*2)+2]))
            embed.add_field(name=".", value="\n".join(_coin_info_s[((lenght//3)*2)+2:lenght]))

            await ctx.send(embed=embed)
            
        except:
            embed=discord.Embed(
                description=f"Invalid search. Try again."
            )
            embed.set_author(name="Error", icon_url=self.client.user.avatar)

            await ctx.send(embed=embed) 


async def setup(client):
    await client.add_cog(Market(client))