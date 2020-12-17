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
    print('\n==================')
    print('searching folder ...', _file[7:]) # print just the relative folder
    isLoaded = re.sub('b|\'|n|\\\\', '', str(subprocess.check_output('if [ -f "' + _file + '/ship.mom" ]; then echo "true"; else echo "false"; fi', shell=True)))
    if isLoaded == 'false':
      date1 = datetime.strptime(time.ctime(os.path.getctime(_file)), "%a %b %d %H:%M:%S %Y") # make ctime into datetime
      dif = (datetime.now() - date1).total_seconds() // 60 # get a deltatime -> function to seconds -> convert to minutes
      if dif > 1:
        print("Time allotted, adding shipment label to folder")
        print('touch "' + _file + '/ship.mom"')
        os.system('touch "' + _file + '/ship.mom"')
      else:
        print("Folder altered", dif, "minutes ago. Label will be added after 1 unaltered minute")
    else:
      print('label already found in folder')
    print('==================\n')
    
ROOT = "/docks"
placeShippingFile(getListOfFiles(ROOT))