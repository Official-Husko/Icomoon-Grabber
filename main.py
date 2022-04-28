from time import sleep
import requests
import ctypes
import os
import shutil
from termcolor import colored
from alive_progress import alive_bar
import re

# Defined Variables
version = "1.0"

# Check if folder exists else create it
if os.path.exists('misc'):
    shutil.rmtree('misc', ignore_errors=True)
    os.makedirs('misc')
elif not os.path.exists('misc'):
    os.makedirs('misc')

if not os.path.exists('css'):
    os.makedirs('css')

# Set CMD Title
ctypes.windll.kernel32.SetConsoleTitleW("Husko's Icomoon Grabber | v" + version)

#Clear the Terminal one last time
os.system('cls')

def main():
    print(colored("======================================================================================================================", "red"))
    print(colored("|                                                                                                                    |", "red"))
    print(colored("|     " + colored("Product: ", "white") + colored("Husko's Icomoon Grabber", "green") + colored("                                                                               |", "red"), "red"))
    print(colored("|     " + colored("Version: ", "white") + colored(version, "green") + colored("                                                                                                   |", "red"), "red"))
    print(colored("|     " + colored("Description: ", "white") + colored("Quickly aqcuire the files for locally hosting custom icons.", "green") + colored("                                       |", "red"), "red"))
    print(colored("|                                                                                                                    |", "red"))
    print(colored("======================================================================================================================", "red"))
    print("")
    downloader()

def downloader():
    print("Please Enter the Quick Usage and Sharing Link")
    link = input(">> ")
    header = "Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0"
    try:
        r = requests.get(link,headers={"User-Agent":header},timeout=10,stream=True)
    except:
        print(colored("Invalid or no link provided!","red"))
        print("")
        sleep(3)
        downloader()
    file_path = os.path.join("css/wolf-awesome.css")
    file = open(file_path, 'wb')
    with alive_bar(title="Getting " + colored("wolf-awesome.css","green")) as bar:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                file.write(chunk)
                file.flush()
                bar()
    file.close()
    with open(file_path, "r") as wa:
        raw = wa.read()
        files = re.findall("url\('(?:[^']|'')*'\)", raw)
    for file in files:
        fx1 = file.strip("url('")
        fx2 = fx1.strip("')")
        raw_filename = fx2.split('/')[-1]
        filename = raw_filename.split('?')[0]
        r = requests.get(fx2,headers={"User-Agent":header},timeout=10,stream=True)
        file_path = os.path.join("misc/" + filename)
        file = open(file_path, 'wb')
        with alive_bar(title="Getting " + colored(filename,"green")) as bar:
            for chunk in r.iter_content(chunk_size=1024):
                if chunk:
                    file.write(chunk)
                    file.flush()
                    bar()
        file.close()
    print("Successfully Grabbed " + colored("wolf-awesome.css","green") + " and all necessary files!")
    print("")

    downloader()


if __name__ == '__main__':
    main()
