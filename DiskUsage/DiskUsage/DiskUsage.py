#diskusage.py
# written by Tony Jones novajitz @ gmail.com
# first attempt at a useful program: one I do miss from linux

# DiskUsage

# arguments:
#
# none specified - list disk usage of all files in the current directory
#
# folder specified - list disk usage of all files in the specified folder
#

import sys
import os
import math

# output a useful number instead of a stupidly large byte count
def convert_size(size):
   if (size == 0):
       return '0B'
   size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
   i = int(math.floor(math.log(size,1024)))
   p = math.pow(1024,i)
   s = round(size/p,2)
   return '%s %s' % (s,size_name[i])

def getdiskusage(strFoldername):
    totalsize = 0

    for dirName, dirList, fileList in os.walk(strFoldername):
        for fname in fileList:
            print("\t{}".format(os.path.join(dirName, fname)))
            totalsize = totalsize + os.path.getsize(os.path.join(dirName, fname))
    return totalsize

def main():

    if len(sys.argv) >1:
        #check path exists
        if os.path.exists(sys.argv):
            os.chdir(sys.argv[1])
        else:
            #path not valid, so quit
            print("Path {} not valid".format(sys.argv[1]))
            exit()

        #we gpt here so either the path is valid or we're using current dir
        strcwd = os.getcwd()

        print('Folder {} is {} bytes'.format(strcwd, convert_size(getdiskusage(strcwd))))

if __name__ == "__main__":
    main()