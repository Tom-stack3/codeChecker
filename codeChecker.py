import re
import os
os.system("color")

SEPERATOR = "-------------------------------------"

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def print_error(error_str):
    print(bcolors.FAIL + error_str + bcolors.ENDC)

def readAndInitPaths(path, lines):

    try:
        file = open(path, "r")
        for line in file:
            # delete the \n in the end of the line
            line = line.strip('\n')
            lines.append(line)
        return True
    except:
        error_msg = "FileNotFoundError: No such file: '" + path + "'"
        print_error(error_msg)
        return False



def printData(num_comments,num_blank_lines, num_space_lines):
    num_lines = len(lines)
    num_of_code_lines = num_lines - num_comments - num_blank_lines - num_space_lines
    print(bcolors.BOLD + "total number of lines:", num_lines)
    print("number of comment lines:", num_comments)
    print("number of code lines:", num_of_code_lines)
    print("number of blank lines:", num_blank_lines)

    if num_comments != 0:
        print("ratio of code/comments = ", num_of_code_lines / num_comments)
    if num_lines != 0:
        print("percentage of each from the total lines:")
        print("comments takes {}%".format(round((num_comments / num_lines) * 100)))
        print("code takes {}%".format(round((num_of_code_lines / num_lines) * 100)))
        print("blank lines takes {}%".format(round((num_blank_lines / num_lines) * 100)))
    print(bcolors.ENDC)
    print(SEPERATOR)

def printWarningHeader():
    print(SEPERATOR)
    print(bcolors.WARNING + "WARNING!!" + bcolors.ENDC)
    print(SEPERATOR)

def printWarning(warning):
    print(bcolors.WARNING + warning + bcolors.ENDC)
    print(SEPERATOR)

def printCommentCodingStyle(firstWarning,line_num):
    warning = 'found a comment block not according to coding style in line:'
    warning += str(line_num)
    if (firstWarning):
        printWarningHeader()
    printWarning(warning)

def printSpaceWrongUsage(firstWarning,line_num):
    warning = 'used less than 4 spaces as an indention in line:'
    warning += str(line_num)
    if (firstWarning):
        printWarningHeader()
    printWarning(warning)

def printUsingTabAndSpaces(firstWarning):
    warning = 'file uses both spaces and tabs as indention'
    if (firstWarning):
        printWarningHeader()
    printWarning(warning)

def print120Warning(firstWarning, line_num):
    warning = 'used more than 120 chars in line:'
    warning += str(line_num)
    if (firstWarning):
        printWarningHeader()
    printWarning(warning)

def printEmptySpaceLine(firstWarning, line_num):
    warning = 'found an empty space line in line:'
    warning += str(line_num)
    if (firstWarning):
        printWarningHeader()
    printWarning(warning)

def printTwoOneLineComments(firstWarning, line_num):
    warning = 'found two one line comments ( //bla bla ) one after another in line:'
    warning += str(line_num)
    if (firstWarning):
        printWarningHeader()
    printWarning(warning)

def work(lines):
    num_comments = 0
    num_space_lines = 0
    num_blank_lines = 0
    line_num = 1
    firstWarning = True
    isInCommentBlock = False
    usingTab = False
    usingSpaces = False

    #goes over the lines of the code
    for line in lines:
        #check is went over 120 chars
        if len(line) > 120:
            print(line)
            print(line)
            print120Warning(firstWarning, line_num)
            firstWarning = False

        #check if using tab as an indention, and not in comment block
        if not isInCommentBlock and '\t' in line:
            usingTab = True

        # check if using space as an indention, and not in comment block
        if not isInCommentBlock and len(line) > 0 and line[0] == ' ':
            usingSpaces = True

            if len(line) < 4:
                #check if empty space short line
                if not re.search('[a-zA-Z0-9]', line):
                    printEmptySpaceLine(firstWarning,line_num)
                    firstWarning = False
                    num_space_lines += 1
                else:
                    printSpaceWrongUsage(firstWarning, line_num)
                    firstWarning = False

            # check is just an empty space
            elif not re.search('[a-zA-Z0-9]', line):
                printEmptySpaceLine(firstWarning, line_num)
                firstWarning = False
                num_space_lines += 1

            #check is using the proper 4 spaces minimum
            elif line[0:4] != "    ":
                printSpaceWrongUsage(firstWarning, line_num)
                firstWarning = False

        #we are in a comment block and the block hasn't ended
        elif isInCommentBlock and "*/" not in line:
            num_comments += 1
        # we are in a comment block and the block ended
        elif isInCommentBlock and "*/" in line:
            # check if there is text in line with the end of the comment block:
            # bla bla */ - not valid
            if re.search('[a-zA-Z0-9]', line):
                # not according to the coding style
                printCommentCodingStyle(firstWarning, line_num)
                firstWarning = False
            num_comments += 1
            isInCommentBlock = False

        #regular one line comment
        elif not isInCommentBlock and "//" in line:
            num_comments += 1
            #if the previous one was also a one line comment (//bla bla)
            if line_num > 1 and "//" in lines[line_num-2]:
                printTwoOneLineComments(firstWarning, line_num)

        #the block is actually one line
        elif "/*" in line and "*/" in line:
            #not according to the coding style
            printCommentCodingStyle(firstWarning,line_num)
            firstWarning = False
            num_comments += 1
            isInCommentBlock = True
        #we start a comment block
        elif "/*" in line:
            #check if there is text in line with the start of the comment block:
            # /*textHere - not valid
            if re.search('[a-zA-Z0-9]', line):
                # not according to the coding style
                printCommentCodingStyle(firstWarning, line_num)
                firstWarning = False
            num_comments += 1
            isInCommentBlock = True
        # line is empty from chars
        elif not re.search('[a-zA-Z0-9]', line):
            #just a blank line
            if " " not in line:
                num_blank_lines += 1

        line_num+=1

    #forbidden to use both tabs and spaces as indention
    if usingTab and usingSpaces:
        printUsingTabAndSpaces(firstWarning)
        firstWarning = False

    if firstWarning:
        print()
        print(SEPERATOR)
        print(bcolors.OKCYAN + "no problems were found with the file" + bcolors.ENDC)
        print(SEPERATOR)

    print()
    printData(num_comments,num_blank_lines,num_space_lines)

if __name__ == '__main__':
    finished = False
    while not finished:
        lines = []
        print("Enter 0 to exit")
        print("Enter 1 to check a file")
        user_input = input("your choice: ")

        if user_input == "0":
            finished = True
        elif user_input == "1":
            path = input("enter file path:")
            succedded = readAndInitPaths(path, lines)
            if succedded:
                work(lines)
            print()
        else:
            print_error("Please enter an option from the menu")
            print()
