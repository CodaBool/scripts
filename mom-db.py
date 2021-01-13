import psycopg2
import os
import shutil
import re
import subprocess
from dotenv import load_dotenv
from datetime import datetime

def getInternalSpace():
  total, used, free = shutil.disk_usage(__file__)
  percent = free / total * 100
  # print('internal storage ---> ', int(percent))
  return int(percent)

def getExternalSpace():
  newout = re.sub('b|\'|n|\\\\', '', str(subprocess.check_output("sudo df /dev/sda1", shell=True)))
  # print('external storage ---> ', (100 - int(newout.split()[10][:-1])))
  return 100 - int(newout.split()[10][:-1])

def executeQuery(cursor, connection):
  videos = re.sub('b|\'|n|\\\\', '', str(subprocess.check_output("python3 /home/codabool/scripts/count-simple.py /mnt/sd1/ven/media/ n", shell=True))) # requires sudo for drive
  # print('Videos on Drive ---> ', videos)
  # print(f'UPDATE mom SET "Space Left Internal"={getInternalSpace()}, "Space Left External"={getExternalSpace()}, "Videos"={videos}, "Last Ran"=CURRENT_TIMESTAMP;')
  cursor.execute(f'UPDATE mom SET "Space Left Internal"={getInternalSpace()}, "Space Left External"={getExternalSpace()}, "Videos"={videos}, "Last Ran"=CURRENT_TIMESTAMP;') # syntax requires > python 3.6 

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