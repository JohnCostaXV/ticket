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
        await client.change_presence(game=discord.Game(name="Online com mais de 144{} membros!".format(str(len(set(client.get_all_members())))), url="https://www.twitch.tv/johncostaxv", type=1))
        await asyncio.sleep(300)
        await client.change_presence(game=discord.Game(name="Criando tickets!", url="https://www.twitch.tv/johncostaxv", type=1))
        await asyncio.sleep(300)
        await client.change_presence(game=discord.Game(name="Criado pelo Johnn#0001", url="https://www.twitch.tv/johncostaxv", type=1))
        await asyncio.sleep(300)

@client.event
async def on_message(message):
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
             await client.remove_reaction(msg, "💎", user)
     everyone_perms = discord.PermissionOverwrite(read_messages=False)
     my_perms = discord.PermissionOverwrite(read_messages=True)

     everyone = discord.ChannelPermissions(target=msg.server.default_role, overwrite=everyone_perms)
     mine = discord.ChannelPermissions(target=msg.server.me, overwrite=my_perms)   
     await client.create_channel(msg.server, "Suporte-{}".format(user.name), everyone, mine)
     return

    if reaction.emoji == "📋" and msg.id == msg_id: #and user == msg_user:
     for role in user.roles:
         if role.name == "👨🏻‍🚀 Jogador":
             await client.remove_reaction(msg, "📋", user)
     everyone_perms = discord.PermissionOverwrite(read_messages=False)
     my_perms = discord.PermissionOverwrite(read_messages=True)

     everyone = discord.ChannelPermissions(target=msg.server.default_role, overwrite=everyone_perms)
     mine = discord.ChannelPermissions(target=msg.server.me, overwrite=my_perms)   
     await client.create_channel(msg.server, "Suporte-{}".format(user.name), everyone, mine)
     return

    if reaction.emoji == "⛔" and msg.id == msg_id: #and user == msg_user:
     for role in user.roles:
         if role.name == "👨🏻‍🚀 Jogador":
             await client.remove_reaction(msg, "⛔", user)
     everyone_perms = discord.PermissionOverwrite(read_messages=False)
     my_perms = discord.PermissionOverwrite(read_messages=True)

     everyone = discord.ChannelPermissions(target=msg.server.default_role, overwrite=everyone_perms)
     mine = discord.ChannelPermissions(target=msg.server.me, overwrite=my_perms)   
     await client.create_channel(msg.server, "Suporte-{}".format(user.name), everyone, mine)
     return

    if reaction.emoji == "🎳" and msg.id == msg_id: #and user == msg_user:
     for role in user.roles:
         if role.name == "👨🏻‍🚀 Jogador":
             await client.remove_reaction(msg, "🎳", user)
     everyone_perms = discord.PermissionOverwrite(read_messages=False)
     my_perms = discord.PermissionOverwrite(read_messages=True)

     everyone = discord.ChannelPermissions(target=msg.server.default_role, overwrite=everyone_perms)
     mine = discord.ChannelPermissions(target=msg.server.me, overwrite=my_perms)   
     await client.create_channel(msg.server, "Suporte-{}".format(user.name), everyone, mine)
     return


client.run(os.environ.get("BOT_TOKEN"))
