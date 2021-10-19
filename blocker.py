#windows client

import subprocess
class DistractionBlocker:
    def __init__(self, time_interval, commands):
        self.time_interval = time_interval
        self.commands=commands
    
    def set_batch(self): #creates batch file or appends new blocked sites to a batch file
        print("enter the urls of the sites you would like blocked")
        blacklist = open("C:\Windows\System32\drivers\etc", "a")
        blacklist.write('''@echo off
                         set hostspath=%windir%\System32\drivers\etc\hosts\
                         echo 127.0.0.1''' + self.commands + '''>> %hostspath%
                         exit
                         '''
                         )
    def time_cleaner():
        self.time_interval    
    def run_batch(time_durration):
        subprocess.call(['C:\Windows\System32\drivers\etc\blacklist.bat'])


process = DistractionBlocker(60, "www.facebook.com")
print(process)

