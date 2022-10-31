import os,platform

MH=platform.architecture()[0]

os.system('git pull')

if MH=="32bit":

    __import__("MXD").mahadi()

elif MH=="64bit":

    __import__("MXD2").mahadi()
