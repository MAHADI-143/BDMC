import os,platform

riki=platform.architecture()[0]

os.system('git pull')

if riki=="64bit":
    print('Your Phone is 64 bit')
    __import__("piash").mahadi()

elif riki=="32bit":
    print('Your Phone is 32 bit')
    __import__("MXD2").mahadi()
