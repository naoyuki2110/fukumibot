# coding: utf-8
import discord
from discord.ext import commands
import time
import random
import datetime
import os
TOKEN = os.environ['DISCORD_BOT_TOKEN']
bot = commands.Bot(command_prefix='fm!')
erroremoji = "<:error:804911445900918784>"
checkemoji = "<:check:805241582399914044>"
janbr = [":fist:", ":v:", ":hand_splayed:"]
janwin = ["みぃの負け...君強いね！", "みぃの負け...くやし～～！！", "みぃの負け...むっ、悔しくなんかないんだからねっ！"]
jandraw = ["引き分け。嬉しくないけどっ！", "引き分け。次こそ！", "引き分け。つまらないよ～"]
janlose = ["みぃの勝ち！ほら、じゃんけん代払ってよねっ！", "みぃの勝ち！次も勝ちたい！", "みぃの勝ち！やった～！"]
janura = [":love_you_gesture:", ":wave:", ":fingers_crossed:", ":muscle:", ":ok_hand:"]
janurar = ["あっ...すみません。変なものを出してしまいました...", "ごめんなさい！つい興味本位で...", "ご、ごめんだみぃ...次は頑張るからよろしくみぃ"]
unsr = ["「大吉」！", "「中吉」！", "「吉」！", "「吉」！", "「吉」！", "「吉」！", "「小吉」", "「小吉」", "「末吉」", "「凶」...", "「大凶」......"]
unsrc = ["青", "黄", "緑", "ライトグリーン", "ピンク", "あなたの好きな", "赤", "オレンジ", "紫", "エメラルドグリーン", "コバルトブルー", "藍", "青緑", "茜", "黄緑", "錆納戸", "紺", "朱", "青磁", "菫", "露草", "常盤", "砥粉", "紅赤", "萌葱", "瑠璃", "ターコイズブルー", "セルリアンブルー", "マラカイトグリーン", "ミッドナイトブルー", "フォレストグリーン"]
unsrs = ["☆ ☆ ☆ ☆ ☆", "★ ☆ ☆ ☆ ☆", "★ ★ ☆ ☆ ☆", "★ ★ ★ ☆ ☆", "★ ★ ★ ★ ☆", "★ ★ ★ ★ ★"]
unsrc = ["青", "黄", "緑", "ライトグリーン", "ピンク", "あなたの好きな", "赤", "オレンジ", "紫", "エメラルドグリーン", "コバルトブルー", "藍", "青緑", "茜", "黄緑", "錆納戸", "紺", "朱", "青磁", "菫", "露草", "常盤", "砥粉", "紅赤", "萌葱", "瑠璃", "ターコイズブルー", "セルリアンブルー", "マラカイトグリーン", "ミッドナイトブルー", "フォレストグリーン"]
unsrs = ["☆ ☆ ☆ ☆ ☆", "★ ☆ ☆ ☆ ☆", "★ ★ ☆ ☆ ☆", "★ ★ ★ ☆ ☆", "★ ★ ★ ★ ☆", "★ ★ ★ ★ ★"]
mentmsg = ["むっ、なにかな", "なんですみぃ？", "むぅ、いま腹立ててるからはなしかけないで！", "どうしたの？？", "すやすや...ん、むにゃ...", "おおーっ！どうしたのかな？なんでもきいてあげるよー！"]

@bot.event
async def on_ready():
 print('起動完了しました。')
   await bot.change_presence(activity=discord.Game(name="fm!com | 新機能！「グローバルチャット」ができるようになったよ！"))

