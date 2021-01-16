import psycopg2
import os
import re
import subprocess
import shutil
import time
from datetime import datetime
from dotenv import load_dotenv

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
  if (raw.decode('utf-8').find('67.8.111.220') == 0):
    return 'inactive'
  else:
    return 'active'
    
def executeQuery(cursor, connection):  
  completed = re.sub('b|\'|n|\\\\', '', str(subprocess.check_output("python3 /home/codabool/scripts/count-simple.py /home/codabool/qbit/complete n", shell=True)))
  downloading = re.sub('b|\'|n|\\\\', '', str(subprocess.check_output("/home/codabool/tor/qbt/qbt torrent list -F list -f downloading | grep -o Hash | wc -l", shell=True)))
  transferring = re.sub('b|\'|n|\\\\', '', str(subprocess.check_output("python3 /home/codabool/scripts/count-simple.py /docks n", shell=True)))
  space = getSpace()
  qbit = getQbit()
  vpn = getVPN()
  # os.system('touch /home/codabool/db-s.{space}-c.{completed}-d.{downloading}-t{transferring}-s{getStatus()}-q{getQbitStatus()}')
  # print(f'UPDATE p4a SET "Space Left"={space}, "Completed"={completed}, "Downloading"={downloading}, "Transferring"={transferring}, "VPN Status"=\'{vpn}\', "QBit Status"=\'{qbit}\', "Last Ran"=CURRENT_TIMESTAMP;')
  cursor.execute(f'UPDATE p4a SET "Space Left"={space}, "Completed"={completed}, "Downloading"={downloading}, "Transferring"={transferring}, "VPN Status"=\'{vpn}\', "QBit Status"=\'{qbit}\', "Last Ran"=CURRENT_TIMESTAMP;') # syntax requires > python 3.6 

try:
  load_dotenv()
  connection = psycopg2.connect(os.getenv('URI'))
  cursor = connection.cursor()
  executeQuery(cursor, connection)
  connection.commit()
except (Exception, psycopg2.Error) as error :
  print ("Error while connecting to PostgreSQL", error)
finally:
  if (connection):
    cursor.close()
    connection.close()
    print("PostgreSQL connection is closed")