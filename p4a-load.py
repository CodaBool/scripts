import os
import os.path, time
from datetime import datetime
from os.path import join, isdir, isfile

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

MOVIE_DIR = "/docks/movie/"
SHOWS_DIR = "/docks/shows/"

placeShippingFile(getListOfFiles(MOVIE_DIR))
placeShippingFile(getListOfFiles(SHOWS_DIR))