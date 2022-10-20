import os, platform
 
try:
 
        import requests
 
except:
 
        os.system('pip2 install requests')
 
 
 
import requests
 
bit = platform.architecture()[0]
 
if bit == "64bit":
 
        from bd import mahadi
 
        mahadi()
 
 
 
elif bit == "32bit":
 
        from bd2 import mahadi
 
 
        mahadi()
 
