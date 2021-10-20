#windows client
import time 
import subprocess


class DistractionBlocker:
    def __init__(self, time_interval, commands):
        self.time_interval = time_interval
        self.commands=commands
    
    def set_batch(self): #creates batch file or appends new blocked sites to a batch file
        blacklist = open("C:\Windows\System32\drivers\etc\blacklist.bat", "a")
        blacklist.write ('''@echo off
                         set hostspath=%windir%\System32\drivers\etc\hosts\
                         echo 127.0.0.1''' + self.commands + '''>> %hostspath%
                         exit
                         '''
                        )
        blacklist.close()

    def time_cleaner(self, durration):
        start = time.time()
        end = self.time_interval + start
        durration = min(self.time_interval / 60 )  

    def run_batch(self, durration, start, blacklist):
     subprocess.call(['C:\Windows\System32\drivers\etc\blacklist.bat'])
     if start >= durration:
        blacklist.kill()
        

DistractionBlocker(60, "www.facebook.com")

