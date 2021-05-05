# coding: utf-8
import discord
from discord.ext import commands
import time
import random
import datetime
from pyokaka import okaka
from googletrans import Translator
import requests
from bs4 import BeautifulSoup
import os
TOKEN = os.environ['DISCORD_BOT_TOKEN']
intents=discord.Intents.default()
intents.members=True
bot = commands.Bot(command_prefix='fm!',help_command=None,intents=intents)
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
translator = Translator()
ranreacc = 0
thinkr = ["<:thonk:828451872217366588>", "<:authink:828451874314387497>"]
lrurl = "https://patolesoft.net/Games/PatnetResort/PatolePusherQuintessence/LegionRankers.php"
ppqstmy = "https://patnetresort.com/myriad"

@bot.event
async def on_ready():
  print('起動完了しました。')
  print(bot.guilds)
  while True:
    guildone = str(bot.guilds)
    guildtwo = guildone.split(',')
    guildcount = len(guildtwo)
    await bot.change_presence(activity=discord.Game(name=f"fm!help 1~4| {guildcount}サーバーがBOTを導入中"))

@bot.event
async def on_message(message):
  await bot.process_commands(message)
  if message.author.bot:
    return
  if "discord" in message.content:
    await message.add_reaction('<:DiscordLogo:828436198157975563>')
  if "ディスコード" in message.content:
    await message.add_reaction('<:DiscordLogo:828436198157975563>')
  if "ディスコ" in message.content:
    await message.add_reaction('<:DiscordLogo:828436198157975563>')
  if "だろう" in message.content:
    await message.channel.send("そうだろう")
  if "こんにちは" in message.content:
    await message.channel.send("こんだみぃ！")
  if "こんばんは" in message.content:
    await message.channel.send("こんばんは！遅くまで大変だね")
  if "おはよう" in message.content:
    await message.channel.send("おはようだみぃ！今日も一日よろしくみぃ！")
  if "\N{THINKING FACE}" in message.content:
    await message.channel.send(":thinking:")
  if "お願いします" in message.content:
    await message.channel.send("本当に、お願いしますっ...！")
  if "よろしく" in message.content:
    await message.channel.send("こちらこそよろしくみぃ")
  if "誤字" in message.content:
    await message.channel.send("みぃは御侍しなうみぃいよ...！？＞")
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
    if isinstance(error, commands.BadArgument):
        embed3=discord.Embed(description="引数が不正です。コマンドを見直してみてください。",color=0xfa2911)
        embed3.set_author(name="エラー", icon_url="https://cdn.discordapp.com/emojis/804911445900918784.png?v=1")
        await ctx.send(embed=embed3)

@bot.command(aliases=["team","staff"])
async def credit(ctx):
  """
  ふくみぃBOTの開発メンバーを表示します。
  """
  user = await bot.fetch_user(524872647042007067)
  embed=discord.Embed(title="クレジット",description=f"1名\nBOT総合開発者:{user.name}#{user.discriminator}",color=0x05b9e6)
  await ctx.send(embed=embed)

@bot.command(aliases=["dhelp"])
async def devhelp(ctx):
  embed=discord.Embed(title="テスト中コマンド",description="**ユーティリティ**\n~~`fm!calc`:指定した和、差、積、商を表示します。<:alpha:812541506191491093>\n`fm!calc <四則演算(半角>`\n記述法は`fm!calchelp`をご覧ください\n`translate`:内容を指定した言語に翻訳します。<:alpha:812541506191491093>\n`fm!translate <ロケールID上2桁> <翻訳内容>`~~",color=0x05b9e6)
  await ctx.send(embed=embed)

