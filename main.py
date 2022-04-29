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
    print("")
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
        raw_filename2 = raw_filename.split('?')[0]
        filename = raw_filename2.replace("icomoon", "wolf")
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

    # Fix css file to load local files
    with open("css/wolf-awesome.css","r") as wa:
        lines = wa.readlines()
        lines[2] = ""        
        lines[3] = "  src: url('../misc/icomoon.eot');\n"
        lines[4] = "  src: url('../misc/icomoon.eot') format('embedded-opentype'), url('../misc/icomoon.ttf') format('truetype'), url('../misc/icomoon.woff') format('woff'), url('../misc/icomoon.svg') format('svg');\n"
        lines[5] = ""
        lines[6] = ""
        lines[7] = ""
        lines[12] = '[class^="wa-"], [class*=" wa-"] {'
    with open("css/wolf-awesome.css","w") as wa:
        wa.writelines(lines)

    # Correct Icon Names
    with open(r'css/wolf-awesome.css', 'r') as file:
        data = file.read()
        data = data.replace(".icon", ".wa")
    with open(r'css/wolf-awesome.css', 'w') as file:
        file.write(data)
        file.close()
    with open(r'css/wolf-awesome.css', 'r') as file:
        data = file.read()
        data = data.replace("icomoon", "wolf")
    with open(r'css/wolf-awesome.css', 'w') as file:
        file.write(data2)
        file.close()

    # Correct SVG
    with open(r'misc/wolf-awesome.css', 'r') as file:
        data = file.read()
        data = data.replace(".icon", ".wa")
    with open(r'css/wolf-awesome.css', 'w') as file:
        file.write(data)
        file.close()
    with open(r'css/wolf-awesome.css', 'r') as file:
        data2 = file.read()
        data2 = data2.replace("icomoon", "wolf")
    with open(r'css/wolf-awesome.css', 'w') as file:
        file.write(data2)
        file.close()
    
    print("")
    print("Successfully Grabbed all necessary files and built " + colored("wolf-awesome.css","green") + "!")
    print("")
    print("")
    downloader()

if __name__ == '__main__':
    main()