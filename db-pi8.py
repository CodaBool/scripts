import psycopg2
import os
import shutil
import re
import subprocess
from dotenv import load_dotenv
from datetime import datetime

def getSpace():
  total, used, free = shutil.disk_usage(__file__)
  percent = free / total * 100
  return int(percent)

def getExternalSpace():
  newout = re.sub('b|\'|n|\\\\', '', str(subprocess.check_output("df /dev/sda1", shell=True)))
  return 100 - int(newout.split()[10][:-1])

def executeQuery(cursor, connection):
  new = re.sub('b|\'|n|\\\\', '', str(subprocess.check_output("python /home/codabool/Downloads/codadash-scripts/count-simple.py /mnt/sd1/ven/jellyfin/new n", shell=True)))
  # space = getSpace() # this is not as useful as external drive space, could use this if I add new column for it in db
  externalSpace = getExternalSpace()
  lastRan = datetime.now()
  cursor.execute(f'UPDATE pi8 SET "Space Left"={externalSpace}, "New Videos"={new}, "Last Ran"=\'{lastRan}\' WHERE id=1;') # syntax requires > python 3.6

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