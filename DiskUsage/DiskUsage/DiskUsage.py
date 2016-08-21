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
        os.chdir(sys.argv[1])

    strcwd = os.getcwd()

    print('Folder {} is {} bytes'.format(strcwd, convert_size(getdiskusage(strcwd))))

if __name__ == "__main__":
    main()