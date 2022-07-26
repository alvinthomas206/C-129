import csv
from email import header
dataset1=[]
dataset2=[]

with open("final.csv","r")as f:
    csvreader=csv.reader(f)
    for row in csvreader:
        dataset1.append(row)

with open("archive_dataset_sorted1.csv","r")as f:
    csvreader=csv.reader(f)
    for row in csvreader:
        dataset2.append(row)

headers1=dataset1[0]
starsdata1=dataset1[1:]

headers2=dataset2[0]
starsdata2=dataset2[1:]

headers=headers1+headers2

starsdata=[]

for index,data_row in enumerate (starsdata1):
    starsdata.append(starsdata1[index]+starsdata2[index])

with open("merge.csv","a+")as f:
    csvwriter=csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(starsdata)
