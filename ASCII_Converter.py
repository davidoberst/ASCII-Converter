import pyfiglet
from colorama import Fore,Style
import time
import cv2
import os
#------------------BANNER--------------------
print(Fore.RED + pyfiglet.figlet_format("ASCII Converter", font="small").rstrip() + Style.RESET_ALL)
time.sleep(0.5)
print("")
print(Fore.YELLOW + "v.0.0.1 | by davidoberst | https://github.com/davidoberst" + Style.RESET_ALL)
print("-"*58)
time.sleep(1)

#----Select and Proccess the IMG-------------
def proccessIMG():
 path = input(Fore.BLUE +"[::] Enter the path to your image! : " + Style.RESET_ALL) #IMG path
 time.sleep(1)
 imgName = os.path.basename(path) #IMG NAME
 time.sleep(1) ; print(Fore.CYAN + f"Converting {imgName}..." + Style.RESET_ALL)
 time.sleep(15)
 cv2.imread(path)
 


proccessIMG()
