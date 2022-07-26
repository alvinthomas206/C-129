import csv
from dataclasses import field
from email import header

data=[]
with open("archive_dataset.csv","r")as f:
    csvreader=csv.reader(f)
    for row in csvreader:
        data.append(row)
headers=data[0]
stars_data=data[1:]

for data_point in stars_data:
    data_point[2]=data_point[2].lower()

stars_data.sort(key=lambda stars_data:stars_data[2])

with open("archive_dataset_sorted.csv","a+")as f:
    csvwriter=csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(stars_data)

with open("archive_dataset_sorted.csv")as input,open('archive_dataset_sorted1.csv','w',newline='')as output:
    writer=csv.writer(output)
    for row in csv.reader(input):
        if any(field.strip()for field in row):
            writer.writerow(row)
