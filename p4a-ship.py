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

def moveFolder(listOfFiles, isMovie):
  print(countVideos(listOfFiles), "videos found\n")
  for _file in listOfFiles:
    if "ship.mom" in _file:
      pathArr = _file.split("/")
      readyFolderPath = _file[:-8]
      readyFolderName = pathArr[-2:][0]
      
      print("SSH Copy of ...", readyFolderName)
      if isMovie == True:
        # print("DEBUG " + "scp -r \"" + readyFolderPath + "\" " + SSH + ":/mnt/sd1/ven/media/movies")
        os.system("scp -r \"" + readyFolderPath + "\" " + SSH + ":/mnt/sd1/ven/media/movies")
        print("SSH Adding im.done file")
        # print("DEBUG " + "scp " + IM_DONE_FILE + " " + SSH + ":\'\"/mnt/sd1/ven/media/movies/" + readyFolderName + "\"\'")
        os.system("scp " + IM_DONE_FILE + " " + SSH + ":\'\"/mnt/sd1/ven/media/movies/" + readyFolderName + "\"\'")
      else:
        # print("DEBUG " + "scp -r \"" + readyFolderPath + "\" " + SSH + ":/mnt/sd1/ven/media/shows")
        os.system("scp -r \"" + readyFolderPath + "\" " + SSH + ":/mnt/sd1/ven/media/shows")
        print("SSH Adding im.done file")
        # print("DEBUG " + "scp " + IM_DONE_FILE + " " + SSH + ":\'\"/mnt/sd1/ven/media/shows/" + readyFolderName + "\"\'")
        os.system("scp " + IM_DONE_FILE + " " + SSH + ":\'\"/mnt/sd1/ven/media/shows/" + readyFolderName + "\"\'")
      print("SSH Copy Complete\nRemoving shipment folder from docks")
      print("rm -rf \"" + readyFolderPath + "\"")
      # os.system("rm -rf \"" + readyFolderPath + "\"")


MOVIE_DIR = "/docks/movie/"
SHOWS_DIR = "/docks/shows/"
ROOT = '/docks/'
TYPES = ['mp4', 'mkv', 'avi']
SSH = 'root@192.168.1.25'
IM_DONE_FILE = '/home/codabool/scripts/im.done'

print('\n==================')
if isfile(ROOT + "shipping.started"):
  print("Shipment in progress try again later.\nTo force start remove " + ROOT + "shipping.started")
else:
  try:
    moveMovie = sys.argv[1] # throws error if no arguments in cli
    os.system("touch " + ROOT + "shipping.started")
    if moveMovie == 'true':
      print('checking for movies')
      moveFolder(getListOfFiles(MOVIE_DIR), True)
    else:
      print('checking for shows')
      moveFolder(getListOfFiles(SHOWS_DIR), False)
  except:
    os.system("rm " + ROOT + "shipping.started")
    print("\nError occured.\nPlease provide if you want to ship from the movie or show directory\n(true for movies, false for shows)\npython3 ~/scripts/p4a-ship.py true") 
print('==================\n')