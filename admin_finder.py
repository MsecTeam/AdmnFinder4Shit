import os,sys
import argparse
import requests as r
from colorama import Fore

os.system("clear")

parser = argparse.ArgumentParser()
wordlist = open("main/wordlist.txt")
list = wordlist.readlines()

print('''

      ___           ___           ___                       ___     
     /\  \         /\  \         /\__\          ___        /\__\    
    /::\  \       /::\  \       /::|  |        /\  \      /::|  |   
   /:/\:\  \     /:/\:\  \     /:|:|  |        \:\  \    /:|:|  |   
  /::\~\:\  \   /:/  \:\__\   /:/|:|__|__      /::\__\  /:/|:|  |__ 
 /:/\:\ \:\__\ /:/__/ \:|__| /:/ |::::\__\  __/:/\/__/ /:/ |:| /\__\    
 \/__\:\/:/  / \:\  \ /:/  / \/__/~~/:/  / /\/:/  /    \/__|:|/:/  /
      \::/  /   \:\  /:/  /        /:/  /  \::/__/         |:/:/  / 
      /:/  /     \:\/:/  /        /:/  /    \:\__\         |::/  /  
     /:/  /       \::/__/        /:/  /      \/__/         /:/  /   
     \/__/         ~~            \/__/                     \/__/    

[+] Author : VarelSecurity

''')
parser.add_argument('-u','--url', type=str, required=True, help="Masukan URL")
parser.add_argument('-o','--output', type=str, required=True, help="Masukan Output (eg: output.txt)")
args = parser.parse_args()

os.system("clear")
print (Fore.LIGHTCYAN_EX, '''

      ___           ___           ___                       ___     
     /\  \         /\  \         /\__\          ___        /\  \    
    /::\  \       /::\  \       /:/  /         /\  \       \:\  \   
   /:/\:\  \     /:/\ \  \     /:/__/          \:\  \       \:\  \  
  /::\~\:\  \   _\:\~\ \  \   /::\  \ ___      /::\__\      /::\  \ 
 /:/\:\ \:\__\ /\ \:\ \ \__\ /:/\:\  /\__\  __/:/\/__/     /:/\:\__\    
 \/_|::\/:/  / \:\ \:\ \/__/ \/__\:\/:/  / /\/:/  /       /:/  \/__/
    |:|::/  /   \:\ \:\__\        \::/  /  \::/__/       /:/  /     
    |:|\/__/     \:\/:/  /        /:/  /    \:\__\       \/__/      
    |:|  |        \::/  /        /:/  /      \/__/                  
     \|__|         \/__/         \/__/                         

[+] Pasive Admin Login Finder
[+] Author : VarelSecurity
''')
print (f"[+] Url Website : {args.url}")
print (f"[+] Output file : {args.output}")
print()
for i in list:
    line = i.strip()
    req = r.get(f'{args.url}{line}')
    if req.status_code ==200:
        print (Fore.LIGHTGREEN_EX, f"(status: {req.status_code}) (size: {len(req.content)}) {args.url}{line}")
        f = open(f"{args.output}", "a")
        f.write(f"(status: {req.status_code}) (size: {len(req.content)}) {args.url}{line}\n")
        f.close()

