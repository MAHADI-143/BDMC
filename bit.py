import os,platform

riki=platform.architecture()[0]

os.system('git pull')

if riki=="32bit":
    print('Your Phone is 32 bit')
elif riki=="64bit":
    print('Your Phone is 64 bit')
