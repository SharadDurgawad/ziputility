#-------------------------------------------------------------------------------
# Name:         ziputility
# Purpose:      archives the files, extract the files, append the files
#                in the archives etc
#
# Author:      sdurgawad
#
# Created:     16/07/2016
# Copyright:   (c) sdurgawad 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import zipfile, os, sys


def toArchive(file, zipfilename):
    """ This function creates the archive """

    if os.path.isfile(zipfilename):
        zf = zipfile.ZipFile(zipfilename, 'a')
    else:
        zf = zipfile.ZipFile(zipfilename, 'w')

    try:
        if os.path.isfile(file):
            zf.write(file)
        else:
            addFolderToZip(zipfilename, file)
    except KeyError:
        print "Error in creating the Archive file"
    finally:
        print "Closing"
        zf.close()

def addFolderToZip(zip_file, folder):
    zip_file = zipfile.ZipFile(zip_file, 'a')
    for file in os.listdir(folder):
        full_path = os.path.join(folder, file)
        if os.path.isfile(full_path):
            print 'File added: ' + str(full_path)
            zip_file.write(full_path)
        elif os.path.isdir(full_path):
            print 'Entering folder: ' + str(full_path)
            addFolderToZip(zip_file, full_path)

    zip_file.close()

def extractArchiveFile(zipfilename):
    """ This function extract the archive """
    zip_file = zipfile.ZipFile(zipfilename, 'r')
    try:
        zip_file.extractall()
        print "Archive file is successfully extracted"
    except KeyError:
        print "Error in extracting the Archive file"

def AppendFilesToArchive():
    """ This function appends the files to the archive """
    zf = zipfile.ZipFile('file.zip', 'a')
    try:
        zf.write('file1.txt')
        zf.write('file2.txt')
    except KeyError:
        print "Error in appending the file to the Archive"
    finally:
        zf.close()

def listFilesFromArchive(zipfilename):
    """ This function list out the contents of the archive """
    zf = zipfile.ZipFile(zipfilename, 'r')
    try:
        print "file.zip contains below list:"
        zf.printdir()
    except IOError:
        print "Error in listing the file info"
    finally:
        zf.close()

def exitApp():
    """ Gets exit from the program """
    print "Successfully exited the program"
    exit



options = {
            1 : toArchive,
            2 : extractArchiveFile,
            3 : listFilesFromArchive,
            4 : exitApp,
        }

def PrintOptions():
    """ This function lists the options """
    print("""
            1. Add to archive file
            2. Extract a Archive file
            3. List files from the Archive
            4. Exit  """)


def main():
    filename = 'file.zip'
    directory = 'calculator'

    while True:
        PrintOptions()
        option = input("Enter the option from the list: ")

        if options.has_key(option):
            if option == 1:
                options[option](directory, filename)
            elif option == 2:
                options[option](filename)
                pass
            elif option == 3:
                options[option](filename)
            elif option == 4 :
                options[option]()
                break

        continue

main()