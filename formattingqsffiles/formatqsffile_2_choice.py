import re
import os
import random
import csv
def sortimagelist(currentlist):
   mappedlist =  list(map(int, re.findall(r'\d+', currentlist)))[0]
   return mappedlist

def main():



    ################################################

    imagestoaddg1 = []
    allinesg1 = []
    with open('imagestoaddg1.txt') as f:
        lines = f.readlines()
        lines.sort(key=sortimagelist)
        allinesg1 = lines
    if os.path.exists("imagestoaddg1sorted.txt"):
        os.remove("imagestoaddg1sorted.txt")
    else:
        print("The file does not exist")
    with open('imagestoaddg1sorted.txt', 'a') as f:

        f.writelines(allinesg1)

    with open('imagestoaddg1sorted.txt') as f:
        lines = f.readlines()
        imageRE = 'IM_[0-9a-zA-Z]{11,15}$'
        for line in lines:

            graphicID = re.findall(imageRE, line)
            imagestoaddg1.append(graphicID[0])

    ################################################
    imagestoaddg2 = []
    allinesg2 = []
    with open('imagestoaddg2.txt') as f:
        lines = f.readlines()
        lines.sort(key=sortimagelist)
        allinesg2 = lines
    if os.path.exists("imagestoaddg2sorted.txt"):
        os.remove("imagestoaddg2sorted.txt")
    else:
        print("The file does not exist")
    with open('imagestoaddg2sorted.txt', 'a') as f:

        f.writelines(allinesg2)
    with open('imagestoaddg2sorted.txt') as f:
        lines = f.readlines()
        imageRE = 'IM_[0-9a-zA-Z]{11,15}$'
        for line in lines:

            graphicID = re.findall(imageRE, line)
            imagestoaddg2.append(graphicID[0])
    ################################################
    imagestoaddg3 = []
    allinesg3 = []
    with open('imagestoaddg3.txt') as f:
        lines = f.readlines()
        lines.sort(key=sortimagelist)
        allinesg3 = lines
    if os.path.exists("imagestoaddg3sorted.txt"):
        os.remove("imagestoaddg3sorted.txt")
    else:
        print("The file does not exist")
    with open('imagestoaddg3sorted.txt', 'a') as f:

        f.writelines(allinesg3)

    with open('imagestoaddg3sorted.txt') as f:
        lines = f.readlines()
        imageRE = 'IM_[0-9a-zA-Z]{11,15}$'
        for line in lines:

            graphicID = re.findall(imageRE, line)
            imagestoaddg3.append(graphicID[0])
    ################################################
    imagestoaddg4 = []
    allinesg4 = []
    with open('imagestoaddg4.txt') as f:
        lines = f.readlines()
        lines.sort(key=sortimagelist)
        allinesg4 = lines
    if os.path.exists("imagestoaddg4sorted.txt"):
        os.remove("imagestoaddg4sorted.txt")
    else:
        print("The file does not exist")
    with open('imagestoaddg4sorted.txt', 'a') as f:

        f.writelines(allinesg4)

    with open('imagestoaddg4sorted.txt') as f:
        lines = f.readlines()
        imageRE = 'IM_[0-9a-zA-Z]{11,15}$'
        for line in lines:

            graphicID = re.findall(imageRE, line)
            imagestoaddg4.append(graphicID[0])



    ################################################

    imagestoadd = []
    imagestoaddwithnames = []


    for i in range(0, 64):
        innerlist = []
        innerlistwithnames = []

        innerlist.append(imagestoaddg1[i])
        innerlistwithnames.append(allinesg1[i])


        innerlist.append(imagestoaddg2[i])
        innerlistwithnames.append(allinesg2[i])

        innerlist.append(imagestoaddg3[i])
        innerlistwithnames.append(allinesg3[i])

        innerlist.append(imagestoaddg4[i])
        innerlistwithnames.append(allinesg4[i])

        imagestoadd.append(innerlist)
        imagestoaddwithnames.append(innerlistwithnames)

    imagestoaddall = []
    imagestoaddwithnamesall = []
    for i in range(0, 64):
        shuffleidx = [0, 1, 2, 3]
        random.shuffle(shuffleidx)
        random.shuffle(shuffleidx)
        print(shuffleidx)
        curimagestoadd = imagestoadd[i]
        curimagestoaddwithnames = imagestoaddwithnames[i]
        for j in shuffleidx:
            imagestoaddall.append(curimagestoadd[j])
            imagestoaddwithnamesall.append(curimagestoaddwithnames[j])



    if os.path.exists("allimagesrandom.txt"):
        os.remove("allimagesrandom.txt")
    else:
        print("The file does not exist")
    with open('allimagesrandom.txt', 'a') as f:

        f.writelines(imagestoaddwithnamesall)



    linelist = []

    with open('Template.qsf') as f:
        lines = f.readlines()

        imageRE = '["]IM_[0-9a-zA-Z]{11,15}["]$'
        count = 0
        for line in lines:

            graphicID = re.findall(imageRE, line)
            if len(graphicID) > 0:
                currentGraphicID = graphicID[0]
                print("currentGraphicID: ", currentGraphicID)
                print("count: ", count)
                currentImagestoAdd = "\"" + imagestoaddall[count] + "\""
                print("currentImagestoAdd ", currentImagestoAdd)
                # print("line before ", line)
                newline = line.replace(currentGraphicID, currentImagestoAdd)
                # print("line after ", newline)
                linelist.append(newline)
                count += 1
                print("------------------")
            else:
                linelist.append(line)




    if os.path.exists("surveybinaryrandom.qsf"):
        os.remove("surveybinaryrandom.qsf")
    else:
        print("The file does not exist")
    with open('surveybinaryrandom.qsf', 'a') as f:


        f.writelines(linelist)







if __name__ == '__main__':
    main()