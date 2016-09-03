import os
import sys
import glob
import random

######################
# Combines
#
# trainval.txt
# test.txt
# train.txt
# val.txt
#
# of all subfolders
######################


def checkPath(path):
    if not os.path.isdir(path):
        print ">> " + path + " <<" + " does not exist."
        print "exit"
        sys.exit()
    return

def init(inputParam):
    print "\n##############"
    print "Pascal VOC style DATA-SET COMBINER"
    print " by Markus Solbach "
    print "    solbach@cse.yorku.ca"
    print "##############\n"

    if len(inputParam) < 2:
        print "\nNot enough arguments (%i)" % len(inputParam)
        print "Usage: synchronize.py <folder>"
        print "<folder> needs subfolders: Annotations with .xml and JPEGImages .JPEG"
        print "exit"
        sys.exit()
    return

def createDirs(outputDir):
    # Create directories
    if not os.path.exists(outputDir):
        os.makedirs(outputDir)

################## Main

init(sys.argv)
path = str(sys.argv[1])
outputDir = path + "ImageSets/"

if not os.path.exists(outputDir):
        os.makedirs(outputDir)

# Combine test.txt files
pathTest = path + "*/ImageSets/test.txt"
txtFilesTest = glob.glob(pathTest)
testData = []
for files in txtFilesTest:
    with open(files, 'r') as myfile:
        fileRead = myfile.read()
        testData = testData + fileRead.split("\n")

random.shuffle(testData)
fileTest = open(outputDir + "test.txt", 'w+')
count = 0
for item in testData:
    count = count + 1
    if count < len(testData):
        fileTest.write("%s\n" % item)
    else:
        fileTest.write("%s" % item)


print testData
print len(testData)

# fileTest = open(outputDir + "test.txt", 'w+')

# fileTest.write("\n")

# fileTest.close()