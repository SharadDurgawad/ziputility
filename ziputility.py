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

from os.path import basename
import zipfile, os, sys

def zipfolder(foldername, target_dir):
    zipobj = zipfile.ZipFile(foldername + '.zip', 'w', zipfile.ZIP_DEFLATED)
    rootlen = len(target_dir) + 1
    for base, dirs, files in os.walk(target_dir):
        for file in files:
            fn = os.path.join(base, file)
            zipobj.write(fn, fn[rootlen:])
    zipobj.close()


def extractArchiveFile(zipfilename, extractpath):
    """ This function extract the archive """
    extractpath = os.path.join(extractpath, zipfilename[:-4])
    zip_file = zipfile.ZipFile(zipfilename, 'r')
    try:

        zip_file.extractall(extractpath)
        print "Archive file is successfully extracted"
    except KeyError:
        print "Error in extracting the Archive file"

def listFilesFromArchive(zipfilename):
    """ This function list out the contents of the archive """
    base_file = os.path.basename(zipfilename)
    zf = zipfile.ZipFile(base_file, 'r')
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
            1 : zipfolder,
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
    directory = ""

    while True:
        PrintOptions()
        option = input("Enter the option from the list: ")

        if options.has_key(option):
            if option == 1:
                if os.path.isfile(filename):
                    pass
                else:
                    directory = raw_input("Enter the full directory path to zip: ")
                    filename = os.path.basename(directory)
                    if not filename: filename = 'download.zip'
                options[option](filename, directory)

            elif option == 2:
                filename = raw_input("Enter the zip file name, example test.zip: ")
                extractpath = raw_input("Enter the full path to extract: ")
                options[option](filename, extractpath)

            elif option == 3:
                filename = raw_input("Enter the zip file name with complete path: ")
                options[option](filename)

            elif option == 4:
                filename = raw_input("Enter the zip file name, example test.zip: ")
                filetodelete = raw_input("Enter the file name to delete, example file.txt: ")
                options[option](filename, filetodelete)

            elif option == 5 :
                options[option]()
                break

        continue
    sys.exit()

main()