@bot.command()
async def update(ctx):
  embed=discord.Embed(color=0x05b9e6)
  embed.set_author(name="v2.1.2, 2.1.3更新情報", icon_url="https://cdn.discordapp.com/emojis/812569029365465108.png?v=1")
  embed.add_field(name="変更点",value="fmjpcとlastjpとdevhelpとwebtitleコマンドを実装(詳細は`fm!help`)\n\n・ローマ字かな文字変換機能を実装(詳細は`fm!help`)\n・inviteコマンドを削除、linkコマンドに置き換え\n・creditコマンドのレイアウトを修正\n・ヘルプコマンドを`fm!com`から`fm!help`に変更\n・updateコマンドを実装(詳細は`fm!help`)")
  embed.add_field(name="不具合修正",value="Send、Sayコマンドでメッセージ内容を指定する際半角スペースや改行以降の文字列が表示されない不具合を修正")
  await ctx.send(embed=embed)

@bot.command()
async def embed(ctx):
  embed = discord.Embed(title="埋め込みテスト",description="埋め込みテストです",color=0x123456)
  await ctx.send(embed=embed)

@bot.command()
async def help(ctx, page):
  hpage1=discord.Embed(title="コマンド一覧",description="**ユーティリティ**\n`help`:現在のコマンド\n`fm!help <ページ番号(半角)`\n`devhelp`:テスト中のコマンド一覧を表示します\n`credit`:制作者が見れます\n`link`:BOTの招待リンクを表示します\n`send`:他のチャンネルへメッセージを送信できます\n`fm!send <channel_id> <待機秒数(半角)> <メッセージ内容>`\n`sendguide`:sendコマンドについてのガイドラインです。利用する前に必ずお読みください。\n`kanc`:ローマ字からひらがなに変換します\n`fm!kanc <ローマ字(半角)>`\n`update`:最新のBOT更新情報を表示します。\n`webtitle`:指定したサイトのタイトル情報を表示します\n`fm!webtitle <URL>`",color=0x05b9e6)
  hpage1.set_footer(text="1/4")
  hpage2=discord.Embed(title="コマンド一覧",description="**ゲーム**\n`janken`:じゃんけんに挑戦できます\n`omikuji`:おみくじがひけます\n`dice`:サイコロができます\n`fm!dice <最大値(半角)>`\n`say`:メッセージをそのまま返します\n`fm!say <メッセージ>`\n`fmjpc`:ふくみぃJACKPOTCHANCEに挑戦できます(メダルはもらえません)\n`lastjp`:最新のふくみぃJACKPOT獲得者を表示します\n`fmimage`:ふくみぃってどんなイメージ？\n`fm!fmimage <イメージ内容>`\n`fmima`:ふくみぃのみんなのイメージを見ることができます",color=0x05b9e6)
  hpage2.set_footer(text="2/4")
  hpage3=discord.Embed(title="コマンド一覧",description="**グローバルチャット**\n`gcjoin`:コマンドを実行したチャンネルにグローバルチャットを作成します。",color=0x05b9e6)
  hpage3.set_footer(text="3/4")
  hpage4=discord.Embed(title="コマンド一覧",description="**期間限定**\n`legrk`:PNRレギオンランカーズの順位表が見れます。\n`legrktp`:PNRレギオンランカーズの順位表(トレパレTOTAL)が見れます。\n`legrkgjp`:PNRレギオンランカーズの順位表(GJPTOTAL)が見れます。\n`legrkcf`:PNRレギオンランカーズの順位表(CFWINTOTAL)が見れます。\n`legrkcfd`:PNRレギオンランカーズの順位表(CFDUPTOTAL)が見れます。\n`myriadinfo`:PNRのミリアドJPゲームに関する情報が見れます。",color=0x05b9e6)
  hpage4.set_footer(text="4/4")
  hels=discord.Embed(description="ページが存在しません。\n現在取得可能なページ数は**3**です。",color=0xfa2911)
  hels.set_author(name="エラー", icon_url="https://cdn.discordapp.com/emojis/804911445900918784.png?v=1")
  if page == "1":
    await ctx.send(embed=hpage1)
  elif page == "2":
    await ctx.send(embed=hpage2)
  elif page == "3":
    await ctx.send(embed=hpage3)
  elif page == "4":
    await ctx.send(embed=hpage4)
  else:
    await ctx.send(embed=hels)

