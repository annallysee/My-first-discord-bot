import discord
from discord import Client
import logging

logging.basicConfig(filename='journalisation.log', encoding='utf-8', level=logging.INFO, format='%(asctime)s %(message)s')

class SuunyBot(Client):
    def __init__(self):
        super().__init__()

    async def on_ready(self):
        print(f"{self.user} is ready to get sun !")
        logging.info("Hey !! Je suis prête à vous envoyer du soleil ^^")

    async def on_message(self, message):
        if (message.author == self.user):
            return

        if (message.content.lower() == "!ping"):
            await message.channel.send("pong")
            logging.info("Je veux faire une petite partie de ping pong !")

        if (message.content.lower() == "!invite"):
            invite = await message.channel.create_invite(unique = False)
            await message.channel.send(invite.url)
            logging.info("On vient de me demander le lien du channel")
        
        if(message.content.lower() =="!help"):
            embed = discord.Embed(title="Liste des commandes", color=0xc05479)
            embed.add_field(name="!ping", value="pong", inline=False)
            embed.add_field(name="!invite", value="lien non expirable du channel", inline=False)
            await message.channel.send(embed=embed)
            logging.info("On vient de me demander la liste des commandes")

suuny_bot = SuunyBot()
suuny_bot.run("Mettre ici token du bot")
