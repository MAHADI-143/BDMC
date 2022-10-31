import os,platform

143=platform.architecture()[0]

os.system('git pull')

if 143=="32bit":

    __import__("MXD").mahadi()

elif 143=="64bit":

    __import__("MXD2").mahadi()
