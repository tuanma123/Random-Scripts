import spice_api as spice
import requests
import os

mal_username = ""
mal_password = ""
manga_directories = [""]

credentials = spice.init_auth(mal_username, mal_password)

"""
Goes through a the directories labeled as manga directories and attempts to download covers from myanimelist.com for 
mangas that do not already have one. Manga that could not be found are skipped.

"""

for directory in manga_directories:



    no_results = []
    processed = []
    already_processed = []
    for manga in os.listdir(directory):
        if not"folder.jpg" in os.listdir(directory + "\\" + manga) and manga != "desktop.ini":
            search_results = spice.search(manga, spice.get_medium('manga'), credentials)
            if len(search_results) > 0:
                image_url = search_results[0].image_url
                image_directory = directory + "\\" + manga + "\\" + "folder.jpg"
                image_file = open(image_directory, 'wb')  # create file locally
                image_file.write(requests.get(image_url).content)
                image_file.close()
                processed.append(manga)
            else:
                no_results.append(manga)
        else:
            if manga != "desktop.ini":
                already_processed.append(manga)
print(already_processed)
print("The following manga covers were downloaded:")
for manga in processed:
    print(manga)
print("No covers were found for these manga. Please recheck the title or find a cover manually.")
for manga in no_results:
    print(manga)

