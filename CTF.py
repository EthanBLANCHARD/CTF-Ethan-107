from colorama import Back, Fore, init, Style
import os

Flag_base = {"F1":"PASS01",
             "F2":"LOYOLA",
             "F3":"Rami MALEK",
             "F4":"linkinpark",
             "F5":"Domino Park",
             "F6":"https://lesjouxjouxdewilly.us",
             "F7":"AlGo269$",
             "F8":"28111977@rgh",
             "F9":"FSOCIETY01",
             "F10":"2159035789"}

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
    print("Un lien de téléchargement du niveau suivant vous sera remis après chaque flag donné.")
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
                print("Lien vers la première épreuve:"+ Fore.YELLOW + " https://mega.nz/file/SBkSnCxD#xaGmTrS6fVZbv0-ZbywOTzA7RBvQ4PXZYyroKQtG6G4" + Fore.WHITE)
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
                            print("Lien vers la deuxième épreuve:"+ Fore.YELLOW + " https://mega.nz/file/XFEyBb4a#H1cuELoVm3h7xFNEmsym8pvSbzBqaoiu0xQDq-gIM3s" + Fore.WHITE)
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
                            print("Lien vers la troisième épreuve:"+ Fore.YELLOW + " https://mega.nz/file/aE1XWbpK#ucQSNWq_mZlTJy1enB3pvEI2TzGSZVxzuWNn4xBIfZs" + Fore.WHITE)
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
                            print("Lien vers la quatrième épreuve:"+ Fore.YELLOW + " https://mega.nz/file/LZ8HXCwC#kPqJgbCjEBM0gf2VCdNuIAAUvKMZP0Z7FTiuBHf3-j8" + Fore.WHITE)
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
                            print("Lien vers la cinquième épreuve:" + Fore.YELLOW + " https://mega.nz/file/rcETVIyY#hCyq_ShEziDLxzZ1uui5yYFqOJ4zRVMoIqWjwipwUOA" + Fore.WHITE)
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
                            print("Lien vers la sixième épreuve:"+ Fore.YELLOW + " https://mega.nz/file/XR9lzZLB#9a9ST1ayXixUtV9J3HHWYTHM9zXnB3F_fTosJ6MSl2c" + Fore.WHITE)
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
                            print("Lien vers la septième épreuve:"+ Fore.YELLOW + " https://mega.nz/file/6Bd0jTqa#8iE-2BktnQ0v86GNRLLpHmz8RL-ekdBUbj3gTA7HY3E" + Fore.WHITE)
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
                            print("Lien vers la huitième épreuve:"+ Fore.YELLOW + " https://mega.nz/file/fFUzRZCZ#3aO6BX-8kAIgybJ1jytgeaB_TTV_QQWrzcXIGN3IWNc" + Fore.WHITE)
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
                            print("Lien vers la neuvième épreuve:"+ Fore.YELLOW + " https://mega.nz/file/jQkGDJoZ#qRG7F_Yj0Gf2zMLKZ0SxXx1HDr21XwwhqERPWSNrJ48" + Fore.WHITE)
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
                            print("Lien vers la dixième épreuve:"+ Fore.YELLOW + " https://mega.nz/file/TZNDQaYA#vJqUdtjs1By6wLFdXKwe3gG3jpgn65-bLPTnv-class" + Fore.WHITE )
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
