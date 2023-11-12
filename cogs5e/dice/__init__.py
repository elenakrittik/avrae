from .cog import Dice


async def setup(bot):
    await bot.add_cog(Dice(bot))
