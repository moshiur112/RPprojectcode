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



onlyimageids = onlyimageids[6:]

onlyimageids.pop(30)
onlyimageids.pop(30)



onlyimageids.pop(62)
onlyimageids.pop(62)


onlyimageids.pop(106)
onlyimageids.pop(106)

onlyimageids.pop(126)
onlyimageids.pop(126)


onlyimageids.pop(178)
onlyimageids.pop(178)


onlyimageids.pop(238)
onlyimageids.pop(238)


onlyimageidsstructured = []
onlyimageidslength = len(onlyimageids)
for i in range(0, 128):
	innerlist = []


	for j in range(0,2):
		innerlist.append(onlyimageids[i * 2 + j])
	onlyimageidsstructured.append(innerlist)

print(onlyimageidsstructured)

filename = 'responsedata.csv'

df2 = pd.read_csv(filename)






# remove consent and attraction attention
df2['consentcheck'] = np.where((df2['Q294'] == "Yes, I consent") , df2['Q294'], np.nan)


df2.dropna(subset = ["consentcheck"], inplace=True)
df2.drop(["consentcheck"], inplace=True, axis=1)


chosenlist =  []
for i in range(1, 129):
	colname = "Q{cur_i}".format(cur_i = i)
	curlist = df2[colname].tolist()


	chosenlist.append(curlist)


chosentime =  []
for i in range(1, 129):
	colname = "Q{cur_i}_Page Submit".format(cur_i = i + 128)
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

df3 = pd.DataFrame(
	df3listformat[0],columns = ['Q1_time', 'Q1_chosen','Q1_image1','Q1_image2'])



for i in range(1, len(df3listformat)):
	dfcurr = pd.DataFrame(
		df3listformat[i], columns=['Q{x}_time'.format(x=i + 1),
								   'Q{x}_chosen'.format(x = i + 1),
								   'Q{x}_image1'.format(x = i + 1),
								   'Q{x}_image2'.format(x = i + 1),
])
	df3 = df3.join(dfcurr)

responseids = df2["ResponseId"].tolist()
dfresponse = pd.DataFrame(responseids, columns=["ResponseIDs"])

resultdf = dfresponse.join(df3)
# resultdf.to_csv("survey_binary_response.csv")
# #
# # # ###############################################
gandf = pd.read_csv("ganandimages.csv")
#
# # ######################################

countlist = [0, 0, 0, 0]

g1list = gandf["This_City_Does_Not_Exist"].tolist()
g2list = gandf["Satellite"].tolist()
g3list = gandf["Test_100"].tolist()
g4list = gandf["GAN_250"].tolist()

for i in range(1, 129):


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


#
gancountdf = {'GAN_Table': ["This_City_Does_Not_Exist",	"Satellite",	"Test_100",	"GAN_250"],
			  	'Image_shown': [1024, 1024, 1024, 1024],
        		'Image_Count': countlist
        }

gancountdf = pd.DataFrame(gancountdf)

gancountdf.to_csv("final_results_binary.csv")

