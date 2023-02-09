#                                      ARRANQUE DEL BOT
#------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------

from colorama import init, Fore
init(autoreset=True)
import discord
from discord.ext import commands
bot = commands.Bot(command_prefix=">", intents=discord.Intents.all())


#                                      EVENTOS DEL BOT
#------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------

@bot.event
async def on_ready():
    print(Fore.GREEN + "######################################################################################")
    print(Fore.GREEN + "#                                                                                    #")
    print(Fore.GREEN + "#                              Bienvenido a CryptoCat                                #")
    print(Fore.GREEN + "#                                      - Bot -                                       #")
    print(Fore.GREEN + "#                                                                                    #")
    print(Fore.GREEN + "######################################################################################")
    print(Fore.GREEN + "")
    print(Fore.GREEN + "######################################################################################")
    print(Fore.GREEN + "#                  Este es un bot de chat desarrollado en Python.                    #")
    print(Fore.GREEN + "#                                    - Arsenel -                                     #")   
    print(Fore.GREEN + "######################################################################################")
    print("")
 
    print("")
    print("  User:                Date:      Time Extended:                Command:     Result:       ")
    print("---------------------------------------------------------------------------------------------------")
      

@bot.event
async def on_command_completion(ctx):
    
    print(Fore.GREEN + f"> {ctx.author}   {ctx.message.created_at}         {ctx.command}        Successfully")
    
@bot.event

async def on_command_error(ctx, exception):
    print(Fore.RED + f"> {ctx.author}   {ctx.message.created_at}         {ctx.command}        Unsuccessfully")
    print(Fore.RED + f' ﹂ Se produjo la siguiente excepción durante la ejecución del comando: {exception}')
    

#                                      COMANDOS DEL BOT
#------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------
#Comando Ping-Pong
@bot.command(description=" 🏓 Ni me preguntes viene de serie",brief=">ping")
async def ping(ctx):
    await ctx.send("pong")


#------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------
@bot.command(description=" 📋 Muestra una lista de los comandos disponibles extendida",brief=">comandos")
async def comandos(ctx):
    # Crear una lista de viñetas vacía
    command_list = []
    # Recorrer la lista de comandos del bot
    for command in bot.commands:
        # Añadir una viñeta con el nombre y la descripción del comando
        command_list.append(f"") 
        command_list.append(f"• Nombre de comando: `{command.name}`")
        command_list.append(f"• Descripción:{command.description}")
        command_list.append(f"• Ejemplo:{command.brief}")
        command_list.append(f"")
    # Unir la lista de viñetas en una sola cadena de texto
    command_string = "\n".join(command_list)
    # Enviar la lista de comandos al canal de texto
    await ctx.send(f"Lista de comandos disponibles:\n{command_string}")
    await ctx.send(help)


#------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------
#Comando para limpiar el chat de texto
@bot.command(description=" 🗑️ Permite borrar X cantidad de mensajes de texto",brief=">clear x")
async def clear(ctx, amount: int):
    await ctx.channel.purge(limit=amount+1)
    await ctx.send(f'🗑️ Se han eliminado {amount} mensajes.')


#------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------
#Comando para limpiar el chat de texto
@bot.command(description=" 🗑️ Permite borrar todos los mensajes de texto",brief=">clear_all")
async def clear_all(ctx):
    await ctx.channel.purge(limit=10000000)
    await ctx.send(f'🗑️ Se han eliminado todos los mensajes.')


#------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------
#Comando para desconectar del canal de voz
@bot.command(description=" 📶 Desconecta al bot del canal de voz",brief=">disconect")
async def disconect(ctx):
    vc = bot.voice_clients[0]
    #vc.stop()
    #vc.clear()
    await vc.disconnect()


#------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------
@bot.command(description=" ♻️ Para y borra el buffer de canciones",brief=">stop")
async def stop(ctx):
    # Obtener el cliente de voz del bot
    vc = bot.voice_clients[0]

    # Detener la reproducción y vaciar el buffer de canciones
    vc.stop()

    # Enviar un mensaje al usuario confirmando que se ha vaciado el buffer
    await ctx.send("♻️ Buffer de canciones vaciado.")


