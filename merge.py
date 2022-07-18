import csv 
dataset1=[]
dataset2=[]

with open('dwarf_stars.csv.csv','r') as f:
    csvreader=csv.reader(f)
    for row in csvreader:
        dataset1.append(row)

with open('browndwarfs_sorted.csv.csv','r') as f:
    read=csv.reader(f)
    for row in read:
        dataset2.append(row)

headers_1=dataset1[0]
star_data1=dataset1[1:]

headers_2=dataset2[0]
star_data2=dataset2[1:]

headers=headers_1+headers_2
star_data=[]

for index,row in enumerate(star_data1):
    star_data.append(star_data1[index]+star_data2[index])

#with open('archives_dataset_sorted.csv') as input,open("archives_data1.sorted.csv",'w',newline='') as output:
  #  write=csv.writer(output)
   # for row in csv.reader(input):
   #     if any(field.strip() for field in row):
   #         write.writerow(row)

with open("merged.csv",'a+') as f:
    csvWriter=csv.writer(f)
    csvWriter.writerow(headers)
    csvWriter.writerows(star_data)

