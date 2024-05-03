import discord
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('TOKEN')

def main():
    bot = discord.Bot()

    @bot.event
    async def on_ready():
        print(f"We have logged in as {bot.user}")

    @bot.slash_command(description="Testowa komenda")
    async def test(ctx):
        await ctx.respond("witam!")

    bot.run(TOKEN)

if __name__ == "__main__":
    main()