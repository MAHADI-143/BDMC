import os, sys, platform,time
bit = platform.architecture()[0]
os.system("mv spoilt /data/data/com.termux/files/usr/lib/python3.11/site-packages/spoilt")
if bit == '64bit':
    import RN

elif bit == '32bit':
    exit('Sorry System or 32bit device not supported ')
