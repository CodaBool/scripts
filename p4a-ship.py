import os
import sys
import subprocess
from os.path import join, isdir, isfile

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

def countVideos(listOfFiles):
  totalVideos = 0
  for _type in TYPES:
    for _file in listOfFiles:
      if _file.endswith(_type):
        totalVideos += 1
  return totalVideos

def moveFolder(listOfFiles):
  videosFound = countVideos(listOfFiles)
  print(videosFound, "videos found in", ROOT)
  for _file in listOfFiles:
    if "ship.mom" in _file:
      pathArr = _file.split("/")
      readyFolderPath = _file[:-8]
      readyFolderName = pathArr[-2:][0]
      
      print("\nSSH Copy of folder " + readyFolderName)
      print("DEBUG " + "scp -r \"" + readyFolderPath + "\" " + SSH + ":/mnt/sd1/ven/media/new")
      os.system("scp -r \"" + readyFolderPath + "\" " + SSH + ":/mnt/sd1/ven/media/new")
      print("SSH Adding im.done file")
      print("DEBUG " + "scp " + SCRIPTS_HOME + "im.done " + SSH + ":\'\"/mnt/sd1/ven/media/new/" + readyFolderName + "\"\'")
      os.system("scp " + SCRIPTS_HOME + "im.done " + SSH + ":\'\"/mnt/sd1/ven/media/new/" + readyFolderName + "\"\'")
      print("SSH Copy Complete\n\nRemoving shipment folder from docks")
      print("rm -rf \"" + readyFolderPath + "\"")
      # os.system("rm -rf \"" + readyFolderPath + "\"")

ROOT = "/docks/"
TYPES = ['mp4', 'mkv', 'avi']
SSH = 'root@192.168.1.25'
SCRIPTS_HOME = '/home/codabool/scripts/'

print('\n==================')
moveFolder(getListOfFiles(ROOT))

# if isfile(ROOT + "shipping.started"):
#   print("Shipment in progress try again later.\nTo force start remove " + ROOT + "shipping.started")
# else:
#   os.system("touch " + ROOT + "shipping.started")
#   moveFolder(getListOfFiles(ROOT))
#   os.system("rm " + ROOT + "shipping.started")
print('==================\n')