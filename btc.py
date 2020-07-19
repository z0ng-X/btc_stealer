from telethon import TelegramClient, events, sync
import re
import os
from colorama import Fore, Back, Style

def cls():
    os.system('clear')

cls()
print(Fore.YELLOW + '''
                           _    
                        __|_|___       BTC GRABBER v.1.0
                       (  _____/
                       | (|_|__ 
                       (_____  )
                       /\_|_|) |
                       \_______)
                          |_|   
''')
print(Fore.CYAN + '@wannadeauth && @wannadeauth_chat (telegram)')
print(Fore.CYAN + '-----------------------------------------------')
print('''




''')

api_id = int(input(Fore.MAGENTA + ' API ID: ' + Fore.BLUE))
print('')        
api_hash = input(Fore.MAGENTA + ' API HASH: ' + Fore.BLUE)
print(Fore.WHITE + '')
regex = r"BTC_CHANGE_BOT\?start="

client = TelegramClient('session', api_id, api_hash)
client.start() 
print('\n Успешно! Ждем улова :D \n')
@client.on(events.NewMessage())
async def normal_handler(event):
    user_mess = event.message.to_dict()['message']
    m_from = event.message.to_dict()
    to_id = event.message.to_dict()['to_id']['channel_id']
 
    if re.search(r'BTC_CHANGE_BOT\?start=', user_mess):
        m = re.search(r'c_\S+', user_mess)
        await client.send_message('BTC_CHANGE_BOT', '/start ' + m.group(0))
        print(m.group(0))
 

client.run_until_disconnected()
