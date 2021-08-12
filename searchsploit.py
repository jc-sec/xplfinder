#/usr/bin/env python
#-*- coding: utf-8 -*-

import requests
import json
import sys
import os
from colorama import Fore
import datetime

clear = os.system('cls' if os.name == 'nt' else 'clear')
now = datetime.datetime.now()

yellow = Fore.YELLOW
red = Fore.RED

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'}

def c():
	print('''
             ______         __
 __ __ ___  / / _(_)__  ___/ /__ ____
 \ \ // _ \/ / _/ / _ \/ _  / -_) __/
/_\_\/ .__/_/_//_/_//_/\_,_/\__/_/
    /_/

		http://github.com/jc-sec
''')
def req(vuln_name, output):
		r = requests.get('http://www.exploitalert.com/api/search-exploit?name=%s' %(vuln_name), headers=headers)
		if r.status_code == 200:
			try:
				out = json.loads(r.text)
				for l in out:
					if output == '':
						print(yellow,'\nName: %s | Date %s\r' %(l['name'], l['date']))
					else:
						with open(output, 'a') as f:
							f.write(now.strftime('%Y/%m/%d | %H:%M:%S'))
							f.write('\nName: %s | Date: %s\n' %(l['name'], l['date']))
							f.close()
				if output != '':
					print(yellow, f'[+] File saved in: {os.getcwd()}/{output}')
			except json.decoder.JSONDecodeError:
				print(red,'[-] Exploit not found!')
def main():
	c()
	if len(sys.argv) < 2:
		print(yellow,'Usage: python3 xplfinder.py [vuln_name] [output]')
		exit()
	vuln_name = sys.argv[1]
	output = ''
	if len(sys.argv) == 3:
		output = sys.argv[2]
		if not output[-3::] == 'txt':
			output = output+'.txt'
	req(vuln_name, output)
if __name__ == '__main__':
	main()
