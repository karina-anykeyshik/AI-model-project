import discord
from discord.ext import commands
from setting import TOKEN
from model import get_class


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
async def photo(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            photo_name = attachment.filename
            await attachment.save(f'images/{photo_name}')
            msg = await ctx.send('Ожидайте')
            name, score = get_class(model_path='cl_model/keras_model.h5', labels_path='cl_model/labels.txt', image_path=f'images/{photo_name}')
            await msg.delete()
            await ctx.send(f'С вероятностью {score}% на фото {name}')
    else:
        await ctx.send('Ты забыл загрузить картинку ;c')


bot.run(TOKEN)
