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

def executeQuery(cursor, connection):  
  total = re.sub('b|\'|n|\\\\', '', str(subprocess.check_output("/home/codabool/tor/qbt/qbt torrent list -F list | grep -o Hash | wc -l", shell=True)))
  completed = re.sub('b|\'|n|\\\\', '', str(subprocess.check_output("/home/codabool/tor/qbt/qbt torrent list -F list -f completed | grep -o Hash | wc -l", shell=True)))
  downloading = re.sub('b|\'|n|\\\\', '', str(subprocess.check_output("/home/codabool/tor/qbt/qbt torrent list -F list -f downloading | grep -o Hash | wc -l", shell=True)))
  transferring = re.sub('b|\'|n|\\\\', '', str(subprocess.check_output("python3 /home/codabool/scripts/count-simple.py /docks False", shell=True)))
  space = getSpace()
  lastRan = datetime.now()
  print(f'UPDATE pi4 SET "Space Left"={space}, "Completed"={completed}, "Downloading"={downloading}, "Total"={total}, "Last Ran"=\'{lastRan}\', "Transferring"={transferring} WHERE id=1;')
  # cursor.execute(f'UPDATE pi4 SET "Space Left"={space}, "Completed"={completed}, "Downloading"={downloading}, "Total"={total}, "Last Ran"=\'{lastRan}\', "Transferring"={transferring} WHERE id=1;') # syntax requires > python 3.6 

try:
  load_dotenv()
  print(os.getenv('URI'))
  connection = psycopg2.connect( # os.getenv('URI')
    host='ec2-54-84-98-18.compute-1.amazonaws.com',
    database='d376p41o8fn3mh',
    user='psnpsggrdczrwp',
    password='9d511f208454d1f0bbdfa8858c3a00c1a35c74c42ffcbba2bfa6586e61cf19c6',
    connect_timeout=5
  )
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