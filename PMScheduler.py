while True:
    certChoice = input("Type 1 for Network+ or 2 for Security+ and press enter: ")
    if certChoice not in ('1', '2'):
        print("Sorry, I only accept 1 or 2. \n")
    else:
        break

totalSeconds = 0
inFile = ""
outFile = ""
if certChoice == "1":
    inFile = "PMNetVids.txt"
    outFile = "PMNetSched.txt"
    totalSeconds = 43742
elif certChoice == "2":
    inFile = "PMSecVids.txt"
    outFile = "PMSecSched.txt"
    totalSeconds = 49494

secondsPerWeek = 0
while True:
    try:
        weeksToStudy = int(input('How many weeks do you have to study?: '))
    except ValueError:
        print("Sorry, I only accept integers. \n")
        continue
    else:
        secondsPerWeek = totalSeconds//weeksToStudy
        break


videoList = []
f = open(inFile, "r")
for line in f:
    if not line.startswith("Section") and not line[2:3].isdigit() and line.isspace() == False:
        videoList.append((line[5:line.rfind("-")-1],line[-10:-2], int(line[-7:-5]) * 60 + int(line[-4:-2])))
    # if line.startswith("Section"):    get sections
    # if line[2:3].isdigit():    get lessons
    else: continue
f.close()

weekTotal = 0
weekStart = 0
weekNum = 1
f = open(outFile,"w+")

avgMTotal, avgSeconds = divmod(secondsPerWeek, 60)
avgHours, avgMinutes = divmod(avgMTotal, 60)
if secondsPerWeek < sorted(videoList, key=lambda video: video[2])[0][2]:
    f.write("Watch 1 video per week to finish in " + str(weeksToStudy) + " weeks. \n")
else:
    f.write("Watch approximately (" + str(avgHours).zfill(2) + ":" + str(avgMinutes).zfill(2) + ":" + str(avgSeconds).zfill(2) + ") per week to finish in " +  str(weeksToStudy) + " weeks.\n")

for video in videoList:
    if weekTotal <= secondsPerWeek:
        if weekTotal == 0:
            f.write("------------- Week " + str(weekNum) + " Schedule ------------- \n")
            if weekNum != 1:
                weekTotal += weekStart
                f.write(videoList[videoList.index(video)-1][0] + " - (" + videoList[videoList.index(video)-1][1] + ") \n")
            else: pass
            if weekTotal <= secondsPerWeek:
                f.write(video[0] + " - (" + video[1] + ") \n")
                weekTotal += video[2]
                weekStart = weekTotal
            else:
                weekStart = video[2]
                wM, weekSeconds = divmod(weekTotal, 60)
                weekHours, weekMinutes = divmod(wM, 60)
                f.write("Week " + str(weekNum) + " total: (" + str(weekHours).zfill(2) + ":" + str(weekMinutes).zfill(2) + ":" + str(weekSeconds).zfill(2) + ") \n\n")
                weekTotal = 0
                weekNum += 1
        else:
            f.write(video[0] + " - (" + video[1] + ") \n")
            weekTotal += video[2]
            weekStart = weekTotal
    else:
        weekStart = video[2]
        wM, weekSeconds = divmod(weekTotal, 60)
        weekHours, weekMinutes = divmod(wM, 60)
        f.write("Week " + str(weekNum) + " total: (" + str(weekHours).zfill(2) + ":" + str(weekMinutes).zfill(2) + ":" + str(weekSeconds).zfill(2) + ") \n\n")
        weekTotal = 0
        weekNum += 1

if weekTotal == 0:
    f.write("------------- Week " + str(weekNum) + " Schedule ------------- \n")
    f.write(videoList[-1][0] + " - (" + videoList[-1][1] + ") \n")
else: pass
wM, weekSeconds = divmod(weekStart, 60)
weekHours, weekMinutes = divmod(wM, 60)
f.write("Week " + str(weekNum) + " total: (" + str(weekHours).zfill(2) + ":" + str(weekMinutes).zfill(2) + ":" + str(weekSeconds).zfill(2) + ")")
