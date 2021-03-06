import discord
import random
import asyncio
import time
import datetime
import sys
import io
import os
import re
import json
import base64

client = discord.Client()

COR = 0x3498DB
VERM = 0xFA0909

@client.event
async def on_ready():
    print("Iniciado com sucesso!")
    while True:
        await client.change_presence(game=discord.Game(name="Trasmitindo amor para 3 servidores, digite y!help se precisar de ajuda ", url="https://www.twitch.tv/maria_uchida", type=1))
        await client.change_presence(game=discord.Game(name="Criando tickets!", url="https://www.twitch.tv/johncostaxv", type=1))
        await asyncio.sleep(300)
        await client.change_presence(game=discord.Game(name="Criado pelo Johnn#0001", url="https://www.twitch.tv/johncostaxv", type=1))
        await asyncio.sleep(300)

@client.event
async def on_message(message):
    if message.content.lower().startswith("!reportar"):
        await client.add_reaction(message, "🔩")
        await asyncio.sleep(1)
        await client.send_message(message.author, "📢 **DENÚNCIA**:\nDeseja reportar um usuário que cometeu uma infração em nosso servidor, {}? Faça a denúncia!\n\nVamos lá!\n📌**Qual o usuário que deseja reportar?**")
        usuário = await client.wait_for_message(author=message.author)
        await client.send_message(message.author, "📌 **Qual motivo da denúncia?**")
        motivo = await client.wait_for_message(author=message.author)
        await client.send_message(message.author, "📌 **Possui alguma prova do ocorrido?**")
        prova = await client.wait_for_message(author=message.author)
        await client.send_message(message.author, "📌 **Denúncia enviada com sucesso!**")

        canal = client.get_channel("498300664607408129")
        embed = discord.Embed(
            title="",
            color=COR,
            description="Denúncia recebida. \nEnviada por: {}".format(message.author.mention)
        )
        embed.set_author(name='Denúncia', icon_url='https://images-ext-1.discordapp.net/external/BCKxPNzZzEVfkbIublv7_3wG2016jTwGk3onTemVRnM/%3Fv%3D1/https/cdn.discordapp.com/emojis/450112878108999680.gif')
        embed.add_field(
            name="Suspeito:",
            value=usuário.content,
            inline=False
        )
        embed.add_field(
            name="Motivo:",
            value=motivo.content,
            inline=False
        )
        embed.add_field(
            name="Prova:",
            value=prova.content,
            inline=False
        )
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_footer(
            text="Denúncia postada com sucesso.",
            icon_url=message.author.avatar_url
        )
        await client.send_message(canal, embed=embed)

    
    if message.content.lower().startswith("!criarticket"):
        cargos = [
            # IDs dos cargos:
            "412708220021506058", #Master
        ]
        for r in message.author.roles:
            if r.id in cargos:

                ticket = discord.Embed(
                    color=VERM,
                    description="**Como funciona?**\nPara solicitar suporte, clique na reação de sua dúvida.\nIrá ser criado um chat com nossa equipe.\n\n"
                                "`💎 - Compras`\n"
                                "`📋 - Aplicações`\n"
                                "`⛔ - Punições`\n"
                                "`🎳 - Outros`"
                )
                ticket.set_author(name="Sistema de suporte")
                ticket.set_footer(text="Equipe de desenvolvimento do discord", icon_url="https://images-ext-1.discordapp.net/external/BCKxPNzZzEVfkbIublv7_3wG2016jTwGk3onTemVRnM/%3Fv%3D1/https/cdn.discordapp.com/emojis/450112878108999680.gif")
                ticket.timestamp = datetime.datetime.utcnow()

                react = await client.send_message(message.channel, embed=ticket)
                
                await client.add_reaction(react, "💎")
                await client.add_reaction(react, "📋")
                await client.add_reaction(react, "⛔")
                await client.add_reaction(react, "🎳")

                global msg_id
                msg_id = react.id

                global msg_user
                msg_user = message.author

