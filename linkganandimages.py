import re
import pandas as pd

def header(msg):
	print('-' * 50)
	print('[ ' + msg + ' ]')

def sortimagelist(currentlist):
   mappedlist =  list(map(int, re.findall(r'\d+', currentlist)))[0]
   return mappedlist

imagestoaddg1 = []
allinesg1 = []
lines = []
with open('imagestoaddg1.txt') as f:
    lines = f.readlines()

lines.sort(key=sortimagelist)
allinesg1 = lines

imageRE = 'IM_[0-9a-zA-Z]{11,15}$'
for line in lines:
    graphicID = re.findall(imageRE, line)
    imagestoaddg1.append(graphicID[0])

print(imagestoaddg1)
print(len(imagestoaddg1))


################

imagestoaddg2 = []
allinesg2 = []
lines = []
with open('imagestoaddg2.txt') as f:
    lines = f.readlines()

lines.sort(key=sortimagelist)
allinesg2 = lines

imageRE = 'IM_[0-9a-zA-Z]{11,15}$'
for line in lines:
    graphicID = re.findall(imageRE, line)
    imagestoaddg2.append(graphicID[0])

print(imagestoaddg2)
print(len(imagestoaddg2))

################

imagestoaddg3 = []
allinesg3 = []
lines = []
with open('imagestoaddg3.txt') as f:
    lines = f.readlines()

lines.sort(key=sortimagelist)
allinesg3 = lines

imageRE = 'IM_[0-9a-zA-Z]{11,15}$'
for line in lines:
    graphicID = re.findall(imageRE, line)
    imagestoaddg3.append(graphicID[0])

print(imagestoaddg3)
print(len(imagestoaddg3))


################

imagestoaddg4 = []
allinesg4 = []
lines = []
with open('imagestoaddg4.txt') as f:
    lines = f.readlines()

lines.sort(key=sortimagelist)
allinesg4 = lines

imageRE = 'IM_[0-9a-zA-Z]{11,15}$'
for line in lines:
    graphicID = re.findall(imageRE, line)
    imagestoaddg4.append(graphicID[0])

print(imagestoaddg4)
print(len(imagestoaddg4))


df = pd.DataFrame(
    {'This_City_Does_Not_Exist': imagestoaddg1,
     'Satellite': imagestoaddg2,
     'Test_100': imagestoaddg3,
     'GAN_250': imagestoaddg4
    })
print(df)
df.to_csv("ganandimages.csv")