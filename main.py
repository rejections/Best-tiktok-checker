#this does not work anymore
try:
    from discord_webhook import DiscordWebhook, DiscordEmbed
    import requests, ctypes, time, os, threading, platform
    from colorama import Fore
except ImportError:
    input("Error while importing modules. Please install the modules in requirements.txt")
    
    
#banned detection not working, change status codes



if platform.system() == "Windows":
    clear = "cls"
else:
    clear = "clear"

class tiktok:

    def __init__(self):
        self.lock = threading.Lock()
        self.checking = True
        self.usernames = []
        self.proxies = []
        self.unavailable = 0
        self.available = 0
        self.counter = 0

    def load_proxies(self):
        if not os.path.exists("proxies.txt"):
            self.print_console("File proxies.txt not found")
            time.sleep(10)
            os._exit(0)
        with open("proxies.txt", "r", encoding = "UTF-8") as f:
            for line in f.readlines():
                line = line.replace("\n", "")
                self.proxies.append(line)
            if not len(self.proxies):
                self.print_console("No proxies loaded in proxies.txt")
                time.sleep(10)
                os._exit(0)

    def update_title(self):
        remaining = len(self.usernames) - (self.available + self.unavailable)
        ctypes.windll.kernel32.SetConsoleTitleW(
            f"sigma claimer | 404: {self.available} | 200: {self.unavailable} | checked: {(self.available + self.unavailable)} | remaining: {remaining} | Developed by @useragents on Github"
        )
    
    def safe_print(self, arg):
        self.lock.acquire()
        print(arg)
        self.lock.release()
    
    def print_console(self, status, arg, color = Fore.RED):
        self.safe_print(f"       {Fore.WHITE}[{color}{status}{Fore.WHITE}] {arg}")
    
    def check_username(self, username, proxies):
        if username.isdigit():
            self.unavailable += 1
            self.print_console("TAKEN", username)
            return
        with requests.Session() as session:
            proxies = {"https": "http://{}".format(proxies)}
            headers = {
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36",
                "accept-encoding": "gzip, deflate, br",
                "accept-language": "en-US",
                "content-type": "application/json"
            }

            r = session.get("https://www.tiktok.com/@{}".format(username), headers = headers, proxies = proxies)

            if r.status_code == 200:
                self.unavailable += 1
                self.print_console("TAKEN", username)
                with open("iii.txt", "a") as f:
                        f.write(username + "\n")
            elif r.status_code == 404:
                self.available += 1
                self.print_console("POSSIBLE CLAIM", username, Fore.GREEN)
                webhook = DiscordWebhook(url='https://discord.com/api/webhooks/971408343782539324/OsjhKea3Q6x_OW5sdFNRCW2LFN5iQFW3Zni-bEoeiSuBVdBxHpJHpf2xHjPOYaYcEmFd', username="Autoclaimer")
                embed = DiscordEmbed(title='bruh', description='2fast', color='03b2f8')
                embed.set_author(name='tiktoky usernamy autoclaimy', url='https://github.com/rejections', icon_url='https://ih1.redbubble.net/image.3028756260.2658/st,small,507x507-pad,600x600,f8f8f8.jpg')
                embed.set_footer(text='blahblah')
                embed.set_timestamp()
                embed.add_embed_field(name='Username', value='{}'.format(username))
                embed.add_embed_field(name='Status Code', value='{}'.format(r.status_code))
                webhook.add_embed(embed)
                response = webhook.execute()
                with open("2laa1.txt", "a") as f:
                        f.write(username + "\n")
                        self.update_title()
 
    def load_usernames(self):
        with open("ii.txt", "r", encoding = "UTF-8") as f:
            for line in f.readlines():
                line = line.replace("\n", "")
                self.usernames.append(line)
    
    def main(self):
        os.system(clear)
        if clear == "cls":
            ctypes.windll.kernel32.SetConsoleTitleW("tiktoky usernamy checkerino")
        self.load_proxies()
        self.load_usernames()
        threads = int(input(f"       {Fore.WHITE}[{Fore.RED}Console{Fore.WHITE}] Threads: "))
        print()
        
        def thread_starter():
            self.check_username(self.usernames[self.counter], self.proxies[self.counter])


        while self.checking:
            if threading.active_count() <= threads:
                try:
                    threading.Thread(target = thread_starter).start()
                    self.counter += 1
                except:
                    pass
                if len(self.usernames) <= self.counter:
                    self.counter = 0

obj = tiktok()
obj.main()
input()