@bot.command()
async def link(ctx):
  embed=discord.Embed(title="関連リンク",description="ふくみぃ関連のリンク集です。\n\n[BOT導入URL](https://discord.com/oauth2/authorize?client_id=754190285382352920&permissions=8&scope=bot)\n[サポートサーバー](https://discord.gg/CuD8jfK)",color=0x023ded)
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
async def send(ctx, ch, waitcou, *, sendmsg):
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
  seev3.set_footer(text=tme.strftime('%Y/%m/%d %H:%M:%S'))
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
async def ctexsend(ctx, exch, *, exdesc):
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
async def say(ctx, *, msg):
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

@bot.command()
async def kanc(ctx, *, msg):
 cvresult = okaka.convert(msg)
 embed=discord.Embed(description=cvresult,color=0x05b9e6)
 embed.set_author(name="ローマ字→かな文字変換結果", icon_url="https://cdn.discordapp.com/emojis/812530847886213130.png?v=1")
 await ctx.send(embed=embed)

@bot.command()
async def translatefgtgbgrb(ctx, locale, *, msg):
  print("コマンドOK")
  trsmsg = translator.translate('テスト', dest='en')
  print("代入OK")
  embed=discord.Embed(description=trsmsg.text,color=0x05b9e6)
  print("Embed代入OK")
  embed.set_author(name="翻訳結果", icon_url="https://cdn.discordapp.com/emojis/812893291540250645.png?v=1")
  print("ユーザーOK")
  await ctx.send(embed=embed)
  print("送信OK")
  print(trsmsg.text)

@bot.command()
async def webtitle(ctx, url):
  html = requests.get(url)
  soup = BeautifulSoup(html.content, "html.parser")
  embed=discord.Embed(title=f"{url}\nのタイトル情報",description=soup.find("title").text,color=0x05b9e6)
  await ctx.send(embed=embed)

@bot.command()
async def fmjpc3721632367813yed(ctx):
  agojpcmsg = await ctx.send("<a:loading1:812923199116410940>抽選中です...")
  jpcsleep = random.randint(3,15)
  time.sleep(jpcsleep)
  await agojpcmsg.delete()
  jpcrand = random.randint(1,100)
  if jpcrand >= 1 and jpcrand <= 50:
    await ctx.send(f"<@{ctx.message.author.id}>**100Win!**\nまた挑戦してだみぃ！")
  elif jpcrand >= 51 and jpcrand <= 80:
    await ctx.send(f"<@{ctx.message.author.id}>**200Win!**\nまた挑戦してだみぃ！")
  elif jpcrand >= 81 and jpcrand <= 99:
    await ctx.send(f"<@{ctx.message.author.id}>**300Win!**\nまた挑戦してだみぃ！")
  elif jpcrand == 100:
    jtme = datetime.datetime.now()
    jprand = random.randint(1000,99999)
    await ctx.send(f"<@{ctx.message.author.id}>**J A C K P O T !**\n**Congratulations!!!**\nJACKPOT枚数**{jprand}枚！**\nまた挑戦してだみぃ！")
    f = open(r'C:\Users\user\Documents\dispy\fukumijackpot.txt', 'w')
    datalist = [f'獲得者:**{ctx.message.author}**\n', f'JACKPOT枚数:**{jprand}枚**\n', jtme.strftime('%Y/%m/%d %H:%M:%S')]
    f.writelines(datalist)
    f.close()

@bot.command()
async def lastjpftrgbtrbt(ctx):
  if ctx.message.author.id == 524872647042007067:
    jp=open(r'C:\Users\user\Documents\dispy\fukumijackpot.txt')
    jpline=jp.read()
    embed=discord.Embed(title="ふくみぃJACKPOT最終獲得者",description=jpline,color=0x05b9e6)
    await ctx.send(embed=embed)
    jp.close()
  else:
    embed=discord.Embed(description="あなたにはこのコマンドを実行する権限がありません。\nこのコマンドは一般利用者には実行できません。",color=0xfa2911)
    embed.set_author(name="エラー", icon_url="https://cdn.discordapp.com/emojis/804911445900918784.png?v=1")
    await ctx.send(embed=embed)

