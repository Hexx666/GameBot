import requests , random 
from os import name , system 
from hashlib import md5

if name == 'nt':
    system('cls') # Cleaning the terminal in Windows
elif name == 'posix':
    system('clear') # Cleaning the terminal in Linux&Unix base

print("""
⢿⣿⣿⣿⣭⠹⠛⠛⠛⢿⣿⣿⣿⣿⡿⣿⠷⠶⠿⢻⣿⣛⣦⣙⠻⣿
⣿⣿⢿⣿⠏⠀⠀⡀⠀⠈⣿⢛⣽⣜⠯⣽⠀⠀⠀⠀⠙⢿⣷⣻⡀⢿      
⠐⠛⢿⣾⣖⣤⡀⠀⢀⡰⠿⢷⣶⣿⡇⠻⣖⣒⣒⣶⣿⣿⡟⢙⣶⣮      
⣤⠀⠀⠛⠻⠗⠿⠿⣯⡆⣿⣛⣿⡿⠿⠮⡶⠼⠟⠙⠊⠁⠀⠸⢣⣿      
⣿⣷⡀⠀⠀⠀⠀⠠⠭⣍⡉⢩⣥⡤⠥⣤⡶⣒⠀⠀⠀⠀⠀⢰⣿⣿
⣿⣿⡽⡄⠀⠀⠀⢿⣿⣆⣿⣧⢡⣾⣿⡇⣾⣿⡇⠀⠀⠀⠀⣿⡇⠃
⣿⣿⣷⣻⣆⢄⠀⠈⠉⠉⠛⠛⠘⠛⠛⠛⠙⠛⠁⠀⠀⠀⠀⣿⡇⢸
⢞⣿⣿⣷⣝⣷⣝⠦⡀⠀⠀⠀⠀⠀⠀⠀⡀⢀⠀⠀⠀⠀⠀⠛⣿⠈
⣦⡑⠛⣟⢿⡿⣿⣷⣝⢧⡀⠀⠀⣶⣸⡇⣿⢸⣧⠀⠀⠀⠀⢸⡿⡆
⣿⣿⣷⣮⣭⣍⡛⠻⢿⣷⠿⣶⣶⣬⣬⣁⣉⣀⣀⣁⡤⢴⣺⣾⣽⡇
""")


session = requests.session()
session.headers = {
    "Referer": "https://prizes.gamee.com/"
}
#===============================================================

Game_Url = input("\033[0mKntlCheat\033[2;31;5m( GameUrl )\033[0;m > \033[96m")

Game_Hash = ((Game_Url.split("#")[0]).split("/")[3:])[1]

#===============================================================
data =  session.post("https://api.service.gameeapp.com/" , json={
        "jsonrpc":"2.0",
        "id":"game.getWebGameplayDetails",
        "method":"game.getWebGameplayDetails",
        "params":{
            "gameUrl":f"/game-bot/{Game_Hash}"

        }}).json()

gameid = data['result']['game']['id']
release = data['result']['game']['release']['number']
#===============================================================

auth_load = {
    "jsonrpc":"2.0",
    "id":"user.authentication.botLogin",
    "method":"user.authentication.botLogin",
    "params":{
        "botName":"telegram",
        "botGameUrl":f"/game-bot/{Game_Hash}",
        "botUserIdentifier":None
    }
}

auth_r = requests.post("https://api.service.gameeapp.com/" , headers={
    "Content-Type":"application/json",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45", 
    "X-Install-Uuid":"23ce11ca-a85d-4540-a4b2-89d32d76623a"
    } , json=auth_load).json()

authni = auth_r['result']['tokens']['refresh']

session.headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36",
    "authorization":"Bearer %s"%authni,
    "Content-Type":"application/json"
    }


#-------------------------------
time = data['time']
playtime = random.randint(300,2000)

score = input("\033[0mFoxCheat\033[2;31;5m( YourScore )\033[0;m > \033[96m")
gameStateData = ''


hashs1 =  md5(f'{str(score)}:{str(playtime)}:/game-bot/{Game_Hash}:{gameStateData}:crmjbjm3lczhlgnek9uaxz2l9svlfjw14npauhen'.encode()).hexdigest()



result = session.post("https://api.service.gameeapp.com/" , json={
    "jsonrpc":"2.0",
    "id":"game.saveWebGameplay",
    "method":"game.saveWebGameplay",
    "params":{
        "gameplayData":{
                "gameId":int(gameid),
                "score":int(score),
                "playTime":int(playtime),
                "gameUrl":f"/game-bot/{Game_Hash}",
                "metadata":{"gameplayId":3},
                "releaseNumber":int(release),
                "gameStateData":None,
                "createdTime":"%s"%time,
                "checksum":hashs1,
                "replayVariant":None,
                "replayData":None,
                "replayDataChecksum":None,
                "isSaveState":False,
                "gameplayOrigin":"game"
        }
    }
}).json()

main = result['result']['surroundingRankings'][0]['ranking']
for user in main[::-1]:
    print(f"\033[96m========\033[32m[ \033[91m{user['rank']} \033[32m]\033[96m========")
    print(f"""
\033[93mNumId     \033[91m: \033[32m{user['user']['id']}
\033[93mFirstName \033[91m: \033[32m{user['user']['firstname']}
\033[93mLastName  \033[91m: \033[32m{user['user']['lastname']}
\033[93mNickName  \033[91m: \033[32m{user['user']['nickname']}
\033[93mScore     \033[91m: \033[32m{user['score']}  
""")

