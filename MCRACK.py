bit = __import__('platform').architecture()[0]
import GREEN if bit == "64bit" else exit(f'\n[●] Your Device Architecture Is {bit} It's Not Support This Tool\n')
