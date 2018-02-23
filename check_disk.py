import shutil
from utilities import send_email


disk_directories = []
thresh_hold = .1

from_address = ""
from_password = ""
to_address = ""
subject = "Disk Usage Above Thresh Hold"
body = "Disk Report:\n\n"
over = 0

for directory in disk_directories:
    disk_usage = shutil.disk_usage(directory)
    print(disk_usage)
    percentage = disk_usage[1] / disk_usage[0]

    print(percentage)
    if percentage > thresh_hold:
        over += 1
        body += "Disk directory: " + directory
        body += "\nTotal space:" + str(disk_usage[0] / 1073741824) + " GB(s)"
        body += "\nUsed space:" + str(disk_usage[1] / 1073741824) + " GB(s)"
        body += "\nAvailable space:" + str(disk_usage[2] / 1073741824) + " GB(s)"
        body += "\nPercentage in use: " + str(percentage) + "\n"

if over > 0:
    send_email.send_email(from_address, from_password, to_address, subject, body)