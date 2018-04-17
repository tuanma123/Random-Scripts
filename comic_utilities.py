#!/usr/bin/python
import os
import sys


def usage():
    print("Usage:" + sys.argv[0] + "<directory> [-r]")

def convert_comics(directory):
    """
    Goes a directory to convert any files of supported formatss to .cbz files.

    Support file formats: .zip, .rar, .7z, .cbr

    :param directory: The directory to go through.
    :return:
    """
    for file in os.listdir(directory):
        if file.endswith(".zip") or file.endswith(".rar"):
            file_name = file[:len(file) - 4]
            print(file_name)
            os.rename(directory + "\\" + file, directory + "\\" + file_name + ".cbz")


def convert_comics_recursive(rootdir):
    """
    Goes through a root directory and any subfolders to convert any files of supported formats to .cbz files.
    Support file formats: .zip, .rar, .7z, .cbr

    :param rootdir: The root directory to go through. Will go through any subdirectories.
    :return:
    """

    for root, subdirs, files in os.walk(rootdir):
        for file in os.listdir(root):
            if file.endswith(".zip") or file.endswith(".rar") or file.endswith(".7z") or file.endswith(".cbr"):
                file_name = file[:len(file) - 4]
                print(file_name)
                os.rename(root + "\\" + file, root + "\\" + file_name + ".cbz")


if __name__ == "__main__":
    if len(sys.argv) != 2 and sys.argv != 3:
        usage()
    else:
        if len(sys.argv) == 2:
            convert_comics(sys.argv[1])
        if len(sys.argv) == 3:
            if sys.argv[2] != "-r":
                usage()
            else:
                convert_comics_recursive(sys.argv[1])