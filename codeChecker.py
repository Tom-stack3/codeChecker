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

def read_init_paths(path, lines):
    try:
        #remove blank characters from beginning and end
        path = path.strip()
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

def print_data(num_comments,num_blank_lines):
    num_lines = len(lines)
    num_of_code_lines = num_lines - num_comments - num_blank_lines
    print(bcolors.BOLD + "total number of lines:", num_lines)
    print("number of comment lines:", num_comments)
    print("number of code lines:", num_of_code_lines)
    print("number of blank lines:", num_blank_lines)

    if num_comments != 0:
        ratio = str(round(num_of_code_lines / num_comments, 3))
        print("ratio of code/comments = ", ratio)
    if num_lines != 0:
        print("percentage of each from the total lines:")
        print(" - comments takes {}%".format(round((num_comments / num_lines) * 100)))
        print(" - code takes {}%".format(round((num_of_code_lines / num_lines) * 100)))
        print(" - blank lines takes {}%".format(round((num_blank_lines / num_lines) * 100)))
    print(bcolors.ENDC)
    print(SEPERATOR)

def print_warning_header():
    print(SEPERATOR)
    print(bcolors.WARNING + "WARNING!!" + bcolors.ENDC)
    print(SEPERATOR)

def print_warning(warning):
    print(bcolors.WARNING + warning + bcolors.ENDC)
    print(SEPERATOR)

def print_comment_coding_style(first_warning,line_num):
    warning = 'found a comment block not according to coding style in line:'
    warning += str(line_num)
    if (first_warning):
        print_warning_header()
    print_warning(warning)

def print_space_wrong_usage(first_warning,line_num):
    warning = 'used less than 4 spaces as an indention in line:'
    warning += str(line_num)
    if (first_warning):
        print_warning_header()
    print_warning(warning)

def print_using_tab_and_spaces(first_warning):
    warning = 'file uses both spaces and tabs as indention'
    if (first_warning):
        print_warning_header()
    print_warning(warning)

def print_120_warning(first_warning, line_num):
    warning = 'used more than 120 chars in line:'
    warning += str(line_num)
    if (first_warning):
        print_warning_header()
    print_warning(warning)

def print_empty_space_line(first_warning, line_num):
    warning = 'found an empty space line in line:'
    warning += str(line_num)
    if (first_warning):
        print_warning_header()
    print_warning(warning)

def print_too_many_blank_lines(first_warning, line_num):
    warning = 'found too many blank lines consecutively in line:'
    warning += str(line_num)
    if (first_warning):
        print_warning_header()
    print_warning(warning)


def print_two_one_line_comments(first_warning, line_num):
    warning = 'found two one line comments ( //comment_here ) one after another in line:'
    warning += str(line_num)
    if (first_warning):
        print_warning_header()
    print_warning(warning)

def work(lines):
    num_blank_lines_in_row = 0
    num_comments = 0
    num_blank_lines = 0
    line_num = 1
    first_warning = True
    is_in_comment_block = False
    using_tab = False
    using_spaces = False

    #goes over the lines of the code
    for line in lines:
        #check is went over 120 chars
        if len(line) > 120:
            print(line)
            print(line)
            print_120_warning(first_warning, line_num)
            first_warning = False

        #check if using tab as an indention, and not in comment block
        if not is_in_comment_block and '\t' in line:
            using_tab = True

        # check if using space as an indention, and not in comment block
        if not is_in_comment_block and len(line) > 0 and line[0] == ' ':
            using_spaces = True

            if len(line) < 4:
                #check if empty space short line
                if not re.search('[a-zA-Z0-9{}]', line):
                    print_empty_space_line(first_warning,line_num)
                    first_warning = False
                    num_blank_lines += 1
                else:
                    print_space_wrong_usage(first_warning, line_num)
                    first_warning = False

            # check is just an empty space
            elif not re.search('[a-zA-Z0-9{}]', line):
                print_empty_space_line(first_warning, line_num)
                first_warning = False
                num_blank_lines += 1

            #check is using the proper 4 spaces minimum
            elif line[0:4] != "    ":
                print_space_wrong_usage(first_warning, line_num)
                first_warning = False

        #we are in a comment block and the block hasn't ended
        elif is_in_comment_block and "*/" not in line:
            num_comments += 1
        # we are in a comment block and the block ended
        elif is_in_comment_block and "*/" in line:
            # check if there is text in line with the end of the comment block:
            # bla bla */ - not valid
            if re.search('[a-zA-Z0-9{}]', line):
                # not according to the coding style
                print_comment_coding_style(first_warning, line_num)
                first_warning = False
            num_comments += 1
            is_in_comment_block = False

        #regular one line comment
        elif not is_in_comment_block and "//" in line:
            num_comments += 1
            #if the previous one was also a one line comment (//bla bla)
            if line_num > 1 and "//" in lines[line_num-2]:
                print_two_one_line_comments(first_warning, line_num)
                first_warning = False

        #the block is actually one line
        elif "/*" in line and "*/" in line:
            #not according to the coding style
            print_comment_coding_style(first_warning,line_num)
            first_warning = False
            num_comments += 1
            is_in_comment_block = True
        #we start a comment block
        elif "/*" in line:
            #check if there is text in line with the start of the comment block:
            # /*textHere - not valid
            if re.search('[a-zA-Z0-9{}]', line):
                # not according to the coding style
                print_comment_coding_style(first_warning, line_num)
                first_warning = False
            num_comments += 1
            is_in_comment_block = True
        # line is empty from chars
        elif not re.search('[a-zA-Z0-9{}]', line):
            num_blank_lines += 1

        #if not in comment block, and line is empty.
        if not is_in_comment_block and not re.search('[a-zA-Z0-9{}]', line):
            num_blank_lines_in_row += 1
        else:
            num_blank_lines_in_row = 0

        #if there are more than 2 blank lines in row
        if num_blank_lines_in_row > 2:
            num_blank_lines_in_row = 0
            print_too_many_blank_lines(first_warning,line_num)
            first_warning = False

        line_num += 1


    #forbidden to use both tabs and spaces as indention
    if using_tab and using_spaces:
        print_using_tab_and_spaces(first_warning)
        first_warning = False

    if first_warning:
        print()
        print(SEPERATOR)
        print(bcolors.OKCYAN + "no problems were found with the file" + bcolors.ENDC)
        print(SEPERATOR)

    print()
    print_data(num_comments,num_blank_lines)

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
            succedded = read_init_paths(path, lines)
            if succedded:
                work(lines)
            print()
        else:
            print_error("Please enter an option from the menu")
            print()
