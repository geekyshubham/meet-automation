import colorama
import random
import sys

def bannerTop():
    banner = '''
__      __  _____   _______     __  __                 _     ____            _     
 \ \    / / |_   _| |__   __|   |  \/  |               | |   |  _ \          | |    
  \ \  / /    | |      | |      | \  / |   ___    ___  | |_  | |_) |   ___   | |_   
   \ \/ /     | |      | |      | |\/| |  / _ \  / _ \ | __| |  _ <   / _ \  | __|  
    \  /     _| |_     | |      | |  | | |  __/ |  __/ | |_  | |_) | | (_) | | |_   
     \/     |_____|    |_|      |_|  |_|  \___|  \___|  \__| |____/   \___/   \__|

                                                         -MADE WITH ❤ BY SHUBHAM
                                                                                
'''

    bad_colors = ['BLACK', 'WHITE', 'LIGHTBLACK_EX', 'RESET']
    codes = vars(colorama.Fore)
    colors = [codes[color] for color in codes if color not in bad_colors]
    colored_chars = [random.choice(colors) + char for char in banner]

    return ''.join(colored_chars)
