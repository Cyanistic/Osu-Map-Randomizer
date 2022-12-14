import os
import random

inputData = input(f"If you are using a file name please ensure that it is in the \"{os.getcwd()}\" directory.\nEnter the data from a .osu file or the file's name: \n")

while(True):
    if(inputData.endswith(".txt") or inputData.endswith(".osu")):
        if(os.path.exists(inputData)):
            inputFile = open(inputData, "r")
            try:
                dataArray = inputFile.readlines()
            except UnicodeDecodeError:
                print("Error: File contains unicode characters.")
                break
            inputData = ""
            for line in dataArray:
                inputData += line
            break
        else:
            print("Error! That file does not exist!\nPlease try again:")
            inputData = input()
    else:
        dataArray = inputData.split("\n")
gamemode = int(inputData[inputData.find("Mode: ")+6:inputData.find("Mode: ")+7])
diffName = inputData[inputData.find("Version:"):inputData.find("\n",inputData.find("Version:"))+1]
objectAreaIndex = dataArray.index("[HitObjects]\n")+1
dataArray[dataArray.index(diffName)] = diffName[0:diffName.find("\n")] + " (Randomized)\n"

def find_nth_overlapping(haystack, needle, n):
    start = haystack.find(needle)
    while start >= 0 and n > 1:
        start = haystack.find(needle, start+1)
        n -= 1
    return start

def lnCheck(data, ln):
    for i in range(len(ln)):
        if(data[0:data.find(",")] == ln[i][0:ln[i].find(",")] and int(data[find_nth_overlapping(data, ",", 2)+1:find_nth_overlapping(data, ",", 3)]) > int(ln[i][find_nth_overlapping(ln[i], ",", 1)+1:find_nth_overlapping(ln[i], ",", 2)])) and int(data[find_nth_overlapping(data, ",", 2)+1:find_nth_overlapping(data, ",", 3)]) <= int(ln[i][find_nth_overlapping(ln[i], ",", 2)+1:len(ln[i])]):
            return True
    return False

def std():
    print("std")
    print("Standard map detected.")
    print("This gamemode is not supported yet.")

def taiko():
    print("Taiko map detected.")

    hitsoundArray = ["8","0","12","4"]
    """ newHitsound = True

    for i in range(objectAreaIndex,len(dataArray)):
        for j in range(len(hitsoundArray)):
            if(hitsoundArray[j] == dataArray[i][find_nth_overlapping(dataArray[i],",", 4)+1:find_nth_overlapping(dataArray[i],",", 5)]):
                newHitsound = False
                break
            else:
                newHitsound = True
        if(newHitsound):
            hitsoundArray.append(dataArray[i][find_nth_overlapping(dataArray[i],",", 4)+1:find_nth_overlapping(dataArray[i],",", 5)])
 """
    for i in range(objectAreaIndex,len(dataArray)):
        if(dataArray[i][find_nth_overlapping(dataArray[i],",", 4)+1:find_nth_overlapping(dataArray[i],",", 5)] == "0" or dataArray[i][find_nth_overlapping(dataArray[i],",", 4)+1:find_nth_overlapping(dataArray[i],",", 5)] == "8"):
            dataArray[i] = dataArray[i][0:find_nth_overlapping(dataArray[i],",", 4)+1] + hitsoundArray[random.randint(0,1)] + dataArray[i][find_nth_overlapping(dataArray[i],",", 5):]
        else:
            dataArray[i] = dataArray[i][0:find_nth_overlapping(dataArray[i],",", 4)+1] + hitsoundArray[random.randint(2,3)] + dataArray[i][find_nth_overlapping(dataArray[i],",", 5):]
    
    out = open(input("Enter the output file name:"), "w")
    out.writelines(dataArray)
    # print(dataArray[objectAreaIndex:len(dataArray)])
    print("Success!")

def ctb():
    print("ctb")
    print("CTB map detected.")
    print("This gamemode is not supported yet.")

