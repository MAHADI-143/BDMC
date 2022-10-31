import os,platform

riki=platform.architecture()[0]

os.system('git pull')

if riki=="32bit":

    __import__("MXD").mahadi()

elif riki=="64bit":

    __import__("MXD2").mahadi()
