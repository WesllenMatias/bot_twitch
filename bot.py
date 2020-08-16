from twitchio.ext import commands
import config
#import talk
from time import sleep
import random

#oauth:v59boop5cjueuckcv0jnpnok678s2g
bot = commands.Bot(
    irc_token=config.TMI_TOKEN,
    client_id=config.CLIENT_ID,
    nick=config.BOT_NICK,
    prefix=config.BOT_PREFIX,
    initial_channels=[config.CHANNEL]
)

@bot.event
async def event_ready():
    print(f'Rodando {config.BOT_NICK}')
    ws = bot._ws
    await ws.send_privmsg(config.CHANNEL, f"/me e ae? o que ta rolando por aqui?")

@bot.event
async def event_message(ctx):
    #'Runs every time a message is sent in chat.'
    
    # make sure the bot ignores itself and the streamer
    if ctx.author.name.lower() == config.BOT_NICK.lower():
       return
    
    #sleep(30)
    print(ctx.content)
    frases = [
        "GERALLL",
        "Performance Total essa galera aqui!!!",
        "ALFA TANGO ZULU",
        "AGUIA SENTADA!!!",
        "É a galerinha do Gulag",
        "Iiixii só tem mochila!!!",
        "Duds Rei do Gulag",
        "Pedrinhoooo PIROCAAAAA",
        "Vai Tomar Report!!",
        "Reportem esse Newba",
        "Vai chorar?",
        "Esse mid ai ta zuado!",
        "Cadê o A-I-D-S???",
        "Eu ACCCHHHHHHOOOO... que vai dar bosta!",
        "Whiski Mike Mike",
        "Inimigo chegando na AO!!",
        "O Que porra é AO?",
        "Só tem mochila",
        "Dudu ta uma mochila hoje!",
        "Vamo se inscrever no canal que essa merda da trabalho!",
        "XAMAAAAA!!",
        "X1 no Rio!",
        "A Galera da Bala ta Frenetica hoje!",
        "Cadê a galerinha da caixa baixa??",
        "Vai ter sorteio hoje?",
        "TÔ NA LARICA, vou pedir um Burgão!",
        "Cadê o Duds Gourmet??",
        "Freské!",
        "Ai dento",
        "Que hora que começa a sacanagemzinha?",
        "Cadê o bola?",
        "Parece que a pipoca virou sabão...",
        "Um Oferecimento de PEDRINHO GAMES!!!",
        "O dudu já sabe marcar??",
        "Ta saindo som ai pra vcs?",
        "Vê se não tem que matar uma desgraça dessa!"
    ]
    #print(len(frases))
    aleatorio = random.randrange(0,len(frases))
    fala = frases[aleatorio]
    #sleep(60)
    await ctx.channel.send(fala)

@bot.command(name='teste')
async def test(ctx):
    print(ctx)
    await ctx.send(f'Test Pasado! Gracias {ctx.author.name}')
    


if __name__ == "__main__":
    bot.run()