import os
from os.path import join, isdir

def getListOfFiles(dirName): # create a list of file and sub directories
  listOfFile = os.listdir(dirName) # names in the given directory
  allFiles = list()
  for entry in listOfFile:
    fullPath = join(dirName, entry)
    if isdir(fullPath): # If entry is a directory then get the list of files in this directory
      allFiles = allFiles + getListOfFiles(fullPath)
    else:
      allFiles.append(fullPath)
  return allFiles

def switch(listOfFiles):
  count = 0
  empty = True
  for _file in listOfFiles:
    count = count + 1
  print('scanning', count, 'files')
  for _file in listOfFiles:
    if _file.endswith('win') or _file.endswith('pi8'):
      empty = False
      fileEnd = _file[-3:]
      folder = _file[:-8]
      print("\n===================")

      if fileEnd == 'win': # make into windows shipment
        print('@', _file)
        print('fold', folder)
        print("rm \"" + _file + "\"")
        print("touch \"" + _file + "ship.pi8\"")
        # os.system("rm \"" + _file + "\"")
        # os.system("touch \"" + _file + "ship.pi8\"")
      elif fileEnd == 'pi8': # make into windows shipment
        print('@', _file)
        print('fold', folder)
        print("rm \"" + _file + "\"")
        print("touch \"" + folder + "ship.win\"")
        # os.system("rm \"" + _file + "\"")
        # os.system("touch \"" + _file + "ship.win\"")
        
      print("===================\n")
  if empty:
    print('No shipments found, run \'count\' to see if video is there')  

ROOT = "/home/codabool/Downloads/docks"
switch(getListOfFiles(ROOT))