@bot.event
async def on_message(message):
  await bot.process_commands(message)
  if message.author.bot:
    return
  if bot.user in message.mentions:
    await message.channel.send(random.choice(mentmsg))
  GLOBAL_CH_NAME = "fukumi-global" # グローバルチャットのチャンネル名
  GLOBAL_WEBHOOK_NAME = "fukumigc-webhooks" # グローバルチャットのWebhook名

  if message.channel.name == GLOBAL_CH_NAME:
      # hoge-globalの名前をもつチャンネルに投稿されたので、メッセージを転送する
      await message.delete()
      channels = bot.get_all_channels()
      global_channels = [ch for ch in channels if ch.name == GLOBAL_CH_NAME]

      for channel in global_channels:
          ch_webhooks = await channel.webhooks()
          webhook = discord.utils.get(ch_webhooks, name=GLOBAL_WEBHOOK_NAME)

          if webhook is None:
              # そのチャンネルに hoge-webhook というWebhookは無かったので無視
              continue
          await webhook.send(content=message.content,
              username=f"{message.author} | {message.guild.name}",
              avatar_url=message.author.avatar_url_as(format="png"))

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        embed=discord.Embed(description=f"`{ctx.message.content}`というコマンドは存在しません。\n\n:bulb:ヒント:コマンドに誤字脱字がないか確認してください\n`help`で別のコマンドを発見してみてください。",color=0xfa2911)
        embed.set_author(name="エラー", icon_url="https://cdn.discordapp.com/emojis/804911445900918784.png?v=1")
        await ctx.send(embed=embed)
    if isinstance(error, commands.errors.MissingPermissions): #エラーの内容を判別
        embed2=discord.Embed(description=f"BOTかあなたに管理者権限が付与されていません。\n\n:bulb:ヒント:このBOTに管理者権限が付いている役職が付与されていますか？されていない場合はBOTに権限を渡してください。\nあなたに管理者権限が付与されていない可能性があります。サーバーの管理者に連絡をお願いいたします。",color=0xfa2911)
        embed2.set_author(name="エラー", icon_url="https://cdn.discordapp.com/emojis/804911445900918784.png?v=1")
        await ctx.send(embed=embed2)

@bot.command()
async def credit(ctx):
 ce = await ctx.send("ㅤ")
 time.sleep(2)
 await ce.edit(content="ーークレジットーー")
 time.sleep(1)
 await ce.edit(content="ーークレジットーー\n\ㅤ")
 time.sleep(1)
 await ce.edit(content="ーークレジットーー\n\ㅤ\n\ㅤ")
 time.sleep(1)
 await ce.edit(content="ーークレジットーー\n\ㅤ\n\ㅤ\n\ㅤ")
 time.sleep(1)
 await ce.edit(content="ーークレジットーー\n\ㅤ\n\ㅤ\n\ㅤ\nBOT総合開発者:naoyuki#5883")
 time.sleep(1)
 await ce.edit(content="ㅤ\n\ㅤ\n\ㅤ\n\ㅤ\nBOT総合開発者:naoyuki#5883\n\ㅤ")
 time.sleep(1)
 await ce.edit(content="ㅤ\n\ㅤ\n\ㅤ\nBOT総合開発者:naoyuki#5883\n\ㅤ\n\このBOTは")
 time.sleep(1)
 await ce.edit(content="ㅤ\n\ㅤ\nBOT総合開発者:naoyuki#5883\n\ㅤ\n\このBOTは\n\皆様のおかげで稼働しています。")
 time.sleep(1)
 await ce.edit(content="ㅤ\nBOT総合開発者:naoyuki#5883\n\ㅤ\n\このBOTは\n\皆様のおかげで稼働しています。\n\これからも応援")
 time.sleep(1)
 await ce.edit(content="BOT総合開発者:naoyuki#5883\n\ㅤ\n\このBOTは\n\皆様のおかげで稼働しています。\n\これからも応援\n\よろしくお願いいたします！")
 time.sleep(1)
 await ce.edit(content="ㅤ\n\このBOTは\n\皆様のおかげで稼働しています。\n\これからも応援\n\よろしくお願いいたします！\nThank you so much for introducing it!!!")
 time.sleep(1)
 await ce.edit(content="このBOTは\n\皆様のおかげで稼働しています。\n\これからも応援\n\よろしくお願いいたします！\nThank you so much for introducing it!!!\n\ㅤ")
 time.sleep(1)
 await ce.edit(content="皆様のおかげで稼働しています。\n\これからも応援\n\よろしくお願いいたします！\nThank you so much for introducing it!!!\n\ㅤ\n\ㅤ")
 time.sleep(1)
 await ce.edit(content="これからも応援\n\よろしくお願いいたします！\nThank you so much for introducing it!!!\n\ㅤ\n\ㅤ\n\ーByー")
 time.sleep(1)
 await ce.edit(content="よろしくお願いいたします！\nThank you so much for introducing it!!!\n\ㅤ\n\ㅤ\n\ーByー\nnaoyuki")
 time.sleep(1)
 await ce.edit(content="Thank you so much for introducing it!!!\n\ㅤ\n\ㅤ\n\ーByー\nnaoyuki\n\ㅤ")
 time.sleep(1)
 await ce.edit(content="ㅤ\n\ㅤ\n\ーByー\nnaoyuki\n\ㅤ\n\ㅤ")

