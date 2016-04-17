import os

#creating empty .txt files
def createFile(number):
	for n in range(1,number+1):
		open((('%d.txt' % n)),'w')

#deleting all the odd numbered files
def deleteODD(maxNumber):
	for n in range(1,maxNumber+1):
		if (n%2 != 0):
			os.remove(('%d.txt' %n))

#to rename all the files
def renameFiles(numOfFiles):
	count = 1
	for n in range(2,numOfFiles+1,2):
		print "Inside"
		print n
		os.rename("%d.txt" % n,"%d.txt" % count )
		count = count + 1

#will create 103 files
createFile(103)
#will delete bunch of files
deleteODD(103)
#will rename the files so that they are named starting from 1 to 51
renameFiles(102)
