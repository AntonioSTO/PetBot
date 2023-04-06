import discord
from discord.ext import commands

intents = discord.Intents.all()
intents.members = True

bot = commands.Bot(command_prefix='!', case_insensitive = True, intents=intents)

filaMonitoria = []


@bot.event
async def on_ready():
    print(f'{bot.user.name} está pronto para ser utilizado!')
    
@bot.event
async def on_message(message):
    print(message.content)
    await bot.process_commands(message)

@bot.event
async def on_member_join(member):
    welcome_channel = bot.get_channel(1091452635728576676)
    regras = bot.get_channel(1091452635728576672)
    mensagem = await welcome_channel.send(f"Bem vindo {member.mention}!\nLeia as regras em {regras.mention} ;)")

    await asyncio.sleep(20)
    await mensagem.delete()

@bot.command()
async def monitoria(ctx):
    if ctx.author.id in filaMonitoria:
        await ctx.send(f'{ctx.author.name}, você já está na fila de monitoria! Ka-chow!!!')
    else:
        filaMonitoria.append(ctx.author.id)
        await ctx.send(f'{ctx.author.name}, você foi adicionado à fila de monitoria! Ka-chow!!!')
        await atualizarFila(ctx)
        
@bot.command()
async def fila(ctx):
    await atualizarFila(ctx)

@bot.command()
async def sairfila(ctx):
    if ctx.author.id in filaMonitoria:
        filaMonitoria.remove(ctx.author.id)
        await ctx.send(f'{ctx.author.name}, você foi removido da fila de monitoria! Ka-chow!!!')
        await atualizarFila(ctx)
    else:
        await ctx.send(f'{ctx.author.name}, você não está na fila de monitoria! Ka-chow!!!')

async def atualizarFila(ctx):
    filaString = 'Fila de monitoria:\n'
    if len(filaMonitoria) == 0:
        filaString += ' Vazia :('
    else:
        for i in range(len(filaMonitoria)):
            user = await bot.fetch_user(filaMonitoria[i])
            filaString += f'- {user.name}\n'
    await ctx.send(filaString)

bot.run('MTA5Mjk2NTYwNDY3NzM5ODU0OA.Gndyjb.36cVtA2KpSRbP8uWdmt5J9gDncVuv0QmC-rdxc')