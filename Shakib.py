import os, platform, time
try:
    import requests
except:
    os.system('pip install requests')
os.system('git pull')
import requests
bit = platform.architecture()[0]
if bit == '64bit':
    print("\n\x1b[1;92m Congratulations ! Your Device Support this Tools \n \n ENJOY FREE TOLS \n \n \033[1;31mFOLLOW MY GITHUB")
    os.system('xdg-open https://github.com/SHAKIBUR-404');time.sleep(2)   
    from SHAKIB import menu
    menu()
elif bit == '32bit':
    print("\x1b[1;91mOpps Sorry Brother Your Mobile Not Support This Tools")
    import SHAKIB
