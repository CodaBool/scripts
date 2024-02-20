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
  print(countVideos(listOfFiles), "videos found\n")
  for _file in listOfFiles:
    if "ship.mom" in _file:
      pathArr = _file.split("/")
      readyFolderPath = _file[:-8]
      readyFolderName = pathArr[-2:][0]

      print("SSH Copy of ...", readyFolderName)
      # if isMovie == True:
      #   # print("DEBUG " + "scp -r \"" + readyFolderPath + "\" " + SSH + ":/hdd/media/movies")
      #   os.system("scp -r \"" + readyFolderPath + "\" " + SSH + ":/hdd/media/movies")
      #   print("SSH Adding im.done file")
      #   # print("DEBUG " + "scp " + IM_DONE_FILE + " " + SSH + ":\'\"/hdd/media/movies/" + readyFolderName + "\"\'")
      #   os.system("scp " + IM_DONE_FILE + " " + SSH + ":\'\"/hdd/media/movies/" + readyFolderName + "\"\'")
      # else:
      #   # print("DEBUG " + "scp -r \"" + readyFolderPath + "\" " + SSH + ":/hdd/media/tv")
      #   os.system("scp -r \"" + readyFolderPath + "\" " + SSH + ":/hdd/media/tv")
      #   print("SSH Adding im.done file")
      #   # print("DEBUG " + "scp " + IM_DONE_FILE + " " + SSH + ":\'\"/hdd/media/tv/" + readyFolderName + "\"\'")
      #   os.system("scp " + IM_DONE_FILE + " " + SSH + ":\'\"/hdd/media/tv/" + readyFolderName + "\"\'")
        # print("DEBUG " + "scp -r \"" + readyFolderPath + "\" " + SSH + ":/hdd/media/movies")

      os.system("scp -r \"" + readyFolderPath + "\" " + SSH + ":/hdd/qbit/complete")
      print("SSH Adding im.done file")
      print("DEBUG " + "scp " + IM_DONE_FILE + " " + SSH + ":\'\"/hdd/media/movies/" + readyFolderName + "\"\'")
      os.system("scp " + IM_DONE_FILE + " " + SSH + ":\'\"/hdd/qbit/complete/" + readyFolderName + "\"\'")

      print("SSH Copy Complete\nRemoving shipment folder from docks")
      print("rm -rf \"" + readyFolderPath + "\"")
      os.system("rm -rf \"" + readyFolderPath + "\"")

COMPLETE_DIR = "/home/codabool/qbit/complete"
# MOVIES_DIR = "/home/codabool/radarr/movies"
# TV_DIR = "/home/codabool/sonarr/tv"
ROOT = '/home/codabool/'
TYPES = ['mp4', 'mkv', 'avi']
SSH = 'codabool@192.168.0.25'
IM_DONE_FILE = '/home/codabool/scripts/im.done'

print('\n==================')
if isfile(ROOT + "shipping.started"):
  print("Shipment in progress try again later.\nTo force start remove " + ROOT + "shipping.started")
else:
  try:
    os.system("touch " + ROOT + "shipping.started")
    print('checking for media')
    moveFolder(getListOfFiles(COMPLETE_DIR))
    os.system("rm " + ROOT + "shipping.started") # remove shipment file to allow future shipments

    # moveMovie = sys.argv[1] # throws error if no arguments in cli
    # os.system("touch " + ROOT + "shipping.started")
    # if moveMovie == 'true':
    #   print('checking for movies')
    #   moveFolder(getListOfFiles(MOVIES_DIR), True)
    # else:
    #   print('checking for shows')
    #   moveFolder(getListOfFiles(TV_DIR), False)
    # os.system("rm " + ROOT + "shipping.started") # remove shipment file to allow future shipments
  except:
    # os.system("rm " + ROOT + "shipping.started") # remove shipment file
    print("""== Unknown Error =
For proper syntax provide where to ship to, movie or show directory
Example: (true for movies, false for shows)

python3 ~/scripts/p4a-ship.py true""") 
print('==================\n')
