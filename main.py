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
                   name: discord.Option(str, "Imię postaci",max_length=60),  # type: ignore
                   health: discord.Option(int, "Zdrowie", max_value=6, min_value=1),  # type: ignore
                   strength: discord.Option(int, "Siła", max_value=6, min_value=1),  # type: ignore
                   agility: discord.Option(int, "Zręczność", max_value=6, min_value=1),   # type: ignore
                   magic: discord.Option(int, "Magia",max_value=6, min_value=1),  # type: ignore
                   defense: discord.Option(int, "Obrona",max_value=6, min_value=1), # type: ignore
                   player: discord.Option(discord.User, "Gracz")):  # type: ignore
        role_ids = [1230571733363200159, 1236033602815393852, 1230571733409333330]
        discord_user_id = player.id
        if not ctx.author.guild_permissions.administrator or not any(role.id in role_ids for role in ctx.author.roles):
            await ctx.respond(embed=discord.Embed(title="Nie masz uprawnień!", description="Nie masz uprawnień, aby używać tej komendy."),ephemeral=True)
            return
        suma_pkt=strength + agility + magic + defense
        if suma_pkt > 11:
            await ctx.respond(embed=discord.Embed(title="Nieprawidłowe statystyki!", description=f"Suma punktów statysyk musi wynosić 11.\n{suma_pkt-11} za dużo punktów!"),ephemeral=True)
            return
        if not cm.Warrior.character_exists(name):
            warrior = cm.Warrior(name, health, strength, agility, magic, defense, discord_user_id)
            warrior.save_to_db()
            await ctx.respond(embed = discord.Embed(title="Postać dodana!", description=f"Dodano postać **{name}** do bazy danych!"),ephemeral=True)
        else:
            await ctx.respond(embed = discord.Embed(title="Postać już istnieje", description=f"Istnieje już postać o imieniu **{name}**!"),ephemeral=True)

    @bot.slash_command(description="Sprawdź punkty lub statystyki danych postaci")
    async def showcharacters(ctx: discord.ApplicationContext,
                           player: discord.Option(discord.User, "Gracz",required=False),stats: discord.Option(bool, "Czy zmienić punkty na statystyki?",required=False) ):  # type: ignore
        role_ids = [1230571733363200159, 1236033602815393852, 1230571733409333330]
        if not player:
            id = ctx.author.id
        elif player!=ctx.author and not (ctx.author.guild_permissions.administrator or any(role.id in role_ids for role in ctx.author.roles)):
            await ctx.respond(embed=discord.Embed(title="Nie masz uprawnień!", description="Nie masz uprawnień, aby używać tej komendy."),ephemeral=True)
            return
        else:
            id = player.id
        characters = cm.Warrior.get_characters_by_user_id(id)
        if not characters:
            await ctx.respond(embed=discord.Embed(title="Brak postaci!", description="Nie posiadasz żadnych postaci!"),ephemeral=True)
            return
        embed = discord.Embed(title="Twoje postacie:")
        if not stats:
            for character in characters:
                embed.add_field(name=character[0], value=f"Zdrowie: {character[1]} PKT\nSiła: {character[2]} PKT\nZręczność: {character[3]} PKT\nMagia: {character[4]} PKT\nObrona: {character[5]} PKT", inline=False)
        else:
            for character in characters:
                embed.add_field(name=character[0], value=f"HP: {100 + (15*character[1])}\nMax DMG: {(character[2]+2)*6}\nZręczność: {character[3]}\nMax Magiczny DMG: {6*(character[4]+1)}\nObrona: {4*character[5]}% redukcji DMG", inline=False)
        await ctx.respond(embed=embed,ephemeral=True)

    bot.run(TOKEN)

if __name__ == "__main__":
    main()