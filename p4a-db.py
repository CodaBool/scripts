import os
import re
import subprocess
import shutil
from pymongo import MongoClient
from dotenv import load_dotenv
from datetime import datetime
from pprint import pprint

def getSpace():
  total, used, free = shutil.disk_usage(__file__)
  percent = free / total * 100
  return int(percent)

def getQbit():
  out = subprocess.Popen(['systemctl', 'is-active', 'qbittorrent'], 
    stdout=subprocess.PIPE, 
    stderr=subprocess.STDOUT)
  stdout, stderr = out.communicate()
  return stdout.decode('utf-8').rstrip()

def getVPN():
  raw = subprocess.check_output('curl ifconfig.me', shell=True)
  if (raw.decode('utf-8').find(os.getenv('IP')) == 0):
    return False
  else:
    return True
    
try:
  load_dotenv()

  # get variables
  completed = re.sub('b|\'|n|\\\\', '', str(subprocess.check_output("python3 /home/codabool/scripts/count-simple.py /home/codabool/qbit/complete n", shell=True)))
  downloading = re.sub('b|\'|n|\\\\', '', str(subprocess.check_output("/home/codabool/tor/qbt/qbt torrent list -F list -f downloading | grep -o Hash | wc -l", shell=True)))
  transferring = re.sub('b|\'|n|\\\\', '', str(subprocess.check_output("python3 /home/codabool/scripts/count-simple.py /docks n", shell=True)))
  space = getSpace()
  vpn = getVPN()
  if getQbit() == 'inactive':
    qbit = False
  else:
    qbit = True

  client = MongoClient(os.getenv('MONGODB_URI'))
  mon = client['codadash']['collections']
  print('uri =', os.getenv('MONGODB_URI'))
  print('mon', type(mon))
  pprint({
    'Space Left': space,
    'Completed': completed,
    'Downloading': downloading,
    'Transferring': transferring,
    'VPN Status': vpn,
    'Qbit Status': qbit,
    'Last Ran': datetime.now(),
  })
  mon.update_one(
    {'name': 'p4a'},
    {'$set':
      {
        'Space Left': space,
        'Completed': completed,
        'Downloading': downloading,
        'Transferring': transferring,
        'VPN Status': vpn,
        'Qbit Status': qbit,
        'Last Ran': datetime.now(),
      }
    }
  )
except (Exception) as error:
  print (error)