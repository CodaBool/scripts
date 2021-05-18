import os
import shutil
import re
import subprocess
from pymongo import MongoClient
from dotenv import load_dotenv
from datetime import datetime
from pprint import pprint

def getInternalSpace():
  total, used, free = shutil.disk_usage(__file__)
  percent = free / total * 100
  print('internal storage ---> ', int(percent))
  return int(percent)

def getExternalSpace():
  newout = re.sub('b|\'|n|\\\\', '', str(subprocess.check_output("sudo df /dev/sda1", shell=True)))
  print('external storage ---> ', (100 - int(newout.split()[10][:-1])))
  return 100 - int(newout.split()[10][:-1])

def updateHerokuTable():
  out = re.sub('b|\'|n|\\\\', '', str(subprocess.check_output('/home/codabool/scripts/bash-scripts/getHeroku.sh', shell=True)))
  print(out)
  client = MongoClient(os.getenv('MONGODB_URI'))
  mon = client['codadash']['collections']
  mon.update_one(
    {'name': 'heroku'},
    {'$set':
      {
        'hours': out,
        'Last Ran': datetime.now(),
      }
    }
  )

try:
  load_dotenv()
  
  # update mom
  internal_space = getInternalSpace()
  external_space = getExternalSpace()
  videos = re.sub('b|\'|n|\\\\', '', str(subprocess.check_output("python3 /home/codabool/scripts/count-simple.py /mnt/sd1/ven/media/ n", shell=True))) # requires sudo for drive
  client = MongoClient(os.getenv('MONGODB_URI'))
  mon = client['codadash']['collections']
  mon.update_one(
    {'name': 'mom'},
    {'$set':
      {
        'Space Left Internal': internal_space,
        'Space Left External': external_space,
        'Videos': videos,
        'Last Ran': datetime.now(),
      }
    }
  )

  # update heroku
  updateHerokuTable()
  
except (Exception) as error :
  print (error)