@client.event
async def on_reaction_add(reaction, user):
    msg = reaction.message

    if reaction.emoji == "💎" and msg.id == msg_id: #and user == msg_user:
     for role in user.roles:
         if role.name == "👨🏻‍🚀 Jogador":
             cargo = discord.utils.get(msg.server.roles, name="🌑 Staff+")
             cargo2 = discord.utils.get(msg.server.roles, name="🌑 Staff")

             everyone_perms = discord.PermissionOverwrite(read_messages=False)
             my_perms = discord.PermissionOverwrite(read_messages=True)
             everyone = discord.ChannelPermissions(target=msg.server.default_role, overwrite=everyone_perms)
             mine = discord.ChannelPermissions(target=user, overwrite=my_perms)
             ch = await client.create_channel(msg.server, "Compras-{}".format(user.name), everyone, mine)
             await client.edit_channel_permissions(ch, cargo, my_perms)
             await client.edit_channel_permissions(ch, cargo2, my_perms)
             await client.remove_reaction(msg, "💎", user)
             embed = discord.Embed(title="`Tópico de COMPRAS`", color=VERM, description="Novo tópico!\nCriado por: {}".format(user.mention))
             embed.set_author(name="{} | {}".format(user.name, user), icon_url=user.avatar_url)
             embed.set_footer(text="ID: {}".format(user.id))
             await client.send_message(ch, user.mention + " nossa equipe já foi mencionada e logo estará prestando suporte. {} & {}".format(cargo.mention, cargo2.mention))
             await client.send_message(ch, embed=embed)
             return

    if reaction.emoji == "📋" and msg.id == msg_id: #and user == msg_user:
     for role in user.roles:
         if role.name == "👨🏻‍🚀 Jogador":
             cargo = discord.utils.get(msg.server.roles, name="🌑 Staff+")
             cargo2 = discord.utils.get(msg.server.roles, name="🌑 Staff")
             everyone_perms = discord.PermissionOverwrite(read_messages=False)
             my_perms = discord.PermissionOverwrite(read_messages=True)

             everyone = discord.ChannelPermissions(target=msg.server.default_role, overwrite=everyone_perms)
             mine = discord.ChannelPermissions(target=user, overwrite=my_perms)   
             ch = await client.create_channel(msg.server, "Aplicações-{}".format(user.name), everyone, mine)
             await client.edit_channel_permissions(ch, cargo, my_perms)
             await client.edit_channel_permissions(ch, cargo2, my_perms)
             await client.remove_reaction(msg, "📋", user)
             embed = discord.Embed(title="`Tópico de APLICAÇÕES`", color=VERM, description="Novo tópico!\nCriado por: {}".format(user.mention))
             embed.set_author(name="{} | {}".format(user.name, user), icon_url=user.avatar_url)
             embed.set_footer(text="ID: {}".format(user.id))
             await client.send_message(ch, user.mention + " nossa equipe já foi mencionada e logo estará prestando suporte. {} & {}".format(cargo.mention, cargo2.mention))
             await client.send_message(ch, embed=embed)
             return

    if reaction.emoji == "⛔" and msg.id == msg_id: #and user == msg_user:
     for role in user.roles:
         if role.name == "👨🏻‍🚀 Jogador":
             cargo = discord.utils.get(msg.server.roles, name="🌑 Staff+")
             cargo2 = discord.utils.get(msg.server.roles, name="🌑 Staff")
             everyone_perms = discord.PermissionOverwrite(read_messages=False)
             my_perms = discord.PermissionOverwrite(read_messages=True)

             everyone = discord.ChannelPermissions(target=msg.server.default_role, overwrite=everyone_perms)
             mine = discord.ChannelPermissions(target=user, overwrite=my_perms)   
             ch = await client.create_channel(msg.server, "Punições-{}".format(user.name), everyone, mine)
             await client.edit_channel_permissions(ch, cargo, my_perms)
             await client.edit_channel_permissions(ch, cargo2, my_perms)
             await client.remove_reaction(msg, "⛔", user)
             embed = discord.Embed(title="`Tópico de PUNIÇÕES`", color=VERM, description="Novo tópico!\nCriado por: {}".format(user.mention))
             embed.set_author(name="{} | {}".format(user.name, user), icon_url=user.avatar_url)
             embed.set_footer(text="ID: {}".format(user.id))
             await client.send_message(ch, user.mention + " nossa equipe já foi mencionada e logo estará prestando suporte. {} & {}".format(cargo.mention, cargo2.mention))
             await client.send_message(ch, embed=embed)
             return

    if reaction.emoji == "🎳" and msg.id == msg_id: #and user == msg_user:
     for role in user.roles:
         if role.name == "👨🏻‍🚀 Jogador":
             cargo = discord.utils.get(msg.server.roles, name="🌑 Staff+")
             cargo2 = discord.utils.get(msg.server.roles, name="🌑 Staff")

             everyone_perms = discord.PermissionOverwrite(read_messages=False)
             my_perms = discord.PermissionOverwrite(read_messages=True, send_messages=True)

             everyone = discord.ChannelPermissions(target=msg.server.default_role, overwrite=everyone_perms)
             mine = discord.ChannelPermissions(target=user, overwrite=my_perms)

             ch = await client.create_channel(msg.server, "Outros-{}".format(user.name), everyone, mine)
             await client.edit_channel_permissions(ch, cargo, my_perms)
             await client.edit_channel_permissions(ch, cargo2, my_perms)
             await client.remove_reaction(msg, "🎳", user)
             embed = discord.Embed(title="`Tópico de OUTROS`", color=VERM, description="Novo tópico!\nCriado por: {}".format(user.mention))
             embed.set_author(name="{} | {}".format(user.name, user), icon_url=user.avatar_url)
             embed.set_footer(text="ID: {}".format(user.id))
             await client.send_message(ch, user.mention + " nossa equipe já foi mencionada e logo estará prestando suporte. {} & {}".format(cargo.mention, cargo2.mention))
             await client.send_message(ch, embed=embed)
             return


client.run(os.environ.get("BOT_TOKEN"))
