import os
import sys
from os.path import join, isdir, abspath
from os import listdir, walk, getcwd, popen
from dotenv import load_dotenv
from time import sleep
import subprocess

def getListOfFiles(directory): # create a list of file and sub directories
  listOfFile = os.listdir(directory) # names in the given directory
  allFiles = list()
  for entry in listOfFile:
    fullPath = join(directory, entry)
    if isdir(fullPath): # If entry is a directory then get the list of files in this directory
      allFiles = allFiles + getListOfFiles(fullPath)
    else: 
      allFiles.append(fullPath)
  return allFiles

def findShipment(listOfFiles):
  for _file in listOfFiles:
    if 'ship.mom' in _file:
      return _file[:-9]

try:
  load_dotenv()
  folder = findShipment(getListOfFiles('/docks/'))

  # Ship folder
  print('cmd /c pscp -P 22 -pw ' + os.getenv('MOM_PASS') + ' -r \"' + folder + '\" codabool@192.168.0.25:/docks')
  os.system('cmd /c pscp -P 22 -pw ' + os.getenv('MOM_PASS') + ' -r \"' + folder + '\" codabool@192.168.0.25:/docks')
  
  # Delete folder
  # print('DELETE: rmdir /Q /S \"' + '\\Transcode' + '\\push\"')
  # os.system('cmd /c rmdir /Q /S \"' + ROOT + '\\push\"')
except subprocess.CalledProcessError:
  print ('error catch, cannot perform scp')
