import os.path


def findFile(f1, x):
    '''checks for file f1 and if found returns x = 1'''
    if os.path.exists(f1):
        print "\nUsing the following file", f1, "...\n"
        x = 1
        return x
    else:
        print "File Not Found\nthe file", f1, "was not found\n"


def find2Files(f1, f2, x):
    '''checks for files f1 and f2; and if found returns x = 1'''
    if os.path.exists(f1):
        if os.path.exists(f2):
            print "\nUsing the following files:", f1, "and", f2, "...\n"
            x = 1
            return x
        else:
            print "File Not Found\nthe file", f2, "was not found\n"
    else:
        print "File Not Found\nthe file", f1, "was not found\n"


def find3Files(f1, f2, f3, x):
    '''checks for files f1, f2 and f3; and if found returns x = 1'''
    if os.path.exists(f1):
        if os.path.exists(f2):
            if os.path.exists(f3):
                print "\nUsing the following files:\
                ", f1, ", ", f2, "and", f3, "...\n"
                x = 1
                return x
            else:
                print "File Not Found\nthe file", f3, "was not found\n"
        else:
            print "File Not Found\nthe file", f2, "was not found\n"
    else:
        print "File Not Found\nthe file", f1, "was not found\n"
