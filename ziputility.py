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
import zipfile, os, sys, shutil

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
    dir1, zipname = os.path.split(zipfilename)
    extractpath = os.path.join(extractpath, os.path.splitext(zipname)[0])
    os.chdir(dir1)
    zip_file = zipfile.ZipFile(zipname, 'r')
    try:

        zip_file.extractall(extractpath)
        print "\n Archive file is successfully extracted"
    except KeyError:
        print "Error in extracting the Archive file"

def listFilesFromArchive(zipfilename):
    """ This function list out the contents of the archive """
    dir1, zipname = os.path.split(zipfilename)
    os.chdir(dir1)
    zf = zipfile.ZipFile(zipname, 'r')
    try:
        print '\n'
        print '********** ' + zipname + ' contains below list:' + ' **********'
        print '\n'
        zf.printdir()
    except IOError:
        print "Error in listing the file info"
    finally:
        zf.close()

def deleteFilesFromArchive(zipfilename, filetodelete):
    tmpzip = 'archve_new.zip'
    dir1, zipname = os.path.split(zipfilename)
    os.chdir(dir1)
    zin = zipfile.ZipFile (zipname, 'r')
    zout = zipfile.ZipFile (tmpzip, 'w')
    for item in zin.infolist():
        buffer = zin.read(item.filename)
        if (item.filename <> filetodelete):
            zout.writestr(item, buffer)
    zout.close()
    zin.close()

    shutil.move(tmpzip, zipname)

def exitApp():
    """ Gets exit from the program """
    print "\n Successfully exited the program"
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
            # Call zipfolder function
            if option == 1:
                if os.path.isfile(filename):
                    pass
                else:
                    directory = raw_input("Enter the full directory path to zip: ")
                    dir1, filename = os.path.split(directory)
                    if not filename: filename = 'download.zip'
                options[option](filename, directory)

                filename += '.zip'
                shutil.move(filename, dir1)

            # Call extractArchiveFile function
            elif option == 2:
                filename = raw_input("Enter the zip file name with complete path: ")
                extractpath = raw_input("Enter the full path to extract: ")
                options[option](filename, extractpath)

            # Call listFilesFromArchive function
            elif option == 3:
                filename = raw_input("Enter the zip file name with complete path: ")
                options[option](filename)

            # Call deleteFilesFromArchive function
            elif option == 4:
                filename = raw_input("Enter the zip file name with complete path: ")
                filetodelete = raw_input("Enter the file name to delete, example file.txt: ")
                options[option](filename, filetodelete)

            # Call exitApp function
            elif option == 5 :
                options[option]()
                break

        continue
    sys.exit()

main()