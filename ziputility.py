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
            addFolderToZip(zipfilename, file, zf)
    except KeyError:
        print "Error in creating the Archive file"
    finally:
        print "Closing"
        zf.close()

def addFolderToZip(zip_file, folder, zip_file1):
    for file in os.listdir(folder):
        full_path = os.path.join(folder, file)
        if os.path.isfile(full_path):
            print 'File added: ' + str(full_path)
            zip_file1.write(full_path)
        elif os.path.isdir(full_path):
            print 'Entering folder: ' + str(full_path)
            addFolderToZip(zip_file, full_path, zip_file1)

    zip_file1.close()

def extractArchiveFile(zipfilename, extractpath):
    """ This function extract the archive """
    zip_file = zipfile.ZipFile(zipfilename, 'r')
    try:

        zip_file.extractall(extractpath)
        print "Archive file is successfully extracted"
    except KeyError:
        print "Error in extracting the Archive file"

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

def deleteFilesFromArchive(zipfilename, filetodelete):
    tmpzip = 'archve_new.zip'
    zin = zipfile.ZipFile (zipfilename, 'r')
    zout = zipfile.ZipFile (tmpzip, 'w')
    for item in zin.infolist():
        buffer = zin.read(item.filename)
        if (item.filename <> filetodelete):
            zout.writestr(item, buffer)
    zout.close()
    zin.close()

    os.unlink(zipfilename)
    os.rename(tmpzip, zipfilename)

def exitApp():
    """ Gets exit from the program """
    print "Successfully exited the program"
    exit



options = {
            1 : toArchive,
            2 : extractArchiveFile,
            3 : listFilesFromArchive,
            4 : deleteFilesFromArchive,
            5 : exitApp,
        }

def PrintOptions():
    """ This function lists the options """
    print("""
            1. Add to archive file
            2. Extract a Archive file
            3. List files from Archive
            4. Remove files from Archive
            5. Exit  """)


def main():
    filename = ""
    directory = 'calculator'

    while True:
        PrintOptions()
        option = input("Enter the option from the list: ")

        if options.has_key(option):
            if option == 1:
                if os.path.isfile(filename):
                    pass
                else:
                    filename = raw_input("Enter the zip file name, example test.zip: ")
                    if not filename: filename = 'download.zip'
                options[option](directory, filename)

            elif option == 2:
                filename = raw_input("Enter the zip file name, example test.zip: ")
                extractpath = raw_input("Enter the full path to extract: ")
                options[option](filename, extractpath)

            elif option == 3:
                options[option](filename)

            elif option == 4:
                filename = raw_input("Enter the zip file name, example test.zip: ")
                filetodelete = raw_input("Enter the file name to delete, example file.txt: ")
                options[option](filename, filetodelete)

            elif option == 5 :
                options[option]()
                break

        continue

main()