#------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------
@bot.command(description=" ⏸ Pausa la canción en marcha",brief=">pause")
async def pause(ctx):
    # Obtener el cliente de voz del bot
    vc = bot.voice_clients[0]

    # Detener la reproducción y vaciar el buffer de canciones
    vc.pause()

    # Enviar un mensaje al usuario confirmando que se ha parado la canción
    await ctx.send("⏸ Se ha parado la canción.")


#------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------
@bot.command(description=" ⏯️ Continua la canción en marcha",brief=">resume")
async def resume(ctx):
    # Obtener el cliente de voz del bot
    vc = bot.voice_clients[0]

    # Reanudar la reproducción de la canción pausada
    vc.resume()
    # Enviar un mensaje al usuario confirmando que se ha parado la canción
    await ctx.send("⏯️ Continua la canción.")
#------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------
@bot.command(description=" ⏭️ Salta a la canción en marcha",brief=">skip")
async def skip(ctx):
    # Obtener el cliente de voz del bot
    vc = bot.voice_clients[0]

    # Salta a la siguiente canción del buffer
    vc.skip()
    # Enviar un mensaje al usuario confirmando que se ha parado la canción
    await ctx.send("⏭️ Salta a la siguiente canción.")

#------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------
#Comando reproducir Night Lovell
@bot.command(description=" 💿  Reproduce la canción de Night Lovell",brief=">nl")
async def nl(ctx):
    # Obtener todos los clientes de voz del bot
    voice_clients = bot.voice_clients

    # Comprobar si el bot ya está conectado al canal
    already_connected = False
    for client in voice_clients:
        if client.channel == ctx.message.author.voice.channel:
            already_connected = True
            break
    
    if already_connected:
        # El bot ya está conectado al canal
        vc = bot.voice_clients[0]
        vc.play(discord.FFmpegPCMAudio("shillin - Night Lovell - Polozhenie  Situation - slowed down.mp3"))
        await ctx.send("💿  Reproduciendo ahora mismo : shillin - Night Lovell - Polozhenie  Situation")
    else:
        # El bot no está conectado al canal
        # Puedes conectarte aquí
        channel = ctx.message.author.voice.channel
        vc = await channel.connect()
        vc = bot.voice_clients[0]
        vc.play(discord.FFmpegPCMAudio("shillin - Night Lovell - Polozhenie  Situation - slowed down.mp3"))
        await ctx.send("💿  Reproduciendo ahora mismo : shillin - Night Lovell - Polozhenie  Situation")

 
#------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------
#Comando de reproducir DIOR
@bot.command(description=" 💿  Reproduce la canción de dior",brief=">dior")
async def dior(ctx):
    # Obtener todos los clientes de voz del bot
    voice_clients = bot.voice_clients

    # Comprobar si el bot ya está conectado al canal
    already_connected = False
    for client in voice_clients:
        if client.channel == ctx.message.author.voice.channel:
            already_connected = True
            break
    
    if already_connected:
        # El bot ya está conectado al canal
        vc = bot.voice_clients[0]
        vc.play(discord.FFmpegPCMAudio("Dior-положение (Peaky Blinders).mp3"))
        await ctx.send("💿  Reproduciendo ahora mismo : Dior-положение")
    else:
        # El bot no está conectado al canal
        # Puedes conectarte aquí
        channel = ctx.message.author.voice.channel
        vc = await channel.connect()
        vc = bot.voice_clients[0]
        vc.play(discord.FFmpegPCMAudio("Dior-положение (Peaky Blinders).mp3"))
        await ctx.send("💿  Reproduciendo ahora mismo : Dior-положение")

