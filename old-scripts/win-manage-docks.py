import os
import sys
from os.path import join, isdir, abspath
from os import listdir, walk, getcwd, popen
from dotenv import load_dotenv
from time import sleep
import subprocess

ROOT = '\\Transcode'
folder = ''

# TODO: investigate issues of moving subfolders push and tran
# Likely due to running while pull dir is empty

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

def moveToTran(listOfFiles):
  for _file in listOfFiles:
    if 'im.done' in _file:
      global folder
      folderPath = _file[:-8] # Removes [kept...]\im.done
      folder = _file[16:-8] # Removes \Transcode\pull\[...kept]
      print('folderPath', folderPath)
      print('folder', folder)
      print('DELETE: del \"' + _file + '\"')
      print('DELETE: del \"' + folderPath + '\\ship.win\"')
      print('MOVE: move \"C:' + folderPath + '\" \"C:' + ROOT + '\\tran\\' + folder + '\"')
      os.system('cmd /c del \"' + _file + '\"')
      os.system('cmd /c del \"' + folderPath + '\\ship.win\"')
      os.system('cmd /c move \"C:' + folderPath + '\" \"C:' + ROOT + '\\tran\\' + folder + '\"')

      break

def moveToPush(listOfFiles):
  for _file in listOfFiles:
    if 'tran.done' in _file:
      folderPath = _file[:-10] # Removes [removed...]\tran.done
      print('folderPath', folderPath)
      print('folder', folder)
      print('_file', _file)

      print('DELETE: del \"' + _file + '\"')
      print('MOVE: move \"' + folderPath + '\" \"' + ROOT + '\\push\\' + folder + '\"')
      os.system('cmd /c del \"' + _file + '\"')
      os.system('cmd /c move \"' + folderPath + '\" \"' + ROOT + '\\push\\' + folder + '\"')

      break

def main():

  # Move folder to transcode
  moveToTran(getListOfFiles('\\Transcode\\pull'))

  if (len(folder.strip())) == 0:
    print("Docks are clear")
    sys.exit()

  print('TRANSCODE: python C:\\Transcode\\codadash-scripts\\tran-win.py \"C:' + ROOT + '\\tran\\' + folder + '\" y \" y\" 30 \" \"')
  os.system('cmd /c python C:\\Transcode\\codadash-scripts\\tran-win.py \"C:' + ROOT + '\\tran\\' + folder + '\" y \" y\" 30 \" \"') # logs[yes] auto[yes] qualit[1-30] extra
  
  # signal that the folder is ready to be moved to push
  print('CREATE: call >> \"' + ROOT + '\\tran\\' + folder + '\\tran.done\"')
  os.system('cmd /c call >> \"' + ROOT + '\\tran\\' + folder + '\\tran.done\"')
  
  # Move folder to scp
  moveToPush(getListOfFiles('\\Transcode\\tran'))

  # SCP
  try:
    load_dotenv()
    source = 'C:\\Transcode\\push\\' + folder
    print('cmd /c pscp -P 22 -pw ' + os.getenv('PI8_PASS') + ' -r \"' + source + '\" codabool@192.168.0.207:/media/book/jellyfin/new')
    os.system('cmd /c pscp -P 22 -pw ' + os.getenv('PI8_PASS') + ' -r \"' + source + '\" codabool@192.168.0.207:/media/book/jellyfin/new')
    
    # Delete folder
    print('DELETE: rmdir /Q /S \"' + ROOT + '\\push\\' + folder + '\"')
    os.system('cmd /c rmdir /Q /S \"' + ROOT + '\\push\\' + folder + '\"')
  except subprocess.CalledProcessError:
    print ('scp does not exist')

if __name__ == "__main__":
  main()