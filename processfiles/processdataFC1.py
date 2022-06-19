import numpy as np
import pandas as pd
import re





lines = []
with open('questiondetails.csv') as f:
	lines = f.readlines()


imagewholeline = []
# 	remove all the lines that does not have the image regular expression
imageRE = 'IM_[0-9a-zA-Z]{11,15}'
for line in lines:

	regexp = re.compile(imageRE)
	if regexp.search(line):
		imagewholeline.append(line)


imageRE = 'IM_[0-9a-zA-Z]{11,15}'
onlyimageids = []
for line in imagewholeline:
	graphicID = re.findall(imageRE, line)
	onlyimageids.append(graphicID[0])

# 	remove the first 16

onlyimageids = onlyimageids[12:]


# print(onlyimageids[60])
# print(onlyimageids[61])
# print(onlyimageids[62])
# print(onlyimageids[63])
onlyimageids.pop(60)
onlyimageids.pop(60)
onlyimageids.pop(60)
onlyimageids.pop(60)



# print(onlyimageids[124])
# print(onlyimageids[124])
# print(onlyimageids[124])
# print(onlyimageids[124])

onlyimageids.pop(124)
onlyimageids.pop(124)
onlyimageids.pop(124)
onlyimageids.pop(124)

#
# print(onlyimageids[208])
# print(onlyimageids[209])
# print(onlyimageids[210])
# print(onlyimageids[211])

onlyimageids.pop(208)
onlyimageids.pop(208)
onlyimageids.pop(208)
onlyimageids.pop(208)


onlyimageidsstructured = []
onlyimageidslength = len(onlyimageids)
for i in range(0, 64):
	innerlist = []


	for j in range(0,4):
		innerlist.append(onlyimageids[i * 4 + j])
	onlyimageidsstructured.append(innerlist)

















######################################3

def header(msg):
	print('-' * 50)
	print('[ ' + msg + ' ]')

# pd.set_option('max_columns', 93)
pd.set_option('display.max_columns', None)

header("1. load raw Qualitrics data")

filename = 'survey_response_table_all_clean_and_only_one_bad.csv'

df2 = pd.read_csv(filename)




# print(df2.columns)


# df2['check'] = np.where((df2['Q75'] == df2['randomid']) , df2['Q75'], np.nan)

# df2['Q75'] = df2['Q75'].str.strip()
# a = df2.iloc[6]['Q75']
# b = df2.iloc[6]['randomid']
# df2['check'] = np.where((df2['Q75'] == df2['randomid']) , df2['Q75'], np.nan)


# remove consent and attraction attention
df2['consentcheck'] = np.where((df2['Q69'] == "Yes, I consent") , df2['Q69'], np.nan)
# df2['attentioncheck1'] = np.where((df2['Q66'] == "IM_3PE9uVSyGaj2c2q") , df2['Q66'], np.nan)
# df2['attentioncheck2'] = np.where((df2['Q67'] == "IM_0NZ5kvItVoOkAGG") , df2['Q67'], np.nan)
# df2['attentioncheck3'] = np.where((df2['Q68'] == "IM_5uvTkqYDpjVvwfc") , df2['Q68'], np.nan)

df2.dropna(subset = ["consentcheck"], inplace=True)
df2.drop(["consentcheck"], inplace=True, axis=1)
print("||||||||||||||")

chosenlist =  []
for i in range(1, 65):
	colname = "Q{cur_i}".format(cur_i = i)
	curlist = df2[colname].tolist()


	chosenlist.append(curlist)

print("chosenllist", chosenlist)
print("chosenllist", len(chosenlist[0]))
chosentime =  []
for i in range(1, 65):
	colname = "Q{cur_i}_Page Submit".format(cur_i = i + 78)
	curlist = df2[colname].tolist()


	chosentime.append(curlist)



df3listformat = []

for i in range(0, len(chosenlist)):
	innerlist = []
	getchoselistlist = chosenlist[i]
	getchosetimelist = chosentime[i]

	for j in range(0, len(getchoselistlist)):
		innerinnerlist = []
		innerinnerlist.append(getchosetimelist[j])

		innerinnerlist.append(getchoselistlist[j])

		innerinnerlist.extend(onlyimageidsstructured[i])
		innerlist.append(innerinnerlist)

	df3listformat.append(innerlist)

print(df3listformat[0])
df3 = pd.DataFrame(
	df3listformat[0],columns = ['Q1_time', 'Q1_chosen','Q1_image1','Q1_image2','Q1_image3','Q1_image4'])



for i in range(1, len(df3listformat)):
	dfcurr = pd.DataFrame(
		df3listformat[i], columns=['Q{x}_time'.format(x=i + 1),
								   'Q{x}_chosen'.format(x = i + 1),
								   'Q{x}_image1'.format(x = i + 1),
								   'Q{x}_image2'.format(x = i + 1),
								   'Q{x}_image3'.format(x = i + 1),
								   'Q{x}_image4'.format(x = i + 1)])
	df3 = df3.join(dfcurr)

responseids = df2["ResponseId"].tolist()
dfresponse = pd.DataFrame(responseids, columns=["ResponseIDs"])

resultdf = dfresponse.join(df3)
resultdf.to_csv("survey_response_table_only_one_bad.csv")

# ###############################################

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



gandf = pd.DataFrame(
    {'GAN1': imagestoaddg1,
     'GAN2': imagestoaddg2,
     'GAN3': imagestoaddg3,
     'GAN4': imagestoaddg4
    })



######################################

countlist = [0, 0, 0, 0]

g1list = gandf.GAN1.tolist()
g2list = gandf.GAN2.tolist()
g3list = gandf.GAN3.tolist()
g4list = gandf.GAN4.tolist()

for i in range(1, 65):

	columnname = "Q{x}_chosen".format(x = i)
	columnlist = df3[columnname].tolist()

	for j in columnlist:

		if j in g1list:
			countlist[0] = countlist[0] + 1
		elif j in g2list:
			countlist[1] = countlist[1] + 1
		elif j in g3list:
			countlist[2] = countlist[2] + 1
		elif j in g4list:
			countlist[3] = countlist[3] + 1
		else:
			print("problem")



gancountdf = {'GAN_Table': ['GAN1', 'GAN2', 'GAN3', 'GAN4'],
			  	'Image_shown': [1856, 1856, 1856, 1856],
        		'Image_Count': countlist
        }

gancountdf = pd.DataFrame(gancountdf)

gancountdf.to_csv("final_results_all_clean_and_only_one_bad.csv")