#------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------
#Comando de reproducir Rohirrim
@bot.command(description=" 📯 Llama a los caballeros de Rohan a la batalla!",brief=">rohirrim")
async def rohirrim(ctx):
    # Obtener todos los clientes de voz del bot
    voice_clients = bot.voice_clients

    # Comprobar si el bot ya está conectado al canal
    already_connected = False
    for client in voice_clients:
        if client.channel == ctx.message.author.voice.channel:
            already_connected = True
            break
    
    if already_connected:
        # El bot ya está conectado al canal
        vc = bot.voice_clients[0]
        vc.play(discord.FFmpegPCMAudio("The Ride of the Rohirrim.mp3"))
        await ctx.send("“🛡️⚔️ ¡Llegada es la hora! ¡Jinetes de Rohan, os ata un juramento! ¡Dadle ahora cumplimiento! ¡Por el Rey, y la tierra!⚔️🛡️”")
    else:
        # El bot no está conectado al canal
        # Puedes conectarte aquí
        channel = ctx.message.author.voice.channel
        vc = await channel.connect()
        vc = bot.voice_clients[0]
        vc.play(discord.FFmpegPCMAudio("The Ride of the Rohirrim.mp3"))
        await ctx.send("“🛡️⚔️ ¡Llegada es la hora! ¡Jinetes de Rohan, os ata un juramento! ¡Dadle ahora cumplimiento! ¡Por el Rey, y la tierra!⚔️🛡️”")



#------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------
#Comando de reproducir DIOR
@bot.command(description=" 🐱 Llama a Crypto Cat para acariciarle",brief=">pspsps")
async def pspsps(ctx):
    # Obtener todos los clientes de voz del bot
    voice_clients = bot.voice_clients

    # Comprobar si el bot ya está conectado al canal
    already_connected = False
    for client in voice_clients:
        if client.channel == ctx.message.author.voice.channel:
            already_connected = True
            break
    
    if already_connected:
        # El bot ya está conectado al canal
        vc = bot.voice_clients[0]
        vc.play(discord.FFmpegPCMAudio("Cat Prr.mp3"))
        await ctx.send("🐱 Prr prr....prr prr 🐱")
        await ctx.send("https://1.bp.blogspot.com/-sNXXO6Mp_P4/WHo70F6kijI/AAAAAAAAtac/MJtB1N4q1oAxgfdwKOV8S6BrQv6dmbEagCLcB/s1600/ronroneo%2Bgif.gif")
    else:
        # El bot no está conectado al canal
        # Puedes conectarte aquí
        channel = ctx.message.author.voice.channel
        vc = await channel.connect()
        vc = bot.voice_clients[0]
        vc.play(discord.FFmpegPCMAudio("Cat Prr.mp3"))
        await ctx.send("🐱 Prr prr....prr prr 🐱")
        await ctx.send("https://1.bp.blogspot.com/-sNXXO6Mp_P4/WHo70F6kijI/AAAAAAAAtac/MJtB1N4q1oAxgfdwKOV8S6BrQv6dmbEagCLcB/s1600/ronroneo%2Bgif.gif")


#------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------
#Comando de reproducir Rick-Rolled
@bot.command(description=" 🆙 Accede a los comandos que aún se encuentran en su versión Alpha",brief=">upgrade_commands")
async def upgrade_commands(ctx):
    # Obtener todos los clientes de voz del bot
    voice_clients = bot.voice_clients

    # Comprobar si el bot ya está conectado al canal
    already_connected = False
    for client in voice_clients:
        if client.channel == ctx.message.author.voice.channel:
            already_connected = True
            break
    
    if already_connected:
        # El bot ya está conectado al canal
        vc = bot.voice_clients[0]
        vc.play(discord.FFmpegPCMAudio("Rick Astley - Never Gonna Give You Up (video oficial)  Español.mp3"))
        await ctx.send("🆙 Ni te rayes que ya tienes acceso a todos los comandos...jajaja")
        await ctx.send("https://j.gifs.com/rRkznp.gif")
    else:
        # El bot no está conectado al canal
        # Puedes conectarte aquí
        channel = ctx.message.author.voice.channel
        vc = await channel.connect()
        vc = bot.voice_clients[0]
        vc.play(discord.FFmpegPCMAudio("Rick Astley - Never Gonna Give You Up (video oficial)  Español.mp3"))
        await ctx.send("🆙 Ni te rayes que ya tienes acceso a todos los comandos...jajaja")
        await ctx.send("https://j.gifs.com/rRkznp.gif")

#Ejecución de los comandos mediante el TOKEN del BOT
bot.run("MTA1NTkwMzk3MDY2Njc0MTg3MQ.GSLPa_.6Rs6m__gQOEfDP4GevRoMyEukl7HpzqbIhKXOs")