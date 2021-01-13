import psycopg2
import os
import re
import subprocess
import shutil
from datetime import datetime
from dotenv import load_dotenv

def getSpace():
  total, used, free = shutil.disk_usage(__file__)
  percent = free / total * 100
  return int(percent)

def getStatus():
  raw = subprocess.check_output(['protonvpn', 'status'])
  return raw.split()[1].decode('UTF-8')

def getQbitStatus():
  raw = subprocess.check_output(['systemctl', 'is-active', 'qbittorrent'])
  return raw.decode('UTF-8').strip()

def executeQuery(cursor, connection):  
  completed = re.sub('b|\'|n|\\\\', '', str(subprocess.check_output("python3 /home/codabool/scripts/count-simple.py /home/codabool/qbit/complete n", shell=True)))
  downloading = re.sub('b|\'|n|\\\\', '', str(subprocess.check_output("/home/codabool/tor/qbt/qbt torrent list -F list -f downloading | grep -o Hash | wc -l", shell=True)))
  transferring = re.sub('b|\'|n|\\\\', '', str(subprocess.check_output("python3 /home/codabool/scripts/count-simple.py /docks n", shell=True)))
  status = getStatus()
  qbit = getQbitStatus()
  space = getSpace()
  # print(f'UPDATE p4a SET "Space Left"={space}, "Completed"={completed}, "Downloading"={downloading}, "Transferring"={transferring}, "VPN Status"=\'{status}\', "QBit Status"=\'{qbit}\', "Last Ran"=CURRENT_TIMESTAMP;')
  cursor.execute(f'UPDATE p4a SET "Space Left"={space}, "Completed"={completed}, "Downloading"={downloading}, "Transferring"={transferring}, "VPN Status"=\'{status}\', "QBit Status"=\'{qbit}\', "Last Ran"=CURRENT_TIMESTAMP;') # syntax requires > python 3.6 

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