@bot.command()
async def ping(ctx):
  await ctx.send('pong!')

@bot.command()
async def embed(ctx):
  embed = discord.Embed(title="埋め込みテスト",description="埋め込みテストです",color=0x123456)
  await ctx.send(embed=embed)

@bot.command()
async def com(ctx):
  embed=discord.Embed(title="コマンド一覧",description="**ユーティリティ**\n`com`:現在のコマンド\n`credit`:制作者が見れます\n`invite`:BOTの招待リンクを表示します\n`send`:他のチャンネルへメッセージを送信できます\n`fm!send <channel_id> <待機秒数(半角)> <メッセージ内容>`\n`sendguide`:sendコマンドについてのガイドラインです。利用する前に必ずお読みください。\n\n**ゲーム**\n`janken`:じゃんけんに挑戦できます\n`omikuji`:おみくじがひけます\n`dice`:サイコロができます\n`fm!dice <最大値(半角)>`\n`say`:メッセージをそのまま返します\n`fm!say <メッセージ>`\n\n**グローバルチャット**\n`gcjoin`:コマンドを実行したチャンネルにグローバルチャットを作成します。",color=0x05b9e6)
  await ctx.send(embed=embed)

@bot.command()
async def invite(ctx):
  embed=discord.Embed(title="あなたのサーバーにもBOTを導入",description="ふくみぃBOTの導入URLです。http://bit.do/fmbotinvitenew",color=0x023ded)
  await ctx.send(embed=embed)

@bot.command()
async def janken(ctx):
  embed=discord.Embed(title="じゃんけん",description="最初はグー！",color=0x05f752)
  embed2=discord.Embed(title="じゃんけん",description="最初はグー！じゃんけんポン！",color=0x05f752)
  janwinmsg=discord.Embed(title="じゃんけん",description=random.choice(janbr)+"\n"+random.choice(janwin),color=0x05b9e6)
  jandrawmsg=discord.Embed(title="じゃんけん",description=random.choice(janbr)+"\n"+random.choice(jandraw),color=0xe9f50a)
  janlosemsg=discord.Embed(title="じゃんけん",description=random.choice(janbr)+"\n"+random.choice(janlose),color=0xfa5b11)
  januramsg=discord.Embed(title="じゃんけん",description=random.choice(janura)+"\n"+random.choice(janurar),color=0xfa2f8b)
  janunmsg=discord.Embed(title="じゃんけん",description=":star:\nえっ！？もしかしてあなたは、108分の2を引いた人ですみぃ！？すごすぎるみ...これはじゃんけんで連続5回勝ったほどです！おめでとうだみぃ！",color=0x9dff00)
  janunmsg2=discord.Embed(title="じゃんけん",description=":star:\nえっ！？もしかしてあなたは、108分の2を引いた人ですみぃ！？すごすぎるみ...これはじゃんけんで連続5回勝ったほどです！おめでとうだみぃ！",color=0x00e1ff)
  janunmsg3=discord.Embed(title="じゃんけん",description=":star:\nえっ！？もしかしてあなたは、108分の2を引いた人ですみぃ！？すごすぎるみ...これはじゃんけんで連続5回勝ったほどです！おめでとうだみぃ！",color=0x5100ff)
  janun2msg=discord.Embed(title="じゃんけん",description=":star2:\nえええっ！？もしかしてあなたは、108分の1を引いた人ですみぃ！？すごすぎるみ...！！これはじゃんけんで連続10回勝ったほどです！！おめでとうだみぃ！！",color=0xfabb00)
  janun2msg2=discord.Embed(title="じゃんけん",description=":star2:\nえええっ！？もしかしてあなたは、108分の1を引いた人ですみぃ！？すごすぎるみ...！！これはじゃんけんで連続10回勝ったほどです！！おめでとうだみぃ！！",color=0x057aff)
  janun2msg3=discord.Embed(title="じゃんけん",description=":star2:\nえええっ！？もしかしてあなたは、108分の1を引いた人ですみぃ！？すごすぎるみ...！！これはじゃんけんで連続10回勝ったほどです！！おめでとうだみぃ！！",color=0xff0550)
  jkrdnb = random.randint(1,108)
  jmsg = await ctx.send(embed=embed)
  time.sleep(0.5)
  await jmsg.edit(embed=embed2)
  time.sleep(1)
  if jkrdnb >= 1 and jkrdnb <= 25:
    await jmsg.edit(embed=janwinmsg)
  elif jkrdnb >= 26 and jkrdnb <= 50:
    await jmsg.edit(embed=jandrawmsg)
  elif jkrdnb >= 51 and jkrdnb <= 100:
    await jmsg.edit(embed=janlosemsg)
  elif jkrdnb >= 101 and jkrdnb <= 105:
    await jmsg.edit(embed=januramsg)
  elif jkrdnb >= 106 and jkrdnb <= 107:
    await jmsg.edit(embed=janunmsg)
    time.sleep(0.5)
    await jmsg.edit(embed=janunmsg2)
    time.sleep(0.5)
    await jmsg.edit(embed=janunmsg3)
  elif jkrdnb == 108:
    await jmsg.edit(embed=janun2msg)
    time.sleep(0.5)
    await jmsg.edit(embed=janun2msg2)
    time.sleep(0.5)
    await jmsg.edit(embed=janun2msg3)

