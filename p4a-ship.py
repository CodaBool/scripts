import os
import sys
import subprocess
from os.path import join, isdir, isfile
from dotenv import load_dotenv

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
  print(countVideos(listOfFiles), "videos found in", ROOT)
  for _file in listOfFiles:
    if "ship.mom" in _file:
      # variables
      pathArr = _file.split("/")

      # _file[7:]
      readyFolderPath = _file[:-8]
      readyFolderName = pathArr[-2:][0]
      print(countVideos(getListOfFiles(readyFolderPath)), " videos found in this transfer to mom")
      print('variables')
      print('pathArr', pathArr)
      print('readyFolderPath', readyFolderPath)
      print('readyFolderName', readyFolderName)
      print('os.getenv(MOM_PASS)', os.getenv(MOM_PASS))
    else:
      print('no shipment label found', _file)
    #   if 'n' in auto:
    #     response = input("\nContinue? [y/n] ")
    #     if response == 'n':
    #       os.system("rm /home/codabool/Documents/shipping.started")
    #       sys.exit()

    #   print("\nSSH Copy of folder " + readyFolderName)
    #   print("DEBUG sshpass -p " +  os.getenv('WIN_PASS') + " scp -r \"" + readyFolderPath + "\" Dougie@192.168.1.27:/Transcode/pull")
    #   os.system("sshpass -p " +  os.getenv('WIN_PASS') + " scp -r \"" + readyFolderPath + "\" Dougie@192.168.1.27:/Transcode/pull")
    #   print("SSH Adding im.done file")
    #   print("DEBUG sshpass -p " +  os.getenv('WIN_PASS') + " scp /home/codabool/Documents/im.done Dougie@192.168.1.27:\'\"/Transcode/pull/" + readyFolderName + "\"\'")

    #   os.system("sshpass -p " +  os.getenv('WIN_PASS') + " scp /home/codabool/Documents/im.done Dougie@192.168.1.27:\'\"/Transcode/pull/" + readyFolderName + "\"\'")
    #   print("SSH Copy Complete\n\nRemoving shipment folder from docks")
    #   print("rm -rf \"" + readyFolderPath + "\"")
    #   # os.system("rm -rf \"" + readyFolderPath + "\"")
    # elif "ship.pi8" in _file:
    #   # variables
    #   pathArr = _file.split("/")
    #   readyFolderPath = _file[:-8]
    #   readyFolderName = pathArr[-2:][0]
    #   print(countVideos(getListOfFiles(readyFolderPath)), " videos found in this transfer to pi8")

    #   if 'n' in auto:
    #     response = input("\nContinue? [y/n] ")
    #     if response == 'n':
    #       os.system("rm /home/codabool/Documents/shipping.started")
    #       sys.exit()

      
    #   print("\nSSH Copy of folder " + readyFolderName)
    #   os.system("sshpass -p " +  os.getenv('PI8_PASS') + " scp -r \"" + readyFolderPath + "\" codabool@192.168.1.32:/mnt/sd1/ven/jellyfin/new")
    #   print("SSH Adding im.done file")
    #   os.system("sshpass -p " +  os.getenv('PI8_PASS') + " scp /home/codabool/Documents/im.done codabool@192.168.1.32:\'\"/mnt/sd1/ven/jellyfin/new/" + readyFolderName + "\"\'")
    #   print("SSH Copy Complete\n\nRemoving shipment folder from docks")
    #   print("rm -rf \"" + readyFolderPath + "\"")
    #   os.system("rm -rf \"" + readyFolderPath + "\"")

ROOT = "/docks/"
TYPES = ['mp4', 'mkv', 'avi']
load_dotenv()

print('\n==================')
if isfile(ROOT + "shipping.started"):
  print("Shipment in progress try again later.\nTo force start remove " + ROOT + "shipping.started")
else:
  os.system("touch " + ROOT + "shipping.started")
  moveFolder(getListOfFiles(ROOT))
  os.system("rm " + ROOT + "shipping.started")
print('==================\n')