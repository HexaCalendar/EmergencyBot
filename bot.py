import disnake
import os
import config
import traceback
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
  ok = []
  channels = member.guild.text_channels
  for channel in channels:
      if (
          channel.topic is not None
          and str(channel.topic).find("-AltLog") != -1
      ):
          ok.append(channel.id)
          break
      else:
          pass
        
  for guild in guilds:
    channels = guild.text_channels
    for _channel in channels:
        if len(ok) > 0:
            break
        random_channel = random.choices(channels)
        ok.append(random_channel[0].id)
        break
          
  # Alts Kicker
  days = datetime.now().replace(tzinfo=None) - member.created_at.replace(tzinfo=None)
  if days < timedelta(days=30):
      await member.ban()
      
      for i in ok:
          channel = bot.get_channel(i)
          try:
              await channel.send(f"[Bot]: 🔨 Banned an alt ({member.name}#{member.discriminator})")
          except discord.Forbidden:
              pass
          except:
              logger.error(f"[Bot]: ❌ Error! {str(traceback.format_exc())}")
              
      setup_name = member.guild
              
      try:
        embed = disnake.Embed(
          title = f"{setup_name} 자동 차단",
          description = f'Discord 계정이 가입한지 30일이 경과되지 않았어요.\n테러 방지 차원으로 이런 조치를 취하게 되어 양해 부탁드려요.'
        )
        await member.send(embed = embed, view = Link())
        for i in ok:
            channel = bot.get_channel(i)
            try:
                await channel.send(f"[Bot]: ✅ Sent a DM to the banned member. ({member.name}#{member.discriminator})")
            except discord.Forbidden:
                pass
            except:
                logger.error(f"[Bot]: ❌ Error! {str(traceback.format_exc())}")
      except:
        for i in ok:
            channel = bot.get_channel(i)
            try:
                await channel.send(f"[Bot]: ❌ Couldn't send a DM to the kicked member. ({member.name}#{member.discriminator})")
            except discord.Forbidden:
                pass
            except:
                logger.error(f"[Bot]: ❌ Error! {str(traceback.format_exc())}")

@bot.command(name="alts")
async def alts(ctx):
  # Alts Kicker
  for member in ctx.guild.members:
    days = datetime.now().replace(tzinfo=None) - member.created_at.replace(tzinfo=None)
    if days < timedelta(days=30):
        await member.ban()
        await ctx.reply("[Bot]: 🔨 Banned an alt ({member.name}#{member.discriminator})")
        setup_name = ctx.guild
        try:
          embed = disnake.Embed(
            title = f"{setup_name} 자동 차단",
            description = f'Discord 계정이 가입한지 30일이 경과되지 않았어요.\n테러 방지 차원으로 이런 조치를 취하게 되어 양해 부탁드려요.'
          )
          await member.send(embed = embed, view = Link())
          await ctx.reply(f"[Bot]: ✅ Sent a DM to the kicked member. ({member.name}#{member.discriminator})")
        except:
          await ctx.reply(f"[Bot]: ❌ Couldn't send a DM to the kicked member. ({member.name}#{member.discriminator})")
    else:
      await ctx.reply(f"[Bot]: ⚡ This account is not banned. ({member.name}#{member.discriminator})")
      pass
  await ctx.reply(f"[Bot]: ✅ Finish.")
      
bot.run(config.token)
