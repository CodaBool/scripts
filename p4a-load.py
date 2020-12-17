import os
import re
import subprocess
import os.path, time
from datetime import datetime
from os.path import join, isdir

def getListOfFiles(directory): # create a list of file and sub directories
  listOfFile = os.listdir(directory) # names in the given directory
  allFiles = list()
  for entry in listOfFile:
    fullPath = join(directory, entry)
    if isdir(fullPath): # If entry is a directory then get the list of files in this directory
      allFiles.append(fullPath)
    else: 
      print("Found loose file", fullPath)
  return allFiles

def placeShippingFile(listOfFiles):
  for _file in listOfFiles:
    alreadyLoaded = False

    print('\n==================')
    print('1', _file)
    print('2', _file[31:])

    momLoadCount = re.sub('b|\'|n|\\\\', '', str(subprocess.check_output('ls -dq \"' + _file + '\"/ship.mom | wc -l', shell=True)))
    if momLoadCount == '1': # mom
      print('this is a mom shipment')
      alreadyLoaded = True

    date1 = datetime.strptime(time.ctime(os.path.getctime(_file)), "%a %b %d %H:%M:%S %Y") # make ctime into datetime
    dif = (datetime.now() - date1).total_seconds() // 60 # get a deltatime -> function to seconds -> convert to minutes
    print("Created", dif, "minutes ago")
    if dif > 1 and not alreadyLoaded:
      print("Time allotted, preping folder for shipping", _file)
      print('touch \'' + _file + '/ship.' + SHIPMENT_DESTINATION + '\'')
      # os.system('touch \"' + _file + '/ship.win\"')
    print('==================\n')
    

SHIPMENT_DESTINATION = 'mom'
ROOT = "/docks"
placeShippingFile(getListOfFiles(ROOT))