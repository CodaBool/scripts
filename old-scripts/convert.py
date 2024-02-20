import os
import sys
import subprocess
import numbers
from datetime import datetime
from os.path import join, isdir, abspath
from os import listdir, walk, getcwd

# run manually, 
# python /d/utilities/codadash-scripts/tran-win.py ./@y@n

def getListOfFiles(dir): # create a list of file and sub directories
  listOfFile = listdir(dir) # names in the given directory
  allFiles = list()
  for entry in listOfFile:
    fullPath = join(dir, entry)
    if isdir(fullPath): # If entry is a directory then get the list of files in this directory
      allFiles = allFiles + getListOfFiles(fullPath)
    else:
      allFiles.append(fullPath)
  return allFiles

def askInput():
  isAllowed = False
  while (isAllowed == False):
    response = input("Should I convert " + str(tranCount) + " videos? [y/n]: ")
    if response == "y" or response == "yes":
      isAllowed = True
    elif response == "n" or response == "no":
      sys.exit()
    else:
      print("you entered " + response + " Please enter 'yes' or 'no'.")

def writeLog(fileName, status, str1):
  myFile = open(LOG_DIR, 'a')
  printDate = datetime.now().strftime("%d/%m %H:%M:%S")
  if status == 'starting':
    myFile.write('\n=== Starting Transcode of ' + str(tranCount) + ' videos ===\nTime: ' + str(printDate))
  elif status == 'converting':
    myFile.write('\nTranscoding ' + str(cursor) + '/' + str(tranCount) + ' ' + fileName)
  elif status == 'finished':
    myFile.write('\n=== Finished Transcode of ' + str(tranCount) + ' videos in ' + str(str1) + ' ===\n\n')
  myFile.close()

def dry(listOfFiles):
  for _type in TYPES:
    for _file in listOfFiles:
      if _file.endswith(_type):
        out = os.popen('cmd /c D:\\utilities\\ffmpeg\\bin\\ffprobe -v error -show_entries stream=codec_long_name \"' + _file + '\" | grep codec_long_name').read()
        global tranCount, totalNumber
        if '265' in out:
          tranCount += 1
          totalNumber += 1
        elif '264' in out:
          totalNumber += 1
  if tranCount == 0:
    print("No files to convert")
    sys.exit()
  print("Need Transcode / Total Videos = " + str(tranCount) + "/" + str(totalNumber)) 
  if auto == 'n':
    askInput()

def convert(listOfFiles):
  startTime = datetime.now()
  if logs == 'y':
    writeLog(None, 'starting', None)
  for _type in TYPES:
    for _file in listOfFiles:
      if _file.endswith(_type):
        out = os.popen('cmd /c D:\\utilities\\ffmpeg\\bin\\ffprobe -v error -show_entries stream=codec_long_name \"' + _file + '\" | grep codec_long_name').read()
        if '264' not in out:
          # Variable Declaration
          # workingDir = os.path.abspath(os.getcwd()) + "\\"
          # fileName = _file.split("\\")[-1].replace("./", "").replace(".\\", "") # split on / and then only grab last element
          # fileNameNoExt = fileName[:-4] # remove 3 letter extenstion .***
          # fullPath = workingDir + fileName # not working as expected
          #subPath = _file.replace(fileName, "").replace()

          newFile = _file[:-4] + "-CON" + _file[-4:] 

          if logs == 'y':
            global cursor
            cursor += 1
            writeLog(fileNameNoExt, 'converting', None)

          print("\n_file", _file)
          print("newFile", newFile + "\n")

          print('HandBrakeCLI --all-subtitles --all-audio -i \"' + _file + '\" -o \"' + newFile + '\"')

          # convert
          #os.system('cmd /c HandBrakeCLI --all-subtitles --all-audio -i \"' + _file + '\" -o \"' + fileNameNoExt + '-CON.' + _type + '\"')

          # remove
          #os.system('cmd /c del \"' + _file + '\"')
  elapsed = datetime.now() - startTime
  hours, remainder = divmod(elapsed.seconds, 3600)
  minutes, seconds = divmod(remainder, 60)
  printTime = '{:02}h:{:02}m:{:02}s'.format(int(hours), int(minutes), int(seconds))
  print('=== Finished Transcode of ' + str(cursor) + ' of ' + str(tranCount) + ' videos in ' + printTime + ' ===')
  if logs == 'y':
    writeLog(_file, 'finished', printTime)
  
TYPES = ['mp4', 'mkv', 'avi']
LOG_DIR = './transcode-log.txt'
[dirName, logs, auto] = sys.argv[1].split('@')
tranCount = totalNumber = cursor = 0 # Counting variables
listOfFiles = getListOfFiles(dirName)
listOfFiles = list()
for (dirpath, dirnames, filenames) in walk(dirName):
  listOfFiles += [join(dirpath, _file) for _file in filenames]
if logs == 'y':
  print("\nLogs: On ===> " + LOG_DIR)
else:
  print("Logs: Off")
dry(listOfFiles)
convert(listOfFiles)
