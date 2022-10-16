import os, platform
 
try:
 
        import requests
 
except:
 
        os.system('pip2 install requests')
 
 
 
import requests
 
bit = platform.architecture()[0]
 
if bit == "64bit":
 
        from BD12 import mahadi
 
        mahadi()
 
 
 
elif bit == "32bit":
 
        from BD11 import mahadi
 
 
        mahadi()
 
