import sys
import os

if (len(sys.argv) > 5):
	classStr = sys.argv[1]
	proName = sys.argv[2]
	gitUrl = sys.argv[3]
	url = sys.argv[4]
	
i = 0

# create directorys
def createDirs(codePath):
	os.makedirs(codePath)


def exist(codePath):
	return os.path.exists(codePath)



def handle(classStr, proName, gitUrl, url):
	global i
	print "[", i, "] handle:", classStr, proName, gitUrl, url
	i += 1

	codePath = classStr + "/" + proName +  "/" +"code/"
	# print codePath
	proPath =  classStr + "/" + proName +  "/"
	# print proPath

	if not exist(codePath):
		createDirs(codePath)
		# write url
		writeUrlCmd = "echo " + url + ">" + proPath + "url"
		# print writeUrlCmd
		os.system(writeUrlCmd)

		# download git code
		gitCmd = "git clone " + gitUrl + " " + codePath
		# print gitCmd
		os.system(gitCmd)
	else:
		print "already exist"
	print "----------------------------------------------------------------\n"



def splitThenHandle(line):
	args = line.split(" ")
	classStr = args[0]
	proName = args[1]
	gitUrl = args[2]
	url = "nil"
	if len(args) > 3:
		url = args[3]

	handle(classStr, proName, gitUrl, url)

def printList(l):
	for x in l:
		print x

# main

failLines = []
with open("download-list.txt") as f:
	for line in f:
		try :
			line = line.strip()
			if len(line) > 0:
				splitThenHandle(line)
		except:
			failLines.append(line)

if len(failLines) > 0:
	print "+++++++++++++++++++++++++++++++++++"
	print "failed projects:"
	printList(failLines)
	fail = open("fail-list.txt", "w+")
	fail.writelines(failLines)
	fail.close()
