import disnake
import os
import config
from disnake.ext import commands
from utils import createLogger
from datetime import datetime

bot = commands.Bot(command_prefix = ["!"], intents = disnake.Intents.all(), owner_ids=[902700864748273704]) 
logger = createLogger("bot")

@bot.event
async def on_ready():
  logger.info(f"[Bot]: ✅ Loaded bot.py")
  try:
      bot.load_extension("jishaku")
      logger.info(f"✅ [Bot] Loaded jishaku")
  except:
      logger.error(f"❌ [Bot] Load failed jishaku")

@bot.event
async def on_member_join(member):
  # Alts Kicker
  days = datetime.now().replace(tzinfo=None) - member.created_at.replace(tzinfo=None)
  if days < timedelta(days=30):
      await member.ban()
      logger.info("[Bot]: 🔨 Banned an alt ({member.name}#{member.discriminator})")
      setup_name = member.guild
      try:
        embed = disnake.Embed(
          title = f"{setup_name} 자동 차단",
          description = f'Discord 계정이 가입한지 30일이 경과되지 않았어요.\n테러 방지 차원으로 이런 조치를 취하게 되어 양해 부탁드려요.'
        )
        await member.send(embed = embed, view = Link())
        logger.info(f"[Bot]: ✅ Sent a DM to the kicked member. ({member.name}#{member.discriminator})")
      except:
        logger.error(f"[Bot]: ❌ Couldn't send a DM to the kicked member. ({member.name}#{member.discriminator})")

@bot.command(name="alts")
async def alts(ctx):
  # Alts Kicker
  for member in ctx.guild.members:
    days = datetime.now().replace(tzinfo=None) - member.created_at.replace(tzinfo=None)
    if days < timedelta(days=30):
        await member.ban()
        logger.info("[Bot]: 🔨 Banned an alt ({member.name}#{member.discriminator})")
        setup_name = ctx.guild
        try:
          embed = disnake.Embed(
            title = f"{setup_name} 자동 차단",
            description = f'Discord 계정이 가입한지 30일이 경과되지 않았어요.\n테러 방지 차원으로 이런 조치를 취하게 되어 양해 부탁드려요.'
          )
          await member.send(embed = embed, view = Link())
          logger.info(f"[Bot]: ✅ Sent a DM to the kicked member. ({member.name}#{member.discriminator})")
        except:
          logger.error(f"[Bot]: ❌ Couldn't send a DM to the kicked member. ({member.name}#{member.discriminator})")
      
bot.run(config.token)
