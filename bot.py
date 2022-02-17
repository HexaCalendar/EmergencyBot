import disnake
import os
import config
import traceback
from disnake.ext import commands
from datetime import datetime, timedelta
from random import random

def createLogger(name: str, level: int = 20):
    import sys
    import logging
    import config
    from modules.Webhook import WebhookHandler

    LOGGER = logging.getLogger(name)
    FORMATTER = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    streamHandler = logging.StreamHandler(sys.stdout)
    streamHandler.setFormatter(FORMATTER)
    fileHandler = logging.FileHandler(
        filename=f"./{name}.log", mode="w", encoding="utf8"
    )
    webhookHandler = WebhookHandler(
        config.webhook
    )
    webhookHandler.setLevel(level)
    fileHandler.setFormatter(FORMATTER)
    LOGGER.setLevel(level)
    LOGGER.addHandler(streamHandler)
    LOGGER.addHandler(fileHandler)
    LOGGER.addHandler(webhookHandler)
    return LOGGER

  
bot = commands.Bot(command_prefix = ["!"], intents = disnake.Intents.all(), owner_ids=config.owner_ids) 
logger = createLogger("bot")

@bot.event
async def on_ready():
  logger.info(f"[Bot]: ✅ Loaded bot.py")
  try:
      bot.load_extension("jishaku")
      logger.info(f"[Bot] ✅ Loaded jishaku")
  except:
      logger.error(f"[Bot] ❌ Load failed jishaku, ERROR: {str(traceback.format_exc())}")

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
        
  
  channels = member.guild.text_channels
  for _channel in channels:
      if len(ok) > 0:
          break
      random_channel = random.choices(channels)
      ok.append(random_channel[0].id)
      break
          
  # Alts Kicker
  days = datetime.now().replace(tzinfo=None) - member.created_at.replace(tzinfo=None)
  if days < timedelta(days=40):
    
      file = open('whitelist.json', 'r')
      x = file.read()
      if x in member.id:
            return
      file.close()
        
      try:
        embed = disnake.Embed(
          title = f"{setup_name} 자동 차단",
          description = f'Discord 계정이 가입한지 40일이 경과되지 않았어요.\n테러 방지 차원으로 이런 조치를 취하게 되어 양해 부탁드려요.'
        )
        dm = await member.create_dm()
        await dm.send(embed = embed, view = Link())
        for i in ok:
            channel = bot.get_channel(i)
            try:
                await channel.send(f"[Bot]: ✅ Sent a DM to the banned member. ({member.name}#{member.discriminator})")
            except:
                logger.error(f"[Bot]: ❌ Error! {str(traceback.format_exc())}")
      except:
        for i in ok:
            channel = bot.get_channel(i)
            try:
                await channel.send(f"[Bot]: ❌ Couldn't send a DM to the kicked member. ({member.name}#{member.discriminator})")
            except:
                logger.error(f"[Bot]: ❌ Error! {str(traceback.format_exc())}")
                
      try:
        await member.ban()
      except disnake.errors.Forbidden:
          for i in ok:
              channel = bot.get_channel(i)
              try:
                  await channel.send(f"[Bot]: 🔥 I don't have permisson. ({member.name}#{member.discriminator})")
              except:
                  logger.error(f"[Bot]: ❌ Error! {str(traceback.format_exc())}")        
      except:
        logger.error(f"[Bot]: ❌ Error! {str(traceback.format_exc())}")
      else:
          for i in ok:
              channel = bot.get_channel(i)
              try:
                  await channel.send(f"[Bot]: 🔨 Banned an alt ({member.name}#{member.discriminator})")
              except disnake.errors.Forbidden:
                  for i in ok:
                      channel = bot.get_channel(i)
                      try:
                          await channel.send(f"[Bot]: 🔥 I don't have permisson. ({member.name}#{member.discriminator})")
                      except:
                          logger.error(f"[Bot]: ❌ Error! {str(traceback.format_exc())}")
              except:
                  logger.error(f"[Bot]: ❌ Error! {str(traceback.format_exc())}")
              
      setup_name = member.guild
                
  for i in ok:
      channel = bot.get_channel(i)
      try:
          await channel.send(f"[Bot]: ⚡ This account is not banned. ({member.name}#{member.discriminator})")
      except:
          logger.error(f"[Bot]: ❌ Error! {str(traceback.format_exc())}")
  
