import os
import os.path, time
from datetime import datetime
from os.path import join, isdir, isfile

# if a file is older than a minute, label for shipping

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
    print('searching folder ...', _file[13:]) # print just the relative folder
    if isfile(_file + "/ship.mom"):
      print('label already found in folder')
    else:
      date1 = datetime.strptime(time.ctime(os.path.getctime(_file)), "%a %b %d %H:%M:%S %Y") # make ctime into datetime
      dif = (datetime.now() - date1).total_seconds() // 60 # get a deltatime -> function to seconds -> convert to minutes
      if dif > 1:
        print("Time allotted, adding shipment label to folder")
        print('touch "' + _file + '/ship.mom"')
        os.system('touch "' + _file + '/ship.mom"')
      else:
        print("Folder altered", dif, "minutes ago. Label will be added after 1 unaltered minute")
    print('==================\n')

# MOVIES_DIR = "/home/codabool/radarr/movies"
# TV_DIR = "/home/codabool/sonarr/tv"
COMPLETE_DIR = "/home/codabool/qbit/complete"

placeShippingFile(getListOfFiles(COMPLETE_DIR))
# placeShippingFile(getListOfFiles(TV_DIR))