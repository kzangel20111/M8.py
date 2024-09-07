import discord
from discord.ext import commands
from model import eco

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def check(ctx):
    attachments = ctx.message.attachments
    if attachments:
        for attachment in attachments:
            file_name = attachment.filename
            file_url = attachment.url
            await attachment.save(f'images/{file_name}')
            await ctx.send('Ваша картинка была сохранена')

            eco = eco(f'images/{file_name}')
            await ctx.send(f'На картинки изображено{eco}')

            if eco == 'trash':
                await ctx.send('Это мусор мусор очень опасен для природы пожалуеста не выкидывайте мусор куда попало')

            elif eco == 'paper':
                await ctx.send('Это бумага бумага вредит природе после использования бумаги пожалуйста Не выкидывай его куда попало')

            elif eco == 'plastic':
                await ctx.send('пластик тоже опасен для природы например разлагается пластик примерно 450-500 лет. В течение этого времени пластик выделяет много токсичных элементов, которые отравляют почву, воду и воздух, попадают в пищу животных, птиц и рыб, убивая их, наносят непоправимый ущерб природе')

            elif eco == 'metal':
                await ctx.send('Металл тоже опасен для природы в нее входет токсичные елементы которые вредят жывотным и даже людям')
    
    
    else:
        await ctx.send("Вы забыли загрузить картинку")
    


bot.run("MTIyNzIwNzc1ODc5ODEyNzIwNQ.GnHsj_.nwGUIvn8xOrxlT9zvllnrA7OSE9-UKbq_dQBSI")