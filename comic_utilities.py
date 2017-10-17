import os


def convert_comics(directory):
    for file in os.listdir(directory):
        if file.endswith(".zip") or file.endswith(".rar"):
            file_name = file[:len(file) - 4]
            print(file_name)
            os.rename(directory + "\\" + file, directory + "\\" + file_name + ".cbz")


def convert_comics_recursive(rootdir):
    """
    Goes through a root directory and any subfolders to convert any files of supported formats to .cbz files.
    Support file formats: .zip, .rar, .7z, .cbr
    Note: There should still be manual inspections of the files converted to check for any discrepancies.

    :param rootdir:
    :return:
    """

    for root, subdirs, files in os.walk(rootdir):
        for file in os.listdir(root):
            if file.endswith(".zip") or file.endswith(".rar") or file.endswith(".7z") or file.endswith(".cbr"):
                file_name = file[:len(file) - 4]
                print(file_name)
                os.rename(root + "\\" + file, root + "\\" + file_name + ".cbz")


def rename(directory):
    for comic in os.listdir(directory):
        parts = comic[0: len(comic) - 4].split(" - ")
        print(parts)

        old = directory + "\\" + comic
        print(old)
        new = directory + "\\"
        for x in range(1, len(parts)):
            new += parts[x]
            if not x == len(parts) - 1:
                new += " - "
        new += " [" + parts[0] + "].cbz"
        print(new)
        os.rename(old,new)