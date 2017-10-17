import os


def get_directory_size(path):
    """ Recursively counts the size of a directory and its all its sub-folders and files in bytes.

    :param path: The path to the directory.
    :return: An integer representing the size of the directory and its subdirectory in bytes.
    """
    total_size = 0
    for directory_path, directory_names, file_names in os.walk(path):
        for f in file_names:
            fp = os.path.join(directory_path, f)
            total_size += os.path.getsize(fp)

    return total_size


def sort_folders_by_size(directory):
    """ Lists all folders in a directory in order of the size of their contents. Sorts by smallest folders first.

    :param directory: The path to the directory.
    :return: A print out of the folders in the directory in the order of
    """
    folder_size_map = {}
    for folder in sorted(os.listdir(directory)):
        folder_size_map[get_directory_size(directory + "\\" + folder)] = folder

    for folder in sorted(folder_size_map):
        print(folder_size_map[folder])


def get_file_extension_count(directory, file_extension):
    """ Counts the number of files of a specific file extension in a root directory and all its subdirectories.

    :param directory: The root directory.
    :param file_extension: The file extension to count.
    :return:
    """
    file_count = 0
    for (directory_path, directory_names, file_names) in os.walk(directory):
        for file in file_names:
            if file.endswith("." + file_extension):
                file_count += 1
    return file_count


def convert_comics_recursive(rootdir):
    for root, subdirs, files in os.walk(rootdir):
        for file in os.listdir(root):
            if file.endswith(".zip") or file.endswith(".rar"):
                file_name = file[:len(file) - 4]
                print(file_name)
                os.rename(root + "\\" + file, root + "\\" + file_name + ".cbz")
