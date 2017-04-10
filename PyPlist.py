import re

def readPlayList():
    newPlaylist = []
    playListCount = 0

    # TODO(K.S) parse command line arguments
    playList = open("./PlayList1.pls", 'r')
    for line in playList:
        # Get length of playList, first occurence of a number
        newPlaylist.append(line)
        res = re.findall(r'\d+', line)
        if res:
            playListCount = int(res[0])
            break

    for line in playList:
        res = re.findall('^Version', line)
        if res:
            break
        newPlaylist.append(line)
    playList.close()

    # Merge in the other files
    playList = open("./PlayList2.pls", 'r')
    for line in playList:
        res = re.findall(r'File(\d+)', line)
        if res:
            playListCount += 1
            # search for File and replace with incrementing number
            newLine = re.sub('(\d+)', str(playListCount), line, 1)
            newPlaylist.append(newLine)
        res = re.findall(r'Length(\d+)', line)
        if res:
            newLine = re.sub(r'(\d+)', str(playListCount), line, 1)
            newPlaylist.append(newLine)
            newPlaylist.append('\n')

    for line in playList:
        res = re.findall('^Version', line)
        if res:
            break
        newPlaylist.append(line)
    playList.close()

    newList = open('./outputList.pls', 'w')
    # Go to beginning of file and update the NumberOfEntries
    for line in newPlaylist:
        res = re.findall(r'\d+', line)
        if res:
            newLine = re.sub(r'(\d+)', str(playListCount), line, 1)
            newPlaylist.insert(1, newLine)
            newPlaylist.pop(2)
            break

    # Write new composed content into file
    newList.writelines(newPlaylist)

    # append at bottom Version=2
    newList.write('Version=2')
    newList.close()

readPlayList()
