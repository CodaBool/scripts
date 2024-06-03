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
    response = input("\nShould I convert " + str(tranCount) + " videos? [y/n]: ")
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
    myFile.write('\nTranscoding ' + str(cursor) + '/' + str(tranCount) + ' ' + fileName + ' @ ' + printDate)
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
  if 'n' in auto:
    askInput()

def convert(listOfFiles, quality, extraParams):
  startTime = datetime.now()
  if 'y' in logs:
    writeLog(None, 'starting', None)
  for _type in TYPES:
    for _file in listOfFiles:
      if _file.endswith(_type):
        out = os.popen('cmd /c D:\\utilities\\ffmpeg\\bin\\ffprobe -v error -show_entries stream=codec_long_name \"' + _file + '\" | grep codec_long_name').read()
        if '264' not in out:
          # Variable Declaration
          absPath = os.path.abspath(os.getcwd()) + "\\"
          pathArr = _file.split("\\")
          fileName = _file.split("\\")[-1].replace("./", "").replace(".\\", "") # split on / and then only grab last element
          # workingDir = "\\".join(pathArr[:-1]) # not working as expected
          fileNameNoExt = fileName[:-4] # remove 3 letter extenstion .***
          # fullPath = workingDir + "\\" + fileName # not working as expected

          newFile = _file[:-4] + "-CON" + _file[-4:] 

          if 'y' in logs:
            global cursor
            cursor += 1
            writeLog(fileNameNoExt, 'converting', None)

          # print("\n_file", _file)
          # print("newFile", newFile + "\n")

          # print('HandBrakeCLI --all-subtitles --all-audio -i \"' + _file + '\" -o \"' + newFile + '\"')

          # print('HandBrakeCLI --all-subtitles --all-audio -i \"' + _file + '\" -o \"' + fileNameNoExt + '-CONV.' + _type + '\"')

          # convert
          # print('HandBrakeCLI --all-subtitles --subtitle-burned="none" --all-audio -q ' + quality + ' -i \"' + _file + '\" -o \"' + newFile + '\"')
          os.system('cmd /c HandBrakeCLI --all-subtitles --subtitle-burned="none" --all-audio ' + extraParams + ' -i \"' + _file + '\" -o \"' + newFile + '\"')

          # move
          # os.system('cmd /c move \"' + workingDir + '\\' + fileNameNoExt + _type + '\" \"' + workingDir + '\\' + fileNameNoExt + _type + '\"')

          # remove
          #os.system('cmd /c del \"' + _file + '\"')
  elapsed = datetime.now() - startTime
  hours, remainder = divmod(elapsed.seconds, 3600)
  minutes, seconds = divmod(remainder, 60)
  printTime = '{:02}h:{:02}m:{:02}s'.format(int(hours), int(minutes), int(seconds))
  print('=== Finished Transcode of ' + str(cursor) + ' of ' + str(tranCount) + ' videos in ' + printTime + ' ===')
  if 'y' in logs:
    writeLog(_file, 'finished', printTime)
  
TYPES = ['mp4', 'mkv', 'avi']
LOG_DIR = 'C:/Transcode/transcode-log.txt'
# should have ability to choose amount to transcode
dirName = sys.argv[1]
logs = sys.argv[2]
auto = sys.argv[3]
quality = sys.argv[4]
extraParams = sys.argv[5]

print("DEGUG:",dirName, "|", logs,"|", auto, "|",  quality,"|",  extraParams)

tranCount = totalNumber = cursor = 0 # Counting variables
listOfFiles = getListOfFiles(dirName)
listOfFiles = list()
for (dirpath, dirnames, filenames) in walk(dirName):
  listOfFiles += [join(dirpath, _file) for _file in filenames]


if 'n' in auto:
  if logs == " ":
    logs = input("Write logs locally [y/n]: ")
  if quality == " ":
    quality = input("Quality 1-30 (low-high, default is 24): ")
  if extraParams == " ":
    print("You can also provide Extra Parameters e.g. 'tran y 24 \"--stop-at seconds:30\"'")

# print("debug End: ", logs, quality, extraParams)

print("\nQuality ===> " + quality)
if 'y' in logs:
  print("Logs: On ===> " + LOG_DIR)
else:
  print("Logs: Off")
if extraParams == " ":
  extraParams = " -q " + str(quality) + " "
  print('No additional Paramaters provided\n')
else:
  print("Additional Parameters: " + extraParams)
  extraParams = " -q " + str(quality) + " " + extraParams + " "
dry(listOfFiles)
convert(listOfFiles, quality, extraParams)