@bot.command(name="alts")
async def alts(ctx, day:int=None):
  # Alts Kicker
  if day is None:
        day = 40
  for member in ctx.guild.members:
    days = datetime.now().replace(tzinfo=None) - member.created_at.replace(tzinfo=None)
    if days < timedelta(days=day):
        setup_name = ctx.guild
        try:
          embed = disnake.Embed(
            title = f"{setup_name} 자동 차단",
            description = f'Discord 계정이 가입한지 40일이 경과되지 않았어요.\n테러 방지 차원으로 이런 조치를 취하게 되어 양해 부탁드려요.'
          )
          dm = await member.create_dm()
          await dm.send(embed = embed, view = Link())
          await ctx.send(f"[Bot]: ✅ Sent a DM to the kicked member. ({member.name}#{member.discriminator})")
        except:
          await ctx.send(f"[Bot]: ❌ Couldn't send a DM to the kicked member. ({member.name}#{member.discriminator})")
        
        try:
            await member.ban()
        except disnake.errors.Forbidden:
            await ctx.send(f"[Bot]: 🔥 I don't have permisson. ({member.name}#{member.discriminator})")
            continue
        except:
            logger.error(f"[Bot]: ❌ Error! {str(traceback.format_exc())}")
        else:
            await ctx.send(f"[Bot]: 🔨 Banned an alt ({member.name}#{member.discriminator})")
    else:
      await ctx.send(f"[Bot]: ⚡ This account is not banned. ({member.name}#{member.discriminator})")
      pass
  await ctx.send(f"[Bot]: ✅ Finish.")

@bot.command(name="ban")
async def ban(ctx, member: disnake.Member, *, reason=None):
    if ctx.author.guild_permissions.ban_members == True:
        try:
            embed = disnake.Embed(title=f"{ctx.guild.name}에서 차단되셨습니다.")
            
            if reason == None:
                reason = '없음'
                embed.add_filed(name="사유", value=reason)
                
            await bot.get_user(member.id).send(embed=embed)
                
        except:
            pass
            
        try:
            await member.ban()
            embed = disnake.Embed(title="✅️ Success", description=f"{member}를 성공적으로 차단 했습니다.")
            await ctx.reply(embed=embed)
        except:
            embed = disnake.Embed(title="❌️ Error", description=f"봇이 해당 유저를 차단 시킬 권한이 없습니다!")
            await ctx.reply(embed=embed)
            return
            
    else: 
        embed = disnake.Embed(title="❌️ Error", description=f"당신은 해당 유저를 차단 시킬 권한이 없습니다!")
        await ctx.reply(embed=embed)
        return
    
@bot.command(name="kick")
async def kick(ctx, member: disnake.Member, *, reason=None):
    if ctx.author.guild_permissions.kick_members == True:
        try:
            embed = disnake.Embed(title=f"{ctx.guild.name}에서 추방되셨습니다.")         

            if reason == None:
                reason = '없음'
                embed.add_filed(name="사유", value=reason)     

            await bot.get_user(member.id).send(embed=embed)

        except:
            pass     

        try:
            await member.kick()
            embed = disnake.Embed(title="✅️ Success", description=f"{member}를 성공적으로 추방 했습니다.")
            await ctx.reply(embed=embed)                         
        except:
            embed = disnake.Embed(title="❌️ Error", description=f"봇이 해당 유저를 추방 시킬 권한이 없습니다!")
            await ctx.reply(embed=embed)
            return          

    else: 
        embed = disnake.Embed(title="❌️ Error", description=f"당신은 해당 유저를 추방 시킬 권한이 없습니다!")
        await ctx.reply(embed=embed)
        return
      
bot.run(config.token)
