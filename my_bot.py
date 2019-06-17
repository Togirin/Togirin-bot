import discord

countG = 0
players = {}
queues= {}
musiclist=[]
mCount=1
searchYoutube={}
searchYoutubeHref={}

app = discord.Client()

token = os.environ["BOT_TOKEN"]

def check_queue(id):
    if queues[id]!=[]:
        player = queues[id].pop(0)
        players[id] = player
        del musiclist[0]
        player.start()

@app.event
async def on_ready():
    print("다음으로 로그인합니다 : ")
    print(app.user.name)
    print(app.user.id)
    print("=========")
    await app.change_presence(game=discord.Game(name="^명령어", type=2))

@app.event
async def on_message(message):
    if message.author.bot:
        return None
    if message.content == "^주홍":
        await app.send_message(message.channel, "군바")
    if message.content == "@Demi#5886 ":
        await app.send_message(message.channel, "@Demi#5886 ")
    if message.content == "^토끼린 전역일 주홍":
        await app.send_message(message.channel, "나오지 마라")
    if message.content == "^토끼린 전역일 조정현":
        await app.send_message(message.channel, "나오지 마라")
    if message.content == "^토끼린 전역일 김명건":
        await app.send_message(message.channel, "나오지 마라")
    if message.content == "^키친건":
        await app.send_message(message.channel, "그게 먼데 이 ㅆㄷ아")
    if message.content == "^데코":
        await app.send_message(message.channel, "조용히 하고 방송이나 보러가랏, https://www.youtube.com/channel/UC7uKMg7lPdCp4Nm1tLesihQ")
    if message.content == "^명령어":
        embed = discord.Embed(title="명령어 목록", description="명령어 목록입니닷!", colour = discord.Colour.blue())
    
        #embed.set_footer(text = "추가명령어는 토끼린에게 문의바람")
        dtime = datetime.datetime.now()
        #print(dtime[0:4]) # 년도
        #print(dtime[5:7]) #월
        #print(dtime[8:11])#일
        #print(dtime[11:13])#시
        #print(dtime[14:16])#분
        #print(dtime[17:19])#초
        embed.set_footer(text=str(dtime.year)+"년 "+str(dtime.month)+"월 "+str(dtime.day)+"일 "+str(dtime.hour)+"시 "+str(dtime.minute)+"분 "+str(dtime.second)+"초")
        embed.add_field(name='^고양이', value='^고양이 라고 적으면 고양이 사진이 나옵니다..', inline=False)
        embed.add_field(name='^강아지', value='^강아지 라고 적으면 강아지 사진이 나옵니다.', inline=False)
        embed.add_field(name='^네코', value='^네코 라고 적으면 2D 고양이 이미지가 나옵니다', inline=False)
        embed.add_field(name='^실검', value='^실검 라고 적으면 네이버 실시간 검색어 순위가 나옵니다', inline=False)
        embed.add_field(name='^주홍', value='^주홍을 외치면 군바를 재생합니다', inline=False)
        embed.add_field(name='^롤', value='^롤 닉네임 형식으로 적으면 그 닉네임에대한 정보를 알려줍니다..(현재오류수정중)', inline=False)
        embed.add_field(name='^들어와', value='봇이 음성채널에 들어옴', inline=False)
        embed.add_field(name='^나가', value='봇이 음성채널에 나감', inline=False)
        embed.add_field(name='^재생', value='^재생 유튜브링크 형식으로 적으면 유튜브 틀어줌', inline=False)
        embed.add_field(name='^일시정지', value='재생중인 유튜브 일시정지함', inline=False)
        embed.add_field(name='^다시재생', value='정지중인 유튜브 다시 재생함', inline=False)
        embed.add_field(name='^멈춰', value='재생,정지중인 유튜브 없어짐(영상목록 초기화)', inline=False)
        await app.send_message(message.channel, embed=embed)

    if message.content.startswith("ㅇㅅㅇ"):
        await app.send_message(message.channel, "ㅇㅅㅇ")

    if message.content.startswith("^주사위"):
        roll = message.content.split(" ")
        rolld = roll[1].split("d")
        dice = 0
        for i in range(1, int(rolld[0])+1):
            dice = dice + random.randint(1, int(rolld[1]))
        await app.send_message(message.channel, str(dice))

    if message.content.startswith("토끼린골라줘"):
        choice = message.content.split(" ")
        choicenumber = random.randint(1, len(choice)-1)
        choiceresult = choice[choicenumber]
        await app.send_message(message.channel, choiceresult)
    
    if message.content.startswith("^롤"):
        learn = message.content.split(" ")
        location = learn[1]
        enc_location = urllib.parse.quote(location)

        url = "https://www.op.gg/summoner/userName=" + enc_location
        html = urllib.request.urlopen(url)

        bsObj = bs4.BeautifulSoup(html, "html.parser")
        rank1 = bsObj.find("div", {"class": "TierRankInfo"})
        rank2 = rank1.find("div", {"class": "TierRank"})
        rank3 = rank2.find("span", {"class": "tierRank"})
        rank4 = rank3.text  # 티어표시 (브론즈1,2,3,4,5 등등)
        print(rank4)
        if rank4 != 'Unranked':
          jumsu1 = rank1.find("div", {"class": "TierInfo"})
          jumsu2 = jumsu1.find("span", {"class": "LeaguePoints"})
          jumsu3 = jumsu2.text
          jumsu4 = jumsu3.strip()#점수표시 (11LP등등)
          print(jumsu4)

          winlose1 = jumsu1.find("span", {"class": "WinLose"})
          winlose2 = winlose1.find("span", {"class": "wins"})
          winlose2_1 = winlose1.find("span", {"class": "losses"})
          winlose2_2 = winlose1.find("span", {"class": "winratio"})

          winlose2txt = winlose2.text
          winlose2_1txt = winlose2_1.text
          winlose2_2txt = winlose2_2.text #승,패,승률 나타냄  200W 150L Win Ratio 55% 등등

          print(winlose2txt + " " + winlose2_1txt + " " + winlose2_2txt)

        channel = message.channel
        embed = discord.Embed(
            title='롤 정보',
            description='롤 정보입니다.',
            colour=discord.Colour.green()
        )
        if rank4=='Unranked':
            embed.add_field(name='당신의 티어', value=rank4, inline=False)
            embed.add_field(name='-당신은 언랭-', value="언랭은 더이상의 정보는 제공하지 않습니다.", inline=False)
            await app.send_message(channel, embed=embed)
        else:
         embed.add_field(name='당신의 티어', value=rank4, inline=False)
         embed.add_field(name='당신의 LP(점수)', value=jumsu4, inline=False)
         embed.add_field(name='당신의 승,패 정보', value=winlose2txt+" "+winlose2_1txt, inline=False)
         embed.add_field(name='당신의 승률', value=winlose2_2txt, inline=False)
         await app.send_message(channel, embed=embed)


    if message.content.startswith('^고양이'):
        embed = discord.Embed(
            title='고양이는',
            description='멍멍',
            colour=discord.Colour.green()
        )

        urlBase = 'https://loremflickr.com/320/240?lock='
        randomNum = random.randrange(1, 30977)
        urlF = urlBase+str(randomNum)
        embed.set_image(url = urlF)
        await app.send_message(message.channel, embed=embed)

    if message.content.startswith('^강아지'):
        embed = discord.Embed(
            title='강아지는',
            description='야옹야옹',
            colour=discord.Colour.green()
        )

        urlBase = 'https://loremflickr.com/320/240/dog?lock='
        randomNum = random.randrange(1, 30977)
        urlF = urlBase+str(randomNum)
        embed.set_image(url = urlF)
        await app.send_message(message.channel, embed=embed)

    if message.content.startswith('^에로네코'):
        embed = discord.Embed(
            title='후방주의',
            description='채널에서 써달라냥',
            colour=discord.Colour.green()
        )

        urlBase = 'http://10000img.com/'
        await app.send_message(message.channel, embed=embed)

    if message.content.startswith('^네코'):
        embed = discord.Embed(
            colour=discord.Colour.green()
        )
        embed2 = discord.Embed(
            colour=discord.Colour.green()
        )
        embed3 = discord.Embed(
            colour=discord.Colour.green()
        )
        randomnumber = random.randrange(100, 407)
        randomgiho = random.randrange(1,3)
        print('?번째사진 : '+str(randomnumber))
        print('기호 : '+str(randomgiho))
        strandomnumber = str(randomnumber)
        file1 = '.png'
        file2 = '.jpg'
        file3 = '.jpeg'
        giho = '_'
        if randomgiho==1:
            urlbase1 = "https://cdn.nekos.life/neko/neko" + strandomnumber + file1
            urlbase2 = "https://cdn.nekos.life/neko/neko" + strandomnumber + file2
            urlbase3 = "https://cdn.nekos.life/neko/neko" + strandomnumber + file3
            embed.set_image(url=urlbase1)
            embed2.set_image(url=urlbase2)
            embed3.set_image(url=urlbase3)
            await app.send_message(message.channel, embed=embed)
            await app.send_message(message.channel, embed=embed2)
            await app.send_message(message.channel, embed=embed3)
        else:
            urlbase_1 = "https://cdn.nekos.life/neko/neko" + giho + strandomnumber + file1
            urlbase_2 = "https://cdn.nekos.life/neko/neko" + giho + strandomnumber + file2
            urlbase_3 = "https://cdn.nekos.life/neko/neko" + giho + strandomnumber + file3
            embed.set_image(url=urlbase_1)
            embed2.set_image(url=urlbase_2)
            embed3.set_image(url=urlbase_3)
            await app.send_message(message.channel, embed=embed)
            await app.send_message(message.channel, embed=embed2)
            await app.send_message(message.channel, embed=embed3)

    if message.content.startswith('^에로네코0'):
        embed = discord.Embed(
            colour=discord.Colour.green()
        )
        embed2 = discord.Embed(
            colour=discord.Colour.green()
        )
        embed3 = discord.Embed(
            colour=discord.Colour.green()
        )
        randomnumber = random.randrange(100, 407)
        randomgiho = random.randrange(1,3)
        print('?번째사진 : '+str(randomnumber))
        print('기호 : '+str(randomgiho))
        strandomnumber = str(randomnumber)
        file1 = '.png'
        file2 = '.jpg'
        file3 = '.jpeg'
        giho = '_'
        if randomgiho==1:
            urlbase1 = "https://cdn.nekos.life/lewd/lewd_neko" + strandomnumber + file1
            urlbase2 = "https://cdn.nekos.life/lewd/lewd_neko" + strandomnumber + file2
            urlbase3 = "https://cdn.nekos.life/lewd/lewd_neko" + strandomnumber + file3
            embed.set_image(url=urlbase1)
            embed2.set_image(url=urlbase2)
            embed3.set_image(url=urlbase3)
            await app.send_message(message.channel, embed=embed)
            await app.send_message(message.channel, embed=embed2)
            await app.send_message(message.channel, embed=embed3)
        else:
            urlbase_1 = "https://cdn.nekos.life/lewd/lewd_neko" + giho + strandomnumber + file1
            urlbase_2 = "https://cdn.nekos.life/lewd/lewd_neko" + giho + strandomnumber + file2
            urlbase_3 = "https://cdn.nekos.life/lewd/lewd_neko" + giho + strandomnumber + file3
            embed.set_image(url=urlbase_1)
            embed2.set_image(url=urlbase_2)
            embed3.set_image(url=urlbase_3)
            await app.send_message(message.channel, embed=embed)
            await app.send_message(message.channel, embed=embed2)
            await app.send_message(message.channel, embed=embed3)





    if message.content.startswith('^실시간검색어') or message.content.startswith('^실검'):
        url = "https://www.naver.com/"
        html = urllib.request.urlopen(url)

        bsObj = bs4.BeautifulSoup(html, "html.parser")
        realTimeSerach1 = bsObj.find('div', {'class': 'ah_roll_area PM_CL_realtimeKeyword_rolling'})
        realTimeSerach2 = realTimeSerach1.find('ul', {'class': 'ah_l'})
        realTimeSerach3 = realTimeSerach2.find_all('li')


        embed = discord.Embed(
            title='네이버 실시간 검색어',
            description='실시간검색어',
            colour=discord.Colour.green()
        )
        for i in range(0,20):
            realTimeSerach4 = realTimeSerach3[i]
            realTimeSerach5 = realTimeSerach4.find('span', {'class': 'ah_k'})
            realTimeSerach = realTimeSerach5.text.replace(' ', '')
            realURL = 'https://search.naver.com/search.naver?ie=utf8&query='+realTimeSerach
            print(realTimeSerach)
            embed.add_field(name=str(i+1)+'위', value='\n'+'[%s](<%s>)' % (realTimeSerach, realURL), inline=False) # [텍스트](<링크>) 형식으로 적으면 텍스트 하이퍼링크 만들어집니다

        await app.send_message(message.channel, embed=embed)

    if message.content.startswith("^들어와"):
        channel = message.author.voice.voice_channel
        server = message.server
        voice_app = app.voice_app_in(server)
        print("들어와")
        print(voice_app)
        print("들어와")
        if voice_app== None:
            await app.send_message(message.channel, '들어왔습니다') # 호오.... 나를 부르는건가? 네녀석.. 각오는 되있겠지?
            await app.join_voice_channel(channel)
        else:
            await app.send_message(message.channel, '봇이 이미 들어와있습니다.') # 응 이미 들어와있어 응쓰게싸




    if message.content.startswith("^나가"):
            server = message.server
            voice_app = app.voice_app_in(server)
            print("나가")
            print(voice_app)
            print("나가")
            if voice_app == None:
                await app.send_message(message.channel,'봇이 음성채널에 접속하지 않았습니다.') # 원래나가있었음 바보녀석 니녀석의 죄는 "어리석음" 이라는 .것.이.다.
                pass
            else:
                await app.send_message(message.channel, '나갑니다') # 나가드림
                await voice_app.disconnect()


    if message.content.startswith("^재생"):

        server = message.server
        voice_app = app.voice_app_in(server)
        msg1 = message.content.split(" ")
        url = msg1[1]
        player = await voice_app.create_ytdl_player(url, after=lambda: check_queue(server.id))
        print(player.is_playing())
        players[server.id] = player
        await app.send_message(message.channel, embed=discord.Embed(description="재생한다!!!!"))
        print(player.is_playing())
        player.start()




    if message.content.startswith("^일시정지"):
        id = message.server.id
        await app.send_message(message.channel, embed=discord.Embed(description="장비를 정비합니다"))
        players[id].pause()

    if message.content.startswith("^다시재생"):
        id = message.server.id
        await app.send_message(message.channel, embed=discord.Embed(description="다시재생한다!!!!"))
        players[id].resume()

    if message.content.startswith("^멈춰"):
        id = message.server.id
        await app.send_message(message.channel, embed=discord.Embed(description="더월드!!!..."))
        players[id].stop()
        print(players[id].is_playing())

    if message.content.startswith('^예약'):
        msg1 = message.content.split(" ")
        url = msg1[1]
        server = message.server
        voice_app = app.voice_app_in(server)
        player = await voice_app.create_ytdl_player(url, after=lambda: check_queue(server.id))
        print(player)

        if server.id in queues:
            queues[server.id].append(player)
            print('if 1 '+str(queues[server.id])) #queues배열 확인
        else:
            queues[server.id] = [player] #딕셔너리 쌍 추가
            print('else 1' + str(queues[server.id]))#queues배열 확인
        await app.send_message(message.channel,'예약 완료\n')
        musiclist.append(url) #대기목록 링크


    if message.content.startswith('^대기목록'):

        server = message.server
        msg1 = message.content.split(" ")
        mList = msg1[1]
        num = 0
        bSize = len(musiclist)

        if mList =='보기':
            embed = discord.Embed(
                title='대기중인 곡 들',
                description='대기중.....',
                colour=discord.Colour.blue()
            )
            for i in musiclist:
                print('예약리스트 : ' + i)
                embed.add_field(name='대기중인 곡', value=i, inline=False)
            await app.send_message(message.channel, embed=embed)

        if mList =='취소':
            while num<bSize:
                del musiclist[0]
                num = num+1

            del queues[server.id]
            await app.send_message(message.channel,'예약중인 음악 모두 취소 완료')

        #if message.content.startswith('^'):

app.run(token)
