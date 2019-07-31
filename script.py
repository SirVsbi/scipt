import os
import sys


def replaceString(fileName, oldString, newString):
    if not(os.path.isfile(fileName) and os.access(fileName, os.W_OK)):
        return False

    fileUpdated = False




    with open(fileName, 'r') as f:
	    for line in f.readlines():
		    if (oldString in line) :
			    fileUpdated = True


    if fileUpdated :
        filedata = None
        with open(fileName, 'r') as file : 
            filedata = file.read()
        
        newdata = filedata.replace(oldString, newString)

        with open(fileName, 'w') as file: 
            file.write(newdata)
       
    return fileUpdated


def findFiles(oldString, newString):
    patterns = ['.txt', '.html', '.ts']
    print("cserelt: "  + oldString)
    print("erre: " + newString)
    path = os.path.dirname(os.path.realpath(__file__))
    print("pwd:" + path)

    matchingFileList = \
			[os.path.join(dp, f) \
				for dp, dn, filenames in os.walk(path) \
					for f in filenames \
						if os.path.splitext(f)[1] in patterns and f != "words.txt"]

    print('talalt fileok: ' + str(len(matchingFileList)))
    fileCount = 0
    filesReplaced = 0


    for currentFile in matchingFileList:
		
        fileCount+=1
        fileReplaced = replaceString(currentFile, oldString, newString)
        if fileReplaced:
        	filesReplaced+=1

    print("Frissitett fileok : " + str(filesReplaced))



def main():

    if len(sys.argv) < 1: 
        print("baj van az input fileban")
        sys.exit(-1)
    elif len(sys.argv) == 3:
        oldString = sys.argv[1]
        newString = sys.argv[2]
    
    elif len(sys.argv) == 2:
        print(sys.argv)
        with open(sys.argv[1], 'r') as g:
            for line in g.readlines():
                strings = line.split(" ")
                oldString = strings[0]
                oldString.lstrip()
                newString = strings[1].rstrip()
                print(newString)
                findFiles(oldString, newString)



    


if __name__ == '__main__':
    main()