@bot.command()
async def omikuji(ctx):
  embed=discord.Embed(title="おみくじ",description="今日の運勢を占っちゃおう！",color=0x05f752)
  omk=discord.Embed(title="おみくじ",description=f"今日の運勢は{random.choice(unsr)}\nラッキーカラーは{random.choice(unsrc)}色\n健康運:{random.choice(unsrs)}\n勝負運:{random.choice(unsrs)}\n恋愛運:{random.choice(unsrs)}\n仕事運:{random.choice(unsrs)}\n金運:{random.choice(unsrs)}\n明日も占っちゃおう！",color=0x05f752)
  omkmsg = await ctx.send(embed=embed)
  time.sleep(1)
  await omkmsg.edit(embed=omk)

@bot.command()
async def send(ctx, ch, waitcou, sendmsg):
  tme = datetime.datetime.now()
  print ("ーーーーーSendコマンド使用通知ーーーーー")
  print (ctx.message.guild.name)
  print (ctx.message.guild.id)
  print (ctx.message.channel.name)
  print (ctx.message.channel.id)
  print (ctx.message.author)
  print (ctx.message.author.id)
  seev=discord.Embed(title="予約完了",description=f"{waitcou}秒後に<#{ch}>へメッセージを送信します。",color=0x05f752)
  seev2=discord.Embed(description=f"<@{ctx.message.author.id}>\n<#{ch}>へメッセージを送信しました。",color=0x05f752)
  seev2.set_author(name="送信完了", icon_url="https://cdn.discordapp.com/emojis/805241582399914044.png?v=1")
  seev3=discord.Embed(description=f"{sendmsg}",color=0x05b9e6)
  seev3.set_footer(text=f"{tme.year}/{tme.month}/{tme.day} {tme.hour}:{tme.minute}:{tme.second}")
  seev3.set_author(name=f"{ctx.message.author}", icon_url=ctx.message.author.avatar_url_as(format="png"))
  resch = int(ch)
  await ctx.send(embed=seev)
  print (sendmsg)
  print (ctx.message.content)
  time.sleep(int(waitcou))
  await ctx.send(embed=seev2)
  channel = bot.get_channel(resch)
  await channel.send(embed=seev3)
  print ("ーーーーーーーーーーーーーーーーーーーー")

@bot.command()
async def sendguide(ctx):
  embed=discord.Embed(title="Sendコマンドガイドライン",description="**禁止事項**\n荒らし・spam\n殺害予告\n他人への侮辱行為\nその他管理者が不適切と思われる使用法\n\n宣伝はOKですがサーバーのメンバーに迷惑が掛からない程度でお願いします。\n**管理者が日々監視しています。くれぐれも注意して使用してください。**",color=0x05f752)
  embed.set_footer(text="更新日時:2021/01/31")
  await ctx.send(embed=embed)