@bot.command()
async def fmimagegtrbgtbet(ctx, msg):
  if ctx.message.author.id == 524872647042007067:
    f = open(r'C:\Users\user\Documents\dispy\fukumiimage.txt', 'a', encoding='UTF-8')
    await ctx.send(f"みぃって{msg}んだね！\nありがとう！")
    f.write(f"{msg}、")
    f.close()
  else:
    embed=discord.Embed(description="あなたにはこのコマンドを実行する権限がありません。\nこのコマンドは一般利用者には実行できません。",color=0xfa2911)
    embed.set_author(name="エラー", icon_url="https://cdn.discordapp.com/emojis/804911445900918784.png?v=1")
    await ctx.send(embed=embed)

@bot.command()
async def fmimatgbeb(ctx):
  if ctx.message.author.id == 524872647042007067:
    f = open(r'C:\Users\user\Documents\dispy\fukumiimage.txt', encoding='UTF-8')
    fl=f.read()
    embed=discord.Embed(title="ふくみぃってどんなイメージ？",description=fl,color=0x05b9e6)
    await ctx.send(embed=embed)
    f.close()
  else:
    embed=discord.Embed(description="あなたにはこのコマンドを実行する権限がありません。\nこのコマンドは一般利用者には実行できません。",color=0xfa2911)
    embed.set_author(name="エラー", icon_url="https://cdn.discordapp.com/emojis/804911445900918784.png?v=1")
    await ctx.send(embed=embed)

@bot.command()
async def kickhfhfuerhferfhe(ctx, use):
  user = await bot.fetch_user(int(use))
  embed=discord.Embed(title="ユーザーキック確認",description="本当にこのユーザーをキックしますか？\nよければ<:check2:805283656984952845>を、キャンセルの場合は<:error2:805283657412902930>を押してください。",color=0xfa2911)
  embed.set_thumbnail(url=user.avatar_url)
  embed.add_field(name="対象ユーザー", value=f"{user.name}#{user.discriminator}")
  embed.add_field(name="実行ユーザー", value=ctx.message.author)
  embed2=discord.Embed(title="ユーザーキック確認",description="5秒後にキックを実行します。少々お待ちください。",color=0xfa2911)
  embed3=discord.Embed(description="ユーザーをキックしました。",color=0x05f752)
  embed3.set_author(name="ユーザーキック完了", icon_url="https://cdn.discordapp.com/emojis/805241582399914044.png?v=1")
  embed3.set_thumbnail(url=user.avatar_url)
  embed3.add_field(name="対象ユーザー", value=f"{user.name}#{user.discriminator}")
  embed3.add_field(name="実行ユーザー", value=ctx.message.author)
  kmsg = await ctx.send(embed=embed)
  await kmsg.add_reaction('<:check2:805283656984952845>')
  await kmsg.add_reaction('<:error2:805283657412902930>')
  target_reaction = await bot.wait_for_reaction(message=kmsg)
  print("まちOK")
  if target_reaction.user == msg.author:
    print("おなじじゃない確認OK")
    if target_reaction.reaction.emoji == '<:check2:805283656984952845>':
      print("チェック準備OK")
      await kmsg.delete()
      print("けしOK")
      kmsg2 = await ctx.send(embed=embed2)
      time.sleep(5)
      await kmsg2.edit(embed=embed3)
      print("チェックOK")
    elif target_reaction.reaction.emoji == '<:error2:805283657412902930>':
      await kmsg.delete()
      await ctx.send("キャンセルしました。")
  else:
    await kmsg.remove_reaction(target_reaction.reaction.emoji, target_reaction.user)

@bot.command()
async def serverinfo(ctx, svid):
  guild = bot.get_guild(int(svid))
  embed=discord.Embed(title="サーバー情報",description=f"サーバーID:{guild.id}\nサーバー名:{guild.name}\nオーナー名:{guild.owner.name}\nオーナーID:{guild.owner.id}\n",color=0x05b9e6)
  await ctx.send(embed=embed)

