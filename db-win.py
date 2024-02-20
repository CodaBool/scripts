import psycopg2
import os
from dotenv import load_dotenv
import os
from os.path import join, isdir, abspath
from os import listdir, walk
from datetime import datetime

def getListOfFiles(dirName): 
  listOfFile = listdir(dirName) 
  allFiles = list()
  for entry in listOfFile:
    fullPath = join(dirName, entry)
    if isdir(fullPath):
      allFiles = allFiles + getListOfFiles(fullPath)
    else:
      allFiles.append(fullPath)
  return allFiles

def getVideoCount(dirName):
  videoCount = 0
  dirName = abspath(dirName)
  listOfFiles = getListOfFiles(dirName)
  listOfFiles = list()
  for (dirpath, dirnames, filenames) in walk(dirName):
    listOfFiles += [join(dirpath, _file) for _file in filenames]
  for _type in ['mp4', 'mkv', 'avi']:
    for _file in listOfFiles:
      if _file.endswith(_type):
        videoCount += 1
  return videoCount

def executeQuery(cursor, connection):
  transcoding = getVideoCount("\\Transcode\\tran")
  transferring = getVideoCount("\\Transcode\\push")
  waiting = getVideoCount("\\Transcode\\pull")
  lastRan = datetime.now()
  cursor.execute(f'UPDATE win SET "Transcoding"={transcoding}, "Transferring"={transferring}, "Waiting"={waiting}, "Last Ran"=\'{lastRan}\' WHERE id=1;') # syntax requires > python 3.6 

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