@bot.command()
async def exsend(ctx, exch):
  if ctx.message.author.id == 524872647042007067:
    print ("ーーーーー警告Sendコマンド使用通知ーーーーー")
    print (ctx.message.channel.name)
    print (ctx.message.channel.id)
    exseev=discord.Embed(title="警告完了",description=f"<#{exch}>へ警告メッセージを送信しました。",color=0x05f752)
    exseev2=discord.Embed(title="警告",description=f"<#{exch}>で必要以上のSend投稿数が確認されました。迷惑にならない程度で使用してください。\n:bulb:ヒント:Sendコマンドのガイドラインを確認するには`sendguide`",color=0xe9f50a)
    resexch = int(exch)
    await ctx.send(embed=exseev)
    channel = bot.get_channel(resexch)
    await channel.send(embed=exseev2)
    print ("ーーーーーーーーーーーーーーーーーーーー")
  else:
    embed=discord.Embed(description="あなたにはこのコマンドを実行する権限がありません。\nこのコマンドは一般利用者には実行できません。",color=0xfa2911)
    embed.set_author(name="エラー", icon_url="https://cdn.discordapp.com/emojis/804911445900918784.png?v=1")
    await ctx.send(embed=embed)

@bot.command()
async def ctexsend(ctx, exch, exdesc):
  if ctx.message.author.id == 524872647042007067:
    print ("ーーーーーカスタム警告Sendコマンド使用通知ーーーーー")
    print (ctx.message.channel.name)
    print (ctx.message.channel.id)
    ctexseev=discord.Embed(title="警告完了",description=f"<#{exch}>へカスタム警告メッセージを送信しました。",color=0x05f752)
    ctexseev2=discord.Embed(title="警告",description=f"{exdesc}",color=0xe9f50a)
    resexch = int(exch)
    await ctx.send(embed=ctexseev)
    channel = bot.get_channel(resexch)
    await channel.send(embed=ctexseev2)
    print ("ーーーーーーーーーーーーーーーーーーーー")
  else:
    embed=discord.Embed(description="あなたにはこのコマンドを実行する権限がありません。\nこのコマンドは一般利用者には実行できません。",color=0xfa2911)
    embed.set_author(name="エラー", icon_url="https://cdn.discordapp.com/emojis/804911445900918784.png?v=1")
    await ctx.send(embed=embed)

@bot.command()
async def dice(ctx, max):
    fmdice = random.randint(1,int(max))
    embed=discord.Embed(title=f"{max}面サイコロの結果",description=f"**{fmdice}**が出ました！",color=0x05f752)
    await ctx.send(embed=embed)

@bot.command()
async def say(ctx, msg):
  await ctx.message.delete()
  await ctx.send(msg)
  
@bot.command()
@commands.has_permissions(administrator=True)
async def gcjoin(ctx):
 embed=discord.Embed(title="グローバルチャット作成中",description="このチャンネルにグローバルチャットを作成しています。しばらくお待ちください...\n\n準備中...",color=0x05b9e6)
 embed2=discord.Embed(title="グローバルチャット作成中",description="このチャンネルにグローバルチャットを作成しています。しばらくお待ちください...\n\nチャンネル名を変更しています...",color=0x05b9e6)
 embed3=discord.Embed(title="グローバルチャット作成中",description="このチャンネルにグローバルチャットを作成しています。しばらくお待ちください...\n\nWebhookを作成しています。...",color=0x05b9e6)
 embed4=discord.Embed(title="グローバルチャット作成中",description="このチャンネルにグローバルチャットを作成しています。しばらくお待ちください...\n\n最後の設定を適用しています...",color=0x05b9e6)
 embed5=discord.Embed(description="このチャンネルにグローバルチャットを作成しました！ほかのサーバーの人との会話を楽しんでくださいっ！",color=0x05f752)
 embed5.set_author(name="グローバルチャット作成完了", icon_url="https://cdn.discordapp.com/emojis/805241582399914044.png?v=1")
 embed6=discord.Embed(description=f"新たなサーバーがグローバルチャットに参加しました！\nサーバー:{ctx.message.guild.name}\nチャンネル:{ctx.message.channel.name}",color=0x05f752)
 embed6.set_author(name="新たなサーバーが参加", icon_url="https://cdn.discordapp.com/emojis/805241582399914044.png?v=1")
 gcjoinmsg = await ctx.send(embed=embed)
 time.sleep(2.5)
 await gcjoinmsg.edit(embed=embed2)
 time.sleep(1.2)
 await ctx.message.channel.edit(name="fukumi-global")
 await gcjoinmsg.edit(embed=embed3)
 time.sleep(1.6)
 await ctx.message.channel.create_webhook(name="fukumigc-webhooks")
 await gcjoinmsg.edit(embed=embed4)
 time.sleep(1.3)
 await gcjoinmsg.edit(embed=embed5)
 
bot.run(TOKEN)
