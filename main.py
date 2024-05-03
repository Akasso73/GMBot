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
                   defense: discord.Option(int, "Obrona",choices=[1,2,3,4,5,6]),
                   player: discord.Option(discord.User, "Gracz")):
        role_ids = [1230571733363200159, 1236033602815393852, 1230571733409333330]
        discord_user_id = player.id
        if not ctx.author.guild_permissions.administrator or not any(role.id in role_ids for role in ctx.author.roles):
            await ctx.respond(embed=discord.Embed(title="Nie masz uprawnień!", description="Nie masz uprawnień, aby używać tej komendy."))
            return
        
        if not cm.Warrior.character_exists(name):
            warrior = cm.Warrior(name, health, strength, agility, magic, defense, discord_user_id)
            warrior.save_to_db()
            await ctx.respond(embed = discord.Embed(title="Postać dodana!", description=f"Dodano postać **{name}** do bazy danych!"))
        else:
            await ctx.respond(embed = discord.Embed(title="Postać już istnieje", description=f"Istnieje już postać o imieniu **{name}**!"))

    bot.run(TOKEN)

if __name__ == "__main__":
    main()