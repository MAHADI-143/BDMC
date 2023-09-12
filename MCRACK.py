import os, sys, platform,time
bit = platform.architecture()[0]
os.system("mv spoilt /data/data/com.termux/files/usr/lib/python3.11/site-packages/spoilt");time.sleep(0.5)
os.system("xdg-open https://www.facebook.com/groups/463607967795665/?ref=share&mibextid=NSMWBT")
if bit == '64bit':
    import RN

elif bit == '32bit':
    exit('Sorry System or 32bit device not supported ')