def mania():
    print("Mania map detected.")

    xPos = []
    newKey = True
    
    for i in range(objectAreaIndex, len(dataArray)):
        for j in range(len(xPos)):
            if(xPos[j] == dataArray[i][0:dataArray[i].find(",")]):
                newKey = False
                break
            else:
                newKey = True
        if(newKey):
             xPos.append(dataArray[i][0:dataArray[i].find(",")])
    
    totalNoteNum = 0
    noteNum = 0
    lnArray = []
    noteTiming = dataArray[objectAreaIndex][find_nth_overlapping(dataArray[objectAreaIndex], ",", 2)+1:find_nth_overlapping(dataArray[objectAreaIndex], ",", 3)]
    dataArray.append("")

    while (totalNoteNum+1 < len(dataArray)-objectAreaIndex):
        randomChoose = [*range(len(xPos))]
        while(noteTiming == dataArray[objectAreaIndex+totalNoteNum+noteNum][dataArray[objectAreaIndex+totalNoteNum+noteNum].find(",", dataArray[objectAreaIndex+totalNoteNum+noteNum].find(",")+1)+1:dataArray[objectAreaIndex+totalNoteNum+noteNum].find(",", dataArray[objectAreaIndex+totalNoteNum+noteNum].find(",", dataArray[objectAreaIndex+totalNoteNum+noteNum].find(",")+1)+1)] and totalNoteNum+noteNum+1 < len(dataArray)-objectAreaIndex):
            noteNum +=1
        for k in range(noteNum):
            firstCheck = True
            while(lnCheck(dataArray[objectAreaIndex+totalNoteNum+k], lnArray) or firstCheck):
                tempStore = dataArray[objectAreaIndex+totalNoteNum+k][dataArray[objectAreaIndex+totalNoteNum+k].find(","):len(dataArray[objectAreaIndex+totalNoteNum+k])]
                randSave = random.randint(0, len(randomChoose)-1)
                dataArray[objectAreaIndex+totalNoteNum+k] = xPos[randomChoose[randSave]] + tempStore
                randomChoose.pop(randSave)
                firstCheck = False
            if (dataArray[objectAreaIndex+totalNoteNum+k][find_nth_overlapping(dataArray[objectAreaIndex+totalNoteNum+k], ",", 5):dataArray[objectAreaIndex+totalNoteNum+k].find(":")] != "0"):
                lnArray.append(dataArray[objectAreaIndex+totalNoteNum+k][0:dataArray[objectAreaIndex+totalNoteNum+k].find(",")] + dataArray[objectAreaIndex+totalNoteNum+k][find_nth_overlapping(dataArray[objectAreaIndex+totalNoteNum+k], ",", 2):find_nth_overlapping(dataArray[objectAreaIndex+totalNoteNum+k], ",", 3) ] + dataArray[objectAreaIndex+totalNoteNum+k][find_nth_overlapping(dataArray[objectAreaIndex+totalNoteNum+k], ",", 5):dataArray[objectAreaIndex+totalNoteNum+k].find(":")])

        randomChoose.clear()
        
        noteTiming = dataArray[objectAreaIndex+totalNoteNum+noteNum][dataArray[objectAreaIndex+totalNoteNum+noteNum].find(",", dataArray[objectAreaIndex+totalNoteNum+noteNum].find(",")+1)+1:dataArray[objectAreaIndex+totalNoteNum+noteNum].find(",", dataArray[objectAreaIndex+totalNoteNum+noteNum].find(",", dataArray[objectAreaIndex+totalNoteNum+noteNum].find(",")+1)+1)]
        totalNoteNum += noteNum
        noteNum = 0

    out = open(input("Enter the output file name:"), "w")
    out.writelines(dataArray)
    # print(dataArray[objectAreaIndex:len(dataArray)])
    print("Success!")

match gamemode:
    case 0:
        std()
    case 1:
        taiko()
    case 2:
        ctb()
    case 3:
        mania()
    case _:
        print("Error! Invalid gamemode!")