import os
import sys
import re
import subprocess
from datetime import datetime
from os.path import join, isdir, abspath
from os import listdir, walk, getcwd, popen

 
# example way to run 
# python /d/Downloads/codadash-scripts/read-all-windows.py $PWD False
# do a split on / to get "265 / total"

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

def dry(listOfFiles):
  startTime = datetime.now()
  for _type in TYPES:
    for _file in listOfFiles:
      if _file.endswith(_type):

        # Variable Declaration
        absPath = os.path.abspath(os.getcwd()) + "\\"
        pathArr = _file.split("\\")
        fileName = pathArr[-1] # split on / and then only grab last element
        # workingDir = "\\".join(pathArr[:-1]) 
        fileNameNoExt = fileName[:-4]
        # fullPath = workingDir + "\\" + fileName
        # print('ffprobe -v error -show_entries stream=codec_long_name \"' + _file + '\" | grep codec_long_name')
        codec = re.sub('b|\'|n|\\\\', '', str(subprocess.check_output('ffprobe -v error -show_entries stream=codec_long_name \"' + _file + '\" | grep codec_long_name', shell=True)))
        # print('codec =', codec)
        # codec = popen('cmd /c D:\\utilities\\ffmpeg\\bin\\ffprobe -v error -show_entries stream=codec_long_name \"' + _file + '\" | grep codec_long_name').read()
        # codec = popen('/bin/ffprobe -v error -show_entries stream=codec_long_name \"' + _file + '\" | grep codec_long_name').read()
        
        if '265' in codec:
          if VERBOSE == "True":
            print('265 for ' + fileNameNoExt[31:]) # removes /home/codabool/Downloads/docks/
          global codec265Count
          codec265Count += 1
        elif '264' in codec:
          if VERBOSE == "True":
            print('264 for ' + fileNameNoExt[31:]) # removes /home/codabool/Downloads/docks/
        global totalVideos
        totalVideos += 1
  if VERBOSE == "True":
    print("\nRaw/Total = " + str(codec265Count) + "/" + str(totalVideos))
  else:
    print(str(codec265Count) + "/" + str(totalVideos))
  elapsed = datetime.now() - startTime
  hours, remainder = divmod(elapsed.seconds, 3600)
  minutes, seconds = divmod(remainder, 60)
  printTime = '{:02}h:{:02}m:{:02}s'.format(int(hours), int(minutes), int(seconds))
  if VERBOSE == "True":
    print("found in " + printTime)

TYPES = ['mp4', 'mkv', 'avi']
codec265Count = totalVideos = cursor = 0 # Counting variables
if len(sys.argv) < 2:
  print('missing directory argument')
  sys.exit()
dirName = sys.argv[1]
VERBOSE = 'True'
dirName = abspath(dirName)
listOfFiles = getListOfFiles(dirName)
listOfFiles = list()
for (dirpath, dirnames, filenames) in walk(dirName):
  listOfFiles += [join(dirpath, _file) for _file in filenames]
dry(listOfFiles)