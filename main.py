import requests
import time
import json
import os


os.system('clear')

M = "\033[31;1m"
print('''
╭╮╱╱╱╱╭╮╱╱╭╮╱╱╱╱╱╭╮
┃┃╱╱╱╱┃┃╱╱┃┃╱╱╱╱╱┃┃
┃╰━┳━━┫╰━┳┫╰━┳┳━━┫╰━┳━━┳╮╱╭╮
┃╭╮┃╭╮┃╭╮┣┫╭╮┣┫╭╮┃╭╮┃╭╮┃┃╱┃┃s
┃┃┃┃╭╮┃╰╯┃┃╰╯┃┃╭╮┃╰╯┃╰╯┃╰━╯┃
╰╯╰┻╯╰┻━━┻┻━━┻┻╯╰┻━━┻━━┻━╮╭╯
╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╭━╯┃
╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╰━━╯
''')

print(35*'=')

url='https://api.banghasan.com//quran/format/json/surat'
response=requests.get(url)
jsonData=json.loads(response.text)
j=0

print('Al Quran Indonesia')

for data in jsonData['hasil']:
    j += 1
    print('['.format(M) + str(j) + ']')
    print('    - Surat   :', data['nama'])
    print('    - Ayat   :', data['ayat'])
    print('    - arti   :', data['arti'])
    print('')
    time.sleep(0.1)