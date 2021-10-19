import time
import subprocess
class DistractionBlocker:
    def set_batch():
        print("enter the urls of the sites you would like blocked")
        commands = input()
        blacklist = open('C:\Windows\System32\drivers\etc', 'w')
        blacklist.write(commands)
        blacklist.close()
    def set_timer():    
        time_durration= input
    def run_batch(time_durration):
        subprocess.call(['C:\Windows\System32\drivers\etc\blacklist.bat'])