@bot.command()
async def userinfo(ctx, usid):
  usnm = bot.get_user(int(usid))
  embed=discord.Embed(title="ユーザー情報",description=f"ユーザーID:{usnm.id}\nサーバー名:{usnm.name}",color=0x05b9e6)
  await ctx.send(embed=embed)

@bot.command()
async def legrk(ctx):
  html = requests.get(lrurl)
  soup = BeautifulSoup(html.content, "html.parser", from_encoding='utf-8')
  lgrk = soup.select('strong')
  lgrk2 = str(lgrk)
  embed=discord.Embed(title="レギオンランカーズ順位表（すべて）",url="https://patolesoft.net/Games/PatnetResort/PatolePusherQuintessence/LegionRankers.php",color=0xfcba03)
  embed.add_field(name="トレパレ TOTAL", value=f"**1.{lgrk[0].contents[0]}　Score:{lgrk[1].contents[0].strip()}**\n2.{lgrk[2].contents[0]}　Score:{lgrk[3].contents[0].strip()}\n3.{lgrk[4].contents[0]}　Score:{lgrk[5].contents[0].strip()}\n4.{lgrk[6].contents[0]}　Score:{lgrk[7].contents[0].strip()}\n5.{lgrk[8].contents[0]}　Score:{lgrk[9].contents[0].strip()}")
  embed.add_field(name="ゴールデンJP TOTAL", value=f"**1.{lgrk[20].contents[0]}　Score:{lgrk[21].contents[0].strip()}**\n2.{lgrk[22].contents[0]}　Score:{lgrk[23].contents[0].strip()}\n3.{lgrk[24].contents[0]}　Score:{lgrk[25].contents[0].strip()}\n4.{lgrk[26].contents[0]}　Score:{lgrk[27].contents[0].strip()}\n5.{lgrk[28].contents[0]}　Score:{lgrk[29].contents[0].strip()}")
  embed.add_field(name="コズミックWIN TOTAL", value=f"**1.{lgrk[40].contents[0]}　Score:{lgrk[41].contents[0].strip()}**\n2.{lgrk[42].contents[0]}　Score:{lgrk[43].contents[0].strip()}\n3.{lgrk[44].contents[0]}　Score:{lgrk[45].contents[0].strip()}\n4.{lgrk[46].contents[0]}　Score:{lgrk[47].contents[0].strip()}\n5.{lgrk[48].contents[0]}　Score:{lgrk[49].contents[0].strip()}",inline=False)
  embed.add_field(name="コズミックDUP TOTAL", value=f"**1.{lgrk[60].contents[0]}　Score:{lgrk[61].contents[0].strip()}**\n2.{lgrk[62].contents[0]}　Score:{lgrk[63].contents[0].strip()}\n3.{lgrk[64].contents[0]}　Score:{lgrk[65].contents[0].strip()}\n4.{lgrk[66].contents[0]}　Score:{lgrk[67].contents[0].strip()}\n5.{lgrk[68].contents[0]}　Score:{lgrk[69].contents[0].strip()}",inline=True)
  await ctx.send(embed=embed)

@bot.command()
async def legrktp(ctx):
  html = requests.get(lrurl)
  soup = BeautifulSoup(html.content, "html.parser", from_encoding='utf-8')
  lgrk = soup.select('strong')
  lgrk2 = str(lgrk)
  embed=discord.Embed(title="レギオンランカーズ順位表（トレパレ TOTAL）",description=f"**1.{lgrk[0].contents[0]}　Score:{lgrk[1].contents[0].strip()}**\n2.{lgrk[2].contents[0]}　Score:{lgrk[3].contents[0].strip()}\n3.{lgrk[4].contents[0]}　Score:{lgrk[5].contents[0].strip()}\n4.{lgrk[6].contents[0]}　Score:{lgrk[7].contents[0].strip()}\n5.{lgrk[8].contents[0]}　Score:{lgrk[9].contents[0].strip()}",url="https://patolesoft.net/Games/PatnetResort/PatolePusherQuintessence/LegionRankers.php",color=0xfcba03)
  await ctx.send(embed=embed)

