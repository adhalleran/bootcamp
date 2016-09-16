import os

pathList = []
for files in os.listdir('../data/HG105_images'):
    pathList.append(files)

print(pathList)
