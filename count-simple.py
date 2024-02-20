import os
import sys
import subprocess
from os.path import join, isdir, abspath
from os import listdir, walk, getcwd, popen

# example way to run 
# WINDOWS: python /d/Utilities/codadash-scripts/count-videos.py "$PWD" y

def getListOfFiles(dirName): # create a list of file and sub directories
  listOfFile = listdir(dirName) # names in the given directory
  allFiles = list()
  for entry in listOfFile:
    fullPath = join(dirName, entry)
    if isdir(fullPath): # If entry is a directory then get the list of files in this directory
      allFiles = allFiles + getListOfFiles(fullPath)
    else:
      allFiles.append(fullPath)
  return allFiles

def countVideos(listOfFiles):
  for _type in TYPES:
    for _file in listOfFiles:
      if _file.endswith(_type):
        global totalVideos
        totalVideos += 1
  return totalVideos

TYPES = ['mp4', 'mkv', 'avi']
totalVideos = 0 # Counting variables
dirName = sys.argv[1]
VERBOSE = sys.argv[2]
dirName = abspath(dirName)
listOfFiles = getListOfFiles(dirName)
listOfFiles = list()
for (dirpath, dirnames, filenames) in walk(dirName):
  listOfFiles += [join(dirpath, _file) for _file in filenames]
if VERBOSE == "y":
  print("found", countVideos(listOfFiles), "videos of type", TYPES)
else:
  print(countVideos(listOfFiles))
  
