import os
import sys
import subprocess
import numbers
from datetime import datetime
from os.path import join, isdir, abspath
from os import listdir, walk, getcwd

# run manually, 
# python /d/utilities/codadash-scripts/tran-win.py ./@y@n

TYPES = ['mp4', 'mkv', 'avi']
LOG_DIR = './log.txt'
[dirName, logs, auto] = sys.argv[1].split('@')
tranCount = totalNumber = cursor = limit = 0 # Counting variables


def getListOfFiles(dir): # create a list of file and sub directories
  print(dir)
  listOfFile = listdir(dir) # names in the given directory
  allFiles = list()
  for entry in listOfFile:
    fullPath = join(dir, entry)
    if isdir(fullPath): # If entry is a directory then get the list of files in this directory
      allFiles = allFiles + getListOfFiles(fullPath)
    else:
      allFiles.append(fullPath)
  return allFiles

def askInput(tranCount, totalNumber, limit):
  # determine if script should continue
  isAllowed = False
  while (isAllowed == False):
    response = input("Should I convert " + str(tranCount) + " videos? (or enter an amount to convert) [y/n]: ")
    if response == "y" or response == "yes":
      isAllowed = True
    elif response == "n" or response == "no":
      # isAllowed = True
      sys.exit()
    elif response.isdigit():
      if int(response) > totalNumber:
        print("Please pick a number below", totalNumber + 1)
      elif response == "0":
        sys.exit()
      else:
        print('setting limit to', response)
        limit = int(response)
        isAllowed = True
    else:
      print("you entered " + response + " Please enter 'yes' or 'no' or a valid number.")
  return limit

def writeLog(fileName, status, limit, total, elapsed, cursor):
  myFile = open(LOG_DIR, 'a')
  printDate = datetime.now().strftime("%d/%m %H:%M:%S")
  if status == 'starting':
    myFile.write('=== Starting Transcode of ' + str(limit) + ' videos ===')
  elif status == 'converting':
    myFile.write('\nTranscoding ' + str(cursor) + '/' + str(limit) + ' ' + fileName)
  elif status == 'finished':
    myFile.write('\n=== Finished Transcode of ' + str(limit) + ' videos in ' + elapsed + ' ===\n\n')
  myFile.close()

def dry(tranCount, totalNumber, listOfFiles, limit):
  for _type in TYPES:
    for _file in listOfFiles:
      if _file.endswith(_type):
        out = os.popen('cmd /c D:\\utilities\\ffmpeg\\bin\\ffprobe -v error -show_entries stream=codec_long_name \"' + _file + '\" | grep codec_long_name').read()
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
    limit = askInput(tranCount, totalNumber, limit)
  return limit

def convert(listOfFiles, limit, cursor):
  startTime = datetime.now()
  if logs == 'y':
    writeLog(None, 'starting', str(cursor + 1), None, None, None)
  for _type in TYPES:
    for _file in listOfFiles:
      if _file.endswith(_type):
        out = os.popen('cmd /c D:\\utilities\\ffmpeg\\bin\\ffprobe -v error -show_entries stream=codec_long_name \"' + _file + '\" | grep codec_long_name').read()
        if '264' not in out:
          # Variable Declaration
          absPath = os.path.abspath(os.getcwd()) + "\\"
          pathArr = _file.split("\\")
          fileName = pathArr[-1] # split on / and then only grab last element
          workingDir = "\\".join(pathArr[:-1])
          fileNameNoExt = fileName[:-4] # remove 3 letter extenstion .***
          fullPath = workingDir + "\\" + fileName

          if logs == 'y':
            cursor += 1
            writeLog(fileNameNoExt, 'converting', str(limit), str(totalNumber), '', cursor)
          
          # DEBUG
          # print("absPath", absPath)
          # print("pathArr", pathArr)
          # print("fileName", fileName)
          # print("workingDir", workingDir)
          # print("fileNameNoExt", fileNameNoExt)
          # print("fullPath", fullPath)

          # subprocess is alt. solution to os.system
          # convert
          os.system('cmd /c HandBrakeCLI --all-subtitles --all-audio -i \"' + _file + '\" -o \"' + workingDir + '\\' + fileNameNoExt + '.' +_type + '\"')

          # move
          # os.system('cmd /c move \"' + workingDir + '\\' + fileNameNoExt + _type + '\" \"' + workingDir + '\\' + fileNameNoExt + _type + '\"')

          # remove
          # os.system('cmd /c del \"' + fullPath + '\"')
  elapsed = datetime.now() - startTime
  hours, remainder = divmod(elapsed.seconds, 3600)
  minutes, seconds = divmod(remainder, 60)
  printTime = '{:02}h:{:02}m:{:02}s'.format(int(hours), int(minutes), int(seconds))
  print('=== Finished Transcode of ' + str(cursor) + ' of ' + str(limit) + ' videos in ' + printTime + ' ===')
  if logs == 'y':
    writeLog(_file, 'finished', str(limit), '', printTime, '')
  
def main():

  #Get the list of all files in directory tree at given path
  listOfFiles = getListOfFiles(dirName)
  listOfFiles = list()
  for (dirpath, dirnames, filenames) in walk(dirName):
    listOfFiles += [join(dirpath, _file) for _file in filenames]

  limit = 0
  limit = dry(tranCount, totalNumber, listOfFiles, limit)
  if limit == 0:
    limit = tranCount
    
  print(limit)
  #for x in range(0, limit):
  #Get the list of all files in directory tree at given path
  listOfFiles = getListOfFiles(dirName)
  listOfFiles = list()
  for (dirpath, dirnames, filenames) in walk(dirName):
    listOfFiles += [join(dirpath, _file) for _file in filenames]

  # Print log status and dir if applicable
  if logs == 'y':
    print("\nLogs: On ===> " + LOG_DIR + "\n\nSearching for videos...")
  else:
    print("Logs: Off")
  convert(listOfFiles, limit, cursor)

if __name__ == "__main__":
  main()