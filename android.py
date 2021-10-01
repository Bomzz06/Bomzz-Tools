import os
import pafy

path = "/storage/emulated/0/Python Downloader"

if not FileExistsError(path):
    os.mkdir(path)

if not os.path.exists(path):
    os.makedirs(path)
else:
    print("Please Wait! Delay : 2s")

import time
time.sleep(2)
os.chdir("/storage/emulated/0/Python Downloader")
print("Download file auto located to : {0}".format(os.getcwd()))

print("Python Downloader Tools")
def mainMenu():
    print("1 - .mp4 Youtube Downloader")
    print("2 - .mp3 Youtube Downloader")
    print("3 - EXIT")

mainMenu()
option = int(input("Write down the numbers you want to choose : "))

def MP4():
    mp4downloader = input("Paste your link here : ")
    url = pafy.new(mp4downloader)

    print("Video Title : "+url.title)
    print("Please wait ...")
    import time
    time.sleep(2)

    result = url.getbest()
    result.download(f"{url.title}.mp4")
    import time
    time.sleep(2)
    print("Please Wait! Delay : 2s")
    mainMenu()

def MP3():
    mp3downloader = input("Paste your link here : ")
    url = pafy.new(mp3downloader)

    print("Video Title : "+url.title)
    print("Please Wait! Delay : 2s")
    import time
    time.sleep(2)

    result = url.getbestaudio()
    result.download(f"{url.title}.mp3")
    import time
    time.sleep(2)
    print("Please Wait! Delay : 2s")
    mainMenu()

while option != 0:
    if option == 1: 
        MP4()
    elif option == 2: 
        MP3()
    elif option == 3:
        sure = input("Are you sure? Y/N : ")
        if sure == "Y": break 
        elif sure == "N": print("Please Wait! Delay : 2s")
        import time
        time.sleep(2)
        mainMenu()
    else: print("Invalid Number!")

    option = int(input("Write down the numbers you want to choose : "))

print("Thank you for using this tools!")