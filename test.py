from imgdl import download
import os
from bs4 import BeautifulSoup as BSHTML
import urllib
def Start():
    #Create "Albums" folder if it doesn't exist already
    os.listdir
    T = "Albums"
    if T not in os.listdir():
        os.mkdir("Albums")
    #Check the list.txt file for duplicate with the completed.txt file.
    with open('list.txt','r+') as f:
        linesA = f.read().split("\n")
    with open('completed.txt','r+') as t:
        linesB = t.read().split("\n")
    #Delete said duplicates in the list
    for i in linesA[:]:
        if i in linesB:
            linesA.remove(i)
    #Delete said duplicates from the .txt
    with open('list.txt','w') as y:
        for item in linesA:
            y.write("%s\n" % item)
    with open('completed.txt','w') as u:
        for item in linesB:
            u.write("%s\n" % item)

def Menu():
    #Start of user activity
    A=50
    print("Welcome to my bad bulk image downloader. Also my first actual python project since I learned it\n1.Download from a link\n2.Download from list.txt without user input\n3.Settings")
    inpuut = input()
    if inpuut == "3":
        print("1.Number of download threads(default is 50)\n2.Return")
        V = input()
        if V == "1":
            A =input("Number of threads: ")
            Menu()
        if V == "2":
            Menu()
    if inpuut == "1":
        #Fetching image URLS
        count = "1"
        link = input("Enter link: ")
        page = urllib.request.urlopen(link)
        soup = BSHTML(page)
        images = soup.findAll('img')
        count2 = 'Albums/Folder'+count
        os.mkdir(count2)
        path = count2
        for image in images:
            P=(image['src'])
            try:
                paths = download(P, store_path=path, n_workers=A)
            except:
                pass
        count = count+"1"
    if inpuut == "2":
        print("WIP")
        Menu()
Start()
Menu()
