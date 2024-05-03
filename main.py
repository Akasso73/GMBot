import discord
import os
from dotenv import load_dotenv
import character_manager as cm
import battle_manager as bm

load_dotenv()
TOKEN = os.getenv('TOKEN')

def main():
    bot = discord.Bot()

    @bot.event
    async def on_ready():
        print(f"We have logged in as {bot.user}")

    @bot.slash_command(description="Dodaj postać do bazy danych. Tylko dla adminów!")
    async def addcharacter(ctx: discord.ApplicationContext,
                   name: discord.Option(str, "Imię postaci",max_length=60), 
                   health: discord.Option(int, "Zdrowie", choices=[1,2,3,4,5,6]), 
                   strength: discord.Option(int, "Siła", choices=[1,2,3,4,5,6]), 
                   agility: discord.Option(int, "Zręczność", choices=[1,2,3,4,5,6] ), 
                   magic: discord.Option(int, "Magia",choices=[1,2,3,4,5,6]), 
                   defense: discord.Option(int, "Obrona",choices=[1,2,3,4,5,6])):
        discord_user_id = str(ctx.author.id)
        if not cm.Warrior.character_exists(name, discord_user_id):
            warrior = cm.Warrior(name, health, strength, agility, magic, defense, discord_user_id)
            warrior.save_to_db()
            await ctx.respond(embed = discord.Embed(title="Postać dodana!", description=f"Dodano postać {name} do bazy danych!"))
        else:
            await ctx.respond(embed = discord.Embed(title="Postać już istnieje", description=f"Ten gracz już posiada postać o imieniu {name}!"))
        

    bot.run(TOKEN)

if __name__ == "__main__":
    main()