@bot.command()
async def legrkgjp(ctx):
  html = requests.get(lrurl)
  soup = BeautifulSoup(html.content, "html.parser", from_encoding='utf-8')
  lgrk = soup.select('strong')
  lgrk2 = str(lgrk)
  embed=discord.Embed(title="レギオンランカーズ順位表（ゴールデンJP TOTAL）",description=f"**1.{lgrk[20].contents[0]}　Score:{lgrk[21].contents[0].strip()}**\n2.{lgrk[22].contents[0]}　Score:{lgrk[23].contents[0].strip()}\n3.{lgrk[24].contents[0]}　Score:{lgrk[25].contents[0].strip()}\n4.{lgrk[26].contents[0]}　Score:{lgrk[27].contents[0].strip()}\n5.{lgrk[28].contents[0]}　Score:{lgrk[29].contents[0].strip()}",url="https://patolesoft.net/Games/PatnetResort/PatolePusherQuintessence/LegionRankers.php",color=0xfcba03)
  await ctx.send(embed=embed)

@bot.command()
async def legrkcf(ctx):
  html = requests.get(lrurl)
  soup = BeautifulSoup(html.content, "html.parser", from_encoding='utf-8')
  lgrk = soup.select('strong')
  lgrk2 = str(lgrk)
  embed=discord.Embed(title="レギオンランカーズ順位表（コズミックWIN TOTAL）",description=f"**1.{lgrk[40].contents[0]}　Score:{lgrk[41].contents[0].strip()}**\n2.{lgrk[42].contents[0]}　Score:{lgrk[43].contents[0].strip()}\n3.{lgrk[44].contents[0]}　Score:{lgrk[45].contents[0].strip()}\n4.{lgrk[46].contents[0]}　Score:{lgrk[47].contents[0].strip()}\n5.{lgrk[48].contents[0]}　Score:{lgrk[49].contents[0].strip()}",url="https://patolesoft.net/Games/PatnetResort/PatolePusherQuintessence/LegionRankers.php",color=0xfcba03)
  await ctx.send(embed=embed)

@bot.command()
async def legrkcfd(ctx):
  html = requests.get(lrurl)
  soup = BeautifulSoup(html.content, "html.parser", from_encoding='utf-8')
  lgrk = soup.select('strong')
  lgrk2 = str(lgrk)
  embed=discord.Embed(title="レギオンランカーズ順位表（コズミックDUP TOTAL）",description=f"**1.{lgrk[60].contents[0]}　Score:{lgrk[61].contents[0].strip()}**\n2.{lgrk[62].contents[0]}　Score:{lgrk[63].contents[0].strip()}\n3.{lgrk[64].contents[0]}　Score:{lgrk[65].contents[0].strip()}\n4.{lgrk[66].contents[0]}　Score:{lgrk[67].contents[0].strip()}\n5.{lgrk[68].contents[0]}　Score:{lgrk[69].contents[0].strip()}",url="https://patolesoft.net/Games/PatnetResort/PatolePusherQuintessence/LegionRankers.php",color=0xfcba03)
  await ctx.send(embed=embed)

@bot.command(aliases=["mrinfo"])
async def myriadinfo(ctx):
  html = requests.get(ppqstmy)
  soup = BeautifulSoup(html.content, "html.parser", from_encoding='utf-8')
  myi = soup.select_one('.big').text
  myi2 = soup.select('.big')
  print(f"{myi}")
  embed=discord.Embed(title="ミリアドJPゲーム情報",description=f"現在のミリアドJP枚数は**{myi.replace(',', '')}枚**です。\n次回のミリアドJPゲームは**2021年{myi2[1].contents[0].replace('-', '月').replace(' ', '日 ').replace(':00', '時').strip()}**に開催されます。\n現在の時刻は**{tme.strftime('%Y年%m月%d日 %H時%M分%S秒')}**です。",color=0x05b9e6)
  await ctx.send(embed=embed)
  
bot.run(TOKEN)
